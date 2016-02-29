from cudatext import *
import sys
import os

sys.path.append(os.path.dirname(__file__))
from cssprefixer import process
import format_proc

format_proc.MSG = '[CSS Prefixer] '
format_proc.INI = ''

def do_format(text):
    return process(text)

class Command:
    def run(self):
        format_proc.run(do_format)
