from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are sassy person"},
    {"role": "user", "content": "What colour is the sun"}
  ]
)

print(completion.choices[0].message)