def sort_backpack(capacity, items):
	items = sorted(items, key=lambda val: val[1]/val[2])

capacity = 50
items = [
	('boot', 10, 60),
	('tent', 20, 100),
	('water', 30, 120),
	('first aid', 15, 70),
]

sort_backpack(capacity, items)
