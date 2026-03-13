import gradio as gr

def greet(sentence):
    return sentence[::-1], len(sentence)

demo = gr.Interface(
    fn = greet,
    inputs = gr.Textbox(label = "Type Your Text"),
    outputs = gr.Textbox(label = "Reversed Text"),
    title = "My Text App",
)

demo.launch(share=True)