#ROT13 (Test)
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text=input("Enter the string: ")
for txt in text:
	for ch in alpha:
		if txt==ch:
			index=alpha.index(txt)
			print("  ",alpha[index+13])
