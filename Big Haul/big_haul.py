import sys
import time
from threading import Timer
import pyfiglet
import random


#Game class, contains attribute and methods relevant througout the entire game
class Game:
    def __init__(self, participant):
        self.participant = participant
        self.life = 3
        self.bank = 0
        
    #adds to users bank if they get an aswer correct
    def correct(self):
        if player.bank == 0:
            setattr(player, "bank", 100)
        else:
            setattr(player, "bank", (self.bank*2))
        print(f'your new bank total is: ${player.bank}')
    #takes life from user if incorrect, when lives reach 0 there is a game over
    def incorrect(self):
        setattr(self, "life", self.life-1)
        print(f'you have {self.life} lives remaining!')
        if self.life == 0:
            print(pyfiglet.figlet_format("GAME  OVER !"))
            setattr(self, "bank", 0)
            time.sleep(2)
            print(f'well unfortunately {self.participant} you have run out of lives...')
            time.sleep(2)
            print(f'your new bank total is ${self.bank}')
            time.sleep(2)
            print(f'unfortunately our time together has come to an end')
            time.sleep(2)
            print(f"we hope you'll join us again on THE BIG HAUL")
            #rip
            sys.exit()
            
    #run if player fails the final all or nothing round
    def incorrect_final(self):
            setattr(self, "life", 0)
            time.sleep(2)
            print(f"Unfortunately this means you've lost all the money you've earned so far...")
            time.sleep(2)
            print(pyfiglet.figlet_format("GAME  OVER !"))
            setattr(self, "bank", 0)
            time.sleep(2)
            print(f"well unfortunately today you'll be going home empty handed...")
            time.sleep(2)
            print(f'Cheer up {self.participant} theres always next time!')
            time.sleep(2)
            print(f"we hope you'll join us again on THE BIG HAUL")
            #rip
            sys.exit()
    

    #Function should the user decide to their current bank and walk away, used between rounds
    def take_home(self):
        time.sleep(2)
        print(f'you have decided take home your winnings up to this point...')
        time.sleep(2)
        print(pyfiglet.figlet_format("YOU  WIN !"))
        time.sleep(2)
        print(f"Today you will be taking home ${self.bank} CONGRATULATIONS!!!")
        time.sleep(2.5)
        print(f'It has been so good having you come on the show today {self.participant}')
        time.sleep(2)
        print(f'dont be shy, come back anytime')
        sys.exit()

    def big_haul(self):
        haul = 500000 - self.bank
        setattr(player, "bank", 500000)
        time.sleep(2)
        print(f"You won ${haul} boosting your total to ${self.bank}")
        time.sleep(3)
        print(pyfiglet.figlet_format("YOU  WIN !"))
        time.sleep(2)
        print(f'It has been so good having you come on the show today {self.participant}')
        time.sleep(2)
        print(f'And congratulations on making it all the way to the end, claiming the Big Haul')
        time.sleep(2)
        print(f'dont be shy, come back anytime')
        sys.exit()
        
#person class used in round 4
class Person:
    def __init__(self, name, age, work, appearence, country, networth, work2):
        self.name = name
        self.work = work
        self.age = age
        self.apperance = appearence
        self.country = country
        self.networth = networth
        self.work2 = work2
        self.hints = 3
    #the hint function that reveals attributes of the person class in round 4
    def hint(self, hint):
        if hint == "age":
            return "This person is "+self.age+" years old"
        elif hint == "appearance":
            return "The appearence person is "+self.apperance
        elif hint == "country":
            return "This person is "+self.country
        elif hint == "networth":
            return "This person is worth "+self.networth
        elif hint == "work2":
            return "This person also made "+self.work2

    def __str__(self):
        return "A person whom the contestant must guess by their attributes"


#Function that initiates a round 1 question
def round_1_question(file_q, q_num):
    #opens question from text file in the database
    with open(file_q) as file:
        options = []
        lines = file.read().split("\n")
        for line in lines:
            options.append(line)
    question = options[0]
    answer = options[1]
    choices = options[1:]
    random.shuffle(choices)
    a = choices[0]
    b = choices[1]
    c = choices[2]
    d = choices[3]


    print("Question " + q_num)
    print("-----------------------------------")
    print(question)
    print("A: " + a)
    print("B: " + b)
    print("C: " + c)
    print("D: " + d)
   
    selection = {"A":choices[0], 'B': choices[1], 'C':choices[2], 'D':choices[3]}
    usr_inp = input("Type your answer: ").upper()
    
    while usr_inp not in selection.keys():
        print("")
        print("A: " + a)
        print("B: " + b)
        print("C: " + c)
        print("D: " + d)
        usr_inp = input("please pick from the options availible above: ").upper()
        
    if selection.get(usr_inp) == answer:
        time.sleep(2)
        print("correct!")
        time.sleep(2)
        print("well done")
        time.sleep(2)
        player.correct()
    else:
        time.sleep(2)
        print("incorrect :(")
        time.sleep(2)
        print("better luck next time")
        time.sleep(2)
        print("The correct answer was "+answer)
        player.incorrect()

#function that initiates a round 2 question
def round_2_question(file_q, q_num):
    #opens and reads a file
    with open(file_q) as file:
        options = []
        #splits each line into a list
        lines = file.read().split("\n")
        #adds each line to options
        for line in lines:
            options.append(line)
    #sets values
    old_comp = options[3]
    value_old = options[4]
    question = options[0]
    new_comp = options[1]
    value_new = options[2]
    with open("round2/v-old.txt") as filev: #Opens file and updates new values with the old values
        rows =[]
        row = filev.read().split("\n")
        #adds each line to rows
        for value in row:
            rows.append(value)
        #if the file has 2 or more inputs then update values
        if len(rows) >= 2:
            value_old = rows[0]
            old_comp = rows[1]
        filev.close()
    #if old comparison is same as new comparison the change old comparison and its value
    if old_comp == new_comp:
        old_comp = options[3]
        value_old = options[4]
    print("Question " + q_num)
    print("-----------------------------------")
    print(question + old_comp + " ?")
    print("Higher")
    print("Lower")

   
   #Available options
    selection = ["higher", "lower"]
    usr_inp = input("Type your answer: ").lower()

    #Sets the answer
    if value_new < value_old:
        answer = "lower"
    elif value_new > value_old:
        answer = "higher"
    else:
        answer = "Draw"

    #Checks if the input is part of the options available
    while usr_inp not in selection:
        print("")
        print("The answer is case sensitive you spelled: " + usr_inp)
        print("Higher")
        print("Lower")
        usr_inp = input("please pick from the options availible: ").lower()

    #If user is correct saves the values to file and runs correct function
    if answer == "Draw":
        #if true update 
        old_comp = new_comp
        value_old = value_new
        #reads the saved file
        with open("round2/v-old.txt") as filev:
            line = filev.read().split("\n")
            filev.close()
        for q in line:
            #if the file has values saved then clear the file
            if len(q) >= 2:
                f = open("round2/v-old.txt","w")
                f.close()
        #adds the new values
        with open("round2/v-old.txt", 'a') as filev:
            filev.write(value_old + "\n")
            filev.write(old_comp + "\n")
            filev.close()
            time.sleep(2)
            print("Lucky")
            time.sleep(2)
            print("congrats!")
            time.sleep(2)
            player.correct()
    elif usr_inp == (answer):
        #if true update 
        old_comp = new_comp
        value_old = value_new
        #read saved file
        with open("round2/v-old.txt") as filev:
            line = filev.read().split("\n")
            filev.close()
        for q in line:
            #if file has inputs clear the file
            if len(q) >= 2:
                f = open("round2/v-old.txt","w")
                f.close()
        #add new values
        with open("round2/v-old.txt", 'a') as filev:
            filev.write(value_old + "\n")
            filev.write(old_comp + "\n")
            filev.close()
            time.sleep(2)
            print("correct!")
            time.sleep(2)
            print("well done")
            time.sleep(2)
            player.correct()
    #If User is wrong updates values and runs incorrect function
    else:
        #update values
        old_comp = new_comp
        value_old = value_new
        #read save file
        with open("round2/v-old.txt") as filev:
            line = filev.read().split("\n")
            filev.close()
        for q in line:
            #if file has inputs then clear file
            if len(q) >= 2:
                f = open("round2/v-old.txt","w")
                f.close()
        #add new values
        with open("round2/v-old.txt", 'a') as filev:
            filev.write(value_old + "\n")
            filev.write(old_comp + "\n")
            filev.close()
        time.sleep(2)
        print("incorrect :(")
        time.sleep(2)
        print("better luck next time")
        time.sleep(2)
        player.incorrect()

#function
def round_3_question(file_q, q_num):
    # opens file corresponding to round3 and random questions
    with open(file_q) as file:
        options = []
        lines = file.read().split("\n")
        for line in lines:
            options.append(line)
    question = options[0]
    # the first index of the file is the question
    answer = options[1:]
    # answer everything from index 1 and onwards
    a = answer[0]
    b = answer[1]
    c = answer[2]
    d = answer[3]

    time.sleep(3)
    print(f"Question {q_num}")
    print("-----------------------------------")
    print(question)
    time.sleep(2)

    selection = [a, b, c, d] 
    # they are all correct answers, just spelt differently so user has no problem with spelling issues
    correct_lst = [f"Well done! {a} is correct!", f"Excellent! {a} is correct!", f"Wooo, you got it this! {a} is correct!", f"Sensational! {a} is correct!",f"Stunning! {a} is correct!", f"Incredible! {a} is correct!"] 
    # a being the first index => correctly spelt answer
    incorrect_lst = [f"Hard Luck, it was {a}", f"That was a tough question, the answer was {a} ", f":( that's incorrect, it was {a}", f"Sorry that is incorrect!, it was {a}"]
    timeout = 15
    # the countdown will finish when it reaches 15 seconds
    t = Timer(timeout, print, ['\nYou have run out of time\n\nPlease press "Enter" to proceed'])
    # outputted when timeout
    # start timer now
    print("You have %d seconds to answer this question, good luck!...\n" % timeout)
    t.start()
    usr_inp = input("type here: ") 

    t.cancel()
    # stop timer
    if usr_inp.lower() in [ans.lower() for ans in selection]:
        # if input lowercased is in selection list lowercased
        print(random.choice(correct_lst))
        # print random way of congratulating user from "correct_lst"
        player.correct()

    else:
        print(random.choice(incorrect_lst))
        # print random way of consoling user from "incorrect_lst"
        player.incorrect()

print("Helloooo ladies and gentlemen")
time.sleep(2)
print("my name is Johnny Jackpot and welcome to...")
time.sleep(4)
print(pyfiglet.figlet_format(" THE  BIG  HAUL !"))
time.sleep(2)
print("Today I am joined by our very special contestant")
time.sleep(3)
cont_name = input("Tell me, what is your name? ").capitalize()
while not cont_name.strip():
    cont_name = input("Please enter a valid name: ")
player = Game(cont_name)
print("It's a pleasure to meet you " + player.participant)
time.sleep(3)
address = input("and where are you from " + player.participant + "? ").capitalize()
while not address.strip():
    address = input("Please enter a valid address: ")
print(address + " really... I heard that place is a bit of a kip")
time.sleep(2)
ready = input("Now " + cont_name + " from " + address + " are you ready? If so I wanna hear you say YESSIR! ")
while "y".upper() not in ready.upper():
    ready = input("I can't hear you... ")
time.sleep(2)
print("")
print("THEN IT'S ONTO THE FIRST ROUND!")
time.sleep(2)
print("The first round will consist of FOUR  general knowledge questions")
time.sleep(2)
print("brace yourself....")
time.sleep(2)
print(pyfiglet.figlet_format("ROUND ONE !"))
time.sleep(2)
# # FIRST ROUND

round1_questions = ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt", "Q5.txt", "Q6.txt", "Q7.txt", "Q8.txt", "Q9.txt", "Q10.txt", "Q11.txt", "Q12.txt"]

with open("round1/r-hist.txt") as fileh:
    line = fileh.read().split("\n")
    fileh.close()
for q in line:
    if len(line) >= 8:
        f = open("round1/r-hist.txt","w")
        f.close()
    elif q != "":
        round1_questions.remove(q)
random_choice = random.choice(round1_questions)


loop = 1
while loop < 5:
    round_1_question(f"round1/{random_choice}", str(loop))
    round1_questions.remove(random_choice)
    with open("round1/r-hist.txt", "a") as fileh:
        fileh.write(random_choice + "\n")
        fileh.close()

    random_choice = random.choice(round1_questions)
    loop += 1
    time.sleep(2)
    print("")

#Intermediary between Rounds 1 & 2
time.sleep(2)
print("Congratulations on the first round!!!!")
time.sleep(2)
print(f"You've won ${player.bank} so far!!!")
time.sleep(2)
print("Would you like to take your money and split?")
time.sleep(2)
y_n = ["yes", "no", "y", "n"]
exit_input = input("Or will you stick around and add to your rapidly growing fortune? (yes/no) ").lower()
while exit_input not in y_n:
    print("")
    time.sleep(2)
    exit_input = input(f"You're answer must consist of either YES or NO {player.participant}, try again ")
if exit_input == "yes" or exit_input == "y" :
    player.take_home()
time.sleep(2)
print("You're shaping up to be challenging competitor")
time.sleep(2)
print("This next round will consist of FOUR questions")
time.sleep(2)
print("Each question will present you with a statement comparing two topics...")
time.sleep(3)
print("It is your job to decide whether the 1st topic is higher or lower in terms of popularity than the 2nd!")
time.sleep(3.5)
print(pyfiglet.figlet_format("ROUND TWO !"))

#SECOND ROUND
round2_questions = ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt", "Q5.txt", "Q6.txt", "Q7.txt", "Q8.txt", "Q9.txt", "Q10.txt", "Q11.txt", "Q12.txt"]

with open("round2/r-hist.txt") as fileh:
    line = fileh.read().split("\n")
    fileh.close()
for q in line:
    if len(line) >= 8:
        f = open("round2/r-hist.txt","w")
        f.close()
    elif q != "":
        round2_questions.remove(q)
random_choice = random.choice(round2_questions)

loop = 1
while loop < 5:
    round_2_question(f"round2/{random_choice}", str(loop))
    round2_questions.remove(random_choice)
    with open("round2/r-hist.txt", "a") as fileh:
        fileh.write(random_choice + "\n")
        fileh.close()
    random_choice = random.choice(round2_questions)
    loop += 1
    time.sleep(2)
    print("")

f = open("round2/v-old.txt","w")
f.close()

time.sleep(2)
print("WOW you survived 2 rounds!!!")
time.sleep(1)
print("It's time to step things up a notch")
time.sleep(1)
print(f"You've won ${player.bank} so far!!!")
time.sleep(2)
print("Would you like to take your money and split?")
time.sleep(2)
y_n = ["yes", "no", "y", "n"]
exit_input = input("Or will you stick around and add to your rapidly growing fortune? (yes/no) ").lower()
while exit_input not in y_n:
    print("")
    time.sleep(2)
    exit_input = input(f"You're answer must consist of either YES or NO {player.participant}, try again ")
if exit_input == "yes" or exit_input == "y" :
    player.take_home()
print("This next round will consist of SIX questions")
time.sleep(2)
print("You will be asked a question and given 15 seconds to answer the question correctly")
time.sleep(3)
print("Will you buckle under the pressure?")
time.sleep(1)
print("Lets find out!!")
time.sleep(2)
print(pyfiglet.figlet_format("ROUND THREE !"))


#THIRD ROUND
round3_questions = ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt", "Q5.txt", "Q6.txt", "Q7.txt", "Q8.txt", "Q9.txt", "Q10.txt", "Q11.txt", "Q12.txt"]


with open("round3/r-hist.txt") as fileh:
    line = fileh.read().split("\n")
    fileh.close()
for q in line:
    if len(line) >= 6:
        f = open("round3/r-hist.txt","w")
        f.close()
    elif q != "":
        round3_questions.remove(q)
random_choice = random.choice(round3_questions)

loop = 1
while loop < 7:
    round_3_question(f"round3/{random_choice}", str(loop))
    round3_questions.remove(random_choice)
    with open("round3/r-hist.txt", "a") as fileh:
        fileh.write(random_choice + "\n")
        fileh.close()
    random_choice = random.choice(round3_questions)
    loop += 1
    time.sleep(2)
    print("")

time.sleep(2)
print("HOLY GUACAMOLE")
time.sleep(2)
print("You've beaten 3 rounds exceptional!!")
time.sleep(2)
print("Time to shake thing up")
time.sleep(2)
print(f"You've won ${player.bank} so far!!!")
time.sleep(2)
print("Would you like to take your money and split?")
time.sleep(2)
y_n = ["yes", "no", "y", "n"]
exit_input = input("Or will you stick around and add to your rapidly growing fortune? (yes/no) ").lower()
while exit_input not in y_n:
    print("")
    time.sleep(2)
    exit_input = input(f"You're answer must consist of either YES or NO {player.participant}, try again ")
if exit_input == "yes" or exit_input == "y" :
    player.take_home()
print("This final round will only consist of ONE question")
time.sleep(2)
print("You will be given 3 categories to choose from")
time.sleep(2)
print("In your chosen category will be a famous person in which you must guess the name of")
time.sleep(3)
print("You will have a choice to accept 3 hints about this person")
time.sleep(2)
print("This is all or nothing GOOD LUCK!!")
time.sleep(3)
print(pyfiglet.figlet_format("ROUND FOUR !"))

#FOURTH ROUND
#lets player choose a category which their question will be picked from
picks = {"A":"director", 'B':"writer", 'C':"singer"}
print("Round 4")
print("-----------------------------------")
print("A: A director")
print("B: A writer")
print("C: A singer")
choice = input("Please pick a category to guess from: ").upper()


while choice not in picks.keys():
    print("")
    print("A: A director")
    print("B: A writer")
    print("C: A singer")
round4_questions = ["person1.txt", "person2.txt", "person3.txt"]

#Picks random question from category, makes it dynamic and unique each time
with open("round4/"+picks.get(choice)+"/r-hist.txt") as filein:
    #makes lines
    line = filein.read().split("\n")
    filein.close()
for q in line:
    if len(line) > 3:
        f = open("round4/"+picks.get(choice)+"/r-hist.txt","w")
        f.close()
    elif q != "":
        round4_questions.remove(q)
random_choice = random.choice(round4_questions)
round4_questions.remove(random_choice)
with open("round4/"+picks.get(choice)+"/r-hist.txt", "a") as fileh:
    fileh.write(random_choice + "\n")
    fileh.close()


#Makes randomly picked person object
with open("round4/"+picks.get(choice)+"/"+random_choice) as filein:
    line = filein.read().split("\n")
    artist = line[0]
    artist = Person(line[1], line[3], line[2], line[4], line[5], line[6], line[7])
    filein.close()

#Gives a unique attribute that the user must use to guess the person
print("")
person_desc = ["The person you are trying to guess is a "+picks.get(choice)+" who made "+ artist.work]
print("-----------------------------------")
print ("The person you are trying to guess is a "+picks.get(choice)+" who made "+ artist.work)
time.sleep(2)
#user inputs yes or no as to whether they want to use their hints
yesrno = {"y":"yes", 'n':"no" }
print ("You have "+ str(artist.hints) + " hints, would you like to use them or...")
time.sleep(2)
print ("Do you know this person?")
time.sleep(2)
know = input("Use Hints: (y/n) ").lower()
#if user doesn't input
while know not in yesrno.keys():
    know = input("please pick one of the options (y/n)")

#Two dictionaries that map the optional inputs to questions and correlationg attribute
opt_lst = {"A": "A: The persons age", "B": "B: The persons appearance", "C": "C: The persons country of origin", "D": "D: The persons networth", "E": "E: Another piece by the person"}
choice2attribute = {"A": "age", "B": "appearance", "C": "country", "D": "networth", "E": "work2"}
#if the user chooses to use hints
while know == "y" and artist.hints > 0:
    print("")
    #print optional hints availble
    for opt in opt_lst.keys():
        print(opt_lst.get(opt))
        time.sleep(.75)
    time.sleep(.25)
    #user inputs hint of choosing
    hnt_choice = input("Which hint would you like to use?, please enter the letter ").upper()
    #if user does not pick from the availible options
    while hnt_choice not in opt_lst.keys():
        print("")
        for opt in opt_lst.keys():
            print(opt_lst.get(opt))
            time.sleep(.75)
        hnt_choice = input("please pick a letter from one of the availible hints ").upper()
    #deletes selected hint from pool of availible hints
    del opt_lst[hnt_choice]
    time.sleep(.75)
    print("")
    #prints hint in the form of the persons description, adds this description to a list to be used in the summary
    print(artist.hint(choice2attribute.get(hnt_choice)))
    person_desc.append(artist.hint(choice2attribute.get(hnt_choice)))
    setattr(artist, "hints", artist.hints-1)

time.sleep(1.5)
print("")
print("-----------------------------------")
time.sleep(1)
#prints summary of all information and hints about person so far
print("In summary,")
for hint in person_desc:
    time.sleep(1)
    print(hint)
time.sleep(1)
ans = input("What is this person's full name? Keep in mind your spelling... ")
print("")
#if answer is correct player wins THE BIG HAUL
if ans.lower() == artist.name.lower():
    time.sleep(2)
    print("You are absolutely right! Great work")
    time.sleep(1)
    player.big_haul()
#otherwise player loses their entire fortune
else:
    time.sleep(2)
    print("That is unfortunately incorrect, hard luck buddy")
    time.sleep(1)
    print("The person you were trying to guess was "+artist.name)
    time.sleep(1)
    player.incorrect_final()
