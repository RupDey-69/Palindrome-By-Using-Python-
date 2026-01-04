#Palindrome 

n=int(input("Enter the number:"))
palin_drome=0

while n>0:
    rem=n%10
    palin_drome= (palin_drome*10)+rem
    n=n//10

print("The Number Is Palindrome:",palin_drome)