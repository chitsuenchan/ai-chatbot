import openai

openai.api_key = "sk-"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay about penguins"}])

print(completion.choices[0].message.content)


