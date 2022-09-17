from random import choice, randint, uniform #importing random module
import json #json module needed to be able to .dump and .load json files
import csv #csv module needed so that we can access csv files and add / remove data







def menu1():
    print("\n")
    print("____________________")
    print("1. Create an account")
    print("")
    print("2. log in")
    print("____________________")
    return input("Enter your choice 1-2: ")


def menu2():
    print("\n")
    print("____________________")
    print("enter 1 to start")
    print("")
    print("enter 2 for top 5 winners")
    print("")
    print("enter 3 to Exit")
    print("____________________")
    return input("Enter your choice 1-3: ")


def create_account():
    strong = "no"
    upper_flag = False
    digit_flag = False

    fdata = open("register2.csv", "a", newline="")
    writer = csv.writer(fdata)

    print("welcome to the account creation System")
    name = input("Enter your name: ")
 
    username = f"{name[0:3]}#" + "".join(str(randint(1,9))) + "".join(str(randint(1,9))) + "".join(str(randint(1,9))) + "".join(str(randint(1,9)))
    print(name, "your username is:", username)

    while strong == "no":
        password = input("enter your password: ")
        passlen = len(password)

        for n in range(passlen):
            uccheck = password[n].isupper()
            if uccheck == True:
                upper_flag = True

                print("Uppercase characters:", upper_flag)

                for x in range(passlen):
                    digcheck = password[x].isdigit()
                    if digcheck == True:
                        digit_flag = True

                print("digit characters:", digit_flag)

                if upper_flag == True and digit_flag == True:
                    strong = "yes"
                    print("your password is strong!")

                    writer.writerow((name, username, password))

                else:
                    print("Your pasword is weak, Include uppercase letters and digits!")
    fdata.close()


def login():
    global flag
    flag = False
    fdata = open("register2.csv", "r")
    readCSV = csv.reader(fdata)

    username1 = input("username:  ")
    password1 = input("password:  ")
    for row in csv.reader(open("register2.csv"), delimiter=","):
        if row[1].strip() == username1.strip() and row[2].strip() == password1.strip():
            print("log in sucessful.....")
            print("what do you want to do?")
            print("")
            global loggedin_name
            loggedin_name = username1
            flag = True
            print("")
            break
        if flag == False:
            continue
        else:
            print("could not log you into the system")


class maingame():
    def __init__(self, max_rounds = 5, rounds = 0, current_turn = None, even_num = [2,4,6], odd_num = [1,3,5], double = None, p1_score = 0, p2_score = 0):
        self.reset()
        #self.game = False
        #self.max_rounds = max_rounds
        #self.rounds = rounds
        #self.current_turn = current_turn
        #self.even_num = even_num
        #self.odd_num = odd_num
        #self.double = double
        #self.p1_score = p1_score
        #self.p2_score = p2_score
        #self.first_turn = None #setting all of my game variables

    def reset(self):
        self.game = False
        self.max_rounds = 5
        self.rounds = 0
        self.current_turn = None
        self.even_num = [2,4,6]
        self.odd_num = [1,3,5]
        self.double = None
        self.p1_score = 0
        self.p2_score = 0
        self.first_turn = None  #put all of the game variables into this reset function so when called they are reseted to these values in the __init__


    def startup(self): #this fucntion helps the game to start when once called and will allow for main_game to be called 
     while self.game == False:
      self.p1 = input("what is player 1\'s name: ") #get player 1s name and store it into var p1
      self.p2 = input("what is player 2\'s name: ") #get player 1s name and store it into var p2
      if self.p1.lower() != self.p2.lower():
       self.first_turn = choice((self.p1, self.p2)) #determins the first person to start
       self.game = True
      else:
       print("player 1\'s name cannot be the same as player 2\'s name")

    
    def turns(self): #function when called switches the turn of the player and prints the current turn
     #global current_turn
     if self.current_turn == self.p1:
        current_turn = self.p2
        print("\n")
        print("it is now " + current_turn + " turn")
     elif self.current_turn == self.p2:
        current_turn = self.p1
        print("it is now " + current_turn + " turn")
        print("\n")
     else:
        print("a error has happened")
        print("current player - "+ self.current_turn)
        print("player 1 - " + self.p1)
        print("player 2 - "+ self.p2)



    def score(self, num): #this function when called lets me make changes to the score and takes in a int
        #global current_turn, p1_score, p2_score
        if self.current_turn == self.p1:
            self.p1_score += int(num)
        else:
            self.p2_score += int(num)



    def get_score(self): #this funcion when called returns the score of the user
        #global current_turn, p1_score, p2_score
        if self.current_turn == self.p1:
            return(str(self.p1_score))
        else:
            return(str(self.p2_score))




    def determine_score(self): #when this function is called it generates the score and uses other functions to add/remove points
        num = randint(1,6)
    
        print("you have rolled a " + str(num) + "!")
        if int(num) in self.even_num:
            self.score(10)
            print("10 points have been added\nyour score is " + str(self.get_score()))
            print("\n") 
        elif int(num) in self.odd_num:
            if int(self.get_score()) >= 5:
             self.score(-5)
             print("5 points have been removed\nyour score is " + str(self.get_score()))
             print("\n")
            else:
             self.score(0)
             print("your score is " + str(self.get_score()))
             print("\n")

    def determine_winner(self): #this function returns the winner
        winner = None

        if self.p1_score > self.p2_score:
            winner = self.p1
        elif self.p2_score > self.p1_score:
            winner = self.p2
        return winner 

    def determine_winner_score(self): #this function returns the winners score
        winner_score = None
        if self.p1_score > self.p2_score:
            winner_score = self.p1_score
        elif self.p2_score > self.p1_score:

            winner_score = self.p2_score
        return winner_score


    def get_user_data(self): #this returns the data from the json so that it can be used later
     with open("lb.json","r") as f:
        users = json.load(f)
     return users

    def update_lb_score(self): #this function allows me to change the leaderboard score for the winner or add them if there not current in it! 
        users = self.get_user_data()
        winner = self.determine_winner()
        new_score = int(self.determine_winner_score())
        if users == None:
            users[winner] = {}
            users[winner]["top_score"] = new_score

        elif winner in users:
            old_score = users[winner]["top_score"]
            if int(old_score) < new_score:
             users[winner]["top_score"] = new_score
        else:
            users[winner] = {}
            users[winner]["top_score"] = new_score
        with open("lb.json","r+") as f:
            json.dump(users, f)

    def lb(self, users_to_search_for = 5): #this function when called prints the top 5 if more than 5 people in data otherwise prints the top users in the data in the order of biggest to smallest 
        users = self.get_user_data()
        leader_board = {}
        total = []
        for user in users:
            somedeci = uniform(0.000001, 0.4)
            name = user
            total_amount = users[user]["top_score"] + somedeci
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = id_
            print(str(index) + ") user : " + str(member) + ", score : " + str(int(amt)))
            if index == users_to_search_for:
              break
            else:
             index += 1  

    def main_game(self):
     while self.game == True: #so i can controll when the game starts and when it ends
        self.current_turn = self.first_turn
        print(self.current_turn + " has been chosen to roll first!")
        while self.rounds <= self.max_rounds:
         x = input("press ENTER to roll the dice")
         self.determine_score()
         x = input("press ENTER to roll the dice")
         self.determine_score()
         self.turns()
         print("\n")
         x = input("press ENTER to roll the dice")
         self.determine_score()
         x = input("press ENTER to roll the dice")
         self.determine_score()

         self.rounds += 1
        

         if self.rounds < 5:
          print("\n")
          print(str(self.rounds) + " rounds\'s have passed there are " + str(5- int(self.rounds)) + " left!")
          print("\n")
         elif self.rounds == 5:
          print("\n")
          print("this is the last round 5/5 MAKE IT COUNT!")
          print("\n")
         else: 
            while self.p1_score == self.p2_score:
             print("\n")
             print("BONUS ROUND!")
             print("\n")
             x = input("press ENTER to roll the dice")
             self.determine_score()
             self.turns()
             print("\n")
             x = input("press ENTER to roll the dice")
             self.determine_score()
             print("\n")
             print("\n")


        if self.rounds <= self.max_rounds:
         self.turns()
    
        print("\n")
        print("\n")
        print("THE WINNER IS ...\n" + str(self.determine_winner()) + " with " + str(self.determine_winner_score()) + " points")        
        print("game has ended")
        self.update_lb_score()
        self.lb()
        self.reset() #resets the __init__ so the program can be replayed as the vars are reset like its supposed to, without this line of code the program wouldnt be able to let the users play again rather they would have to restart the program itself.    
        self.game = False










my_game = maingame() #this is so i can call the functions inside the class and instantiate the class (create the object).

class mainprogram():
    def __init__(self):
        self.loop = 0
        self.loop1 = 0


    def func(self):
     self.loop = 0
     while self.loop == 0:
      choice = menu1()
      if choice == "1":
        create_account()
      elif choice == "2":
         login()
         if flag == True:
            self.loop1 = 0
            while self.loop1 == 0:
                choice2 = menu2()
                if choice2 == "1":
                    my_game.startup()
                    my_game.main_game()
                elif choice2 == "2":
                    my_game.lb()
                elif choice2 == "3":
                    self.loop1 = 1
                    exit()
                else:
                    print("Invalid Input.")
         else:
            print("you could not login to the system")
            print("try again")

     else:
        print("invalid choice, try again pick a number between 1 and 4")

pro = mainprogram() #so instantiate the class (object) and then call func.
pro.func() #when called this turns the loop on and so is what makes the whole program run
