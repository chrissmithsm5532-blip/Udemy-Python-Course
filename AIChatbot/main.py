from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

gemini_key = os.getenv('GEMINI_API_KEY')

system_prompt = """
You are Obi Wan Kenobi. Answer questions through Obi Wan Kenobi's questioning
and reasoning...
You will speak from your point of view. You will share personal things from
your life, even when the user doesnt ask for it. For example if the user asks
about the force explain that it is everywhere
Answer in 2-6 sentences
"""

llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature = 0.5
)



response = llm.invoke([
                        {"role":"system","content":system_prompt},
                        {"role":"user",
                        "content": "Hi how are you?"}
                       ])

print(response.content)



#
#
# print("Hello, how can i help you?\n")
# while True:
#     user_input = input("You: ")
#     if input == "exit":
#         break
#     print(user_input)

