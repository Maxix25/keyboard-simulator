#!/usr/bin/env python2
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 2 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>
import platform
from threading import Thread
from subprocess import Popen, PIPE
from playsound import playsound


class PlaySound(Thread):
	def __init__(self, filename, volume):
		Thread.__init__(self)
		self.filename = filename
		self.volume = volume

	def run(self):
		if platform.system() == "Windows":
			playsound(self.filename[1:])
		else:
			cmd = 'play -v ' + self.volume + ' ' + f"'{self.filename}'"
			p = Popen(cmd, shell=True, stderr=PIPE, close_fds=True)
			# TODO: Test if limits the number of clicks
			p.wait()
			if p.returncode != 0:
	  			print ('\033[1;31mWe found a error with SoX, did you install it?\033[1;m')
	  			print(p.stderr.read())
