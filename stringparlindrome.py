def checkPalindrome(inputString):
     if(inputString==inputString[: :-1]):
          return bool(1)
     else:
          return bool(0)
data=input('enter the string to check the palindrome')
print(checkPalindrome(data))
