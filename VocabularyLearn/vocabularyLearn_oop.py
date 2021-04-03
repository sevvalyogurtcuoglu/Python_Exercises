
import pandas as pd
from random import randint
data=pd.read_csv("kelimee.csv",sep=";")

class Vacobulary_Game():
    def __init__(self):
        self.state=True
        self.counter=0
        

    
    def Play(self):
        print("""
        **** WELCOME ****
        for ENGLISH-TURKISH enter 1
        for TURKISH-ENGLISH enter 2
        """)
        choice=input("Enter your choice : ")
        try:
            
            if choice=="1":
                self.Eng_Turk()
            elif choice=="2":
                self.Turk_Eng()
        except:
                choice=input("Enter your choice (1 or 2 ) : ")        

    def Eng_Turk(self):
        while True:
            number=randint(0,len(data)-1)
            print("please write the Turkish meaning")
            print("{}:".format(data.loc[number][0]))
            answer=input("Answer : ")
            if answer=="q":
                self.state=False
            else:
                if answer==data.loc[number][1]:
                    self.counter+=1
                    print("Congratulations :) :) \t\t Score : {}\n".format(self.counter))
                else:
                    self.counter-=1
                    print("your answer {} is false \t\t Score : {} ".format(answer,self.counter))
                    print("correct answer is {}".format(data.loc[number][1]))    
            self.state=False
        

        

    def Turk_Eng(self):
        pass    

game=Vacobulary_Game()
while game.state:
    game.Play()    




