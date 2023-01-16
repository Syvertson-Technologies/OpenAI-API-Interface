import openai

openai.api_key = "ENTER OPENAI API KEY HERE"

# Use the ChatGPT model to generate a response to a given prompt
def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}\n"
             )

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    query = input("> ")
    # Generate a response using the ChatGPT API
    response_text = generate_response(query)
    response_text = response_text.capitalize()
    print(response_text)


# MIT License

# Copyright under Devon Chase, and code was revised by ChatGPT
