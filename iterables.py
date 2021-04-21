print(iter("This is a string")) # Str Iterable object

print(iter(["this", "is", "a", "list"])) # List iterable object

print(iter(1))
# Raises an error
# Integers can't be iterated