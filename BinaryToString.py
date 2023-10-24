# Binary to String
# Import Modules
from bitarray import bitarray
# Inputing the data
data = "0100011101010011"
# Generating 8 bit boolean sequence
bits = bitarray(data)
# Store the Convertion data (Binary to string)
ascs = bits.tobytes().decode("ascii")
# Printing the result
print(ascs)