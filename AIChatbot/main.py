from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import gradio as gr


load_dotenv()

gemini_key = os.getenv('GEMINI_API_KEY')

system_prompt = """
You are Arnold schwarzenegger. You will speak openly and show humour and will be 
polite at all times. your responses will include famous sayings that you say often
"""

llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature = 0.5
)

prompt = ChatPromptTemplate.from_messages(
    [("system",system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user","{input}")]
)

# | means... output of prompt will go to LLM

chain = prompt | llm | StrOutputParser()

def clear_chat(response):
    return "",[]


def chat(user_input,hist):
    print(user_input,hist)

    langchain_history = []
    for item in hist:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    response = chain.invoke({"input":user_input,"history":langchain_history})

    return "", hist + [{'role':'user','content':user_input},
                 {'role':'assistant','content':response}]


page = gr.Blocks(
    title = "AIChatbot",
    theme = gr.themes.Soft(),
)

with page:
    gr.Markdown(
        """
        # Chat with Arnie
        Welcome to your conversation!
        """
    )
    chatbot = gr.Chatbot(avatar_images=[None,'einstein.png'],show_label=False)
    msg = gr.Textbox(show_label=False,placeholder='Enter your message here')
    msg.submit(chat,[msg,chatbot],[msg,chatbot])
    clear = gr.Button("Clear Chat",variant="Secondary")
    clear.click(clear_chat,outputs=[msg,chatbot])

page.launch(share = True)
