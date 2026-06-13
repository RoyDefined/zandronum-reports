#!/usr/bin/env python3
import subprocess
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent

    tools_root = root / "tools"
    zandronum_root = tools_root / "Zandronum_x64"

    zandronum = zandronum_root / "zandronum.exe"
    iwad = zandronum_root / "Doom2.wad"
    wads_root = root / "wads"

    cmd = [
        str(zandronum),
        "-iwad", str(iwad),
    ]

    for file in sorted(wads_root.iterdir()):
        if not file.is_file():
            continue

        if file.name.lower() in {".gitignore", "readme.txt"}:
            continue

        cmd.extend(["-file", str(file)])

    print("Starting Zandronum:")
    print(" ".join(f'"{arg}"' if " " in arg else arg for arg in cmd))

    subprocess.Popen(cmd)


if __name__ == "__main__":
    main()