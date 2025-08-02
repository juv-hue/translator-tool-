import tkinter as tk
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

class LanguageTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("550x350")
        self.root.resizable(False, False)

        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())
        self.language_codes = dict(map(reversed, self.languages.items()))

        self.translator = Translator()

        # Source Language
        self.src_label = tk.Label(root, text="Source Language:", font=("Arial", 12))
        self.src_label.place(x=30, y=20)
        self.src_lang = ttk.Combobox(root, values=self.language_list, state="readonly", width=20)
        self.src_lang.place(x=170, y=22)
        self.src_lang.set("english")

        # Target Language
        self.dest_label = tk.Label(root, text="Target Language:", font=("Arial", 12))
        self.dest_label.place(x=30, y=60)
        self.dest_lang = ttk.Combobox(root, values=self.language_list, state="readonly", width=20)
        self.dest_lang.place(x=170, y=62)
        self.dest_lang.set("spanish")

        # Text Input
        self.input_text = tk.Text(root, height=5, width=60, font=("Arial", 12))
        self.input_text.place(x=30, y=100)

        # Translate Button
        self.translate_button = tk.Button(root, text="Translate", font=("Arial", 12, "bold"),
                                          command=self.translate_text, bg="#4285F4", fg="white")
        self.translate_button.place(x=230, y=210)

        # Output Label
        self.output_label = tk.Label(root, text="Translated Text:", font=("Arial", 12))
        self.output_label.place(x=30, y=250)

        # Output Box
        self.output_text = tk.Text(root, height=3, width=60, font=("Arial", 12), state="disabled")
        self.output_text.place(x=30, y=280)

    def translate_text(self):
        src = self.src_lang.get().lower()
        dest = self.dest_lang.get().lower()
        text = self.input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        try:
            src_code = self.language_codes[src]
            dest_code = self.language_codes[dest]
        except KeyError:
            messagebox.showerror("Language Error", "Invalid language selection.")
            return

        try:
            translated = self.translator.translate(text, src=src_code, dest=dest_code)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
            self.output_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Translation Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorGUI(root)
    root.mainloop()