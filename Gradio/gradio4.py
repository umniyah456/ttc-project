import gradio as gr

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5: category = "Underweight"
    elif bmi < 25: category = "Normal weight"
    elif bmi < 30: category = "Overweight"
    else: category = "Obese"
    return f"{bmi:.1f}", category

with gr.Blocks(title="BMI Pro") as demo:

    gr.Markdown("# BMI Calculator")

    with gr.Row():
        weight = gr.Slider(30, 200, value=70, label="Weight (kg)")
        height = gr.Slider(100, 220, value=170, label="Height (cm)")

    btn = gr.Button("Calculate BMI", variant="primary")

    with gr.Row():
        bmi_out = gr.Textbox(label="BMI Score")
        cat_out = gr.Textbox(label="Category")

    btn.click(
        fn = calculate_bmi,
        inputs = [weight, height],
        outputs = [bmi_out, cat_out]
    )

demo.launch()