version = "alpha_1.0.1"
developer = "Zer0plusOne"
def show_info():
    # Información del programa
    last_updated = "05/11/2024 22:12"
    repository = "https://github.com/Zer0plusOne/DEDSEC.TOOL"

    info_text = (
        f"╭────────────────────────────────────── TOOL INFO ──────────────────────────────────────\n"
        f"│  [\033[0;34m+\033[0m]Version: {version}\n"
        f"│  [\033[0;34m+\033[0m]Developer: {developer}\n"
        f"│  [\033[0;34m+\033[0m]Fecha de la última actualización: {last_updated}\n"
        f"│  [\033[0;34m+\033[0m]GitHub Repository: {repository}\n"
        f"│\n"
        f"│  The usage of this tool is free now and forever, if you paid for anything related for this tool, "
        f"│  sorry but you got scammed.\n"
        f"│  If you use this tool and like the idea please feel free to post new features, also feel free "
        f"│  to contact me in the contact ways I have enabled in my GitHub profile.\n"
        f"╰───────────────────────────────────────────────────────────────────────────\n"
    )

    print(info_text)
