import os
import shutil
import logging
import argparse
import schedule
import time
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def setup_logging():
    logging.basicConfig(
        filename="replication.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def replicate_files(source_dir, destination_dir, file_extensions, log_widget=None):
    if not os.path.exists(source_dir):
        logging.error(f"Source directory {source_dir} does not exist.")
        if log_widget:
            log_widget.insert(tk.END, "Error: Source directory does not exist.\n")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        logging.info(f"Created destination directory: {destination_dir}")
        if log_widget:
            log_widget.insert(tk.END, f"Created destination directory: {destination_dir}\n")

    replicated_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination_dir, file)
                
                shutil.copy2(source_path, dest_path)
                logging.info(f"Copied: {source_path} -> {dest_path}")
                replicated_files.append(file)
                if log_widget:
                    log_widget.insert(tk.END, f"Copied: {source_path} -> {dest_path}\n")
                    log_widget.yview(tk.END)

    if log_widget:
        if replicated_files:
            log_widget.insert(tk.END, f"Successfully copied {len(replicated_files)} files.\n")
        else:
            log_widget.insert(tk.END, "No matching files found for replication.\n")

def schedule_replication(source, destination, extensions, interval, log_widget=None):
    schedule.every(interval).minutes.do(replicate_files, source, destination, extensions, log_widget)
    
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    threading.Thread(target=run_schedule, daemon=True).start()

class ReplicationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Replication Tool")
        
        tk.Label(root, text="Source Directory:").grid(row=0, column=0)
        self.source_entry = tk.Entry(root, width=50)
        self.source_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.select_source).grid(row=0, column=2)
        
        tk.Label(root, text="Destination Directory:").grid(row=1, column=0)
        self.dest_entry = tk.Entry(root, width=50)
        self.dest_entry.grid(row=1, column=1)
        tk.Button(root, text="Browse", command=self.select_destination).grid(row=1, column=2)
        
        tk.Label(root, text="Replication Interval (minutes):").grid(row=2, column=0)
        self.interval_entry = tk.Entry(root, width=10)
        self.interval_entry.grid(row=2, column=1)
        
        self.log_text = scrolledtext.ScrolledText(root, width=70, height=10, state='normal')
        self.log_text.grid(row=4, column=0, columnspan=3)
        
        tk.Button(root, text="Start Replication", command=self.start_replication).grid(row=3, column=1)
        
    def select_source(self):
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filedialog.askdirectory())
        
    def select_destination(self):
        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, filedialog.askdirectory())
        
    def start_replication(self):
        source = self.source_entry.get()
        destination = self.dest_entry.get()
        interval = int(self.interval_entry.get())
        
        if not source or not destination:
            messagebox.showerror("Error", "Please select source and destination directories.")
            return
        
        setup_logging()
        replicate_files(source, destination, [".cfg", ".log", ".dat"], self.log_text)
        schedule_replication(source, destination, [".cfg", ".log", ".dat"], interval, self.log_text)
        messagebox.showinfo("Success", f"Replication scheduled every {interval} minutes.")

import os

if __name__ == "__main__":
    if os.environ.get("CODESPACES"):  # Detect GitHub Codespaces
        print("Running in GitHub Codespaces (GUI not supported). Use command-line mode.")
    else:
        root = tk.Tk()
        app = ReplicationGUI(root)
        root.mainloop()

