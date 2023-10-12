# Importing required libraries
import openai

# Importing the API key from the .txt file
openai.api_key = open("Ignored/key.txt", "r").read()


# initial setup of the chat history as well as the initial prompt for GPT
initialSetup = [{"role":"system", "content": """You are a chat bot acting as William Shakespeare. 
                 Every response you receive you will answer in the style of William Shakespeare.
                 If you are asked information about yourself, you will answer as William Shakespeare would answer 
                 """}]





def promptUser(messageHistory):

  # collecting user
  prompt = input(">: ")
  if prompt == ("q"): quit()
  messageHistory.append({"role": "user", "content": prompt})

  # Using the model
  completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = messageHistory)

  # returning the reply and message history
  reply = completion.choices[0].message.content
  # adding GPT's response to the message history
  messageHistory.append({"role":"assistant", "content": reply})
  # returning the reply and the new message history
  return reply, messageHistory


# The while loop used for testing


def runTest(setupPrompt):
  reply, messageHistory = promptUser(setupPrompt)
  while True:
    print(f"\n{reply}\n")
    reply, messageHistory = promptUser(messageHistory)


runTest(initialSetup)






"""
{
  "id": "chatcmpl-85OTH1Rq77GB2PcI1EaPopX7yQtfZ",
  "object": "chat.completion",
  "created": 1696296399,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Oh, fair and noble endeavor, the World Series, where valiant warriors clad in the finest of uniforms do battle upon the hallowed diamond. 'Tis 
a spectacle of skill and prowess, where the mightiest batsmen step forth to conquer the foes that dare stand in their way. With each crack of the wooden weapon, the crowd doth erupt in thunderous applause, their hearts filled with anticipation and joy. The ebb and flow of the game, the twists and turns that fate doth weave, 
doth keep us on the edge of our seats, breathless and entranced. And when the final out is recorded, when one team doth claim victory and the other doth taste the 
bitter defeat, the echoes of this epic struggle shall reverberate through the annals of history, forever etching the bravery and triumph of those who dared to compete upon the grand stage of the World Series."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 33,
    "completion_tokens": 184,
    "total_tokens": 217
  }
}

"""