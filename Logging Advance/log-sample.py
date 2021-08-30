import logging 
import employee

#logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
'''
This only created the 'employee.log' file, because it was imported before the 'basicConfig' and the
logger method configures the 'root', so it didn't overwrite the previous basicConfig inside the 'employee.py' file.
'''

# Creating Loggers
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('sample.log')
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s ---> %(levelname)s')
stream_formatter = logging.Formatter('%(name)s:%(message)s')

file_handler.setLevel(logging.CRITICAL)
file_handler.setLevel(logging.ERROR)

stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x,y):
	return x + y


def mult(x,y):
	return x * y

def div(x,y):
	return x // y 

num_1 = 2
num_2 = 5

add_result = add(num_1,num_2)
mult_result = mult(num_1,num_2)
div_result = div(num_1,num_2)

logger.debug('Added {} + {} = {}'.format(num_1,num_2,add_result))

logger.critical('Multiplied {} * {} = {}'.format(num_1,num_2,mult_result))

logger.error('Divided {} ÷ {} = {}'.format(num_1,num_2,div_result))
