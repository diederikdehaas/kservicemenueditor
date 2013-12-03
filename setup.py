#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
import os
from DistUtilsExtra.command import *

setup(name="kservicemenueditor",
	  version="0.2a",
      author="David Edmundson",
      author_email="servicemenu@davidedmundson.co.uk",
      license="GPLv2",
      scripts=[
               'kservicemenueditor',
                 ],
      data_files=[
                  ('share/kde4/apps/kservicemenueditor', glob.glob("*.ui")),
                  ('share/applications/',['kservicemenueditor.desktop'])
                 ]
	  )
