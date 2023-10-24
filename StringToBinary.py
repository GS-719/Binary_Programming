# String to Binary
# Inputing data
data = "GS"
# Convertion
result = "".join(format(ord(i), "08b") for i in data)
# Printing the result
print(result)