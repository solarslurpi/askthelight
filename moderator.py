import openai
import os

# Set up your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the check_if_flagged function
def check_if_flagged(topic_string):
    # Check if the input topic_string is empty
    if not topic_string:
        raise ValueError("The input topic string is empty")

    # Send the request to the Moderation API using the OpenAI module
    response = openai.api_resources.Moderation.create(
#        model="content-filter-alpha-1",
        input=topic_string,
#        temperature=0.0,
#        max_tokens=1,
#        top_p=1,
#        frequency_penalty=0,
#        presence_penalty=0,
#        stop=None,
    )

    # Check the response and return the result
    if response.results[0].flagged:
        # return also the category that caused the error.
        categories = response.results[0].categories
        flagged_category = next((category for category in categories if categories[category]), None)
        return True, flagged_category
    else:
        return False, "OK"
