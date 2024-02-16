def arm(n):
    s=f'{n}'
    l=len(s)
    sum=0
    temp=n
    while temp>0:
        sum=sum+(temp%10)**l
        temp=temp//10
    if n==sum:
        return True
    else:
        return False
n=int(input())
if arm(n):
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')