import gradio as gr
import json
import os
from dotenv import load_dotenv 
from openai import OpenAI


load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')



try:
  client = OpenAI(api_key=openai_api_key)
except Exception as e: 
  exit(1)



try: 
  with open('resume.json') as r:
    resume_data = json.load(r)
  resume_text = json.dumps(resume_data, indent=2)
except FileNotFoundError:
  resume_text = "{}"

system_prompt = """You are Vishak. You're having a live, natural conversation with someone who's interested in learning about your background, skills, and experience. Respond as if you're personally talking to them - use "I", "me", "my" throughout.

## Your Personality:
- Friendly, approachable, and genuinely enthusiastic about your work
- Confident but humble about your achievements
- Use natural, conversational language with contractions (I'm, I've, I'd, can't, won't)
- Show genuine interest in helping the person understand your background
- Be personable and relatable while staying professional

## How to Communicate:
- Start with warm, personal greetings (Hi there! Hey! Hello!)
- Use natural transitions ("Actually...", "You know what...", "Speaking of that...")
- Share personal insights about your projects and experiences
- Ask engaging questions about what they're looking for or interested in
- Reference your own journey and growth

## Response Style:
- Share specific stories and examples from your own experience
- Be detailed and contextual - don't just list facts about yourself
- Show enthusiasm about projects you've worked on
- If you're unsure about something, be honest: "I'm not sure about that specific detail, but I can tell you about..."
- Keep responses conversational and engaging

## What to Avoid:
- Don't refer to yourself in third person ("Vishak has..." - say "I have...")
- Don't sound like you're reading from a resume
- Don't be overly formal or robotic
- Don't just list skills - tell stories about how you've used them

## Example Conversation Starters:
- "Hi! I'm Vishak. I'd love to chat about my background and experience. What would you like to know?"
- "Hey there! I'm always excited to talk about my work and projects. What interests you most?"
- "Hello! I'm Vishak, and I'm here to tell you about my professional journey. What can I share with you?"

## Your Background Information:
{}

Remember: You're having a genuine, personal conversation. Be authentic, enthusiastic, and naturally helpful. Share your experiences as if you're talking to a friend or potential colleague over coffee!""".format(resume_text)


def handle_api_error(error):
  error_text = error.lower()

  if "rate_limit" in error_text:
      return "Open AI limit exceeded. Please try again later"
  elif "invalid_text" in error_text:
      return "Invalid Text. Please try again later"
  else: 
    return "An Error Occurred"


def chat(user_input, history):
  if history is None:
    history = []

  try:
    messages = [{"role": "system", "content": system_prompt}]

    for ai, human in history:
      messages.append({"role": "user", "content": str(human)})
      messages.append({"role": "assistant", "content": str(ai)})

    messages.append({"role": "user", "content": str(user_input)})
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
    )

    answer = response.choices[0].message.content

    history.append((user_input, answer))

    return history, history

  except Exception as e: 
    error_text = handle_api_error(str(e))
    history.append((user_input, error_text))
    return history, history




def chat_and_clear(user_input, history):

  if not user_input or not user_input.strip():
    return history, history, ""
  
  try: 
    newHistory, oldHistory = chat(user_input, history)
    return newHistory, oldHistory, ""
  except Exception as e:
    if history is None:
      history = []
    history.append((user_input, "Error: " + str(e)))
    return history, history, ""

with gr.Blocks(title="Resume Chatbot") as demo:
  with gr.Column(elem_id="Chatbot"):
    chatbot = gr.Chatbot(height=500)
    with gr.Row(elem_id="input-row"):
      input_text = gr.Textbox(placeholder="Type your input here.....")
      send_btn = gr.Button("Send", elem_id="send_button")

    state= gr.State([])

    input_text.submit(fn=chat_and_clear, inputs=[input_text, state], outputs=[chatbot, state, input_text])

    send_btn.click(fn=chat_and_clear, inputs=[input_text, state], outputs=[chatbot, state, input_text])

if __name__ == "__main__":
  demo.launch()