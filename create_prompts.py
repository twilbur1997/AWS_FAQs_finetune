import time
from datetime import date, timedelta, datetime

def prompt_create(iteration):
    iter = str(iteration)+". \nQ) "
    # First, ask the user for their prompt
    prompt = input("Enter the prompt: \n")

    # Then, ask the user for the completion
    completion = input("Enter the completion: \n")

    text_input = iter+prompt+'\nA) '+completion+'\n'
    with open("prompts_text.txt", "a") as file1:
        file1.write(text_input+"\n")

    json_lines_input = '{"prompt":"'+prompt+'","completion":"'+completion+'"}'
    with open("staging_data.jsonl", "a") as file2:
         file2.write(json_lines_input+"\n")

# {"prompt":"string","completion":"string"}    

def main():
    # Ask the user for a prompt, then a completion.
    # Write each to a text file and a staging JSONL file

    # TODO check data files for repeated prompts?

    current_time = datetime.now().strftime("%H:%M:%S %y/%m/%d")
    with open("prompts_text.txt", "a") as file1:
        file1.write("\n"+current_time+"\n")
    completion = ""
    iteration = 0
    while not (len(completion) > 0):
        iteration += 1
        prompt_create(iteration)
        completion = input("Press Enter to continue\n")


if __name__ == "__main__":
    main()