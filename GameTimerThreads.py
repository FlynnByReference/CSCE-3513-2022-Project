import time
import thread
 

def GameTimer(int amountMins):
    int Total_Time = (amountMins * 60)
    time.sleep(Total_Time)
    print("GAME OVER!")
    #code to display endgame splash screen


#This would go in the main file wherever the game starts
thread.start_new_thread(GameTimer, (amountMins))

