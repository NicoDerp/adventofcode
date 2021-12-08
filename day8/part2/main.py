with open('input','r') as f:
	#nums=list(map(lambda i:i.split('|'),f.read().split('\n')))
	nums=[]
	for s in f.read().split('\n'):
		if s=='':break
		a,b=s.split(' | ')
		#if b[0]==' ':b=b[1:]
		#if a[-1]==' ':a=a[:-1]
		nums.append([a.split(' '),b.split(' ')])

# Remove b from a
def removeFromString(a,b):
	for c in b:
		a=a.replace(c,'')
	return a

dic={'0':'abcefg', '1':'cf', '2':'acdg', '3':'acdfg', '4':'bcdf', '5':'abdfg', '6':'abdefg', '7':'acf', '8':'abcdefg', '9':'abcdfg'}
idic={v:k for k,v in dic.items()}

s=0
for i in nums:
	o={'a':'','b':'','c':'','d':'','e':'','f':'','g':''}
	k={}
	output=[-1,-1,-1,-1]
	for j,n in enumerate(i[1]):
		l=len(n)
		if l==2:k['1']=n;output[j]='1' # 1
		elif l==4:k['4']=n;output[j]='4' # 4
		elif l==3:k['7']=n;output[j]='7' # 7
		elif l==7:k['8']=n;output[j]='8' # 8
		#else:uk.append(n)
	known = k
	if -1 in output:
		#for n in uk:
			#print(n)
		k={}
		for n in i[0]:
			l=len(n)
			if l==2:k['1']=n
			if l==4:k['4']=n
			if l==3:k['7']=n
			if l==7:k['8']=n
		o['a']=removeFromString(k['7'],k['1'])
		bd=removeFromString(k['4'],k['1'])
		cf=k['1']
		for j,n in enumerate(i[1]):
			l=len(n)
			#print(l)
			if l in [2,4,3,7]:
				#print(n)
				continue
			# 5,6,9
			if bd[0] in n and bd[1] in n:
				# 5,6
				if (cf[0] in n and not cf[1] in n) or (not cf[0] in n and cf[1] in n):
					# 5
					if l==5:
						output[j]='5'
					# 6
					elif l==6:
						output[j]='6'
				# 8,9
				elif cf[0] in n and cf[1] in n:
					# 8
					#if l==7:
					#	output[j]='8'
					# 9
					if l==6:
						output[j]='9'
			# 0,2,3
			else:
				#print(l)
				# 2
				if (cf[0] in n and not cf[1] in n) or (not cf[0] in n and cf[1] in n):
					output[j]='2'
				# 3
				elif l==5:
					output[j]='3'
				# 0
				elif l==6:
					output[j]='0'


	print(output)
	s+=int(''.join(output))

print(s)
