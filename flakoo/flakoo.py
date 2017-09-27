# -*- coding: utf-8 -*-

"""

	This package connect Odoo & Flask using ERPPeek with XMLRPCLIB 
	First method is for check if database exist, if not then create
	database and you can select that or another.

"""
import erppeek
import re

database = ''

class Flakoo(object):
	def __init__(self, server=None):
		self.database = database
		client = False
		if not server or server is None:
			print "El servidor no esta corriendo Odoo instalelo en esa instancia, para poder usarlo"
			self.client = False
			return
		if not self.regex_server(server):
			print "El servidor no es correcto"
			self.client = False
			return
		client = erppeek.Client(server=server)
		print '______ cliente _____ %s' % client
		if not client:
			return False
		self.client = client

	def regex_server(self, server):
		# Regex for Odoo Address Server added by user
		# Return False if not is a valid address
		regex = re.compile(
		r'^(?:http|ftp)s?://' # http:// or https://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|' #localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?' # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		if regex.search(server):
			return True


	def run_server(self):
		if not self.client:
			print "No conectado"
			return False
		else:
			print "Conectado a (%s) " % (self.client)
			return True