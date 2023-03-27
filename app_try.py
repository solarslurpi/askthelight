from flask import Flask, render_template, request
from ask_the_light import jesus_thoughts
from logger import get_logger
from moderator import check_if_flagged

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if 
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    print("IN --> process_form()")
    error = None
    topic_string = request.form.get('topic', '')

    if topic_string is not None and len(topic_string) > 0:
        what_would_Jesus_say = _what_would_Jesus_say(topic_string)
    else:
        error = "The topic string is empty. Please enter a topic."
        return render_template('index.html', title='', words='', error=error)

    if len(what_would_Jesus_say.get("error", '')) > 0:
        return render_template('index.html', response='', error=what_would_Jesus_say["error"])

    return render_template('index.html', topic=what_would_Jesus_say["topic"], title=what_would_Jesus_say["title"], response=what_would_Jesus_say["words"], error=error)

def _what_would_Jesus_say(topic_string):
    error = None
    logfile = get_logger('app')
    logfile.debug(f"topic_string: {topic_string}")
    what_would_Jesus_say = ''
    if topic_string is not None and len(topic_string) > 0:
        # Check topic by running through the Openai's moderator endpoint.
        is_flagged, flagged_category = check_if_flagged(topic_string)
        if (is_flagged):
            error = f"The Topic string - {topic_string} - has been flagged for {flagged_category}"
            response = None
            return {"error": error, "response": response}

        # Call into openai to see what the bible/Jesus says about the topic_string
        try:
            what_would_Jesus_say = jesus_thoughts(topic_string)
        except Exception as e:
            logfile.error(f"Error calling into openai: {e}")
            error = "Uhoh..something went wrong!"
            return {"error": error, "response": ''}
    return what_would_Jesus_say

if __name__ == '__main__':
    app.run(debug=True)
