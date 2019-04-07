# Operations on dictionary

#pseudo hash
def most_significant(value):
	while value >= 10:
		value //= 10
	return value

def add(collection, key, value):
	index = most_significant(key)
	collection[index].append((key, value))

def contains(collection, key):
	index = most_significant(key)
	for k, v in collection[index]:
		if k == key:
			return True
	return False
