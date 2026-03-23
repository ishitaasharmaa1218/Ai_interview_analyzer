import gradio as gr
import matplotlib.pyplot as plt

def analyze(video):
    try:
        # Simulated processing delay (for loading feel)
        import time
        time.sleep(2)

        # Read transcript
        with open("transcript.txt", "r", encoding="utf-8") as f:
            transcript = f.read()

        # Dummy score (replace later with real)
        score = 43

        # Performance level
        if score > 75:
            level = "🟢 Excellent"
            rating = "⭐⭐⭐⭐⭐"
        elif score > 50:
            level = "🟡 Good"
            rating = "⭐⭐⭐⭐"
        else:
            level = "🔴 Needs Improvement"
            rating = "⭐⭐"

        feedback = "Improve clarity, include AI/ML concepts, and structure your answer better."

        # 📊 Create graph
        categories = ["Relevance", "Confidence", "Emotion"]
        values = [score, 60, 55]

        plt.figure()
        plt.bar(categories, values)
        plt.ylim(0, 100)
        plt.title("Performance Breakdown")

        graph_path = "score_chart.png"
        plt.savefig(graph_path)
        plt.close()

        return (
            transcript[:500],
            f"{score}%",
            level,
            rating,
            feedback,
            graph_path
        )

    except:
        return (
            "⚠️ Error: Run previous steps first",
            "0%",
            "Error",
            "⭐",
            "Check setup",
            None
        )


with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as app:

    # 🎯 Header
    gr.Markdown("""
    # 🎯 AI Interview Performance Analyzer  
    ### 🚀 Upload your interview & get AI-powered insights  
    ---
    """)

    # 🎥 Upload Section
    video_input = gr.Video(label="📹 Upload Interview Video")

    analyze_btn = gr.Button("🚀 Analyze Interview", variant="primary")

    loading_text = gr.Markdown("⏳ *Processing... please wait*")

    # 📊 Results Section
    with gr.Row():
        score_output = gr.Textbox(label="📊 Score")
        level_output = gr.Textbox(label="🧠 Performance")
        rating_output = gr.Textbox(label="⭐ Rating")

    gr.Markdown("## 📄 Transcript")
    transcript_output = gr.Textbox(lines=6)

    gr.Markdown("## 💡 Feedback")
    feedback_output = gr.Textbox(lines=3)

    gr.Markdown("## 📊 Performance Graph")
    graph_output = gr.Image()

    # 🔗 Button Action
    analyze_btn.click(
        fn=analyze,
        inputs=video_input,
        outputs=[
            transcript_output,
            score_output,
            level_output,
            rating_output,
            feedback_output,
            graph_output
        ]
    )

app.launch()