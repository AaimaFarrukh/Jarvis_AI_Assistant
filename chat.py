'''
from decouple import config
from hugchat import hugchat
from hugchat.login import Login

email= config('EMAIL')
passw= config('PASS')


# Function for generating LLM response
def generate_response(prompt_input):
    try:
        # Hugging Face Login
        try:
            sign = Login(email, passw)
            
        except Exception as e:
            print(f"Error during login initialization: {e}")
            return "I am sorry, I couldn't generate a response."

        try:
            cookies = sign.login()
        except Exception as e:
            print(f"Error during login: {e}")
            return "I am sorry, I couldn't generate a response."

        try:
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        except Exception as e:
            print(f"Error during chatbot creation: {e}")
            return "I am sorry, I couldn't generate a response."

        try:
            message_result = chatbot.chat(prompt_input)
            message_str = message_result.wait_until_done()  # Get the full response
            return message_str
        except Exception as e:
            print(f"Error during chat generation: {e}")
            return "I am sorry, I couldn't generate a response."
    except Exception as e:
        print(f"Error in generate_response: {e}")
        return "I am sorry, I couldn't generate a response."
'''        