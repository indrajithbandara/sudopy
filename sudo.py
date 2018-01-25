#!python3.6

import ctypes
import os
import subprocess
import sys


def say(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)


# Imports, or gets the win32api module; refuses to run on Unix.
if os.name != 'nt':
    say('Please install the `sudo\' package for your distribution.')
    exit(1)
elif not hasattr(ctypes, 'windll') or not hasattr(ctypes.windll, 'shell32'):
    say('This is not applicable to your system.')
    exit(2)
elif len(sys.argv) < 2:
    say('Please provide some arguments.')
else:
    shell32 = ctypes.windll.shell32

    to_run = subprocess.list2cmdline(sys.argv[1:])

    args = [
        '/c color 4F &', 
        f'title sudo {to_run} &',
        to_run,
        ' & pause & exit']

    args = ' '.join(args)
    args = subprocess.list2cmdline([args])

    shell32.ShellExecuteW(
        None, 
        'runas', 
        'cmd.exe', 
        args,
        None,
        1)
