with open('input','r') as f:
	code=f.read().split('\n')

code.pop()
lu={')':3,']':57,'}':1197,'>':25137}

syntax={'(':')','[':']','{':'}','<':'>'}

count=0
for l in code:
	s=[]
	#w=[]
	for c in l:
		if c in syntax:s.append(c)
		else:
			#print(l, c)
			if syntax[s[-1]]!=c:count+=lu[c];break #w.append(c)
			else:s.pop()
	#print(w)
	#for c in w:
	#	print(w)
	#	count+=lu[c]

print(count)
