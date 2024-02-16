def upca(s):
    count=0
    for i in s:
        if i.isupper():
            count=count+1
    return count
def loca(s):
    count=0
    for i in s:
        if i.islower():
            count=count+1
    return count
def whsp(s):
    count=0
    for i in s:
        if i.isspace():
            count=count+1
    return count
s=input('Enter any string: ')
print(f'Uppercase: {upca(s)}')
print(f'Lowercase: {loca(s)}')
print(f'Whitespaces: {whsp(s)}')