abo=['A','A','A','O','B','B','O','AB','AB','O']
a=0;b=0;o=0;ab=0
for blood in abo:
	if blood=='A':
		a+=1
	elif blood=='B':
		b+=1
	elif blood=='O':
		o+=1
	elif blood=='AB':
		ab+=1
count={'A':a,'O':o,'B':b,'AB':ab}
print(count)

