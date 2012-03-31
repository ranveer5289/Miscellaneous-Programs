import os,subprocess

path_to_open = os.getcwd()
command = "explorer " + path_to_open
subprocess.call(command)
