import random
import string
from math import ceil

def random_word():
    word_list = ["View",
             "Controller",
            "Model",
            "Product Owner",
            "Team",
            "Scrum Master",
            "Ambiguity",
            "Incompleteness",
            "Precision",
            "Superkey",
            "Candidate Key",
            "Primary Key",
            "Foreign Key",
            "Data Definition Language",
            "Data Manipulation Language",
            "Data Control Language",
            "Inner Join",
            "Left Join",
            "Right Join",
            "Full Join",
            "Multitasking",
            "Interrupts",
            "Dispatcher",
            "Program",
            "Process",
            "Context Switch",
            "Preemptive Policy",
            "Non Preemptive Policy",
            "Batch System",
            "Interactive System"]
    defn_list = ["Manages the graphical and textual output to the display.",
               "Commanding the model and/or the view to change.",
               "Manages the behavior and data of the application domain.",
               "Representing the customer and responsible for the product backlog.",
               "Responsible for delivering shippable increments.",
               "Responsible for the overall Scrum process and facilitates communication.",
               "Open to more than one interpretation; inexactness.",
               "Not having all the necessary or appropriate parts",
               "The quality, condition, or fact of being exact and accurate.",
               "A set of one or more attributes that uniquely identifies an entity within a relation",
               "Any column or a combination of columns that can qualify as unique keys in database.",
               "A column or a combination of columns that uniquely identifies a record.",
               "An attribute or a set of attributes that matches the candidate key of some relation.",
               "A language for creating a database, defining and controlling access to data.",
               "A language for accessing a database by retrieving and updating data.",
               "A language for administering a database.",
               "Returns all rows when there is at least one match in BOTH tables.",
               "Return all rows from the left table, and the matched rows from the right table.",
               "Return all rows from the right table, and the matched rows from the left table.",
               "Return all rows when there is a match in ONE of the tables.",
               "Simultaneous running of two or more processes.",
               "Events that cause CPU to stop the current process and switch to the special process.",
               "Performs operation required by interrupt and decides which process to run next.",
               "Code ready to execute.",
               "Program, with its data, in the process of being executed.",
               "An action of storing state of current process and (re)starting another.",
               "A process that can be stopped at any point by timer interrupt.",
               "A process that can’t be stopped during regular operations.",
               "A system designed to run a series of programs without human interaction.",
               "A system designed to communicate with users."]
    
    try:
        choices = []
        chosen = random.randrange(len(word_list))
        word = word_list[chosen]
        ans = defn_list[chosen]
        choices.append(ans)
        defn_list.pop(chosen)
        for i in range(2):
            other = random.randrange(len(defn_list))
            choices.append(defn_list[other])
            defn_list.pop(other)
        random.shuffle(choices)
        return word,ans,choices
    except:
        return
    
def player_char(life):
    body = ["  x",
              "  o",
              "  o\n  |",
              "  o\n  |\n / ",
              "  o\n  |\n / \\",
              "  o\n /|\n / \\",
              "  o\n /|\\\n / \\",
             " o o\n /|\\\n / \\",
             " o o\n//|\\\n / \\",
             " o o\n//|\\\\\n / \\",
             " o o\n//|\\\\\n// \\",
             " o o\n//|\\\\\n// \\\\",
             " ooo\n//|\\\\\n// \\\\",
             "  o\n ooo\n//|\\\\\n// \\\\",
             "  o\n<ooo\n//|\\\\\n// \\\\",
             "  o\n<ooo>\n//|\\\\\n// \\\\",
             "  o\n<ooo>\n//|\\\\\n//w\\\\"]
    print(body[life])
    
def is_word_guessed(scrambled_word,full_word):
    #creates a string from a list, puts it to lower and compares it with the full word
    if "".join(scrambled_word).lower() == full_word:
        return True
    else:
        return False
    
def get_current_guess(usrinput,word_list,current_guess):
    for index,char in enumerate(word_list): #checking every character.
        if usrinput == char: #check if the input is in the secret word.
            current_guess[index] = usrinput #replace underscore with input
    return current_guess

def hint(life,scrambled_word,full_word):
    #make life shorter
    life = life - 1
    #take length of the word
    wordlen = len(scrambled_word)
    #variable stores how many letters to discover, rounded up
    toDiscover = wordlen*0.1
    toDiscover = ceil(toDiscover)
    h=0
    j=0
    while j < len(scrambled_word):
        if scrambled_word[j] == "_":
            scrambled_word[j] = full_word[j]
            h=h+1
        j=j+1
        if h == toDiscover:
            break
    return life,scrambled_word

def show_progress(life,current_guess,not_guessed):
    player_char(life)
    print("What you have now is: "," ".join(current_guess))
    print("Letters you have not yet tried: "," ".join(not_guessed),"\n")
    
def check_highest(life,highest):
    if life > highest:
        highest = life
    return highest

def confirmation(msg):
    while True:
        try:
            decision = input(msg)
            decision = decision.lower()
            print("")
            if decision == "yes":
                break
            elif decision == "no":
                print("Shame.\n")
                break
            elif decision == "rules":
                rules()
            else:
                raise ValueError
        except ValueError:
            print("Only type yes, no, or rules.\n")
    return decision

def rules():
    print("\nRules:")
    print("1. At the start of each session you get 6 chances with your character")
    print("2. Each bad choice of a letter looses you a limb")
    print("3. If you get all the letters right, you get a chance to re-grow one limb, if you select correct definition from available choices")
    print("More to come")
    
def start_round(i,chosen,ans,choices,life,highest):
    word = chosen.lower()
    current_guess = []
    word_list = []
    for char in word:
        word_list.append(char)
    guessed = []
    not_guessed = list(string.ascii_lowercase)
    length = len(word) - word.count(" ")
    for char in word:
        if char == " ":
            current_guess.append(" ")
        else:
            current_guess.append("_")
    print("Word randomed. You are on word number",i+1,"out of 10")
    print("The word has",length,"characters.")
    show_progress(life,current_guess,not_guessed)
    while life > 0:
        try:
            usrinput = input("Guess a letter or type 'hint' for help: ")
            usrinput = usrinput.lower()
            if usrinput == "hint":
                life,current_guess = hint(life,current_guess,word)
                if life == 0:
                    print("Weak.\n")
                    break
                else:
                    show_progress(life,current_guess,not_guessed)
                    continue
            elif usrinput == "" or len(usrinput) > 1:
                raise ValueError
            elif not usrinput.isalpha():
                raise TypeError
            else:
                if usrinput in guessed:
                    print("Already guessed.\n")
                    continue
                else:
                    guessed.append(usrinput)
                    not_guessed.remove(usrinput)
                    if not usrinput in word:
                        life -= 1
                current_guess = get_current_guess(usrinput,word_list,current_guess)
                show_progress(life,current_guess,not_guessed)
                if is_word_guessed(current_guess,word) == True:
                    print("Nice.")
                    print("The word is",chosen+".\n")
                    print("What is",chosen+"?")
                    ch = 1
                    for choice in choices:
                        print(str(ch)+".",choice)
                        if choice == ans:
                            correct = ch
                        ch += 1
                    print("")
                    while True:
                        try:
                            usrinput = int(input("Select the correct answer (1, 2, or 3): "))
                            if usrinput < 1 or usrinput > 3:
                                raise ValueError
                            elif usrinput == correct:
                                life += 1
                                highest = check_highest(life,highest)
                                print("Nice. You get an extra limb.\n")
                                break
                            else:
                                print("Wrong. The answer is: ")
                                print(ans,"\n")
                                break
                        except ValueError:
                            print("Either 1, 2, or 3.")
                            continue
                    break
                elif life == 0:
                    print("Weak.")
                    print("The word is",chosen+".\n")
                    break
        except ValueError:
            print("One char only.")
            continue
        except TypeError:
            print("Needs to be from a-z.")
            continue
    return life,highest
    
def start_session():
    life = 6
    highest = 6
    result = "won"
    for i in range(10):
        word,ans,choices = random_word()
        life,highest = start_round(i,word,ans,choices,life,highest)
        if life == 0:
            result = "lost"
            break
    return result,life,highest

def start_game():
    wins = 0
    loses = 0
    highest = 6
    print("Welcome to Hangman.")
    rules()
    decision = confirmation("Shall we start? yes, no, or rules: ")
    while decision == "yes":
        result,life,highest = start_session()
        if result == "won":
            wins += 1
        else:
            loses += 1
        decision = confirmation("Would you like another game? yes, no, or rules: ")
    print("You have survived",wins,"times.")
    print("You have died",loses,"times.")
    print("The highest form you have achieved is: ")
    player_char(highest)
    
start_game()
end_game = input("\nPress enter to exit.")
