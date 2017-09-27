# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Flakoo',
	version='0.1',
	description='Conector Odoo Flask',
	url='http://github.com/eortizromero/flakoo',
	author='Edgar Ortiz', 
	author_email='edgardoficial.yo@gmail.com',
	license='',
	packages=['flakoo'],
	include_package_data=True,
	platforms='any',
	install_requires=[
		'ERPpeek>=1.6.3',
	],
	zip_safe=False,
	entry_points="""
	[console_scripts]
	flakoo=flakoo:main
	"""
	)