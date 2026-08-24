from colorama import Fore, Back, Style; import time; import random

# make all answers strings for simplicity
# capitalization in answers is already handled
q = [
    {
        "text": "Who plays the character Steve?",
        "answer": "Jack Black",
        "ex": "Jack Black played Steve."
    },
    {
        "text": "Who plays the character Garret \"The Garbage Man\" Garrison?",
        "answer": "Jason Momoa",
        "ex": """Jason Momoa played Garret \"The Garbage Man\" Garrison.
He's also a New Zealander!"""
    },
    {
        "text": """What percentage of people who worked on the \
film were locals? (from New Zealand)""",
        "answer": "89%",
        "ex": "89% of the people behind the film were New Zealanders.",
        "multi": ["36%", "47%", "64%", "89%"]
    }
]

#shuffle questions
random.shuffle(q)

for i in q:
    if i.get("multi") and not type(i.get("multi")) is list:
        list(i.get("multi"))

def clear():
    """Clears the terminal"""
    print("\033[H\033[J", end="")

total_correct = 0
total_asked = 0

def header(tc:int, ta:int):
    """Returns a styled header.
    \ntc = total correct
    \nta = total asked"""
    return f"""{Fore.BLUE}{Style.BRIGHT}\
Question {ta+1}/{len(q)}\t{Fore.RED}{tc}/{ta} correct"""

def ask(question: dict, qnumber: int = 0):
    '''Asks a question using values from a dictionary;
    \n"text" - The question asked
    \n"answer" - The answer to the question
    \n"ex" - An explanation for incorrect answers
    \n"multi" - An optional list of possible answers for multichoice questions
    '''

    if question.get("answer", None) is None:
        print("Question does not have an answer!")
        return
    elif question.get("multi"):
        if not question.get("answer") in question.get("multi"):
            print("Multichoice options do not contain the answer!")
            return

    # import global variables so we can use them here
    global total_correct
    global total_asked

    unanswered = True
    correct = False
    extra_text = None
    while unanswered:
        # clear terminal, print header
        clear()
        print(header(total_correct, total_asked))

        #print the question
        print(f"{Fore.WHITE}{question["text"]}")

        #decide how to handle the question based
        #on whether or not it is multichoice
        if question.get("multi"):
            for i, v in enumerate(question.get("multi")):
                print(f"  {i+1}. {v}")
        else:
            unanswered = False

        if extra_text: print(extra_text)

        print(f"{Style.NORMAL}Your answer: {Style.BRIGHT}", end="")

        #get answer input, removing whitespace at start/end
        #and removing consecutive whitespaces in sequence
        inp = " ".join(input().lower().strip().split())

        #if this was a multichoice, check if this is a valid answer
        if question.get("multi"):
            #try to convert input to a number; if possible and the index
            #is in the range of answers, set the question to answered.
            #otherwise, if the input is not a number, set the question
            #to answered.
            try:
                if int(inp) - 1 <= len(question.get("multi")) - 1:
                    if int(inp) >= 1:
                        unanswered = False
                        inp = int(inp) - 1

            except ValueError:
                unanswered = False
                pass
            
            if not unanswered:
                if type(inp) == int:
                    if question.get("answer") == question.get("multi")[inp]:
                        correct = True
                else:
                    if inp in question.get("multi"):
                        unanswered = False
                        if question.get("answer").lower() == inp:
                            correct = True
                    else:
                        unanswered = True

            if unanswered:
                extra_text = f"'{inp}' is not a valid answer!"

        else:
            correct = inp == question.get("answer").lower()
            
    total_asked += 1
    clear()

    # checks if answer is correct and prints accordingly
    COUNTDOWN = 2
    if correct:
        total_correct += 1
        print(f"{header(total_correct, total_asked)}\n{Fore.BLUE}CORRECT!")
    else:
        COUNTDOWN = 5
        print(f"{header(total_correct, total_asked)}\n{Fore.RED}INCORRECT")
        print(f"{Style.NORMAL}{question["ex"]}{Style.BRIGHT}")

    #countdown to next question
    for i in range(COUNTDOWN):
        print(f"\r{Style.BRIGHT}Proceeding in {COUNTDOWN-i}", end="")
        time.sleep(1)

#loop through questions and ask each
for index, value in enumerate(q):
    ask(value, index)