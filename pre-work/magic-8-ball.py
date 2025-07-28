import random
answer_dict = {
    1: "It is certain.",
    2: "It is decidedly so.",
    3: "Without a doubt.",
    4: "Yes, definitely.",
    5: "You may rely on it.",
    6: "As I see it, yes.",
    7: "Most likely.",
    8: "Outlook good.",
    9: "Yes.",
    10: "Signs point to yes.",
    11: "Reply hazy, try again.",
    12: "Ask again later.",
    13: "Better not tell you now.",
    14: "Cannot predict now.",
    15: "Cocentrate and ask again.",
    16: "Don't count on it.",
    17: "My reply is no.",
    18: "My sources say no.",
    19: "Outlook not so good.",
    20: "Very doubtful."
}
while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("Goodbye!")
        break
    else:
        answer_number = random.randint(1, 20)
        print(f"Magic 8-Ball says: {answer_dict[answer_number]}")