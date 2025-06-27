import os
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
import tkinter.scrolledtext as st
from items import ItemManager
import csv
import subprocess


ROWS = 6
COLS = 10
BUTTON_WIDTH_PX = 80
BUTTON_HEIGHT_PX = 70
CONTROL_Y = 430

class AdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("800x480")
        self.root.resizable(False, False)
        self.item_manager = ItemManager()
        self.root.attributes('-fullscreen', True)
        self.create_buttons()
        self.create_control_buttons()

    def create_buttons(self):
        for r in range(ROWS):
            for c in range(COLS):
                item = self.item_manager.get_item(r, c)
                btn_text = f"{item['name']}\n{item['price']} IRR\nStock: {item['stock']}"

                btn = tk.Button(
                    self.root,
                    text=btn_text,
                    font=("Helvetica", 8),
                    wraplength=70,
                    justify="center",
                    bg="#5A7D7C",
                    fg="white",
                    activebackground="#91B2B1",
                    bd=1,
                    command=lambda row=r, col=c: self.edit_item(row, col)
                )
                btn.place(x=c*BUTTON_WIDTH_PX, y=r*BUTTON_HEIGHT_PX,
                          width=BUTTON_WIDTH_PX, height=BUTTON_HEIGHT_PX)

    def create_control_buttons(self):
        buttons = [
            ("➕ Add Item", self.add_item_prompt, "#4CAF50"),
            ("🗑️ Delete Item", self.delete_item_prompt, "#F44336"),
            ("📜 View Logs", self.show_logs, "#F5F849"),
            ("↩️ Back to Main", self.go_back_to_main, "#2196F3"),
            ("⛔ Exit Program", self.exit_program, "#9E9E9E")
        ]

        for i, (text, command, color) in enumerate(buttons):
            tk.Button(
                self.root,
                text=text,
                command=command,
                bg=color,
                fg="black" if color == "#F5F849" or color == "#9E9E9E" else "white",
                font=("Helvetica", 10, 'bold')
            ).place(x=25 + i * 150, y=CONTROL_Y, width=140, height=45)

    def edit_item(self, row, col):
        item = self.item_manager.get_item(row, col)

        new_price = simpledialog.askinteger("Edit Price", f"Current: {item['price']} IRR\nEnter price:")
        if new_price is None:
            return

        new_stock = simpledialog.askinteger("Edit Stock", f"Current: {item['stock']}\nEnter stock:")
        if new_stock is None:
            return

        self.item_manager.items[row][col]['price'] = new_price
        self.item_manager.items[row][col]['stock'] = new_stock
        self.item_manager.save_items()
        messagebox.showinfo("Success", "Item updated successfully.")
        self.refresh_ui()

    def add_item_prompt(self):
        name = simpledialog.askstring("Add Item", "Enter item name:")
        if not name:
            return
        try:
            price = int(simpledialog.askstring("Add Item", "Enter price:"))
            stock = int(simpledialog.askstring("Add Item", "Enter stock:"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid price or stock.")
            return

        # Find empty slot
        for r in range(ROWS):
            for c in range(COLS):
                if self.item_manager.items[r][c]['name'] == "Empty":
                    self.item_manager.items[r][c] = {
                        "name": name,
                        "price": price,
                        "stock": stock
                    }
                    self.item_manager.save_items()
                    messagebox.showinfo("Success", f"{name} added at ({r},{c})")
                    self.refresh_ui()
                    return

        messagebox.showwarning("Full", "No empty slot available.")

    def delete_item_prompt(self):
        name = simpledialog.askstring("Delete Item", "Enter item name to delete:")
        if not name:
            return

        for r in range(ROWS):
            for c in range(COLS):
                if self.item_manager.items[r][c]['name'].lower() == name.lower():
                    confirm = messagebox.askyesno("Confirm Delete", f"Delete {name} at ({r},{c})?")
                    if confirm:
                        self.item_manager.items[r][c] = {
                            "name": "Empty",
                            "price": 0,
                            "stock": 0
                        }
                        self.item_manager.save_items()
                        messagebox.showinfo("Deleted", f"{name} removed from ({r},{c})")
                        self.refresh_ui()
                        return
        messagebox.showerror("Not Found", f"No item named '{name}' found.")

    def show_logs(self):
        log_window = tk.Toplevel(self.root)
        log_window.title("Transaction Logs")
        log_window.geometry("700x400")

        text_area = st.ScrolledText(log_window, wrap=tk.WORD, font=("Courier New", 10))
        text_area.pack(fill=tk.BOTH, expand=True)

        log_path = "logs.csv"
        if not os.path.isfile(log_path):
            text_area.insert(tk.END, "No logs found.")
            return

        try:
            with open(log_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    text_area.insert(tk.END, "\t".join(row) + "\n")
        except Exception as e:
            text_area.insert(tk.END, f"Error reading logs: {e}")

    def go_back_to_main(self):
        result = messagebox.askyesno("Return", "Return to the main screen?")
        if result:
            self.root.destroy()
            subprocess.Popen([sys.executable, "gui.py"])

    def exit_program(self):
        result = messagebox.askyesno("Exit", "Are you sure you want to exit the program?")
        if result:
            self.root.quit()

    def refresh_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_buttons()
        self.create_control_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminGUI(root)
    root.mainloop()