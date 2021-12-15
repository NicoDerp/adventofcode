with open('small','r') as f:
	template,pairs=f.read().split('\n\n')

print(template)
pairs=pairs.split('\n')
pairs.pop()

pairs=dict(map(lambda i:i.split(' -> '),pairs))

# Steps
for step in range(5):
	print("\nStep", step)
	new=template
	# index, value
	toAdd={}
	for i in range(len(template)):
		pair=new[i]+new[i+1]
		rule=pairs[pair]
		print("Pair: {}, rule: {}".format(pair, rule))
		new=new[:i+1] + rule + new[i+1:]
		print(new)
	template=new

