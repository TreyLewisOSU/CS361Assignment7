import time 
import os 
import json 


def user_interface():
    while True:

        time.sleep(0.25)
 
        file = open("user_wardrobe_input.txt", "w")
        file.write(input("Please type an article of clothing to be added to the wardrobe!: "))
        file.close() 

        file = open("initiate_information_transfer.txt", "w")
        file.write("Confirmed")
        file.close() 
        time.sleep(0.25)
        file = open("initiate_information_transfer.txt", "w")
        file.write("Denied")
        file.close() 

        file = open("user_wardrobe_dictionary_form.txt", "r")
        data_in_file = file.readline()
        file.close()

        time.sleep(0.25)

        data_in_file.replace("\"", "\"")
        data_in_file.replace("\'", "\"")

        dictionary_form = json.loads(data_in_file)

        print(dictionary_form)
        print(type(dictionary_form))

        data = dictionary_form["User_input"]
        print(data)
        print(type(data))



if __name__ == "__main__":
    user_interface()