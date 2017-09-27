"Flakoo | Odoo - Flask Connection" 

## H2 Installation:
	Clone reporitory https://github.com/eortizromero/flakoo.git
	cd flakoo/
	pip install -e . // Install in dev mode

## H2 Basic Usage:
	```python
	from flakoo import Flakoo
	```

	connect_flakoo = Flakoo(server='http://localhost:8069') # Your Odoo Server Address
	connect_flakoo.run_server() # if server is connected return True
	```