parrot="tatama"

for char in parrot:
    print(char)

number="12,3,4,6.6;7343r33,35,2.w,weww,e456"
finalnumber=""
for n in number:
    if n.isnumeric():
        finalnumber+=n
print(finalnumber)