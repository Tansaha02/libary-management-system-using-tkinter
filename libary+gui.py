import tkinter as tk
from tkinter import messagebox, simpledialog

class LibraryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("400x300")

        self.List_of_books = ['java', 'php', 'python', 'javascript']
        self.Library_name = 'National Library'

        self.lend_data = {}

        for book in self.List_of_books:
            self.lend_data[book] = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to National Library")
        self.label.pack(pady=10)

        self.display_button = tk.Button(self, text="Display Books", command=self.display_books)
        self.display_button.pack()

        self.lend_button = tk.Button(self, text="Lend Book", command=self.lend_book)
        self.lend_button.pack()

        self.return_button = tk.Button(self, text="Return Book", command=self.return_book)
        self.return_button.pack()

        self.add_button = tk.Button(self, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Book", command=self.delete_book)
        self.delete_button.pack()

    def display_books(self):
        messagebox.showinfo("Books", "\n".join(self.List_of_books))

    def lend_book(self):
        book_name = self.get_input("Enter Book Name")
        author_name = self.get_input("Enter Your Name")

        if book_name in self.List_of_books:
            if self.lend_data[book_name] is None:
                self.lend_data[book_name] = author_name
                messagebox.showinfo("Success", "Book Lended Successfully!")
            else:
                messagebox.showerror("Error", f"This Book is Lend by {self.lend_data[book_name]}")
        else:
            messagebox.showerror("Error", "Invalid Book Name")

    def return_book(self):
        book_name = self.get_input("Enter Book Name")
        author_name = self.get_input("Enter Your Name")

        if book_name in self.List_of_books:
            if self.lend_data[book_name] == author_name:
                self.lend_data[book_name] = None
                messagebox.showinfo("Success", "Book Returned Successfully!")
            else:
                messagebox.showerror("Error", "This Book is Not Lend to You")
        else:
            messagebox.showerror("Error", "Invalid Book Name")

    def add_book(self):
        book_name = self.get_input("Enter Book Name")
        if book_name not in self.List_of_books:
            self.List_of_books.append(book_name)
            self.lend_data[book_name] = None
            messagebox.showinfo("Success", "Book Added Successfully!")
        else:
            messagebox.showerror("Error", "Book Already Exists")

    def delete_book(self):
        book_name = self.get_input("Enter Book Name")
        if book_name in self.List_of_books:
            self.List_of_books.remove(book_name)
            self.lend_data.pop(book_name)
            messagebox.showinfo("Success", "Book Deleted Successfully!")
        else:
            messagebox.showerror("Error", "Invalid Book Name")

    def get_input(self, message):
        return tk.simpledialog.askstring("Input", message)

if __name__ == "__main__":
    app = LibraryGUI()
    app.mainloop()
