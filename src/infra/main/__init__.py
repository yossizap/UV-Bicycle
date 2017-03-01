#!/usr/bin/env python

# set PYTHONPATH
import sys
import os.path
sys.path.extend([os.path.dirname(os.path.dirname(os.path.abspath(__file__)))])

import program


def reload_program():
    """
    Reloads all the program modules for fast development.
    """
    for module in program.modules:
        reload(__import__(module))
    reload(program)


if __name__ == "__main__":
    from IPython.terminal.embed import InteractiveShellEmbed
    globals().update(locals())
    InteractiveShellEmbed(**program.config.INTERACTIVE_SHELL_EMBED_ARGUMENTS)()
