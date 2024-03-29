import random

answerlist = [
    "apple", "brave", "charm", "drift", "eager",
    "flint", "grasp", "haste", "ideal", "jolly",
    "knack", "latch", "mirth", "noble", "oasis",
    "pluck", "query", "roast", "scale", "truce",
    "ultra", "vivid", "waste", "xenon", "yearn",
    "zebra", "quake", "gloom", "frost", "sweep",
    "bloom", "blush", "creep", "dwarf", "flame",
    "glide", "grief", "pride", "sloth", "smile",
    "snarl", "spark", "spill", "squat", "stack",
    "steal", "sting", "stoop", "swell", "swoop"]
   
instructions = """
    You have 5 tries to find the right 5 letter word.
    Letters in the answer and in the correct order will appear as a normal letter.
    Letters in the answer, but not in the correct order will appear with parenthesis around them.
 
                        Example: Answer - "Words"

            A guess of "flexs" would result in this on the board:
                                _  _  _  _  s 
            (only the "s" is in the answer and correct order)

            A guess of "flows" would result in this on the board:
                                _  _ (o)(w) s 
            ("o" and "w" are in the answer, but in the wrong order, 
                    so there are parenthesis around them.)

            A correct answer would look  like this.
                                w  o  r  d  s  
"""
winscreen = "Congrats, you found the correct word!"
losescreen = "Oh no, you couldn't find the correct word!"
    
     
def check(guess, answer):
    frame = ["_"] * 5
    
    #checking each letter against the answer
    for letter in range(5): 
        if guess[letter] == answer[letter]:
            frame[letter] = guess[letter]
            
        if guess[letter] in answer:
            frame[letter] = "(" + guess[letter] + ")"
    
    string = ""
    for letter in frame:
        string += letter
        
    return frame

def interface():
    print("Welcome to Wordle.")
    choice = input("""Press enter to play, or "I" for instructions:""")
    if choice == "I":
        print(instructions)
        choice2 = input("Press enter to play the game:")
       
    gameswon = 0
    gameslost = 0
    
    for i in range(10):
        print("Score: " + str(gameswon) + ":" + str(gameslost))
        
        answer = random.choice(answerlist)
        frames = [["_" * 5]]
        correct = False
        numguesses = 0
        
        for i in range(5):
            print(frames)
            
            if correct == True:
                print(winscreen)
                gameswon += 1
                break
            if numguesses > 5:
                print(losescreen)
                gameslost += 1
                break
            
            guess = input("* Enter Guess *")
            frames += check(guess, answer)
            if guess == answer:
                correct = True
                
interface()

        
                

    
    