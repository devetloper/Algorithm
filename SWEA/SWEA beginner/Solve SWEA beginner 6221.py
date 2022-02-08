a=["가위","바위","보"]
man1=input()
man2=input()


man1_num=a.index(man1)
man2_num=a.index(man2)

if man1_num==0 and man2_num==2:
	print("Result : Man1 Win!")
elif man1_num==2 and man2_num==0:
	print("Result : Man2 Win!")
	
elif man1_num==man2_num:
	print("Result : Draw")

elif man1_num>man2_num:
	print("Result : Man1 Win!")
else:
	print("Result : Man2 Win!")

