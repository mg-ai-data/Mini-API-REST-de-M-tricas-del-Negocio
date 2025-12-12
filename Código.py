!pip install gradio pandas

import gradio as gr
import pandas as pd

# Simulación de base del negocio
data = {
    "ventas": [100, 130, 90, 160],
    "visitas": [1000, 1400, 950, 2000],
    "conversion_rate": [0.10, 0.093, 0.095, 0.08]
}
df = pd.DataFrame(data)

# Endpoint 1: obtener todo
def obtener_todo():
    return df

# Endpoint 2: obtener una métrica específica
def metric(m):
    return df[m].tolist()

with gr.Blocks() as api:
    
    gr.Markdown("### API REST de métricas del negocio")
    
    btn1 = gr.Button("Obtener todas las métricas")
    output1 = gr.Dataframe()

    btn2 = gr.Button("Ventas")
    output2 = gr.JSON()

    btn1.click(fn=obtener_todo, outputs=output1)
    btn2.click(fn=lambda: metric("ventas"), outputs=output2)

api.launch()
