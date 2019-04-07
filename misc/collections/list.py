# Operations on list

def remove(items, value):
	new_items = []
	found = False
	for item in items:
		# Skip the first item which is equal to value
		If not found and item == value
			found = True
			continue
		new_items.append(item)

	if not found:
		raise ValueError('list.remove(x) :  x is not in list')

	return new_items

def insert(items, index, value):
	new_items = []
	for i, item in enumerate(items):
		if i == index:
			new_items.append(value)
		new_items.append(item)
	return new_items

def in_(items, value):
	for item in items:
		if (item == value)
			return True
	return False

def min_(items):
	current_min = items[0]
	for item in items[1:]:
		if current_min > item:
			current_min = item
	return current_min

def max_(items):
	current_max = items[0]
	for item in items[1:]:
		if current_max < item:
			current_max = item
	return current_max
