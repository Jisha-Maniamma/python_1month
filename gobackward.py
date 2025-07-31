data=[104,101,4,105,308,103,5,107,100,306,106,102,108]
min=100
max=200

for index in range(len(data)-1,-1,-1):
     data_selected=data[index]
     if data_selected<100 or data_selected>200:
         del data[index]
print(data)

