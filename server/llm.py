import os
import google.generativeai as genai
from dotenv import load_dotenv
from time import sleep
from groq import Groq



load_dotenv()
client = Groq()
# Configure the Google Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Function to call the Google Gemini API
def process_gpt(system_msg, file_prompt):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-exp-0827", system_instruction=system_msg
    )

    response = model.generate_content(file_prompt)
    nlp_results = response.text
    #    sleep(8)
    return nlp_results


# Function to call the Groq API
def process_gpt2(file_prompt, system_msg):
    response = client.chat.completions.create(
        model="llama-3.2-90b-text-preview",  # Replace with the appropriate Groq model identifier
        max_tokens=8192,
        temperature=0,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": file_prompt},
        ],
    )
    nlp_results = response.choices[0].message.content
    sleep(8)
    return nlp_results


response = process_gpt2("you're a pirate", "tell me the meaning of life")


print(response)
