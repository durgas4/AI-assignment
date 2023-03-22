import openai
import time
​
openai.api_key = "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"
​
# Define the prompt
prompt = ("an unexpected visitor ")
​
# Set up the OpenAI API parameters
model_engine = "davinci"
temperature = 0.7
max_tokens = 512
stop_sequence = "\n\n"
​
# Generate the story
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    stop=stop_sequence
)
​
# Extract the generated story from the response
generated_text = response.choices[0].text.strip()
​
# Print the generated story
print(generated_text)
​
