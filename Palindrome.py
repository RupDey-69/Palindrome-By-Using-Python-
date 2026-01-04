n = int(input("Enter the number: "))
palindrome = 0
c = n   # original number save

while n > 0:
    rem = n % 10
    palindrome = palindrome * 10 + rem
    n = n // 10

if c == palindrome:
    print("The Number Is Palindrome:", c)
else:
    print("The Number Is Not Palindrome:", c)
