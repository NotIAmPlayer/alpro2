import openai

openai.api_key = "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"
model_engine = "text-babbage-001"

prompt = input("Input something to ChatGPT:\n> ")

completion = openai.Completion.create(
    engine      = model_engine,
    prompt      = prompt,
    max_tokens  = 1024,
    n           = 1,
    stop        = None,
    temperature = 0.5,
)

response = completion.choices[0].text
print(response)