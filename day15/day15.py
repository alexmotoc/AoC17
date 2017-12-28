generator_A = 618
generator_B = 814

# Part 1
samples = 40000000
judge_count = 0

for i in range(samples):
    generator_A = (generator_A * 16807) % 2147483647
    generator_B = (generator_B * 48271) % 2147483647

    if generator_A & 0xFFFF == generator_B & 0xFFFF:
        judge_count += 1

print(judge_count)

# Part 2
samples = 5000000
judge_count = 0

def A():
    generator_A = 618

    while True:
        generator_A = (generator_A * 16807) % 2147483647
        if generator_A % 4 == 0:
            yield generator_A

def B():
    generator_B = 814

    while True:
        generator_B = (generator_B * 48271) % 2147483647
        if generator_B % 8 == 0:
            yield generator_B

a = A()
b = B()
for i in range(samples):
    if a.next() & 0xFFFF == b.next() & 0xFFFF:
        judge_count += 1

print(judge_count)