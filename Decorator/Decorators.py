import os
from functools import wraps

def decfunc(org_func):
	def wrapper(*args,**kwargs):
		print('wrapper executed this before {}'.format(org_func.__name__))
		return org_func(*args,**kwargs)
	return wrapper

class dec_class(object):
	def __init__(self,org_func):
		self.org_func = org_func

	def __call__(self,*args,**kwargs):
		print('Call method executed this before {}'.format(self.org_func.__name__))
		return (self.org_func(*args,**kwargs))

def logger(org_func):
	import logging

	logging.basicConfig(filename='{}.log'.format(org_func.__name__),level=logging.INFO)

	@wraps(org_func)
	def wrapper(*args,**kwargs):
		logging.info('Ran with args {} and kwargs {}'.format(args,kwargs))

		return org_func(*args,**kwargs)
	return wrapper

def timer(org_func):
	import time as t

	@wraps(org_func)
	def wrapper(*args,**kwargs):
		t1 = t.time()
		result = org_func(*args,*kwargs)
		t2 = t.time() - 1

		print("Ran with '{}' and took {} sec to execute".format(org_func.__name__,t2))

		return result
	return wrapper


@timer
def test():
	import time
	time.sleep(1)
	print('This is a Test')

test()

@logger
@timer
def info(frst,lst):
	print('This rans with the args {} and the kwargs {}'.format(frst,lst))

info('Mable','Pines')
info('Dipper','Pines')