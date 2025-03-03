#   Задание 1
import os
f=open('text.txt','r')
line=f.readline().lower()
s={}
while line:
    line=line.split()
    i1=0
    i2=''
    q=0
    t=[]
    min1=0
    for i in line:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
    for values in s.values():
        if values>i1:
            i1=values
    for keys , values in s.items():
        if values==i1:
            min1=keys
    for keys , values in s.items():
        if values==i1:
            if min1>keys:
                min1=keys
    print(min1,i1)
    line=f.readline().lower()
f.close()

#   Задание 2
# import re
# with open('text_1.txt.txt', 'r', encoding='utf-8') as forb, open(input(), 'r', encoding='utf-8') as text:
#     forbidden_words = forb.read().split()
#     out = text.read()
#     for w in forbidden_words:
#         out = re.sub(w, "*" * len(w), out, flags=re.I|re.M)
#     print(out)



#   Задание 3

f = open('Pupils.txt')
suma = 0
n = 0
for i in f:
    g = int(i[len(i)-2])
    suma += g
    n += 1
    if g < 3:
        print(i[:-1])
print('Средний балл: %.2f' % (suma/n))
f.close()
