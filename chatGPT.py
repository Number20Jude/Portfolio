# This should work, but as I don't have chatGPT I have no way of telling.
import openai
openai.api_key = "YOUR_API_KEY"
def chat_with_gpt(messages):
    """Sends messages to the ChatGPT model and returns the response."""
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    conversation = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        conversation.append({"role": "user", "content": user_input})
        response = chat_with_gpt(conversation)
        print("ChatGPT:", response)
        conversation.append({"role": "assistant", "content": response})