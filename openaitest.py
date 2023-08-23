import os
import openai
from config  import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Resignation\n\nDear [Name of Boss],\n\nI am writing to inform you that I am resigning from my current role as [position] with [company]. My last working day will be [date], as per the terms of my contract.\n\nI have enjoyed working with [company] and want to thank you for the opportunities I have had here. During my employment here, I have gained valuable experience in [skills/knowledge], and am grateful for the support I have had from you and my colleagues.\n\nI would like to thank you for the support and direction you have given me during my time here. I am confident that these skills will help me in my next role.\n\nPlease let me know if there is anything further I can do for you to ensure a smooth transition. I am available to offer any assistance needed over the next [time period] before I leave.\n\nOnce again, I appreciate your guidance and the time I have been given here.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1685002316,
  "id": "cmpl-7K0Mebb15n2ZrIayDMHkGKn03MxMc",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 217,
    "prompt_tokens": 9,
    "total_tokens": 226
  }
}
'''
