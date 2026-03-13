import gradio as gr

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5: category = "Underweight"
    elif bmi < 25: category = "Normal weight"
    elif bmi < 30: category = "Overweight"
    else: category = "Obese"
    return f"{bmi:.1f}", category
    
bmi_demo = gr.Interface(
    fn = calculate_bmi,
    inputs = [
        gr.Slider(30, 200, value=70, label="Weight (kg)"),
        gr.Slider(100, 220, value=170, label="Height (cm)")
    ],
    outputs = [
        gr.Textbox(label="BMI Score"),
        gr.Textbox(label="Category")
    ],
    title = "⚖️ BMI Calcualtor",
)
bmi_demo.launch()