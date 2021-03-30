class Game():
    def __init__(self):
        self.board=[["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]]
        self.state=True
        self.move=0

    def Play(self):   # oyuncuların sırasıyla oynamasını sağlar
        if self.move%2==0:
            self.Player1()
        else:
            self.Player2() 

        self.state=self.GameControl()  

        if self.state==False:
            self.ShowBoard()
            winner=""
            if self.move%2==0:
                winner="X"
            else:
                winner="O" 
            
            print("Game Over! winner is {}".format(winner))          

        self.move+=1

    def Player1(self):
        self.ShowBoard()
        print("Player 1")
        row=int(input("Please enter the row number : "))
        column=int(input("Please enter the column number : "))
        while row<1 or row>3:
            print("please input 1,2 or 3")
            row=int(input("Please enter the row number : "))
        while column<1 or column>3:
            print("please input 1,2 or 3")
            column=int(input("Please enter the column number : "))

        if self.IsFull(row,column):
            self.Player1()
        else:
            self.board[row-1][column-1]="X"      



    def Player2(self):
        self.ShowBoard()
        print("Player 2")
        row=int(input("Please enter the row number : "))
        column=int(input("Please enter the column number : "))
        while row<1 or row>3:
            print("please input 1,2 or 3")
            row=int(input("Please enter the row number : "))
        while column<1 or column>3:
            print("please input 1,2 or 3")
            column=int(input("Please enter the column number : "))

        if self.IsFull(row,column):
            self.Player2()
        else:
            self.board[row-1][column-1]="O"      

    def IsFull(self,row,column):  #board daki yerin dolu olup olmadığını kontrol eder
        if self.board[row-1][column-1]!="-":
            return True
        else:
            return False    
            


    def ShowBoard(self):
        for i in self.board:
            for j in i:
                print(j,end=" ")
            print("\n")    

    def GameControl(self):
        # Yatay kontrol
        if [self.board[0][0],self.board[0][1],self.board[0][2]]==["X","X","X"] or [self.board[0][0],self.board[0][1],self.board[0][2]]==["O","O","O"]:
            return False
        if [self.board[1][0],self.board[1][1],self.board[1][2]]==["X","X","X"] or [self.board[1][0],self.board[1][1],self.board[1][2]]==["O","O","O"]:
            return False
        if [self.board[2][0],self.board[2][1],self.board[2][2]]==["X","X","X"] or [self.board[2][0],self.board[2][1],self.board[2][2]]==["O","O","O"]:
            return False  
        # Dikey kontrol    
        if [self.board[0][0],self.board[1][0],self.board[2][0]]==["X","X","X"] or [self.board[0][0],self.board[1][0],self.board[2][0]]==["O","O","O"]:
            return False
        if [self.board[0][1],self.board[1][1],self.board[2][1]]==["X","X","X"] or [self.board[0][1],self.board[1][1],self.board[2][1]]==["O","O","O"]:
            return False
        if [self.board[0][2],self.board[1][2],self.board[2][2]]==["X","X","X"] or [self.board[0][2],self.board[1][2],self.board[2][2]]==["O","O","O"]:
            return False   
        # Çapraz kontrol
        if [self.board[0][0],self.board[1][1],self.board[2][2]]==["X","X","X"] or [self.board[0][0],self.board[1][1],self.board[2][2]]==["O","O","O"]:
            return False     
        if [self.board[0][2],self.board[1][1],self.board[2][0]]==["X","X","X"] or [self.board[0][2],self.board[1][1],self.board[2][0]]==["O","O","O"]:
            return False   

        return True     
    

game=Game()
while game.state:
    game.Play()         

