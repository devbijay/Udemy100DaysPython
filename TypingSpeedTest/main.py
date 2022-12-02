import random
import tkinter
import customtkinter
from datetime import datetime
from words import words


class TypingTest():
    def __init__(self):
        self.root_tk = customtkinter.CTk()

    def stop(self):
        self.root_tk.quit()

    def load_interface(self):
        self.start_btn = customtkinter.CTkButton(master=self.root_tk, text="Start", command=self.start)
        self.start_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def gen_rand_word(self):
        random_words = random.choices(words, k=random.randint(15, 50))
        count = len(random_words)
        random_words = [w.title() for w in random_words]
        random_words = " ".join(random_words)
        return count, random_words

    def complete(self):
        text = self.entry.get()
        if text == self.random_words:
            self.textbox.destroy()
            fin_time = (datetime.now() - self.start_time).total_seconds()
            result = customtkinter.CTkLabel(master=self.root_tk,
                                            text=f"You Completed The Typing in {fin_time} Seconds With {(60 // fin_time) * self.count} WPM")
            result.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER, )

    def start(self):
        self.count, self.random_words = self.gen_rand_word()
        self.start_btn.destroy()
        self.restart_btn = customtkinter.CTkButton(master=self.root_tk, text="Restart", command=self.start)
        self.restart_btn.place(relx=0.2, rely=0.9, anchor=tkinter.CENTER)

        self.stop = customtkinter.CTkButton(master=self.root_tk, text="Stop", command=self.stop)
        self.stop.place(relx=0.8, rely=0.9, anchor=tkinter.CENTER)

        self.textbox = customtkinter.CTkTextbox(self.root_tk)
        self.textbox.insert("0.0", self.random_words)
        self.textbox.configure(state="disabled", width=380, padx=10, pady=10)
        self.textbox.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        self.start_time = datetime.now()

        self.entry = customtkinter.CTkEntry(master=self.root_tk, placeholder_text="Start Typing Here", width=250,
                                            height=30,
                                            border_width=2,
                                            corner_radius=10)
        self.entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.complete = customtkinter.CTkButton(master=self.root_tk, text="Complete", command=self.complete)
        self.complete.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


test = TypingTest()
test.load_interface()

test.root_tk.mainloop()
