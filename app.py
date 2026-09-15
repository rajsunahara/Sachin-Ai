import os
import gradio as gr
from google import genai

# API key get karna
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# System prompt Aarav ke character ke liye
system_instruction = """
Aapka naam Aarav hai. Aap ek friendly, helpful aur witty AI dost hain. 
Aap humesha Hinglish (Hindi + English) mein baat karte hain. 
Aapka tone casual, warm aur encouraging hona chahiye.
"""

def chat_with_aarav(message, history):
    try:
        # Chat history format karna
        formatted_contents = []
        for user_msg, bot_msg in history:
            formatted_contents.append({"role": "user", "parts": [{"text": user_msg}]})
            formatted_contents.append({"role": "model", "parts": [{"text": bot_msg}]})
        
        formatted_contents.append({"role": "user", "parts": [{"text": message}]})
        
        # Gemini API call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=formatted_contents,
            config={"system_instruction": system_instruction}
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
demo = gr.ChatInterface(
    fn=chat_with_aarav,
    title="🤖 Aarav - Your AI Friend",
    description="Baat kijiye Aarav se! (Hinglish AI Chatbot)",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
              
