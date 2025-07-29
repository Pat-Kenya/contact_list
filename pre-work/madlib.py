print("Let's play mad libs!")
noun = input("Enter a noun: ")
while not noun.isalpha():
    print("Please enter a valid noun (letters only).")
    noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
while not verb.isalpha():
    print("Please enter a valid verb (letters only).")
    verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
while not adjective.isalpha():
    print("Please enter a valid adjective (letters only).")
    adjective = input("Enter an adjective: ")
age = input("Enter an age: ")
while not age.isdigit():
    print("Please enter a valid age (numbers only).")
    age = input("Enter an age: ")
print("\nHere's your mad lib:")
print(f"Once upon a time, there was a {adjective} {noun} who loved to {verb}. At the age of {age}. even though they were only {age} years old, they became legends in their town!")