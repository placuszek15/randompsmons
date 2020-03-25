from cx_Freeze import setup, Executable

base = None    

executables = [Executable("randommons.py", base=base)]

packages = ["idna","lists","random","sys","time","selenium","queue"]
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