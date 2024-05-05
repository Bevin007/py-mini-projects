#Testing
#Function to encrypt/decrypt ROT(1-25) (only for lower case charectors)
def rot(text):
	alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	rot=int(input("Enter the which type of ROT algorithm you want(1-25) : "))
	if rot<0:
		print("Enter the correct algorithm !!")
	encrypted=[]
	for r in range(1):	
		for txt in text:
			for ch in alpha:
				if txt==ch:
					index=(alpha.index(txt)+rot) % 26
					encrypted.append(alpha[index])
	encrypted_string = ' '.join(encrypted)
	print(encrypted_string)
text=input("Enter the string you whants to encrypt:")
rot(text)
