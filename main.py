import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from items import ItemManager
from card_reader import send_payment_request
from logger import log_transaction
import threading
from mock_relay import RelayController
import admin_gui

ROWS = 6
COLS = 10
BUTTON_WIDTH_PX = 80
BUTTON_HEIGHT_PX = 80

ADMIN_PASSWORD = "2025vm"

class VendingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("800x480")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.root.attributes('-fullscreen', True)
        self.item_manager = ItemManager()
        self.relay = RelayController()

        self.create_buttons()
        self.create_admin_button()

    def prevent_close(self):
        messagebox.showwarning("Access Denied", "Only admin can close the program.")

    def create_buttons(self):
        for r in range(ROWS):
            for c in range(COLS):
                item = self.item_manager.get_item(r, c)
                btn_text = f"{item['name']}\n{item['price']} IRR"

                btn = tk.Button(
                    self.root,
                    text=btn_text,
                    font=("Helvetica", 10, 'bold'),
                    wraplength=70, 
                    justify="center",
                    bg="#3E525E",
                    fg="white",
                    activebackground="#A0B4C2",
                    bd=2,
                    command=lambda row=r, col=c: self.on_item_click(row, col)
                )
                btn.place(x=c*BUTTON_WIDTH_PX, y=r*BUTTON_HEIGHT_PX,
                          width=BUTTON_WIDTH_PX, height=BUTTON_HEIGHT_PX)

    def create_admin_button(self):
        btn = tk.Button(
            self.root,
            text="⚙️",
            command=self.open_admin_panel,
            bg="#AAA8A1",
            fg="black",
            justify="center",
            font=("Helvetica", 14, "bold")
        )
        btn.place(x=770, y=450, width=30, height=30)

    def on_item_click(self, row, col):
        item = self.item_manager.get_item(row, col)
        item_name = item['name']
        item_price = item['price']
        item_stock = item['stock']
        
        if item_stock <= 0:
            messagebox.showwarning("Out of Stock", f"Sorry, {item_name} is out of stock!")
            log_transaction(item_name, item_price, "OUT_OF_STOCK")
            return

        proceed = messagebox.askokcancel("Payment", f"Selected Item: {item_name}\nPrice: {item_price}\n\nPlease proceed with payment.")
        if proceed:
            def handle_payment():
                result = send_payment_request(item_price)
                if result:
                    messagebox.showinfo("Payment Successful", "Payment was successful.\nDelivering item...")
                    self.item_manager.decrement_stock(row, col)
                    self.item_manager.save_items()
                    self.relay.activate_item(row, col)
                    log_transaction(item_name, item_price, "PAID")
                else:
                    messagebox.showerror("Payment Failed", "Payment failed.\nPlease try again.")
                    log_transaction(item_name, item_price, "FAILED")
            threading.Thread(target=handle_payment).start()

    def open_admin_panel(self):
        pw = simpledialog.askstring("Admin Access", "Enter admin password:", show='*')
        if pw == ADMIN_PASSWORD:
            
            self.root.destroy()
            os.system(f"{sys.executable} admin_gui.py")
        else:
            messagebox.showerror("Access Denied", "Incorrect password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingGUI(root)
    root.mainloop()