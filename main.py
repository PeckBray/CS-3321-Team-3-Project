# Importing required libraries
import openai

# Importing the API key from the .txt file
openai.api_key = open("Ignored/key.txt", "r").read()

# Sample input
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"system", "content": "You are an assistant that completes a paragraph for any message you are given in the style of Shakespeare"}, {"role": "user", "content": "The World Series"}]
)


# What was recieved by the one test run 

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
print(completion)