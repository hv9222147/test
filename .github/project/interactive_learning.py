# # # Interactive Learning Program for Kids
# # # -------------------------------------
# # # Step-by-Step Guide (inside comments):
# # #
# # # 1. Install Python (>=3.8 recommended).
# # # 2. Save this file as `interactive_learning.py`.
# # # 3. Run with: python interactive_learning.py
# # # 4. Use the buttons to explore Alphabets, Numbers, Shapes, and Quizzes.
# # # 5. Each section has interactive activities.
# # #
# # # Libraries used: tkinter (built-in)
# # # No external images are required (emojis used instead).

# # import tkinter as tk
# # from tkinter import messagebox

# # # Main Application Class
# # class InteractiveLearningApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Interactive Learning Program for Kids")
# #         self.root.geometry("500x400")

# #         self.score = 0

# #         # Title
# #         title = tk.Label(root, text="Welcome to Interactive Learning!", font=("Arial", 16, "bold"))
# #         title.pack(pady=15)

# #         # Buttons for sections
# #         tk.Button(root, text="📚 Alphabets", width=20, command=self.alphabets).pack(pady=5)
# #         tk.Button(root, text="🔢 Numbers", width=20, command=self.numbers).pack(pady=5)
# #         tk.Button(root, text="🎨 Shapes & Colors", width=20, command=self.shapes).pack(pady=5)
# #         tk.Button(root, text="🧩 Quiz", width=20, command=self.quiz).pack(pady=5)

# #     # Alphabets Section
# #     def alphabets(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Alphabets")
# #         win.geometry("300x300")

# #         tk.Label(win, text="Click a Letter", font=("Arial", 14)).pack(pady=10)

# #         for letter in ["A", "B", "C", "D"]:
# #             tk.Button(win, text=letter, font=("Arial", 14),
# #                       command=lambda l=letter: messagebox.showinfo("Alphabet", f"{l} is for {self.example_word(l)}"))\
# #                 .pack(pady=5)

# #     def example_word(self, letter):
# #         examples = {"A": "🍎 Apple", "B": "🐻 Bear", "C": "🐱 Cat", "D": "🐶 Dog"}
# #         return examples.get(letter, "Something")

# #     # Numbers Section
# #     def numbers(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Numbers")
# #         win.geometry("300x300")

# #         tk.Label(win, text="Click a Number", font=("Arial", 14)).pack(pady=10)

# #         for num in range(1, 6):
# #             tk.Button(win, text=str(num), font=("Arial", 14),
# #                       command=lambda n=num: messagebox.showinfo("Number", f"{n} means {n} item(s)"))\
# #                 .pack(pady=5)

# #     # Shapes & Colors Section
# #     def shapes(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Shapes & Colors")
# #         win.geometry("300x300")

# #         shapes = {"Circle ⚪": "Round shape", "Square ⬜": "4 equal sides", "Triangle 🔺": "3 sides"}

# #         tk.Label(win, text="Shapes and Colors", font=("Arial", 14)).pack(pady=10)

# #         for shape, meaning in shapes.items():
# #             tk.Button(win, text=shape, font=("Arial", 14),
# #                       command=lambda m=meaning: messagebox.showinfo("Shape", m))\
# #                 .pack(pady=5)

# #     # Quiz Section
# #     def quiz(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Quiz Time!")
# #         win.geometry("400x300")

# #         tk.Label(win, text="What is A for?", font=("Arial", 14)).pack(pady=10)

# #         options = ["🐶 Dog", "🍎 Apple", "🐱 Cat"]
# #         for opt in options:
# #             tk.Button(win, text=opt, font=("Arial", 12),
# #                       command=lambda o=opt: self.check_answer(o, win)).pack(pady=5)

# #     def check_answer(self, option, window):
# #         if option == "🍎 Apple":
# #             self.score += 1
# #             messagebox.showinfo("Correct!", f"Good Job! 🎉 Your Score: {self.score}")
# #         else:
# #             messagebox.showerror("Oops!", "Try Again!")


# # # Run Application
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = InteractiveLearningApp(root)
# #     root.mainloop()








# # import tkinter as tk
# # from tkinter import messagebox

# # # Main Application Class
# # class InteractiveLearningApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Interactive Learning Program for Kids")
# #         self.root.geometry("500x400")

# #         self.score = 0

# #         # Title
# #         title = tk.Label(root, text="Welcome to Interactive Learning!", font=("Arial", 16, "bold"))
# #         title.pack(pady=15)

# #         # Buttons for sections
# #         tk.Button(root, text="📚 Alphabets", width=20, command=self.alphabets).pack(pady=5)
# #         tk.Button(root, text="🔢 Numbers", width=20, command=self.numbers).pack(pady=5)
# #         tk.Button(root, text="🎨 Shapes & Colors", width=20, command=self.shapes).pack(pady=5)
# #         tk.Button(root, text="🧩 Quiz", width=20, command=self.quiz).pack(pady=5)

# #     # Alphabets Section
# #     def alphabets(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Alphabets")
# #         win.geometry("350x300")

# #         tk.Label(win, text="Click a Letter", font=("Arial", 14)).pack(pady=10)

# #         for letter in ["A", "B", "C", "D"]:
# #             tk.Button(win, text=letter, font=("Arial", 14),
# #                       command=lambda l=letter: messagebox.showinfo("Alphabet", f"{l} is for {self.example_word(l)}"))\
# #                 .pack(pady=5)

# #     def example_word(self, letter):
# #         examples = {"A": "🍎 Apple", "B": "🐻 Bear", "C": "🐱 Cat", "D": "🐶 Dog"}
# #         return examples.get(letter, "Something")

# #     # Numbers Section
# #     def numbers(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Numbers")
# #         win.geometry("350x300")

# #         tk.Label(win, text="Click a Number", font=("Arial", 14)).pack(pady=10)

# #         for num in range(1, 6):
# #             tk.Button(win, text=str(num), font=("Arial", 14),
# #                       command=lambda n=num: messagebox.showinfo("Number", f"{n} means {n} item(s)"))\
# #                 .pack(pady=5)

# #     # Shapes & Colors Section
# #     def shapes(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Learn Shapes & Colors")
# #         win.geometry("350x300")

# #         shapes = {"Circle ⚪": "Round shape", "Square ⬜": "4 equal sides", "Triangle 🔺": "3 sides"}

# #         tk.Label(win, text="Shapes and Colors", font=("Arial", 14)).pack(pady=10)

# #         for shape, meaning in shapes.items():
# #             tk.Button(win, text=shape, font=("Arial", 14),
# #                       command=lambda m=meaning: messagebox.showinfo("Shape", m))\
# #                 .pack(pady=5)

# #     # Quiz Section
# #     def quiz(self):
# #         win = tk.Toplevel(self.root)
# #         win.title("Quiz Time!")
# #         win.geometry("400x300")

# #         tk.Label(win, text="What is A for?", font=("Arial", 14)).pack(pady=10)

# #         options = ["🐶 Dog", "🍎 Apple", "🐱 Cat"]
# #         for opt in options:
# #             tk.Button(win, text=opt, font=("Arial", 12),
# #                       command=lambda o=opt, w=win: self.check_answer(o, w)).pack(pady=5)

# #     def check_answer(self, option, window):
# #         if option == "🍎 Apple":
# #             self.score += 1
# #             messagebox.showinfo("Correct!", f"Good Job! 🎉 Your Score: {self.score}")
# #             window.destroy()  # ✅ Close quiz window after correct answer
# #         else:
# #             messagebox.showerror("Oops!", "Try Again!")

# # # Run Application
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = InteractiveLearningApp(root)
# #     root.mainloop()







# # import tkinter as tk
# # from tkinter import messagebox

# # # Main Application Class
# # class InteractiveLearningApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Interactive Learning Program for Kids")
# #         self.root.geometry("600x400")
# #         self.root.config(bg="#F9F5E7")

# #         self.score = 0  # keeps track of kids' points

# #         # Title Label
# #         title = tk.Label(root, text="✨ Interactive Learning Program for Kids ✨",
# #                          font=("Comic Sans MS", 18, "bold"),
# #                          bg="#F9F5E7", fg="#5A2D82")
# #         title.pack(pady=20)

# #         # Buttons for activities
# #         quiz_btn = tk.Button(root, text="📝 Quiz Game", font=("Arial", 14),
# #                              bg="#A8DF8E", command=self.start_quiz)
# #         quiz_btn.pack(pady=10)

# #         math_btn = tk.Button(root, text="➕ Math Game", font=("Arial", 14),
# #                              bg="#FDCEDF", command=self.start_math_game)
# #         math_btn.pack(pady=10)

# #         spelling_btn = tk.Button(root, text="🔤 Spelling Game", font=("Arial", 14),
# #                                  bg="#90E0EF", command=self.start_spelling_game)
# #         spelling_btn.pack(pady=10)

# #         # Score Label
# #         self.score_label = tk.Label(root, text=f"Score: {self.score}",
# #                                     font=("Arial", 14, "bold"),
# #                                     bg="#F9F5E7", fg="#DE201A")
# #         self.score_label.pack(pady=20)

# #         # Exit Button
# #         exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 14),
# #                              bg="#D04B4B", command=self.exit_program)
# #         exit_btn.pack(pady=10)

# #     # ----------------- Functions for activities -----------------
# #     def start_quiz(self):
# #         answer = messagebox.askquestion("Quiz Time!", "Is the sky blue?")
# #         if answer == "yes":
# #             self.update_score(10)
# #             messagebox.showinfo("Correct!", "Great job! +10 points 🎉")
# #         else:
# #             messagebox.showwarning("Oops!", "That’s not correct!")

# #     def start_math_game(self):
# #         answer = messagebox.askinteger("Math Game", "What is 5 + 3 ?")
# #         if answer == 8:
# #             self.update_score(10)
# #             messagebox.showinfo("Correct!", "You got it! +10 points 🎉")
# #         else:
# #             messagebox.showwarning("Oops!", "Try again!")

# #     def start_spelling_game(self):
# #         answer = messagebox.askstring("Spelling Game", "Spell the word: CAT")
# #         if answer and answer.lower() == "cat":
# #             self.update_score(10)
# #             messagebox.showinfo("Correct!", "Awesome! +10 points 🎉")
# #         else:
# #             messagebox.showwarning("Oops!", "That’s not correct!")

# #     def update_score(self, points):
# #         self.score += points
# #         self.score_label.config(text=f"Score: {self.score}")

# #     def exit_program(self):
# #         self.root.quit()


# # # ----------------- Run the App -----------------
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = InteractiveLearningApp(root)
# #     root.mainloop()






# import sys

# try:
#     import tkinter as tk
#     from tkinter import messagebox, simpledialog
# except ImportError:
#     print("ERROR: tkinter is not installed on this system.")
#     print("On Debian/Ubuntu: sudo apt install python3-tk")
#     print("On Fedora: sudo dnf install python3-tkinter")
#     print("On Arch: sudo pacman -S tk")
#     print("With conda: conda install -c anaconda tk")
#     print("On Windows/macOS: install Python from python.org (includes Tcl/Tk).")
#     sys.exit(1)

# class InteractiveLearningApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Interactive Learning Program for Kids")
#         self.root.geometry("600x420")
#         self.root.config(bg="#F9F5E7")

#         self.score = 0  # keeps track of kids' points

#         # Title Label
#         title = tk.Label(root, text="✨ Interactive Learning Program for Kids ✨",
#                          font=("Comic Sans MS", 18, "bold"),
#                          bg="#F9F5E7", fg="#5A2D82")
#         title.pack(pady=18)

#         # Buttons for activities
#         quiz_btn = tk.Button(root, text="📝 Quiz Game", font=("Arial", 14),
#                              bg="#A8DF8E", width=20, command=self.start_quiz)
#         quiz_btn.pack(pady=8)

#         math_btn = tk.Button(root, text="➕ Math Game", font=("Arial", 14),
#                              bg="#FDCEDF", width=20, command=self.start_math_game)
#         math_btn.pack(pady=8)

#         spelling_btn = tk.Button(root, text="🔤 Spelling Game", font=("Arial", 14),
#                                  bg="#90E0EF", width=20, command=self.start_spelling_game)
#         spelling_btn.pack(pady=8)

#         # Score Label
#         self.score_label = tk.Label(root, text=f"Score: {self.score}",
#                                     font=("Arial", 14, "bold"),
#                                     bg="#F9F5E7", fg="#D9534F")
#         self.score_label.pack(pady=14)

#         # Exit Button
#         exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 14),
#                              bg="#FF6B6B", width=10, command=self.exit_program)
#         exit_btn.pack(pady=6)

#     # ----------------- Functions for activities -----------------
#     def start_quiz(self):
#         # askyesno returns True/False (easier to check)
#         ok = messagebox.askyesno("Quiz Time!", "Is the sky blue?")
#         if ok:
#             self.update_score(10)
#             messagebox.showinfo("Correct!", "Great job! +10 points 🎉")
#         else:
#             messagebox.showwarning("Oops!", "That’s not correct!")

#     def start_math_game(self):
#         # use simpledialog for numeric input
#         answer = simpledialog.askinteger("Math Game", "What is 5 + 3 ?", parent=self.root)
#         if answer is None:
#             return  # user cancelled
#         if answer == 8:
#             self.update_score(10)
#             messagebox.showinfo("Correct!", "You got it! +10 points 🎉")
#         else:
#             messagebox.showwarning("Oops!", "Try again!")

#     def start_spelling_game(self):
#         answer = simpledialog.askstring("Spelling Game", "Spell the word: CAT", parent=self.root)
#         if answer is None:
#             return  # user cancelled
#         if answer.strip().lower() == "cat":
#             self.update_score(10)
#             messagebox.showinfo("Correct!", "Awesome! +10 points 🎉")
#         else:
#             messagebox.showwarning("Oops!", "That’s not correct!")

#     def update_score(self, points):
#         self.score += points
#         self.score_label.config(text=f"Score: {self.score}")

#     def exit_program(self):
#         if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
#             self.root.quit()


# # ----------------- Run the App -----------------
# if __name__ == "__main__":
#     # On headless servers you may get: TclError: no display name and no $DISPLAY environment variable
#     # Run this on your local machine with a GUI (Windows, macOS, or desktop Linux)
#     root = tk.Tk()
#     app = InteractiveLearningApp(root)
#     root.mainloop()




import sys
import os
import tkinter as tk
import PIL
import PIL.Image
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # top me import karein

class InteractiveLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Learning Program for Kids")
        self.root.geometry("1500x1000")
        # self.root.config(bg="#F9F5E7")  # background image laga rahe hain, ye comment ya hata dein

        # ----------------- Background Image -----------------
        self.bg_image = Image.open("cartoon_background.png")  # aapka image file
        self.bg_image = self.bg_image.resize((1500, 1000))  # window size ke hisaab se
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.score = 0

        # Title Label
        title = tk.Label(root, text="✨ Interactive Learning Program for Kids ✨",
                         font=("Comic Sans MS", 18, "bold"),
                         bg="#F9F5E7", fg="#5A2D82")
        title.pack(pady=18)

        # Buttons for activities
        quiz_btn = tk.Button(root, text="📝 Quiz Game", font=("Arial", 14),
                             bg="#A8DF8E", width=20, command=self.start_quiz)
        quiz_btn.pack(pady=8)

        math_btn = tk.Button(root, text="➕ Math Game", font=("Arial", 14),
                             bg="#FDCEDF", width=20, command=self.start_math_game)
        math_btn.pack(pady=8)

        spelling_btn = tk.Button(root, text="🔤 Spelling Game", font=("Arial", 14),
                                 bg="#90E0EF", width=20, command=self.start_spelling_game)
        spelling_btn.pack(pady=8)

        # Score Label
        self.score_label = tk.Label(root, text=f"Score: {self.score}",
                                    font=("Arial", 14, "bold"),
                                    bg="#F9F5E7", fg="#D9534F")
        self.score_label.pack(pady=14)

        # Exit Button
        exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 14),
                             bg="#FF6B6B", width=10, command=self.exit_program)
        exit_btn.pack(pady=6)

        # ----------------- Questions -----------------
        self.quiz_questions = [
            {"question": "Is the sky blue?", "answer": "yes"},
            {"question": "Is grass red?", "answer": "no"},
            {"question": "Is the sun yellow?", "answer": "yes"}
        ]

        self.math_questions = [
            {"question": "5 + 3 = ?", "answer": 8},
            {"question": "10 - 4 = ?", "answer": 6},
            {"question": "2 x 3 = ?", "answer": 6}
        ]

        self.spelling_questions = [
            {"question": "spell the word CAT", "answer": "cat"},
            {"question": "spell the word DOG", "answer": "dog"},
            {"question": "spell the word FISH", "answer": "fish"}
        ]

    # ----------------- Functions for activities -----------------
    def start_quiz(self):
        for q in self.quiz_questions:
            user_answer = messagebox.askyesno("Quiz Time!", q["question"])
            correct = q["answer"] == "yes" and user_answer or q["answer"] == "no" and not user_answer
            if correct:
                self.update_score(10)
                messagebox.showinfo("Correct!", "Great job! +10 points 🎉")
            else:
                messagebox.showwarning("Oops!", "That’s not correct!")

    def start_math_game(self):
        for q in self.math_questions:
            answer = simpledialog.askinteger("Math Game", q["question"], parent=self.root)
            if answer is None:
                continue  # skip if cancelled
            if answer == q["answer"]:
                self.update_score(10)
                messagebox.showinfo("Correct!", "You got it! +10 points 🎉")
            else:
                messagebox.showwarning("Oops!", "Try again!")

    def start_spelling_game(self):
        for q in self.spelling_questions:
            answer = simpledialog.askstring("Spelling Game", q["question"], parent=self.root)
            if answer is None:
                continue
            if answer == q["answer"]:
                self.update_score(10)
                messagebox.showinfo("Correct!", "Awesome! +10 points 🎉")
            else:            
                messagebox.showwarning("Oops!", "That’s not correct!")

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
            self.root.quit()


# ----------------- Run the App -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveLearningApp(root)
    root.mainloop()
