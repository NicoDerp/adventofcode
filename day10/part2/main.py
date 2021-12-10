with open('input','r') as f:
	code=f.read().split('\n')

code.pop()
lu={')':1,']':2,'}':3,'>':4}

syntax={'(':')','[':']','{':'}','<':'>'}

p=[]
for l in code:
	s=[]
	inc=False
	#w=[]
	for c in l:
		if c in syntax:s.append(c)
		else:
			#print(l, c)
			if syntax[s[-1]]!=c:inc=True #w.append(c)
			else:s.pop()
	if not inc:
		count=0
		print(s)
		for c in reversed(s):
			count*=5
			count+=lu[syntax[c]]
		p.append(count)

	#print(w)
	#for c in w:
	#	print(w)
	#	count+=lu[c]

print(p)
p=sorted(p)
print(p[len(p)//2])
