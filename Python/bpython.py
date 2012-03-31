import subprocess,shlex

cmd = r'cmd.exe /c F:\\cygwin\\bin\\bash.exe --login -c bpython'
command = shlex.split(cmd)
subprocess.call(command)
