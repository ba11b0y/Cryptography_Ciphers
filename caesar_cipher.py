#Caesar Cipher
print("Enter the key")
key=input()
s=[]
x=0;y=1;
plaintext_arr=[]
encrypted_arr=[]
#Generating the encryption matrix
for i in key:
    if i not in s:
        s.append(i)
key=''.join(s)
matrix = [[0 for i in range(5)] for i in range(5)]

last_letter=''
c=0
i=-1
w=-1
while last_letter!=key[-1]:
    i+=1
    w+=1
    matrix[c][i]=key[w]
    last_letter=matrix[c][i]
    if i>=4:
        c+=1
        i=-1
flag=0
flag1=1
for alphabet in range(97,123):
    flag1=1
    for j in key:
        if j==chr(alphabet):
            flag=1
            break
        else:
            flag=0
    if flag==0 and i>=4 and chr(alphabet)!='j':
        c+=1
        i=0
        matrix[c][i]=chr(alphabet)
        flag1=0
    elif flag==0 and i<4 and flag1==1 and chr(alphabet)!='j':
        i+=1
        matrix[c][i]=chr(alphabet)
        flag1=1
    flag=0
#Printing the generated encryption matrixs
for g in matrix:
    print(g)
print("Enter the plaintext")
plaintext=input()
for i in plaintext:
	plaintext_arr.append(i)
if len(plaintext_arr)%2!=0:
    for i in range(len(plaintext_arr)-1):
        if plaintext_arr[i+1]==plaintext_arr[i]:
            plaintext_arr.insert(i+1,'x')
            break
if len(plaintext_arr)%2!=0:
    plaintext_arr.append('z')
print(plaintext_arr)
c=0;f=0;f1=0;
while c<len(plaintext_arr)/2:
	for i1 in matrix:
		for j in i1:
			if plaintext_arr[x]==j:
				f = 1
				break
		if f==1:
			break

	for i2 in matrix:
		for k in i2:
			if plaintext_arr[y]==k:
				f1=1
				break
		if f1==1:
			break
	if matrix.index(i1)!=matrix.index(i2) and matrix[matrix.index(i1)].index(j)!=matrix[matrix.index(i2)].index(k) and f==1 and f1==1:#if in different rows
		#print("in diff rows")
		encrypted_arr.append(i1[i2.index(plaintext_arr[y])])
		encrypted_arr.append(i2[i1.index(plaintext_arr[x])])
	elif matrix.index(i1)==matrix.index(i2):#if in same row
		#print("in same rows")
		if i1.index(plaintext_arr[x])+1==5:
			encrypted_arr.append(i1[0])
		else:
			encrypted_arr.append(i1[i1.index(plaintext_arr[x]) + 1])
		if i1.index(plaintext_arr[y])+1==5:
			encrypted_arr.append(i1[0])
		else:
			encrypted_arr.append(i1[i1.index(plaintext_arr[y])+1])
	else:#if in same column
		#print("in same col")
		if matrix.index(i1)+1==5:
			encrypted_arr.append(matrix[0][i1.index(plaintext_arr[x])])
		else:
			encrypted_arr.append(matrix[matrix.index(i1)+1][i1.index(plaintext_arr[x])])
		if matrix.index(i2)+1==5:
			encrypted_arr.append(matrix[0][i2.index(plaintext_arr[y])])
		else:
			encrypted_arr.append(matrix[matrix.index(i2)+1][i2.index(plaintext_arr[y])])

	f=0
	f1=0
	c+=1
	x+=2
	y+=2
print(encrypted_arr)
				

				 
