"""s="bacab"
if s==s[::-1]:   
    print(s,"It is palindrome")
#main program""" 
s=input("Enter the string:")
longest=""
for i in range(len(s)):
    current=""
    for j in range(i,len(s)):
        current=current+s[j]
        if current==current[::-1]:
            if len(current)>len(longest):
                longest=current
print(longest,"is the longest palindrome substring")