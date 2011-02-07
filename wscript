#! /usr/bin/env python

def configure(conf):
	conf.load('tex')

def build(bld):
	obj = bld(
		features = 'tex',
		source = 'Packet.tex'
	)
