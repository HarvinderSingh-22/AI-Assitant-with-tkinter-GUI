# AI Assistant with Tkinter GUI

import tkinter as tk
from tkinter import ttk, messagebox

# Simulated AI assistant functions

# Answer factual questions
def answer_questions(question):
    answers = {
        "What is the capital of France?": "The capital of France is Paris.",
        "Who wrote 'Pride and Prejudice'?": "Jane Austen wrote 'Pride and Prejudice'.",
        "What is the tallest mountain in the world?": "Mount Everest is the tallest mountain in the world."
    }
    return answers.get(question, "I don't know the answer to that question.")

# Summarize a given text (mocked summarization)
def summarize_text(text):
    return f"The text you entered is about {len(text.split())} words long."

# Generate creative content (mocked content generation)
def generate_creative_content(content_type):
    if content_type == "story":
        return "Once upon a time, in a faraway land, there lived a brave knight and a cunning dragon..."
    elif content_type == "poem":
        return "The autumn breeze whispers through the trees, as golden leaves fall silently beneath our feet..."
    else:
        return "In a future ruled by machines, one human discovers the key to reclaiming freedom for all."

# Feedback mechanism
def feedback(response):
    user_feedback = feedback_var.get().lower()
    if user_feedback in ['yes', 'no']:
        with open("feedback_log.txt", "a") as file:
            file.write(f"Response: {response}\nFeedback: {user_feedback}\n\n")
        messagebox.showinfo("Feedback", "Thank you for your feedback!")
    else:
        messagebox.showwarning("Invalid Input", "Please enter 'yes' or 'no' for feedback.")

# Function to handle the Question button action
def handle_question():
    question = question_entry.get()
    if question:
        response = answer_questions(question)
        result_text.set(f"AI Response: {response}")
        feedback_frame.pack(pady=10)  # Show the feedback section
    else:
        messagebox.showwarning("Input Error", "Please enter a question.")

# Function to handle the Summarize Text button action
def handle_summarize():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        response = summarize_text(text)
        result_text.set(f"Summary: {response}")
        feedback_frame.pack(pady=10)  # Show the feedback section
    else:
        messagebox.showwarning("Input Error", "Please enter text to summarize.")

# Function to handle Creative Content generation
def handle_creative_content():
    content_type = content_var.get()
    response = generate_creative_content(content_type)
    result_text.set(f"Creative Content: {response}")
    feedback_frame.pack(pady=10)  # Show the feedback section

# Create the main application window
root = tk.Tk()
root.title("AI Assistant")
root.geometry("700x600")
root.configure(bg="#F5F5F5")

# Style configuration for ttk widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12), background="#F5F5F5")
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TFrame", background="#F5F5F5")
style.configure("TRadiobutton", background="#F5F5F5", font=("Helvetica", 12))

# Title label
title_label = ttk.Label(root, text="Welcome to the AI Assistant", font=("Helvetica", 18, "bold"), background="#F5F5F5")
title_label.pack(pady=20)

# Frame for questions
question_frame = ttk.Frame(root)
question_frame.pack(pady=10, padx=10, fill=tk.X)

ttk.Label(question_frame, text="Ask a Question:", anchor="w").pack(anchor="w", padx=5)
question_entry = ttk.Entry(question_frame, width=50)
question_entry.pack(pady=5, padx=5, fill=tk.X)

# Button to ask the question
ttk.Button(question_frame, text="Get Answer", command=handle_question).pack(pady=5)

# Frame for summarization
summarize_frame = ttk.Frame(root)
summarize_frame.pack(pady=10, padx=10, fill=tk.X)

ttk.Label(summarize_frame, text="Enter Text to Summarize:", anchor="w").pack(anchor="w", padx=5)
text_entry = tk.Text(summarize_frame, height=5, width=60, wrap=tk.WORD)
text_entry.pack(pady=5, padx=5, fill=tk.X)

# Button to summarize text
ttk.Button(summarize_frame, text="Summarize Text", command=handle_summarize).pack(pady=5)

# Frame for creative content
creative_frame = ttk.Frame(root)
creative_frame.pack(pady=10, padx=10, fill=tk.X)

ttk.Label(creative_frame, text="Choose Creative Content:", anchor="w").pack(anchor="w", padx=5)
content_var = tk.StringVar(value="story")
ttk.Radiobutton(creative_frame, text="Story", variable=content_var, value="story").pack(anchor="w")
ttk.Radiobutton(creative_frame, text="Poem", variable=content_var, value="poem").pack(anchor="w")
ttk.Radiobutton(creative_frame, text="Science Fiction Idea", variable=content_var, value="sci-fi").pack(anchor="w")

# Button to generate creative content
ttk.Button(creative_frame, text="Generate Creative Content", command=handle_creative_content).pack(pady=5)

# Frame for displaying results
result_frame = ttk.Frame(root)
result_frame.pack(pady=10, padx=10, fill=tk.X)

result_text = tk.StringVar()
result_label = ttk.Label(result_frame, textvariable=result_text, wraplength=600, justify="left", background="#F5F5F5")
result_label.pack(pady=10)

# Frame for feedback
feedback_frame = ttk.Frame(root)
ttk.Label(feedback_frame, text="Was this response helpful? (yes/no):").pack()
feedback_var = ttk.Entry(feedback_frame)
feedback_var.pack(pady=5)
ttk.Button(feedback_frame, text="Submit Feedback", command=lambda: feedback(result_text.get())).pack(pady=5)

# Start the main event loop
root.mainloop()
