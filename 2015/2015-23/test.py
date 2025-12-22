my_dict = {"apple": 5, "banana": 1, "cherry": 5, "date": 3, "elderberry": 5}

# Print the value of an item by key
print(f"{my_dict["banana"]=}")

# Attempting to print an item by non-existing key throws a KeyError exception
try:
    print(f"{my_dict["nada"]=}")
except KeyError:
    pass

my_dict["orange"] = 7

print(my_dict)


def parse(line: str):
    print(tuple(line.replace(",", " ").split()))


parse("inc a")
parse("jio a, +2")
