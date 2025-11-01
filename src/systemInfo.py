import collections
import os
import platform
import socket
from typing import Dict, Iterable, Tuple

import banners

try:
    import psutil  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - executed only when psutil is missing
    psutil = None  # type: ignore


def _get_physical_cores() -> int:
    """Return the number of physical cores parsing /proc/cpuinfo when psutil is not available."""

    try:
        with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as cpuinfo:
            physical_cores = set()
            physical_id = None
            core_id = None
            for line in cpuinfo:
                line = line.strip()
                if not line:
                    if physical_id is not None and core_id is not None:
                        physical_cores.add((physical_id, core_id))
                    physical_id = None
                    core_id = None
                    continue
                if line.startswith("physical id"):
                    physical_id = line.split(":", 1)[1].strip()
                elif line.startswith("core id"):
                    core_id = line.split(":", 1)[1].strip()
            if physical_id is not None and core_id is not None:
                physical_cores.add((physical_id, core_id))
            return len(physical_cores) or (os.cpu_count() or 0)
    except OSError:
        return os.cpu_count() or 0


def _read_cpu_freq() -> Tuple[float, float]:
    """Return (max_freq, current_freq) in MHz when psutil is not available."""

    max_freq = current_freq = 0.0
    # Try cpufreq interface first
    base_path = "/sys/devices/system/cpu/cpu0/cpufreq"
    try:
        with open(os.path.join(base_path, "cpuinfo_max_freq"), "r", encoding="utf-8") as max_file:
            max_freq = float(max_file.read().strip()) / 1000.0
    except OSError:
        pass
    try:
        with open(os.path.join(base_path, "scaling_cur_freq"), "r", encoding="utf-8") as cur_file:
            current_freq = float(cur_file.read().strip()) / 1000.0
    except OSError:
        pass

    if max_freq == 0.0 or current_freq == 0.0:
        # Fall back to /proc/cpuinfo average
        try:
            freqs = []
            with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as cpuinfo:
                for line in cpuinfo:
                    if line.startswith("cpu MHz"):
                        value = line.split(":", 1)[1].strip()
                        freqs.append(float(value))
            if freqs:
                if max_freq == 0.0:
                    max_freq = max(freqs)
                if current_freq == 0.0:
                    current_freq = sum(freqs) / len(freqs)
        except OSError:
            pass
    return max_freq, current_freq


def _load_memory_info() -> Dict[str, float]:
    """Parse /proc/meminfo to approximate psutil.virtual_memory()."""

    meminfo: Dict[str, float] = {"total": 0.0, "available": 0.0, "percent": 0.0}
    try:
        with open("/proc/meminfo", "r", encoding="utf-8") as mem_file:
            info = {}
            for line in mem_file:
                key, value = line.split(":", 1)
                info[key.strip()] = float(value.strip().split()[0])
            total = info.get("MemTotal", 0.0)
            available = info.get("MemAvailable", 0.0)
            meminfo["total"] = total * 1024
            meminfo["available"] = available * 1024
            if total:
                meminfo["percent"] = round((1 - available / total) * 100, 2)
    except OSError:
        pass
    return meminfo


def _disk_partitions_fallback() -> Iterable[Tuple[str, str]]:
    """Iterate over mounted partitions using /proc/mounts."""

    try:
        with open("/proc/mounts", "r", encoding="utf-8") as mounts:
            for line in mounts:
                device, mountpoint, *_rest = line.split()
                yield device, mountpoint
    except OSError:
        return []


def _disk_usage(path: str) -> Tuple[float, float, float]:
    """Return (total, used, free) bytes for the given mountpoint."""

    try:
        stats = os.statvfs(path)
        total = stats.f_frsize * stats.f_blocks
        free = stats.f_frsize * stats.f_bfree
        used = total - free
        return total, used, free
    except OSError:
        return 0.0, 0.0, 0.0


def _print_network_info():
    if psutil is None:
        print("||  [\033[0;33m!\033[0m] Network information unavailable (psutil not installed).")
        return

    info_interfaces = psutil.net_if_addrs()
    for interface, direcciones in info_interfaces.items():
        printed_interface = False
        for direccion in direcciones:
            if direccion.family == socket.AF_INET:  # IPv4
                if not printed_interface:
                    print(f"||  [\033[0;34m+\033[0m]Interface: {interface}")
                    printed_interface = True
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] IPv4: {direccion.address}")
            elif direccion.family == socket.AF_INET6:  # IPv6
                if not printed_interface:
                    print(f"||  [\033[0;34m+\033[0m]Interface: {interface}")
                    printed_interface = True
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] IPv6: {direccion.address}")
            elif getattr(psutil, "AF_LINK", None) and direccion.family == psutil.AF_LINK:  # MAC
                if not printed_interface:
                    print(f"||  [\033[0;34m+\033[0m]Interface: {interface}")
                    printed_interface = True
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] MAC: {direccion.address}")


def SystemInfo():
    print(banners.BANNER_3)
    print(" ")
    print("Informacion del sistema: ")
    print("=" * 64)
    print("||=================== General Information ===================||")
    print(f"||  [\033[0;34m+\033[0m] Operating System: {platform.system()} {platform.release()}")
    print(f"||  [\033[0;34m+\033[0m] Host Name: {platform.node()}")
    print(f"||  [\033[0;34m+\033[0m] System Verison: {platform.version()}")
    print(f"||  [\033[0;34m+\033[0m] Architecture: {platform.machine()}")
    print(f"||  [\033[0;34m+\033[0m] Processor Core: {platform.processor()}")
    print("||===================== CPU Information =====================||")

    logical_cores = os.cpu_count() or 0
    if psutil is not None:
        physical_cores = psutil.cpu_count(logical=False) or logical_cores
        freq = psutil.cpu_freq() or collections.namedtuple("freq", "max current")(0.0, 0.0)
        max_hz = freq.max or 0.0
        current_hz = freq.current or 0.0
        cpu_usage = psutil.cpu_percent(interval=1)
    else:
        physical_cores = _get_physical_cores()
        max_hz, current_hz = _read_cpu_freq()
        # loadavg returns a tuple scaled per CPU, approximate usage percentage
        try:
            load1, _load5, _load15 = os.getloadavg()
            cpu_usage = round(min(100.0, (load1 / logical_cores) * 100.0), 2) if logical_cores else 0.0
        except OSError:
            cpu_usage = 0.0

    print(f"||  [\033[0;34m+\033[0m] Fisical cores: {physical_cores} ")
    print(f"||  [\033[0;34m+\033[0m] Total cores: {logical_cores}")
    if max_hz:
        print(f"||  [\033[0;34m+\033[0m] Max Hz: {max_hz:.2f} MHz")
    else:
        print("||  [\033[0;33m!\033[0m] Max Hz: N/A")
    if current_hz:
        print(f"||  [\033[0;34m+\033[0m] Current Hz: {current_hz:.2f} MHz")
    else:
        print("||  [\033[0;33m!\033[0m] Current Hz: N/A")
    print(f"||  [\033[0;34m+\033[0m] CPU Usage: {cpu_usage}%")

    print("||=================== Memory Information ===================||")
    if psutil is not None:
        mem = psutil.virtual_memory()
        print(f"||  [\033[0;34m+\033[0m] Total: {mem.total / (1024 ** 3):.2f} GB")
        print(f"||  [\033[0;34m+\033[0m] Avalible: {mem.available / (1024 ** 3):.2f} GB")
        print(f"||  [\033[0;34m+\033[0m] Usage: {mem.percent}%")
    else:
        meminfo = _load_memory_info()
        total = meminfo["total"] / (1024 ** 3)
        available = meminfo["available"] / (1024 ** 3)
        percent = meminfo["percent"]
        if total:
            print(f"||  [\033[0;34m+\033[0m] Total: {total:.2f} GB")
            print(f"||  [\033[0;34m+\033[0m] Avalible: {available:.2f} GB")
            print(f"||  [\033[0;34m+\033[0m] Usage: {percent}%")
        else:
            print("||  [\033[0;33m!\033[0m] Unable to read memory information")

    print(f"||=================== Disk Information ===================||")
    if psutil is not None:
        partitions = [(p.device, p.mountpoint) for p in psutil.disk_partitions()]
    else:
        partitions = list(_disk_partitions_fallback())

    if not partitions:
        print("||  [\033[0;33m!\033[0m] No disk information available")
    for device, mountpoint in partitions:
        print(f" == {device} ({mountpoint})")
        if psutil is not None:
            usage = psutil.disk_usage(mountpoint)
            total = usage.total
            used = usage.used
            free = usage.free
            percent = usage.percent
        else:
            total, used, free = _disk_usage(mountpoint)
            percent = round((used / total) * 100, 2) if total else 0.0
        if total:
            print(f"||  [\033[0;34m+\033[0m] Total: {total / (1024 ** 3):.2f} GB")
            print(f"||  [\033[0;34m+\033[0m] Occupied: {used / (1024 ** 3):.2f} GB ({percent}%)")
            print(f"||  [\033[0;34m+\033[0m] Free: {free / (1024 ** 3):.2f} GB")
        else:
            print("||  [\033[0;33m!\033[0m] Unable to read disk usage")

    print("||=================== NET Information ===================||")
    _print_network_info()