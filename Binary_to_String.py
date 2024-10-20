# Binary to String
# Import Modules
from bitarray import bitarray
# Inputing the data
data = "01000110 01110101 01100011 01101011 00100000 01111001 01101111 01110101 00100000 01100111 01110101 01110010 01101010 01101111 01110100"
# Generating 8 bit boolean sequence
bits = bitarray(data)
# Store the Convertion data (Binary to string)
ascs = bits.tobytes().decode("ascii")
# Printing the result
print(ascs)