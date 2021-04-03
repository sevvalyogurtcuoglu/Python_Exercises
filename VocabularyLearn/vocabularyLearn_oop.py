#%%
import pandas as pd
from random import randint
data=pd.read_csv("kelimee.csv",sep=";")

class Vacobulary_Game():
    def __init__(self):
        self.state=True
        self.counter=0
        

    
    def Play(self):
        
        #choice=input("Enter your choice : ")
        choice=randint(1,3)
        try:
            
            if choice==1:
                self.Eng_Turk()
            elif choice==2:
                self.Turk_Eng()
        except:
                choice=input("Enter your choice (1 or 2 ) : ")        

    def Eng_Turk(self):
        while True:
            number=randint(0,len(data)-1)
            print("please write the Turkish meaning (Exit-> 'q')")
            print("{}:".format(data.loc[number][0]))
            answer=input("Answer : ")
            if answer=="q":
                self.state=False
            else:
                if answer==data.loc[number][1]:
                    self.counter+=1
                    print("Congratulations :) :) \t\t\t Score : {}\n".format(self.counter))
                else:
                    self.counter-=1
                    print("your answer '{}' is false!! \t\t Score : {} \n".format(answer,self.counter))
                    print("correct answer is ----->> {}\n".format(data.loc[number][1]))    
            break
        

        

    def Turk_Eng(self):
        while True:
            number=randint(0,len(data)-1)
            print("please write the English meaning (Exit-> 'q')")
            print("{}:".format(data.loc[number][1]))
            answer=input("Answer : ")
            if answer=="q":
                self.state=False
            else:
                if answer==data.loc[number][0]:
                    self.counter+=1
                    print("Congratulations :) :) \t\t\t Score : {}\n".format(self.counter))
                else:
                    self.counter-=1
                    print("your answer '{}' is false!! \t\t Score : {} \n".format(answer,self.counter))
                    print("correct answer is ----->> {}\n".format(data.loc[number][0]))    
            break    

game=Vacobulary_Game()
while game.state:
    game.Play()    




# %%
