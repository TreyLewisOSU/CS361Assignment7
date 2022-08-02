import time 
import os 

def information_transfer(): 
    
    while True:

        file = open("initiate_information_transfer.txt", "r")
        initiation_confirmation = file.readline()
        file.close()

            # Move the information over from one file to another, in a dictionaray format.
        if initiation_confirmation == "Confirmed": 
            file = open("user_wardrobe_input.txt", "r")
            data_from_user = file.readline()
            file.close() 
            file = open("user_wardrobe_dictionary_form.txt", "w")
            file.write(('{"User_input" : ' + f'"{data_from_user}"' +'}'))
            file.close() 

if __name__ == "__main__":
    information_transfer()