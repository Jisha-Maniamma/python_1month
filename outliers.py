data=[4,5,104,105,110,115,119,120,122,130,140,150,160,177,180,189,191,350,360]
# del data[:2]
# print(data)
min=100
max=200
#delete values outside 100 to 200
for index,value in enumerate(data):
    if value<min or value>max:
        del data[index]

print(data)