from flask import Flask, render_template, request, jsonify
from openai import OpenAI

client = OpenAI(api_key=open("apikey.txt", "r").read())

app = Flask(__name__)

# Initial setup of the chat history as well as the initial prompt for GPT
initial_setup = [
    {
        "role": "system",
        "content": """
        You are a chat bot acting as the 
        troll under the bridge in Monty 
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

    # Include initial_setup as user instructions
    prompt = f"{initial_setup[0]['content']}\n\n{message_history[-1]['content']}"

    # Use the 'openai' object to create completions
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000
    )

    reply = completion.choices[0].text
    # Remove newline characters and strip leading/trailing whitespace
    #reply = reply.replace("\n", "").strip()

    message_history.append({"role": "assistant", "content": reply})
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
