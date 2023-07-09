import os
import openai

def improve_code(filename):
    # Load the code file
    with open(filename, "r") as file:
        code = file.read()

    # Call OpenAI API to improve the code
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 Turbo model
        prompt=code,
        max_tokens=100,  # Adjust as per your needs
        n=1,  # Number of completions to generate
        stop=None,  # Stop generating after a specific token if desired
        temperature=0.8,  # Adjust as per your needs
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # Get the improved code
    improved_code = response.choices[0].text.strip()

    # Save the improved code back to the file
    with open(filename, "w") as file:
        file.write(improved_code)

# Get all code files in the repository
code_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            code_files.append(os.path.join(root, file))

# Improve and fix each code file
for file in code_files:
    improve_code(file)
