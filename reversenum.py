'''Write a program to find the reverse of the given number
'''

def reverse(num):
    rev = 0
    while num>0:
        rev = rev *10+num%10
        num//=10
    return rev

def isPalindrome(num):
    return num==reverse(num)



print(reverse(1235))

print(reverse(1234))


print(isPalindrome(1236))

print(isPalindrome(1239))


print(reverse(12156))
print(isPalindrome(121))

def getPalindromes(start,end):
    res = ""
    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res[:-1]+"."

print(getPalindromes(1,10000))









