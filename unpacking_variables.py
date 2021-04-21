string = "Let's learn Python"

# We want to assign the unpacked result in var1
var1 = [*string]

print(var1)

another_str = "The * operator"

# Using a list outside the unpacking
var2 = [*another_str]

print(type(var2)) # List

# Using a tuple
var3 = (*another_str,)

print(type(var3)) # Tuple