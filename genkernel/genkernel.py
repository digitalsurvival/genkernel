__author__ = 'matthew marchese'
__email__ = 'maffblaster@gentoo.org'
__description__ = 'An experimental entire rewrite of Gentoo\'s genkernel for Python 3'
__license__ = 'MIT'
__source__ = 'https://github.com/digitalsurvival/genkernel.git'
__version__ = '4.0.0'
# The command-line interface for genkernel

# cli interface
import argparse

# To parse .config files
import kaudit.config

init()

parser = argparse.ArgumentParser(prog='genkernel', usage='%(prog)s [options]', description=__description__, epilog='wip. send comments to maffblaster@gentoo.org')
parser.add_argument('-V', '--version', action='version', version='%(prog)s v' + __version__)
args = parser.parse_args(''.split())
