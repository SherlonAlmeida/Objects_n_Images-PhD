"""
Description: Converting decimal to binary and removing the prefix(0b).
Input:
    n -> number to convert into binary,
    dtype -> type for the generated result: "string" or "int",
    n_bits -> number of bits for the binary value.
Output:
    The generated binary of a decimal number,
        binary -> as a string or,
        integer -> as a list of integers.
"""
def decimalToBinary(n, dtype="string", n_bits=3):
    binary = bin(n).replace("0b", "")
    curr_size = len(binary)
    new_size  = n_bits - curr_size
    binary = ("0"*new_size) + binary

    if dtype == "string":
        return binary
    elif dtype == "int":
        integer = [int(c) for c in binary]
        return integer

"""
Description: generates a list with all the permutation of angles in (x, y, z)
Input:
    angle -> rotation applied after each iteration.
Output:
    rotations -> a list containing all the possible combinations in 3D,
    count -> total number of combinations performed.
"""
def combine_rotations_3D(angle = 45):
    count = 0
    rotations = []
    for x in range(0, 361, angle):
        for y in range(0, 361, angle):
            for z in range(0, 361, angle):
                rotations.append([x,y,z])
                count += 1
    print(f"{count} rotations were created combining (x, y, z)")
    return rotations, count