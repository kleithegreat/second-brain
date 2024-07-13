import pickle
from pprint import pprint

data = pickle.load(open('./examples_of_instances', 'rb'))
pprint(data)