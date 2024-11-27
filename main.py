import gradio as gr
from tone_analysis import ToneAnalyzer

tone_dict_path = 'tone-dict-uk.tsv'
analyzer = ToneAnalyzer(tone_dict_path)

def gradio_interface(text):
    if not text.strip():
        return "Будь ласка, введіть текст для аналізу.", "", ""

    try:
        highlighted_text, total_tone, tone_label = analyzer.analyze_tone(text)
        return highlighted_text, f"Загальна тональність: {total_tone}", f"Оцінка тональності: {tone_label}"
    except Exception as e:
        return f"Сталася помилка: {str(e)}", "", ""

with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("# Аналіз Тональності Тексту")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(lines=5, placeholder="Введіть текст для аналізу", label="Input")
        with gr.Column():
            output_highlighted = gr.HTML(label="Підсвічений текст")
            output_tone = gr.Textbox(interactive=False, label="Загальна тональність")
            output_label = gr.Textbox(interactive=False, label="Оцінка тональності")

    submit_button = gr.Button("Аналізувати")
    submit_button.click(fn=gradio_interface, inputs=input_text, outputs=[output_highlighted, output_tone, output_label])

iface.launch()
