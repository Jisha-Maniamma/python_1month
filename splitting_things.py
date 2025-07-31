panagram="""the  quick brown fox
 jumps over the\t lazy dog"""
word=panagram.split()
print(word)

numbers="9,5,6,7,8,8,5,4,3,3,5,6,3434,555,44"
print(numbers.split(","))
print(numbers)

Numbers=["1","2"," ","1","2","2"," ","2","2"," ","2"," "]
num1="".join(Numbers)
print(num1)
num2=num1.split()
print(num2)

for index,value in enumerate(num2):
    num2[index]=int(value)
print(num2)