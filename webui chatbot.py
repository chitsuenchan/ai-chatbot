from openai import OpenAI
import gradio

client = OpenAI()

messages = [{"role": "system", "content": "you are a very camp gay guy"}]

def customChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply

demo = gradio.Interface(fn=customChatGPT, inputs = "text", outputs="text", title = "Simple AI Chatbot")

demo.launch()