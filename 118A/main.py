s = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']


for c in s:
    if c.lower() not in vowels:
        print(f".{c.lower()}", end="")