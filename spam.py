menu = [
    ["egg", "chicken"],
    ["spam", "egg"],
    ["bacon", "egg"],
    ["egg", "cheese", "bacon", "spam"],
    ["bacon", "egg", "spam", "spam"]
]
for item in menu:
    if "spam" not in item:
        print(item)
    else:
        if item.count("spam")>1:
            for i in range(len(item)-1,-1,-1):
                if item[i]=="spam":
                    del item[i]
        else:
            item.remove("spam")
        print(item)
print("--------")
print(menu)