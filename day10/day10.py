lengths = [97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190]
input = list(range(256))

def run_hash(input, lengths, repeat):
    """Returns the hash after reversing all the blocks of given lengths"""
    position = 0
    skip = 0
    for times in range(repeat):
        for length in lengths:
            if position + length < len(input):
                input[position:position + length] = reversed(input[position:position + length])
            else:
                # Transform the circular list to be reversed into a linear one and reverse it
                reversed_list = list(reversed(input[position:] + input[:(position + length) % len(input)]))
                input[position:] = reversed_list[:len(input) - position]
                input[:(position + length) % len(input)] = reversed_list[len(input) - position:]

            position = (position + length + skip) % len(input)
            skip += 1
    return input

# Part 1
hash = run_hash(input, lengths, 1)
print(hash[0] * hash[1])

# Part 2
def to_ascii(input):
    """Returns a character to byte conversion using ASCII codes"""
    converted = []
    for i in range(len(input)):
        converted.append(ord(input[i]))
    return converted

def to_dense_hash(hash):
    """Returns the dense hash from a sparse hash by XOR-ing 16 elements
    from consecutive blocks"""
    dense_hash = []
    for i in range(0, len(hash), 16):
        block = reduce(lambda x, y: x ^ y, hash[i:i+16])
        dense_hash.append(block)
    return dense_hash

def hex_form(hash):
    """Returns the hash formatted in hexadecimal form"""
    final_hash = ''
    for i in range(len(hash)):
        final_hash += format(hash[i], '02x')
    return final_hash

lengths = '97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190'
input = list(range(256))
skip = 0
position = 0

sequence = to_ascii(lengths) + [17, 31, 73, 47, 23]

# Run the 64 rounds of hashing
sparse_hash = run_hash(input, sequence, 64)
dense_hash = to_dense_hash(sparse_hash)

print(hex_form(dense_hash))