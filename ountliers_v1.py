data=[4,5,104,105,110,115,119,120,122,130,140,150,160,177,180,189,191,350,360]
# data=[4,5,104,105,110,115,119,120,122,130,140,150,160,177,180,189,191]
# data=[104,105,110,115,119,120,122,130,140,150,160,177,180,189,191,350,360]
# data=[333,334,555,666,777,888]
# data=[]
# del data[:2]
# print(data)
min=100
max=200
#delete values outside 100 to 200
stop=0
#process low values in list
for index,value in enumerate(data):
    if value>=min:
        stop=index
        break
print(stop)
del data[:stop]
print(data)

#delete high values
start=0
# for index,value in enumerate(data):
#     if value>200:
#         start=index
#         break
# print(start)
# del data[start:]
# print(data)

for index in range(len(data)-1,-1,-1):
    if data[index]<=200:
        start=index+1
        break
print(start)
del data[start:]
print(data)

