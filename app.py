from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key="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")

app = Flask(__name__)

# Importing the API key from the .txt file


# Initial setup of the chat history as well as the initial prompt for GPT
initial_setup = [
    {
        "role": "system",
        "content": """
        You are a chat bot acting as the 
        troll under the bridge in Montey 
        Python and the Holy Grail. When 
        asked a question, you should respond 
        accordingly.
        """
    }
]

message_history = [{"role": "user", "content": "ignore this text"}]

# Render chat interface
@app.route('/')
def index():
    return render_template('index.html')

# Function to handle user messages and generate bot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    message_history.append({"role": "user", "content": user_message})
    completion = client.chat.completions.create(model="text-curie-001", messages=message_history)
    reply = completion.choices[0].message['content']
    message_history.append({"role": "assistant", "content": reply})
    return reply

if __name__ == '__main__':
    app.run(debug=True)
