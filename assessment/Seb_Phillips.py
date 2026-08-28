from colorama import Fore, Back, Style; import time; import random

# countdown timer after a question is answered
BASE_COUNTDOWN = 2

# whether or not the questions should be shuffled first
SHUFFLE = True

# do question related stuff first, it just makes it easier to
# edit the questions if i have them all at the top
# and it also makes it easier to create the functions if i have
# a list of questions to refer to first

# capitalization in answers is already handled
q = [
    {
        "text": "Who plays the character Steve?",
        "answer": ["Jack Black", "Jack Blakc"],
        "ex": "Jack Black played Steve."
    },
    {
        "text": "Who plays the character Garret \"The Garbage Man\" Garrison?",
        "answer": ["Jason Momoa", "Jason Mamoa"],
        "ex": """Jason Momoa played Garret \"The Garbage Man\" Garrison.
He's also a New Zealander!"""
    },
    {
        "text": """What percentage of people who worked on the \
film were locals? (from New Zealand)""",
        "answer": "89%",
        "ex": "89% of the people behind the film were New Zealanders.",
        "multi": ["36%", "47%", "64%", "89%"]
    },
    {
        "text": "When did the film start planning?",
        "answer": "2014",
        "ex": """Planning for the film started way back in 2014, but had lots \
of problems\nduring this, which is why the movie released so long after.""",
        "multi": [2014, 2016, 2019, 2020]
    },
    {
        "text": "When is the sequel scheduled to release?",
        "answer": "July 2027",
        "ex": """The sequel, A Minecraft Movie Squared, is scheduled to \
release July 23rd, 2027.""",
        "multi": ["March 2027", "July 2027", "November 2027", "January 2028"]
    },
    {
        "text": "Where was most of the filming done?",
        "answer": ["New Zealand", "NZ"],
        "ex": "The majority of filming was done in New Zealand."
    },
    {
        "text": """Which of these are referenced in the movie?""",
        "answer": "20 minute day-night cycle",
        "ex": "Steve mentions that the day-night cycle lasts 20 minutes.",
        "multi": ["Pearl stasis", "20 minute day-night cycle",
                  "Boat clutch", "CaptainSparklez tribute"]
    },
    {
        "text": "How many directors did the movie have BEFORE the final one?",
        "answer": 3,
        "ex": """The film had three other directors before settling on their \
final one, including Shawn Levy, Rob McElhenney, and Peter Sollett.\
\nEventually, they settled on Jared Hess."""
    },
    {
        "text": """Which of these actresses is famous for her roles in both\
\nA Minecraft Movie and the Netflix series Wednesday?""",
        "answer": "Emma Myers",
        "ex": """Emma Myers played both Enid Sinclair in Wednesday, \
\nand Natalie in A Minecraft Movie.""",
        "multi": ["Danielle Brooks", "Jennifer Coolidge",
                  "Emma Myers", "Rachel House"]
    },
    {
        "text": """How much money was made off of \
the movie during opening weekend? (USD)""",
        "answer": "~$310 million",
        "ex": "A Minecraft Movie generated $313.7 million in one weekend.",
        "multi": ["~$250 million", "~$290 million",
                  "~$310 million", "~$340 million"]
    }
]
# this is still question stuff, just validates multichoices and
# shuffles the questions

# shuffle questions
if SHUFFLE: random.shuffle(q)
# converts any multichoices to lists if they arent already...
# mostly useless but a failsafe just in case
for i in q:
    if not type(i.get("multi", [])) is list:
        i["multi"] = [i["multi"]]

# get variables ready
total_correct = 0
total_asked = 0
question_num = 0

# now the main stuff
def clear():
    """Clears the terminal"""
    print("\033[H\033[J", end="")

def header(tc:int, ta:int, qn:int):
    """Returns a styled header.
    \ntc = total correct
    \nta = total asked
    \nqn = question number"""
    return f"""{Fore.BLUE}{Style.BRIGHT}\
Question {qn}/{len(q)}\t{Fore.RED}{tc}/{ta} correct"""

def ask(question: dict):
    '''Asks a question using values from a dictionary;
    \n"text" - The question asked
    \n"answer" - The answer to the question
    \n"ex" - An explanation for incorrect answers
    \n"multi" - An optional list of possible answers for multichoice questions
    '''

    if not type(question.get("answer", [])) is list:
        question["answer"] = [question["answer"]]

    # convert answer values to strings just in case they arent already
    question["answer"] = [str(item) for item in question["answer"]]

    # convert multichoice options to strings too so that they
    # correctly match when compared later
    if question.get("multi"):
        question["multi"] = [str(item) for item in question["multi"]]

    # check if the question has an answer, or if multichoice, check if
    # the multichoice options contain the answer. otherwise skip.
    if not question.get("answer", None):
        print("Question does not have an answer!")
        time.sleep(1)
        return
    elif question.get("multi"):
        if not any([a in question.get("multi")
                    for a in question.get("answer")]):
            print("Multichoice options do not contain the answer!")
            time.sleep(1)
            return

    # import global variables so we can use them here
    global total_correct
    global total_asked
    global question_num

    # status variables yk
    unanswered = True
    correct = False
    extra_text = None

    question_num += 1

    # keep asking until the user gives a valid answer
    while unanswered:
        # clear terminal, print header
        clear()
        print(header(total_correct, total_asked, question_num))

        # print the question
        print(f"{Fore.WHITE}{question["text"]}")

        # decide how to handle the question based
        # on whether or not it is multichoice
        if question.get("multi"):
            for i, v in enumerate(question.get("multi")):
                print(f"  {i+1}. {v}")
        else:
            unanswered = False

        if extra_text: print(extra_text)


        print(f"{Style.NORMAL}Your answer: {Style.BRIGHT}", end="")

        # get answer input, removing whitespace at start/end, lowercase,
        # and replacing consecutive whitespaces with single ones
        inp = " ".join(input().lower().strip().split())

        # if this was a multichoice, check if this is a valid answer
        if question.get("multi"):
            # try to convert input to a number; if possible and the index
            # is in the range of answers, set the question to answered.
            # otherwise, if the input is not a number, set the question
            # to answered.
            try:
                if int(inp) - 1 <= len(question.get("multi")) - 1:
                    if int(inp) >= 1:
                        unanswered = False
                        inp = int(inp) - 1

            except ValueError:
                unanswered = False

            # if the question has been answered with a valid input,
            # check if the given answer matches the real answer
            if not unanswered:
                if type(inp) == int:
                    if question.get("multi")[inp] in question.get("answer"):
                        correct = True
                else:
                    if inp in question.get("multi"):
                        unanswered = False
                        if inp in question.get("answer"):
                            correct = True
                    else:
                        unanswered = True
            # tell them their answer was invalid next time
            if unanswered:
                extra_text = f"'{inp}' is not a valid answer!"

        else:
            # if the answer is anywhere in the answers, it is correct
            correct = inp in [item.lower() for item in question.get("answer")]
            
    total_asked += 1
    clear()

    # checks if answer is correct and prints accordingly
    countdown = BASE_COUNTDOWN
    if correct:
        total_correct += 1
        print(f"""{header(total_correct, total_asked, question_num)}\
\n{Fore.BLUE}CORRECT!""")
    else:
        countdown = round(BASE_COUNTDOWN/2) + round(len(question.get("ex"))/28)
        print(f"""{header(total_correct, total_asked, question_num)}\
\n{Fore.RED}INCORRECT""")
        # print some info on the answer
        print(f"""{Style.NORMAL}\
{question.get("ex", question["answer"])}{Style.BRIGHT}""")

    # countdown to next question
    for i in range(countdown):
        print(f"\r{Style.BRIGHT}Proceeding in {countdown-i} ", end="")
        time.sleep(1)


# run through a try so that ctrl+c closes cleanly rather than erroring
try:
    # loop through questions and ask each
    for value in q:
        ask(value)

    # show results at the end
    clear()
    if total_correct/total_asked >= 0.5:
        print(f"{Fore.BLUE}You passed! ", end="")
    else:
        print(f"{Fore.RED}You failed... ", end="")
    print(f"""{Fore.WHITE}You answered \
{((total_correct/total_asked)*100):.1f}% of questions correctly.\n""")

# clean exit on keyboardinterrupt instead of erroring
except KeyboardInterrupt:
    clear()
    print(Style.RESET_ALL, end="")