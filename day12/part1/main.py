class TwoWayDict(dict):
	def __setitem__(self, key, value):
		# Remove any previous connections with these values
		#if key in self:
		#	del self[key]
		#if value in self:
		#	del self[value]
		if key in self:
			print("ouo1: {}, {}".format(self[key], type(self[key])))
			if isinstance(self[k], list):
				self[k].append(value)
			else:
				dict.__setitem(self, key, [self[k], value])
			dict.__setitem__(self, value, 0)
		else:
			dict.__setitem__(self, key, value)

		print("ouo2: {}, {}".format(self[key], type(self[key])))

		dict.__setitem__(self, value, key)


	def __delitem__(self, key):
		dict.__delitem__(self, self[key])
		dict.__delitem__(self, key)

	def __len__(self):
		"""Returns the number of connections"""
		return dict.__len__(self) // 2

with open('small','r') as f:
	paths={}
	for l in f.readlines():
		a,b=l.strip().split('-')
		if a in paths:
			paths[a].append(b)
		if b in paths:
			paths[b].append(b)
		else:
		paths[a]=[b]
		paths[b]=[a]

print(paths)
count=0
def recursive(pointer, visited, num):
	global count
	if pointer=='end':
		return ('end',visited)
	if pointer.islower():
		if pointer in visited:
			return (None,visited)
		else:
			visited.append(pointer)
	if pointer not in paths:
		return (pointer,visited)

	choices=paths[pointer]
	print("Function start",num)
	p=[]
	for choice in choices:
		print("Checking choice", choice)
		(a, visited)=recursive(choice, visited, num+1)
		#if a==None: (pointer,visited)
		p.append(a)
	#print('\n{}\n'.format(p))
	print("Function end",num)
	return p, visited

print(recursive('start', [], 0))
print(count)
