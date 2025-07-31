menu = [
    ["egg", "chicken"],
    ["spam", "egg"],
    ["bacon", "egg"],
    ["egg", "cheese", "bacon", "spam"],
    ["bacon", "egg", "spam", "spam"]
]
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            # print(meal)
            del meal[index]
    # print(meal)
    print(", ".join(meal))