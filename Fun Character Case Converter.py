a = input()
if a.islower() and a.isalpha():
    print(a.upper())
elif a.isupper() and a.isalpha():
    print(a.lower())
else:
    print("abcd theriyatha?")
