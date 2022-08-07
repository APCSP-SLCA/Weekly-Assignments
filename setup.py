import sys
import subprocess

# make sure the correct python version is installed

version = sys.version_info
if version[0] < 3:
    print("You must have Python 3 installed to continue!")
    print(f"Please ask for help, or go to https://www.python.org/downloads/macos/"
          f"for the latest python relase!")
    sys.exit()
elif version[1] < 8:
    print("You must have at least Python 3.8 installed to continue!")
    print(f"Please ask for help, or go to https://www.python.org/downloads/macos/"
          f"for the latest python relase!")
    sys.exit()
else:
    print(f"You have the correct Python version installed: "
          f"Python {version[0]}.{version[1]}.{version[2]}!")
    print(f"Python executable located at: {sys.executable}")

# implement pip as a subprocess

# update pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# install pyglet
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyglet"])

# install numpy
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])

# install pillow
subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

# install requests
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

# intall termcolor
subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])

# print installed packages
reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])

installed_packages = [r.decode().split("==")[0] for r in reqs.split()]

from termcolor import cprint, colored

for p in installed_packages:
    package = colored(p, "green", attrs=["bold", "underline"])
    print(package, end=" ")
    cprint("is installed!", "green")