import openai
import json
from logger import get_logger
import re

def jesus_thoughts(topic_string):
    logfile = get_logger('app')
    # Call ask_light with prompt_file=prompts/Jesus/prompt_topic.txt  
    topic_json_str = ask_light("prompts/Jesus/prompt_topic.txt",topic_string)
    # remove spaces and newlines outside of quotes.
    # topic_json_str = re.sub(r'\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', '', topic_json_str)
    # Remove unwanted characters, spaces, and newlines outside of quotes
    topic_json_str = re.sub(r'[^\x00-\x7F]+|\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', '', topic_json_str)
    # Parse the JSON string into a dictionary
    try:
        topic_json_dict = json.loads(topic_json_str)
    except Exception as e:
        print(e)
        return None
    # Call ask_light with the new prompt.
    meaningful_topic = topic_json_dict["meaningful_topic"].lower()
    topic_explanation = ""


    if meaningful_topic != "none":
        topic_explanation = f"You asked about {topic_string}.  The topic Jesus will address is {topic_json_dict['meaningful_topic']}.  The reason for this is {topic_json_dict['reason']}"
        jesus_words = ask_light("prompts/Jesus/prompt_response.txt", topic_json_dict["meaningful_topic"])
        jesus_json = {"topic":topic_explanation,
                      "title": f"What did Jesus think about {topic_json_dict['meaningful_topic']}",
                      "words": f"{jesus_words}".replace('\n', '<br/>')
                    }
    else:
        jesus_json = {"topic": f"I'm very sorry. The topic '{topic_string}' won't work. Reason: {topic_json_dict['reason']}",
                      "title": "",
                      "words": ""
                      }
    logfile.info(f"{jesus_json}")
    return jesus_json



def ask_light(prompt_file, topic_string):
    logfile = get_logger('app')
    prompt = _create_prompt(prompt_file, topic_string)
    # Call the create method with the prompt and temperature
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600,
        temperature=0
        )
    the_message = response.choices[0].text.strip()
    logfile.debug(f"The Message is: {the_message}")
    return the_message

def extract_topic(text):
    topic_pattern = r'Topic:\s*(.*)'
    match = re.search(topic_pattern, text)
    
    if match:
        return match.group(1)
    else:
        return None
    

def _create_prompt(prompt_file, topic_string):
    logfile = get_logger('app')
    try:
        # Open the JSON file and load the data
        with open(prompt_file, "r") as file:
             prompt = file.read()
             prompt = prompt.strip().replace("{topic}", topic_string)
             logfile.debug(f"Prompt: {prompt}")
             return prompt

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None

    except KeyError:
        print("Error: Missing key(s) in JSON file.")
        return None
    

