from cx_Freeze import setup, Executable
import sys

base = None    
if (sys.platform == "win32"):
    base = "Win32GUI"   
executables = [Executable("main.py", base=base)]

packages = ["idna","lists","random","sys","time","selenium","queue","randommons","friigooi","pyqt5"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "RandomPokemon",
    options = options,
    version = "0.1b",
    description = 'pleasework?',
    executables = executables
)