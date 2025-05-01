import time
import sys
from search import search_gemini

def typing_effect(text, speed=0.02):  # Reduced delay to make typing faster
    """Simulate typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)  # Adjusted the typing speed (faster)

    print()  # Move to the next line after the message

def main():
    print("🤖 Real-Time ChatBot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        try:
            time.sleep(1)  # 💤 Add small delay before sending request

            response = search_gemini(user_input)
            typing_effect(f"Bot: {response}")  # Use the typing effect for the response

        except Exception as e:
            print("⚠️ Oops, something went wrong!")
            print(f"Details: {e}")

if __name__ == "__main__":
    main()
