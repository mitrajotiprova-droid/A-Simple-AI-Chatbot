!pip install gradio -q

import gradio as gr

def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"

    elif "name" in message:
        return "I am a simple AI chatbot."

    elif "python" in message:
        return "Python is a popular programming language used for web development, AI, data science, and more."

    elif "college" in message:
        return "I can help answer questions about studies, programming, and projects."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that question."

demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Ask a Question"),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Simple AI Chatbot",
    description="A basic chatbot built using Python and Gradio."
)

demo.launch()
