import pickle
from pprint import pprint

with open('./tests/Examples_of_AdjLists_of_Trees', 'rb') as f:
    adjlist = pickle.load(f)

with open('./tests/Examples_of_k_values', 'rb') as f:
    k_values = pickle.load(f)

with open('./tests/Examples_of_labelling', 'rb') as f:
    labelling = pickle.load(f)

pprint(adjlist)
print()
pprint(k_values)
print()
pprint(labelling)