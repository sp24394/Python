from colorama import Fore, Back, Style; import time; import random

q = [
    {
        "text": "test question?",
        "answer": "test answer",
        "ex": "it was test answer"
    },
    {
        "text": "test question 2?",
        "answer": "test answer 2",
        "ex": "it was test answer 2"
    }
]

random.shuffle(q)

def clear():
    print("\033[H\033[J", end="")

total_correct = 0 # total correct
total_asked = 0 # total questions

def header(tc:int, ta:int):
    return f"{Fore.BLUE}{Style.BRIGHT}Question 1/{len(q)}\t{Fore.RED}{tc}/{ta} correct"

def ask(question: dict):
    '''Asks a question using values from a dictionary;
    \n"text" - The question asked
    \n"answer" - The answer to the question
    \n"ex" - An explanation for incorrect answers'''
    global total_correct
    global total_asked

    clear()
    print(header(total_correct, total_asked))
    print(f"""{Fore.WHITE}{question["text"]}
\n{Style.NORMAL}Your answer: {Style.BRIGHT}""", end="")
    inp = " ".join(input().lower().strip().split())
    total_asked += 1

    clear()

    if inp == question["answer"]:
        total_correct += 1
        print(f"{header(total_correct, total_asked)}\n{Fore.GREEN}CORRECT!")
        for i in range(3):
            print(f"\r{Fore.WHITE}Proceeding in {3-i}", end="")
            time.sleep(1)
    else:
        print(f"{header(total_correct, total_asked)}\n{Fore.RED}INCORRECT")
        print(f"{Style.NORMAL}{question["ex"]}{Style.BRIGHT}")
        for i in range(3):
            print(f"\r{Fore.WHITE}Proceeding in {3-i}", end="")
            time.sleep(1)

for index, value in enumerate(q):
    ask(value)