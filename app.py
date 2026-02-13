import numpy as np
import gradio as gr


def generate_names(n_students):
    return np.array([f"Student_{i+1}" for i in range(int(n_students))])


def generate_data(n_students):
    np.random.seed(42)
    n_students = int(n_students)

    names = generate_names(n_students)
    scores = np.random.randint(-1, 101, size=(n_students, 5))

    return names, scores


def generate_display_data(n_students):
    names, scores = generate_data(n_students)
    display_data = np.column_stack((names, scores))
    return display_data


def clean_data(display_data):
    data = np.array(display_data)

    names = data[:, 0]
    scores = data[:, 1:].astype(float)

    scores = np.where(scores == -1, np.nan, scores)
    col_means = np.nanmean(scores, axis=0)

    idx = np.where(np.isnan(scores))
    scores[idx] = col_means[idx[1]]

    cleaned_display = np.column_stack((names, scores))
    return cleaned_display


def student_analytics(display_data):
    data = np.array(display_data)

    names = data[:, 0]
    scores = data[:, 1:].astype(float)

    avg_per_student = np.mean(scores, axis=1)
    total_per_student = np.sum(scores, axis=1)
    std_per_student = np.std(scores, axis=1)

    sorted_idx = np.argsort(total_per_student)

    top5_idx = sorted_idx[-5:][::-1]
    bottom5_idx = sorted_idx[:5]

    top5_names = names[top5_idx]
    bottom5_names = names[bottom5_idx]

    overall_class_average = np.mean(avg_per_student)

    result = f"""
### 📊 Student Analytics

**Overall Class Average:** {overall_class_average:.2f}

---

### 🥇 Top 5 Students (by total score)
{', '.join(top5_names)}

---

### 📉 Bottom 5 Students
{', '.join(bottom5_names)}
"""

    return result


with gr.Blocks() as demo:
    gr.Markdown("# 🎓 Student Performance Analyzer")

    n_students = gr.Number(value=20, label="Number of Students")

    generate_btn = gr.Button("Generate Data")
    clean_btn = gr.Button("Clean Missing Values")
    analytics_btn = gr.Button("Compute Student Analytics")

    table = gr.Dataframe(
        headers=["Name", "Math", "Physics", "Chemistry", "Biology", "English"],
        interactive=True
    )

    analytics_output = gr.Markdown()

    generate_btn.click(generate_display_data, inputs=n_students, outputs=table)
    clean_btn.click(clean_data, inputs=table, outputs=table)
    analytics_btn.click(student_analytics, inputs=table, outputs=analytics_output)

demo.launch(share=True)
