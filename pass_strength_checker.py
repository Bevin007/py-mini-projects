only_num=False
only_lett=False
mix_num_and_lett=False
with_spec_chr=False
"""def num_or_char(passwd):
	for ch in passwd:
		if ch.isdigit():
			only_num=True"""
			
#function of finding low or up or both case in given password

def low_or_up(passwd):
	global only_lett_in_low
	global only_lett_in_up
	global contain_low_and_up
	only_lett_in_low=False
	only_lett_in_up=False
	contain_low_and_up=False
	for ch in passwd:
		if ch.islower():
			only_lett_in_low=True
		if ch.isupper():
			only_lett_in_up=True
		if only_lett_in_low and only_lett_in_up:
			contain_low_and_up=True
passwd=input("Enter your password: ")
length=len(passwd)
if (length==0):
	print("Please enter your password :")
else:
	low_or_up(passwd)
