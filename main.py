from google import genai #this line imports google genai SDK into your program
# genai module provides classes and methods like Client,models,generate_content

from dotenv import load_dotenv
#dotenv is module provided by python-dotenv library
import os #It provides functions for interacting with the operating system.

load_dotenv() #Load all variables from the .env file into the program's environment.
#load_dotenv is a function defined by dotenv module
#It reads the .env file and loads its contents into the program's environment.

api_key=os.getenv("Gemini_API_Key") #It retrieves the value of an environment variable by its name.

client=genai.Client(api_key=api_key) #Client is a class already written by Google inside the GenAI SDK. 

while True:
    user_prompt=input("You: ")

    if user_prompt.lower()=="exit":
        print("Goodbye!")
        break
    else:
        try:
            response=client.models.generate_content(
                model="gemini-3.5-flash",  #"Flash" is Google's family of fast and efficient models.
                contents=user_prompt)
            print("AI:",response.text)
        except Exception as e:
            print("Error: ",e)





    

