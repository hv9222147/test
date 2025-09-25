# # Interactive Learning Program for Kids
# # -------------------------------------
# # Step-by-Step Guide (inside comments):
# #
# # 1. Install Python (>=3.8 recommended).
# # 2. Save this file as `interactive_learning.py`.
# # 3. Run with: python interactive_learning.py
# # 4. Use the buttons to explore Alphabets, Numbers, Shapes, and Quizzes.
# # 5. Each section has interactive activities.
# #
# # Libraries used: tkinter (built-in)
# # No external images are required (emojis used instead).

# import tkinter as tk
# from tkinter import messagebox

# # Main Application Class
# class InteractiveLearningApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Interactive Learning Program for Kids")
#         self.root.geometry("500x400")

#         self.score = 0

#         # Title
#         title = tk.Label(root, text="Welcome to Interactive Learning!", font=("Arial", 16, "bold"))
#         title.pack(pady=15)

#         # Buttons for sections
#         tk.Button(root, text="📚 Alphabets", width=20, command=self.alphabets).pack(pady=5)
#         tk.Button(root, text="🔢 Numbers", width=20, command=self.numbers).pack(pady=5)
#         tk.Button(root, text="🎨 Shapes & Colors", width=20, command=self.shapes).pack(pady=5)
#         tk.Button(root, text="🧩 Quiz", width=20, command=self.quiz).pack(pady=5)

#     # Alphabets Section
#     def alphabets(self):
#         win = tk.Toplevel(self.root)
#         win.title("Learn Alphabets")
#         win.geometry("300x300")

#         tk.Label(win, text="Click a Letter", font=("Arial", 14)).pack(pady=10)

#         for letter in ["A", "B", "C", "D"]:
#             tk.Button(win, text=letter, font=("Arial", 14),
#                       command=lambda l=letter: messagebox.showinfo("Alphabet", f"{l} is for {self.example_word(l)}"))\
#                 .pack(pady=5)

#     def example_word(self, letter):
#         examples = {"A": "🍎 Apple", "B": "🐻 Bear", "C": "🐱 Cat", "D": "🐶 Dog"}
#         return examples.get(letter, "Something")

#     # Numbers Section
#     def numbers(self):
#         win = tk.Toplevel(self.root)
#         win.title("Learn Numbers")
#         win.geometry("300x300")

#         tk.Label(win, text="Click a Number", font=("Arial", 14)).pack(pady=10)

#         for num in range(1, 6):
#             tk.Button(win, text=str(num), font=("Arial", 14),
#                       command=lambda n=num: messagebox.showinfo("Number", f"{n} means {n} item(s)"))\
#                 .pack(pady=5)

#     # Shapes & Colors Section
#     def shapes(self):
#         win = tk.Toplevel(self.root)
#         win.title("Learn Shapes & Colors")
#         win.geometry("300x300")

#         shapes = {"Circle ⚪": "Round shape", "Square ⬜": "4 equal sides", "Triangle 🔺": "3 sides"}

#         tk.Label(win, text="Shapes and Colors", font=("Arial", 14)).pack(pady=10)

#         for shape, meaning in shapes.items():
#             tk.Button(win, text=shape, font=("Arial", 14),
#                       command=lambda m=meaning: messagebox.showinfo("Shape", m))\
#                 .pack(pady=5)

#     # Quiz Section
#     def quiz(self):
#         win = tk.Toplevel(self.root)
#         win.title("Quiz Time!")
#         win.geometry("400x300")

#         tk.Label(win, text="What is A for?", font=("Arial", 14)).pack(pady=10)

#         options = ["🐶 Dog", "🍎 Apple", "🐱 Cat"]
#         for opt in options:
#             tk.Button(win, text=opt, font=("Arial", 12),
#                       command=lambda o=opt: self.check_answer(o, win)).pack(pady=5)

#     def check_answer(self, option, window):
#         if option == "🍎 Apple":
#             self.score += 1
#             messagebox.showinfo("Correct!", f"Good Job! 🎉 Your Score: {self.score}")
#         else:
#             messagebox.showerror("Oops!", "Try Again!")


# # Run Application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = InteractiveLearningApp(root)
#     root.mainloop()








import tkinter as tk
from tkinter import messagebox

# Main Application Class
class InteractiveLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Learning Program for Kids")
        self.root.geometry("500x400")

        self.score = 0

        # Title
        title = tk.Label(root, text="Welcome to Interactive Learning!", font=("Arial", 16, "bold"))
        title.pack(pady=15)

        # Buttons for sections
        tk.Button(root, text="📚 Alphabets", width=20, command=self.alphabets).pack(pady=5)
        tk.Button(root, text="🔢 Numbers", width=20, command=self.numbers).pack(pady=5)
        tk.Button(root, text="🎨 Shapes & Colors", width=20, command=self.shapes).pack(pady=5)
        tk.Button(root, text="🧩 Quiz", width=20, command=self.quiz).pack(pady=5)

    # Alphabets Section
    def alphabets(self):
        win = tk.Toplevel(self.root)
        win.title("Learn Alphabets")
        win.geometry("350x300")

        tk.Label(win, text="Click a Letter", font=("Arial", 14)).pack(pady=10)

        for letter in ["A", "B", "C", "D"]:
            tk.Button(win, text=letter, font=("Arial", 14),
                      command=lambda l=letter: messagebox.showinfo("Alphabet", f"{l} is for {self.example_word(l)}"))\
                .pack(pady=5)

    def example_word(self, letter):
        examples = {"A": "🍎 Apple", "B": "🐻 Bear", "C": "🐱 Cat", "D": "🐶 Dog"}
        return examples.get(letter, "Something")

    # Numbers Section
    def numbers(self):
        win = tk.Toplevel(self.root)
        win.title("Learn Numbers")
        win.geometry("350x300")

        tk.Label(win, text="Click a Number", font=("Arial", 14)).pack(pady=10)

        for num in range(1, 11):
            tk.Button(win, text=str(num), font=("Arial", 14),
                      command=lambda n=num: messagebox.showinfo("Number", f"{n} means {n} item(s)"))\
                .pack(pady=5)

    # Shapes & Colors Section
    def shapes(self):
        win = tk.Toplevel(self.root)
        win.title("Learn Shapes & Colors")
        win.geometry("350x300")

        shapes = {"Circle ⚪": "Round shape", "Square ⬜": "4 equal sides", "Triangle 🔺": "3 sides"}

        tk.Label(win, text="Shapes and Colors", font=("Arial", 14)).pack(pady=10)

        for shape, meaning in shapes.items():
            tk.Button(win, text=shape, font=("Arial", 14),
                      command=lambda m=meaning: messagebox.showinfo("Shape", m))\
                .pack(pady=5)

    # Quiz Section
    def quiz(self):
        win = tk.Toplevel(self.root)
        win.title("Quiz Time!")
        win.geometry("400x300")

        tk.Label(win, text="What is A for?", font=("Arial", 14)).pack(pady=10)

        options = ["🐶 Dog", "🍎 Apple", "🐱 Cat"]
        for opt in options:
            tk.Button(win, text=opt, font=("Arial", 12),
                      command=lambda o=opt, w=win: self.check_answer(o, w)).pack(pady=5)

    def check_answer(self, option, window):
        if option == "🍎 Apple":
            self.score += 1
            messagebox.showinfo("Correct!", f"Good Job! 🎉 Your Score: {self.score}")
            window.destroy()  # ✅ Close quiz window after correct answer
        else:
            messagebox.showerror("Oops!", "Try Again!")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveLearningApp(root)
    root.mainloop()
