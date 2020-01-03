#!/bin/bash
python2 $(dirname $0)/../geeknote/setup.py build
pip2 install $(dirname $0)/../geeknote/
