import sys
import openai
import re
import time
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("MY_API_KEY") 

def generate_doxygen(function_info):
    # print("got:\n" , function_info)

    # Check if rate limit has been reached
    current_time = time.time()
    if current_time - generate_doxygen.last_call_time < generate_doxygen.rate_limit:
        time.sleep(generate_doxygen.rate_limit - (current_time - generate_doxygen.last_call_time))

    # Use the OpenAI API to generate Doxygen documentation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"generate doxygen for the following function in c vscode format. Use '@' to indicate doxygen itens and add a '*' on the begining of every line inside the '/**/'. Also add inline comments explaining the code. All of it should be in portuguese:\n{function_info}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1
    )

    print("response:\n"+response.choices[0].text)

    # Update the time of the last call to the function
    generate_doxygen.last_call_time = time.time()

    return response.choices[0].text

# Initialize the time of the last call to the function
generate_doxygen.last_call_time = 0
# Set the rate limit in seconds
generate_doxygen.rate_limit = 1.0

def generate_markdown(function_info):
    # print("got:\n" , function_info)

    # Check if rate limit has been reached
    current_time = time.time()
    if current_time - generate_markdown.last_call_time < generate_markdown.rate_limit:
        time.sleep(generate_markdown.rate_limit - (current_time - generate_markdown.last_call_time))

    molde = """
            - Função `add`:
                - **Declaração:** `int add (int a, int b);`
                - **Descrição:** Esta função realiza a adição dos argumentos `a` e `b` e retorna o resultado da soma.
                - **Parâmetros:**  
                    - `a`: inteiro a ser subtraído.
                    - `b`: inteiro que será subtraído de a.
                - **Retorno** Inteiro contendo o resultado da subtração de a por b.
            """

    # Use the OpenAI API to generate Doxygen documentation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Return a markdown list of documentation for all the following functions. Use this molde: \n{molde}\n. All of it should be in portuguese:\n{function_info}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1
    )

    print("response:\n"+response.choices[0].text)

    # Update the time of the last call to the function
    generate_markdown.last_call_time = time.time()

    return response.choices[0].text

# Initialize the time of the last call to the function
generate_markdown.last_call_time = 0
# Set the rate limit in seconds
generate_markdown.rate_limit = 1.0


def extract_functions(file_contents):
    # Regular expression pattern to match a function definition
    pattern = re.compile(r'(\w+)\s*(\w+)\s*\(([^\)]*)\)\s*(\w*)\s*\{(.*?)\}', re.DOTALL)
    functions = pattern.findall(file_contents)

    return functions

def main(file_path):
    # Read the contents of the main.c file
    with open(file_path, 'r') as file:
        file_contents = file.read()
        # Extract the information about all the functions in the file
        functions = extract_functions(file_contents)

        # Generate the Doxygen documentation for all the functions
        documentation = [generate_doxygen(function) for function in functions]

        # Write the Doxygen documentation to a new .c file
        with open('doxygen_documentation.c', 'w') as file:
            file.write('\n\n'.join(documentation))
            print("Doxygen documentation written to doxygen_documentation.c")

        # Generate the Doxygen documentation for all the functions
        documentation = [generate_markdown(function) for function in functions]

        # Write the information to a markdown file
        with open('doxygen_documentation.md', 'w') as file:
            file.write('\n\n'.join(documentation))
            print("Markdown documentation written to doxygen_documentation.md")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 test.py ./main.c")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)