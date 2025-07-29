phone_keypad = {'1':'', '2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ' }
presses  = {'a':1, 'b':2, 'c':3, 'd':1, 'e':2, 'f':3, 'g':1, 'h':2, 'i':3,
            'j':1, 'k':2, 'l':3, 'm':1, 'n':2, 'o':3, 'p':1, 'q':2, 'r':3, 's':4,
            't':1, 'u':2, 'v':3, 'w':1, 'x':2, 'y':3, 'z':4, ' ':0}
user_input = input("Enter your text:")
total_clicks = 0
for char in user_input.upper():
    char = char.lower()
    total_clicks +=presses.get(char, 0)
print(f"Total number of clicks: {total_clicks}")