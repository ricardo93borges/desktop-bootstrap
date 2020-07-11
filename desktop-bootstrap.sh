#!/bin/sh
gnome-terminal --geometry 170x25+0+0 --working-directory=/home
/usr/bin/python3.8 desktop-bootstrap.py --file config-sample.txt
