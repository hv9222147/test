# import tkinter as tk
# from tkinter import messagebox, simpledialog

# class InteractiveLearningApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Interactive Learning Program for Kids")
#         self.root.geometry("1500x1000")
#         self.root.config(bg="#FDEBD0")  # Soft kid-friendly background

#         self.score = 0
#         self.current_question = 0

#         # Questions and answers
#         self.questions = [
#             {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
#             {"question": "Which animal barks?", "options": ["Cat", "Dog", "Cow"], "answer": "Dog"},
#             {"question": "What color is the sky?", "options": ["Blue", "Green", "Red"], "answer": "Blue"}
#         ]

#         # Title label
#         self.title_label = tk.Label(root, text="Welcome to Learning Fun!", font=("Arial", 20, "bold"), bg="#FDEBD0")
#         self.title_label.pack(pady=20)

#         # Start button
#         self.start_button = tk.Button(root, text="Start Quiz", font=("Arial", 16), bg="#85C1E9", command=self.start_quiz)
#         self.start_button.pack(pady=20)

#         # Question label
#         self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, bg="#FDEBD0")
#         self.question_label.pack(pady=20)

#         # Option buttons
#         self.option_buttons = []
#         for i in range(3):
#             btn = tk.Button(root, text="", font=("Arial", 14), width=15, command=lambda idx=i: self.check_answer(idx))
#             btn.pack(pady=5)
#             self.option_buttons.append(btn)

#         # Score label
#         self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="#FDEBD0")
#         self.score_label.pack(pady=20)

#     def start_quiz(self):
#         self.score = 0
#         self.current_question = 0
#         self.score_label.config(text=f"Score: {self.score}")
#         self.show_question()

#     def show_question(self):
#         if self.current_question < len(self.questions):
#             q = self.questions[self.current_question]
#             self.question_label.config(text=q["question"])
#             for idx, option in enumerate(q["options"]):
#                 self.option_buttons[idx].config(text=option)
#         else:
#             messagebox.showinfo("Quiz Finished", f"Congratulations! Your final score is: {self.score}")
#             self.question_label.config(text="")
#             for btn in self.option_buttons:
#                 btn.config(text="")

#     def check_answer(self, idx):
#         q = self.questions[self.current_question]
#         selected_option = q["options"][idx]
#         if selected_option == q["answer"]:
#             self.score += 1
#             messagebox.showinfo("Correct!", "Well done! 🎉")
#         else:
#             messagebox.showerror("Oops!", f"Wrong! The correct answer was: {q['answer']}")
#         self.current_question += 1
#         self.score_label.config(text=f"Score: {self.score}")
#         self.show_question()

# # Main program
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = InteractiveLearningApp(root)
#     root.mainloop()



import tkinter as tk
from tkinter import messagebox

class InteractiveLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Learning Program for Kids")
        self.root.geometry("1300x900")
        self.root.config(bg="#FDEBD0")

        self.score = 0
        self.current_question = 0

        # Questions and answers
        self.questions = [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
            {"question": "Which animal barks?", "options": ["Cat", "Dog", "Cow"], "answer": "Dog"},
            {"question": "What color is the sky?", "options": ["Blue", "Green", "Red"], "answer": "Blue"}
        ]

        # Title label
        self.title_label = tk.Label(root, text="Welcome to Learning Fun!", font=("Arial", 20, "bold"), bg="#FDEBD0")
        self.title_label.pack(pady=20)

        # Start button
        self.start_button = tk.Button(root, text="Start Quiz", font=("Arial", 16), bg="#85C1E9", command=self.start_quiz)
        self.start_button.pack(pady=20)

        # Question label (hidden initially)
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, bg="#FDEBD0")
        
        # Option buttons (hidden initially)
        self.option_buttons = []
        for i in range(3):
            btn = tk.Button(root, text="", font=("Arial", 14), width=15, command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(btn)

        # Score label
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="#FDEBD0")

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.score_label.config(text=f"Score: {self.score}")

        # Hide start button
        self.start_button.pack_forget()

        # Show question and options
        self.question_label.pack(pady=20)
        for btn in self.option_buttons:
            btn.pack(pady=5)
        self.score_label.pack(pady=20)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])
            for idx, option in enumerate(q["options"]):
                self.option_buttons[idx].config(text=option)
        else:
            messagebox.showinfo("Quiz Finished", f"Congratulations! Your final score is: {self.score}")
            self.question_label.pack_forget()
            for btn in self.option_buttons:
                btn.pack_forget()
            self.score_label.pack_forget()
            self.start_button.pack(pady=20)

    def check_answer(self, idx):
        q = self.questions[self.current_question]
        selected_option = q["options"][idx]
        if selected_option == q["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! 🎉")
        else:
            messagebox.showerror("Oops!", f"Wrong! The correct answer was: {q['answer']}")
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.show_question()


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveLearningApp(root)
    root.mainloop()
