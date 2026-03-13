import gradio as gr

def calculate_trip_cost(distance, fuel, price):
    cost = (distance/100) * fuel * price
    return f"Your trip costs ${cost:.2f}"
    
trip_cost = gr.Interface(
    fn = calculate_trip_cost,
    inputs = [
        gr.Slider(0, 2000, value=0, label="Distance (km)"),
        gr.Slider(4, 20, value=5, label="Fuel Efficiency"),
        gr.Number(label="Price Per Liter")
    ],
    outputs = [
        gr.Textbox(label="Result")
    ],
    title = "Trip Cost Estimator",
)
trip_cost.launch()