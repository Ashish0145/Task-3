import time
import os

pathname = os.path.abspath(__file__)
curr_directory = os.path.dirname(os.path.abspath(__file__))

today = time.ctime()

bot = {
    "hi":"Hello", "Hi":"hey!" ,
    "who are you?":"My name is Rusky! I am your personal ChatBot",
    "how are you?":"absolutely fine! What about you?",
    "I am fine too":"cool! what can i do for you?",
    "Can you tell me who is father of Python":"Guido van Rossum is known as Father of Python Programming language",
    "what kind of music do you like?":"i love rock music",
    "can you tell me today's date and time": today,
    "what type of language you use?":"English! and I was written in Python Programming language.",
    "Hello":"Hey there! Good to see you again",
    "Can you tell me this file's path?":pathname,
    "Can you tell me its directory also?":curr_directory,
}


while True:

    ques = input()

    if(ques == "quit" ):
        print("See you soon, Bye")
        break

    else:
        print(bot[ques])

