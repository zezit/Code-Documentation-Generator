import openai
import re
import time

openai.api_key = "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"

def generate_doxygen(function_info):
    print("got:\n" , function_info)

    # Check if rate limit has been reached
    current_time = time.time()
    if current_time - generate_doxygen.last_call_time < generate_doxygen.rate_limit:
        time.sleep(generate_doxygen.rate_limit - (current_time - generate_doxygen.last_call_time))

    # Use the OpenAI API to generate Doxygen documentation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"generate a portuguese doxygen for the following function in c vscode format:\n{function_info}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    print("response:\n"+response.choices[0].text)

    # Update the time of the last call to the function
    generate_doxygen.last_call_time = time.time()

    return response.choices[0].text

# Initialize the time of the last call to the function
generate_doxygen.last_call_time = 0
# Set the rate limit in seconds
generate_doxygen.rate_limit = 1.0


def extract_functions(file_contents):
    # Regular expression pattern to match a function definition
    pattern = re.compile(r'(\w+)\s*(\w+)\s*\(([^\)]*)\)\s*(\w*)\s*\{(.*?)\}', re.DOTALL)
    functions = pattern.findall(file_contents)

    return functions

# Read the contents of the main.c file
with open('main.c', 'r') as file:
    file_contents = file.read()

# Extract the information about all the functions in the file
functions = extract_functions(file_contents)

# Generate the Doxygen documentation for all the functions
documentation = [generate_doxygen(function) for function in functions]

# Write the documentation to a new file
with open('doxygen_documentation.c', 'w') as file:
    file.write('\n\n'.join(documentation))
