from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

print("AI Assistant Ready 🚀 (type 'exit' to quit)")

def get_weather():
    return "Today's weather is sunny 🌞 with 32°C."

def calculate(query):
    try:
        return str(eval(query))
    except:
        return "I can solve basic math only."

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Goodbye 👋")
        break

    elif user_input in ["hi", "hello", "hey"]:
        print("AI: Hello! How can I help you? 😊")

    elif "weather" in user_input:
        print("AI:", get_weather())

    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        print("AI:", calculate(user_input))

    else:
        response = chatbot(
            user_input,
            max_length=60,
            do_sample=True,
            temperature=0.7
        )
        print("AI:", response[0]["generated_text"].replace(user_input, "").strip())
