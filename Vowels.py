greetings = input("Enter a random word")
greetings=greetings.lower()
vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
for c in greetings:
    print(c)
    if c in vowels:
        vowels[c]+=1
print(vowels)