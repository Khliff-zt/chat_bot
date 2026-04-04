# cli_chat.py
import openai
import os

# API key conf
client = openai.OpenAI(api_key = os.getenv("OPENAI_API_KEY","openai-api-key"))

def ask_ai(question):
    """ Function that ask ai question"""
    try:
        response = openai.chat.completions.create(
            model = "gpt-4o-mini", # AI model to use
            messages = [
                {"role" : "system","content" : "Ask only Simple question"},
                {"role" : "user", "content" : question }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error : {e}"
    
# Test Functions
if __name__ == "__main__":
    while True:
        user_question = input("You => ")

        if user_question.lower()=='quit':
            break

        answer = ask_ai(user_question)

        print(f"Response => {answer}")
