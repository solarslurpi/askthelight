from flask import Flask, render_template, request
from ask_the_light import jesus_thoughts
from logger import get_logger
from moderator import check_if_flagged

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/', methods=['GET', 'POST'])
def index():
    logfile = get_logger('app')
    error = None
    topic_string = ''

    if request.method == 'GET':
        topic_string = request.args.get('topic_string', '')
    elif request.method == 'POST':
        topic_string = request.form.get('topic', '')
    logfile.debug(f"topic_string: {topic_string}")
    the_topic_feedback = ''
    what_would_Jesus_say = ''
    if topic_string is not None and len(topic_string) > 0:
        # Check topic by running through the Openai's moderator endpoint.
        is_flagged, flagged_category = check_if_flagged(topic_string)
        if (is_flagged):
            error = f"The Topic string - {topic_string} - has been flagged for {flagged_category}"
            response = None
            return render_template('index.html', response=response, error=error)
        # Call into openai to see what the bible/Jesus says about the topic_string
        what_would_Jesus_say = jesus_thoughts(topic_string)
        print(what_would_Jesus_say["topic"])
        print(what_would_Jesus_say["title"])
        print(what_would_Jesus_say["words"])
        
    else:
        error = "The topic string is empty. Please enter a topic."
        return render_template('index.html', title='', words='', error=error)

    return render_template('index.html', topic=what_would_Jesus_say["topic"], title=what_would_Jesus_say["title"], words=what_would_Jesus_say["words"], error=error)

if __name__ == '__main__':
    app.run(debug=True)
