#!/usr/bin/env python3
import subprocess
from pathlib import Path


PORT = "10666"


def get_file_args(wads_root):
    args = []

    for file in sorted(wads_root.iterdir()):
        if not file.is_file():
            continue

        if file.name.lower() in {".gitignore", "readme.txt"}:
            continue

        args.extend(["-file", str(file)])

    return args


def log_cmd(label, cmd):
    print(label)
    print(" ".join(f'"{arg}"' if " " in arg else arg for arg in cmd))
    print("")


def main():
    root = Path(__file__).resolve().parent.parent

    zandronum_root = root / "tools" / "Zandronum_x64"
    zandronum = zandronum_root / "zandronum.exe"
    iwad = zandronum_root / "Doom2.wad"
    wads_root = root / "wads"

    cmd = [
        str(zandronum),
        "-host", "1",
        "-port", PORT,
        "-iwad", str(iwad),
        *get_file_args(wads_root),
    ]

    log_cmd("Host command:", cmd)

    server = subprocess.Popen(cmd)
    server.wait()


if __name__ == "__main__":
    main()