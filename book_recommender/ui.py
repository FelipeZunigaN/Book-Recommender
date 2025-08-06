import gradio as gr

def launch_dashboard(recommend_callback, categories, tones):
    with gr.Blocks(theme=gr.themes.Glass()) as dashboard:
        gr.Markdown("# 📚 Semantic Book Recommender")

        with gr.Row():
            query = gr.Textbox(label="Describe your book:", placeholder="e.g. A touching story of redemption")
            category = gr.Dropdown(choices=categories, label="Category", value="All")
            tone = gr.Dropdown(choices=tones, label="Emotional tone", value="All")
            button = gr.Button("Recommend")

        gr.Markdown("## Recommendations")
        output = gr.Gallery(label="Books", columns=8, rows=2)

        button.click(fn=recommend_callback, inputs=[query, category, tone], outputs=output)

    return dashboard
