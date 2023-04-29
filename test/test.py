a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

PRIME_NUMS = [2, 3, 5, 7]

print("a = [", end = "")
for i in a:
    print(i, end = "")

    if i != len(a):
        print(", ", end = "")
print("]")

b = a
for i in b:
    if i in PRIME_NUMS:
        b.remove(i)

print("b = [", end = "")
for i in b:
    print(i, end = "")

    if i != len(b):
        print(", ", end = "")
print("]")