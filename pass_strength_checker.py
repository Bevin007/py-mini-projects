#function to find number exist or not.
one_lett_in_low=False
one_lett_in_up=False
contain_low_and_up=False
full_of_low=False
full_of_up=False
num_present=False
full_of_num=False
only_lett_in_low=False
only_lett_in_up=False
spec_present=False

#function to find number exist in password or not
def num_exist(passwd):
	global full_of_num
	global num_present
	if passwd.isdigit():
		full_of_num=True
	for ch in passwd:
		if ch.isdigit():
			num_present=True
			break
	
#function of finding low or up or both case in given password and full passwd is upper or lower in case
def low_or_up(passwd):
	global one_lett_in_low
	global one_lett_in_up
	global contain_low_and_up
	global full_of_low
	global full_of_up
	if passwd.islower():
		full_of_low=True
	if passwd.isupper():
		full_of_up=True
	for ch in passwd:
		if ch.islower():
			one_lett_in_low=True
		if ch.isupper():
			one_lett_in_up=True
		if one_lett_in_low and one_lett_in_up:
			contain_low_and_up=True
			
#function to find the given password contains special charector or not 
def spec_or_not(passwd):
	global spec_present
	spec_char="@#$_&-+()/*:;!?~`|•√π÷×£¢€¥^°={}\%[]<>"
	for ch in passwd:
		if ch in spec_char:
			spec_present=True
			break

#making switch case using function bassed on length of password
def switch(length):
	#case 1 when password length is 3.
	if length==3:
		print("Instantly crackable ,kindly update your password !!")
	#case 2 when password length is 4.
	if length==4:
		print("Instantly crackable,kindly update your password !!")
	#case 3 when password length is 5.
	if length==5:
		if num_present==True and one_lett_in_low==True and one_lett_in_up==True:
			print("It is crackable within 3-10 seconds !!")
		else:
			print("Instantly crackable !!")
	#case 4 when password length is 6.
	if length==6:
		if contain_low_and_up==True :
			print("It is crackable within 8 seconds !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 3 Minutes !!")
		elif one_lett_in_low==True and one_lett_in_up==True and spec_present==True:
			print("It is crackable within 13 Minutes !!")
		else:
			print("It is instantly crackable,kindly update your password !!")
		#case 5 when password length is 7.
	if length==7:
		if contain_low_and_up==True :
			print("It is crackable within  5 Minutes !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 3 hours !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 17 hours !!")
		else:
			print("It is instantly crackable,kindly update your password !!")
		#case 6 when password length is 8.
	if length==8:
		if contain_low_and_up==True :
			print("It is crackable within  3 hours !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 10 days !!")
		elif one_lett_in_low==True and one_lett_in_up==True and spec_present==True:
			print("It is crackable within 57 days !!")
		else:
			print("It is instantly crackable,kindly update your password !!")
		#case 7 when password length is 9.
	if length==9:
		if full_of_num==True:
			print("It is crackable within 4 seconds !!")
		elif contain_low_and_up==True :
			print("It is crackable within  4 days !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 157 days !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 12 years !!")
		#case 8 when password length is 10.
	if length==10:
		if full_of_num==True:
			print("It is crackable within 40 seconds !!")
		elif contain_low_and_up==True :
			print("It is crackable within  169 days !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 1 year !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 928 years !!")
		#case 9 when password length is 11.
	if length==11:
		if full_of_num==True:
			print("It is crackable within 6 minutes !!")
		elif contain_low_and_up==True :
			print("It is crackable within  16 years !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 106 year !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 71000 years !!")
	    #case 10 when password length is 12.
	if length==12:
		if full_of_num==True:
			print("It is crackable within 1 hour !!")
		elif contain_low_and_up==True :
			print("It is crackable within  600 years !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 6000 years !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 5000000 years !!")
		#case 11 when password length is 13.
	if length==13:
		if full_of_num==True:
			print("It is crackable within 11 hour !!")
		elif contain_low_and_up==True :
			print("It is crackable within  21000 years !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 10800 years !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 423000000 years !!")
		#case 12 when password length is 14.
	if length==14:
		if full_of_num==True:
			print("It is crackable within 4 days !!")
		elif contain_low_and_up==True :
			print("It is crackable within  778000 years !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 25000000 years !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 5000000000 years !!")
		#case 13 when password length is 15.
	if length==15:
		if full_of_num==True:
			print("It is crackable within 46 days !!")
		elif contain_low_and_up==True :
			print("It is crackable within  28000000 years !!")
		elif one_lett_in_low==True and num_present==True:
			print("It is crackable within 1000000000 years !!")
		elif one_lett_in_low==True and one_lett_in_up and spec_present==True:
			print("It is crackable within 2000000000000 years !!")
		#case 14 when password length is 16 and above.
	if length>=15:
		print("It is still crackable !! but we don't have that much of time ")

#Actual program starting place
#Using while make the program execute n number of times
while True:
	#Geting input(password) from user 
	passwd=input("Enter your password (between 3-18 charectors) : ")
	#checking length of the password by len() function 
	length=len(passwd)
	#making condition to avoid 2 or less then 2 length of password
	if (length<3):
		print("Please enter your password : ")
	else:
		#function calling 
		low_or_up(passwd)
		num_exist(passwd)
		spec_or_not(passwd)
		switch(length)
