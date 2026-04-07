from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY_HERE") # Get your key at: https://aistudio.google.com/

def start_german_tutor():

    config = types.GenerateContentConfig(
        system_instruction=(
            "You are a professional German language tutor. "
            "Rule 1: Always reply in German first, followed by English in brackets. "
            "Rule 2: Correct my grammar and vocabulary errors. "
            "Rule 3: Always end your response with a follow-up question in German." # Incorporate any other rules or instructions you want the tutor to follow
        ),
        temperature=0.7,
    )

    
    chat = client.chats.create(model="gemini-3-flash-preview", config=config) # Start a chat session

    print("--- Willkommen! Dein Deutschlehrer ist hier. (Type 'exit' to quit) ---\n") 

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "tschüss"]:  # Exit commands
            print("Bis bald! (See you soon!)")
            break

        
        try:
            response = chat.send_message(user_input) # Error conditions
            print(f"\nTutor: {response.text}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    start_german_tutor()
