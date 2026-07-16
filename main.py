from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("Gemini_API_Key")

client=genai.Client(api_key=api_key)

while True:
    user_prompt=input("You: ")

    if user_prompt.lower()=="exit":
        print("Goodbye!")
        break
    else:
        try:
            response=client.models.generate_content(
                model="gemini-3.5-flash",
                contents=user_prompt)
            print("AI:",response.text)
        except Exception as e:
            print("Error: ",e)





    

