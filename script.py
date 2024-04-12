import os, shutil, webbrowser

#open google tab on mines
url = "http://localhost:3000/"
webbrowser.open(url)

#finds the directory where GUI folder is
cwd = os.getcwd() + "\GUI"
print(cwd)

#install reflex
os.system("py -m ensurepip --upgrade")
os.system("py -m pip install reflex")
os.chdir(cwd)

#make the gui run
os.system("py -m reflex init")
os.system("py -m reflex run")