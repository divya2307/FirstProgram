def reverseString1(s):
    return s[::-1] #::1 is used to reverse the string

def reverseString2(s):
    rs = reversed(s)
    return "".join(rs)

def reverseString3(s):
    x = ''
    for i in range(len(s)):
        x += s[len(s)-1-i]
    return x

def main():
    userString = input("Enter a String")
    testString = reverseString1(userString)
    test = reverseString2(userString)

    x = reverseString3(userString)
    print(x)
    print(test)
    print(userString[:-1])
    if testString == userString:
        print("Palindrome")

    else:
        print("Not palindrome")



main()

