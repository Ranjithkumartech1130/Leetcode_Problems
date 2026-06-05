x=int(input("Enter the number: "))
s=str(x)
if s==s[::-1]:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")