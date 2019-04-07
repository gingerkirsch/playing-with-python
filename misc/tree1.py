import json
import functools
import collections

def tree():
    return collections.defaultdict(tree)

# Build the tree:
taxonomy = tree()
reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
reptilia['Squamata']['Serpentes']['Pythonidae'] = ['Liasis', 'Morelia', 'Python']

print(json.dumps(taxonomy, indent=4))

path = 'Chordata.Vertebrata.Reptilia.Squamata.Serpentes'

path = path.split('.')

family = functools.reduce(lambda a, b: a[b], path, taxonomy)
family.items()

suborder = functools.reduce(lambda a, b: a[b], path, taxonomy)
suborder.keys()
dict_keys(['Serpentes'])