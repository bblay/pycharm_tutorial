"""
This module just ensures the venv is set up properly.
We run shash because it requires C code to be built as part of the installation.

"""

#from iocore.shash.shared_hash import SharedHash
from shash.shared_hash import SharedHash

shash = SharedHash()
shash.set('foo', 123.456)
print shash.get('foo')
print 'finished'
