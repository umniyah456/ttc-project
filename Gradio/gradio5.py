import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# 🧮 Multi-Tool App")

    with gr.Tabs():

        with gr.Tab("BMI"):
            w = gr.Slider(30, 200, value=70, label="Weight (kg)")
            h = gr.Slider(100, 220, value=170, label="Height (cm)")
            btn = gr.Button("Calculate")
            out = gr.Textbox(label="Result")
            btn.click(fn=lambda w,h: f"BMI: {w/(h/100)**2:.1f}",
                      inputs=[w, h], outputs=out)

        with gr.Tab("Temperature"):
            celsius    = gr.Number(label="Celsius")
            btn2       = gr.Button("Convert")
            fahrenheit = gr.Number(label="Fahrenheit")
            btn2.click(fn=lambda c: c*9/5+32,
                       inputs=celsius, outputs=fahrenheit)

demo.launch()