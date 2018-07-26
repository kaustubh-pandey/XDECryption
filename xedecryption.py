with open("xecrypt.txt","r") as f:
	a=[]
	for line in f:
		#print(line.strip())
		a+=line.strip().split('.')
for i in a:
	if(i==""):
		a.remove(i)
code=[]
for i in range(0,len(a)-3,3):
	code.append(int(a[i])+int(a[i+1])+int(a[i+2]))
print(code)
print("Min val: ",min(code))
print("Max val: ",max(code))
freq=[]
for b in set(code):
	freq.append([code.count(b),b])
freq.sort()
freq=freq[::-1]
print("The most frequent character is:")
print(freq[0])
print("Enter a character to take it as most frequent character, press enter for default(default <space> )")
ch=input()

if(ch=="\n"):
	ch=" "
if(ch==""):
	ch=" "
key=freq[0][1]-ord(ch)
for i in range(len(code)):
	code[i]=chr(code[i]-key)
print("Decrypted!-------------------------")
print("".join(code))
	
