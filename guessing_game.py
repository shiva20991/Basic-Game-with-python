#python #beginners 


import random


data = ["duke","sony","google","yahoo","nokia","tamil"]#guessing words

data_l = random.choice(data)#random data picking
    
data_n = len(data_l) # length of data_l which is random data

result = []  # empty list is defined for displayingg dash 

tries = 3    

for _ in range(data_n):

    result += "_"  # printing empty dassh according to the guessed words

conditio_n = False
    
while not  conditio_n:
    user_data = input("enter the guessing words")

    if user_data in data_l:

        for position in range(data_n):

            check = data_l[position] # checking the position 

            if user_data == check :  # check the both input is matched or not 

                result[position] = user_data  # replacing the dash by correct word

                result1 = " ".join(result)  # using join fumctiom inserting the letters 

                print(result1)   # printing the results 


    if user_data not in data_l:

        tries -= 1
            
        print(f"Your Guess IS Wrong , Try Again & Your Left Tries = {tries}..")

            

    if tries == 0 :

        conditio_n = True
            
        print("game is Over & and You missed It")

    if "_" not in result:

        conditio_n = True
            
        print("User Win The Game")


#IF anybody want to add any new things ,just give pull request i am also get to know ..#python #beginners 
