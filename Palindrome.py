def palin(n):
    if n == int(f'{n}'[::-1]):
        return True
    else:
        return False
n=int(input())
if palin(n):
    print(f'{n} is a palindrome number')
else:
    print(f'{n} is not a palindrome number')