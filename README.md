# CS361Assignment7

How To Request Data: Data can be recieved by having the "information_transfer.py" file running in the background in tandem with the application. 
To request the microservice to recieve user data and process it, have a call that places the user's data inside a file called "user_wardrobe_input.txt". It is BEST to have the program sleep for 0.25 seconds before this call.

Next, have the "initiatie_information_transfer.txt" contian the phrase "Confirmed". 
Afterwards, have the program sleep for another 0.25 seconds and change the "initiate_information_transfer.txt" file to "Denied".
When the phrase "Confirmed" is added, the information_transfer function, found within information_transfer.py, will begin processining the user's request and turning the user's input into a Python Dictionary type, with User_input as its key. 
When the phrase "Denied" is added, the infromation_transfer function will begin to wait, and not process the user's input. 

Notes: 

A phrase other than Denied will work as well, the phrsae Denied is just convention. The information_transfer function really only activates when "Confirmed" is applied to the "initiate_information_transfer.txt" file. 

While the sleeping requests are not required, to have all the text files, information_transfer function, and user's GUI functions, all be in sync with one another, a sleep time is required. If the times are ommited, you will run into potential bugs. Please add them.  

An example call would be as such: 
        
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



How To Recieve Data: Data can be requested by having the user open the text file "user_wardrobe_dictionary_form.txt" and reading the information from that file. The "user_wardrobe_variable_form.txt" file will contain only the user input, inputted as a dictionary variable for the Python programming language.

An example call would be as such: 

  file = open("user_wardrobe_dictionary_form.txt", "r")
  data_in_file = file.readline()
  file.close()

  print(data_in_file)
  
