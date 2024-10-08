from openai import OpenAI
import gradio

client = OpenAI()

messages = [{"role": "system", "content": "you are a super rational robot"}]


def customChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply


demo = gradio.Interface(fn=customChatGPT, inputs="text", outputs="text", title="Rational robot - AI Chatbot")

demo.launch()
