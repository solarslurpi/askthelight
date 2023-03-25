from ask_the_light import ask_light
topic = input('Enter topic:')

result = ask_light("prompts/Jesus/prompt_topic.txt", topic)

print(f"{result}")