l=[]
a=None
while a!='end':
    print("\x1b[2J\x1b[H", end="")
    l.append(a)
    print('Enter Elements. Type "end" to stop:',end='')
    a=input()
l.sort
v=[]
f=[]
for i in range(len(l)):
    if l[i] not in v:
        v.append(l[i])
        f.append(1)
    else:
        f[v.index(l[i])]=v.index(l[i])+1
print('\x1b[2J\x1b[H')
print('Value\tFrequency')
for j in range(1,len(v)):
    print(v[j],'\t',f[j])
print('Created by Aviator-1230')
