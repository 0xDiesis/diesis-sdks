#!/usr/bin/env python3
"""Regenerate F#, OCaml, and q SDKs through their standalone generators."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
for language in ("fsharp", "ocaml", "q"):
    subprocess.run([sys.executable, str(root / f"diesis-{language}/scripts/generate.py"), *sys.argv[1:]], check=True)
