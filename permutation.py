def combo(k,available,used):
	if len(used)==k:
		#print("Available and used in if : ",available,used)
		yield list(used)
	elif len(available)==0:
		pass
	else:
		head=available.pop(0)
		#print("head in else : ",head)
		used.append(head)
		#print("Available and used in else : ",available,used)
		for c in combo(k,available[:],used[:]):
			yield c
		used.pop()
		for c in combo(k,available[:],used[:]):
			yield c
	

l=[1,2,3,4]
k=2	
#for k in range(len(l)):
mycombs = [c for c in combo(k,l,[])]
print(mycombs)
