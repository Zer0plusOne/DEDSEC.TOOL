# Functional Analysis Report

Date: 2025-11-01T08:16:00Z

## System Information Module
- `systemInfo.SystemInfo()` executed successfully using psutil fallbacks.
- CPU, memory, and disk details rendered correctly.
- Network section reports psutil absence as expected.

## Network Utilities (Ping & Traceroute)
- `pinger.realizar_ping('8.8.8.8', num_pings=1)` completed, no responses received from host.
- Traceroute fallback triggered with message about missing binary.

## OSINT Gathering
- `ipInfoGather.gather_ip_info('8.8.8.8', '', '')` handled blocked IPinfo access and missing optional integrations gracefully.

## Port Scanner
- Fallback socket scanner ran against `127.0.0.1` for range `20-22`, completing without python-nmap.

## Notes
- External network calls remain restricted by environment policies.
- Traceroute functionality requires system binary to be available for full results.
