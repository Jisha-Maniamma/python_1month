data=[104,101,4,105,308,103,5,107,100,306,106,102,108]
min=100
max=200

i=len(data)-1
for index,value in enumerate(reversed(data)):
    print(i-index,value)
    if value<100 or value>200:
        del data[i-index]

print(data)