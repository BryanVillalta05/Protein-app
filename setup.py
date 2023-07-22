import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "requests"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para evitar la apertura de una ventana de consola

executables = [
    Executable("app.py", base=base)
]

setup(
    name="Protein data",
    version="1.0",
    description="Protein data application",
    options={"build_exe": build_exe_options},
    executables=executables
)
