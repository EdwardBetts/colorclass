"""Colorful worry-free console applications for Linux, Mac OS X, and Windows.

Supported natively on Linux and Mac OSX (Just Works), and on Windows it works the same if Windows.enable() is called.

Gives you expected and sane results from methods like len() and .capitalize().

https://github.com/Robpol86/colorclass
https://pypi.python.org/pypi/colorclass
"""

from colorclass.codes import list_tags  # noqa
from colorclass.core import Color  # noqa
from colorclass.toggles import disable_all_colors  # noqa
from colorclass.toggles import set_dark_background  # noqa
from colorclass.toggles import set_light_background  # noqa
from colorclass.windows import Windows  # noqa

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '1.2.0'