

def call_api(msg):
    
    
	
    model_engine = "gpt-3.5-turbo"
    prompt = msg

# Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
)

    response = completion.choices[0].text
    

    return(response)

prompt = input('User:')
print(call_api(prompt))
