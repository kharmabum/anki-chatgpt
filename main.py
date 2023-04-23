import os
import openai
from prompts import PROMPT

TEST_INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# Get the directory containing the script
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))


def write_completion_to_file(completion: str, output_file: str):
    """
    Write completion to a file

    Parameters
    ----------
    completion: str
    """
    output_path = os.path.join(PROJECT_PATH, output_file)
    with open(output_path, "w") as f:
        f.write(completion)


def get_input(input_file: str):
    """
    Read inputs from a file and write them back to the file after deduplicating and sorting

    Parameters
    ----------
    input_file: str

    Returns
    -------
    inputs: list
    """
    input_path = os.path.join(PROJECT_PATH, input_file)

    with open(input_path, "r") as f:
        inputs = f.readlines()

    # deduplicate and sort inputs
    inputs = sorted(set(inputs))

    # write inputs back to file
    with open(input_path, "w") as f:
        f.writelines(inputs)

    return inputs


def get_completion(prompt: str, model: str, temperature: int):
    """
    Get completion from OpenAI

    Parameters
    ----------
    prompt: str
    model: str
    temperature: int

    Returns
    -------
    completion: str
    """
    max_tokens = 4097 - 1444
    response = openai.Completion.create(model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    completion = response.choices[0].text.strip()
    return completion


def sanitize_completion(completion: str):
    """
    Sanitize completion string

    Remove any lines from the completion string that are not valid csv formatted lines
    This is a hack to remove the framing lines that are sometimes added by the model
    """
    lines = completion.split('\n')
    valid_lines = []
    for line in lines:
        if len(line.split('","')) == 2:
            valid_lines.append(line)

    return '\n'.join(valid_lines)


def get_input_file(is_test: bool):
    """
    Get input file name

    Parameters
    ----------
    is_test: bool

    Returns
    -------
    input_file: str
    """
    if is_test:
        return TEST_INPUT_FILE
    else:
        return INPUT_FILE


def main():
    root_prompt = PROMPT
    model = "text-davinci-003"
    temperature = 0

    openai.api_key = os.getenv("OPENAI_API_KEY")
    is_test = os.getenv("OPENAI_TEST_RUN", True)

    input_file = get_input_file(is_test=is_test)
    output_file = OUTPUT_FILE
    full_input = get_input(input_file)
    full_completion = ""
    input_length = len(full_input)
    # Process 10 lines of input at a time
    for i in range(0, input_length, 2):
        slice_index = min(i+2, input_length)
        input = full_input[i:min(i+2, input_length)]
        prompt = root_prompt + "".join(input)
        completion = get_completion(prompt, model, temperature)
        completion = sanitize_completion(completion)
        full_completion += completion
        print(f"Processed {slice_index} of {input_length} lines of input.")

    write_completion_to_file(full_completion, output_file)


if __name__ == '__main__':
    main()