# 🥤 Vending Machine with Raspberry Pi

This is a complete vending machine system built using a Raspberry Pi 3 and a touchscreen monitor. It features a customer interface, an admin panel, relay-based control logic, and a mock payment system simulating real-world card transactions.

This project was developed as a real-world engineering challenge during my university studies and represents my first hands-on experience with hardware integration and embedded GUI systems.


---

## 📸 Screenshots

**Customer Panel:**



![Screenshot from 2025-06-27 18-19-24](https://github.com/user-attachments/assets/c5e4f9b7-c2bb-4140-a467-cc7bb99dcc2f)


**Admin Panel:**	



![Screenshot from 2025-06-27 18-19-39](https://github.com/user-attachments/assets/2052ec6b-18e9-484e-9d24-5f7290fd0a58)

---

## 🚀 Features

**👤 Customer Panel**

Simple and touch-friendly GUI built with tkinter

Displays a 6×10 grid of items (name, price, and stock)

Items are loaded from a JSON file

Handles product selection, mock payment processing, and relay triggering

Disables out-of-stock items automatically


**🛠 Admin Panel**

Secure login for admin access

View and edit items and stock levels

Add or remove products dynamically

Real-time activity logs

Restore item data from a backup


**⚡ Hardware Integration**

Controls a 6×10 matrix of products using 2 relays (one for row, one for column)

Connected to a touchscreen HDMI display

Communicates with a mock payment in development phase (simulates behavior of a real card reader used in production)


**🪵 Logging System**

Logs customer purchases, payment outcomes, and system events

Logs are viewable in the admin panel



---

## 💾 Technologies Used

Language: Python

Libraries: tkinter, json, datetime, os, sys, csv, threading, GPIO(fpr relay)

Hardware: Raspberry Pi 3, 5" HDMI LCD touchscreen, 2 relays

Version Control: Git & GitHub



---

## 🧠 What I Learned

Building hardware-software integrated systems from scratch

Managing GUI layouts using tkinter

Reading and writing JSON files efficiently

Controlling physical hardware components (relays) from Python

Handling real-world user flow with stock management and error handling

Structuring a multi-part project with readable code, logging, and backups

Using Git and GitHub for version tracking and modular development
