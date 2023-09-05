import random
import hangmanpic #.py file extension 

letters_list=['apple','potato','banana','orange','car','bike']

lifes=6

word=random.choice(letters_list)
print(word)

display=[]

for i in range(len(word)):#if the word is apple then len=5 so 0,1,2,3,4 
    display+='_'#display=display+'_'
print(display)

game_over=False
while not game_over: #true   not fasles=true 
            
    guess_letter =input("enter guess letter:").lower()

    for position  in range(len(word)):
        letter=word[position] #index o,1,2  etc letter=a index value=0 
        if letter==guess_letter:
            
            display[position]=guess_letter
    print(display)
    
    
    if guess_letter not in word:
        lifes-=1
        if lifes==0:
            game_over=True
            print("you loose ")
    if '_' not in display:
        game_over=True
        print("you win")
    print(hangmanpic.stages[lifes])
        

