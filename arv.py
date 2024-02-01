import random
from typing import Tuple, Union, List, Dict, Any 
import datetime
import random
import tkinter as tk
from tkinter import messagebox
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QDateTimeEdit

class EventTaskingUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Event number and status
        event_number_layout = QHBoxLayout()
        event_number_label = QLabel('Event number:')
        event_number_input = QLineEdit()
        event_number_layout.addWidget(event_number_label)
        event_number_layout.addWidget(event_number_input)

        current_event_status_label = QLabel('Current event status:')
        event_number_layout.addWidget(current_event_status_label)
        
        main_layout.addLayout(event_number_layout)

        # Setup
        setup_label = QLabel('Setup')
        main_layout.addWidget(setup_label)

        # Tasking
        tasking_label = QLabel('1. Enter event information:')
        main_layout.addWidget(tasking_label)

        # Wording/Cue
        wording_label = QLabel('2. Create wording/cue for your task:')
        main_layout.addWidget(wording_label)

        # TRN(s)
        trn_label = QLabel('3. Generate TRN(s) for your task:')
        main_layout.addWidget(trn_label)

        trn_layout = QHBoxLayout()
        names = ['Andrew', 'Kyle Turner:', 'Vincent', 'Mark Howey']
        for name in names:
            trn_layout.addWidget(QLabel(name))
            trn_layout.addWidget(QLineEdit())

        main_layout.addLayout(trn_layout)

        # Date/Time
        date_time_layout = QHBoxLayout()
        date_time_label = QLabel('4. Set transcript(s) due date / time:')
        date_time_edit = QDateTimeEdit()
        date_time_layout.addWidget(date_time_label)
        date_time_layout.addWidget(date_time_edit)
        main_layout.addLayout(date_time_layout)

        # Buttons
        preview_button = QPushButton('Preview task/email:')
        send_button = QPushButton('Send (to all)')
        main_layout.addWidget(preview_button)
        main_layout.addWidget(send_button)

        self.setLayout(main_layout)
        self.setWindowTitle('Event Tasking UI')
        self.setGeometry(300, 300, 400, 200)

def main():
    app = QApplication(sys.argv)
    ex = EventTaskingUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


class TaskingView(tk.Toplevel):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tasking View")
        self.create_widgets()

    def create_widgets(self):
        self.reveal_button = tk.Button(
            self.root, text="Reveal", command=self.reveal)
        self.reveal_button.pack()
        self.text = tk.Text(self.root, height=12, width=40)
        self.text.pack()

    def reveal(self):
        self.associations = self.mode.assign()
        display_text = "\n".join(
            f"{key}: {value}" for key, value in self.associations.items())
        self.text.delete(1.0, tk.END)
        self.text.insert

class Event:
    def __init__(self, event_id, event_name, event_type, event_date, event_time, event_pair, outcomes, full_line_info):
        self.event_id = event_id
        self.event_name = event_name
        self.event_type = event_type
        self.event_date = event_date
        self.event_time = event_time
        self.event_pair = event_pair
        self.outcomes = outcomes
        self.full_line_info = full_line_info

    def set_event_attributes(self):
        root = tk.Tk()

        # Create entry forms for each attribute
        event_id_entry = tk.Entry(root)
        event_name_entry = tk.Entry(root)
        event_type_entry = tk.Entry(root)
        event_date_entry = tk.Entry(root)
        event_time_entry = tk.Entry(root)
        event_pair_entry = tk.Entry(root)
        outcomes_entry = tk.Entry(root)
        full_line_info_entry = tk.Entry(root)

        # Function to set the attributes when the button is clicked
        def set_attributes():
            self.event_id = event_id_entry.get()
            self.event_name = event_name_entry.get()
            self.event_type = event_type_entry.get()
            self.event_date = event_date_entry.get()
            self.event_time = event_time_entry.get()
            self.event_pair = event_pair_entry.get()
            self.outcomes = outcomes_entry.get()
            self.full_line_info = full_line_info_entry.get()

            messagebox.showinfo("Success", "Event attributes set successfully!")

        # Create a button to set the attributes
        set_attributes_button = tk.Button(root, text="Set Attributes", command=set_attributes)

        # Grid layout for the entry forms and button
        event_id_entry.grid(row=0, column=1)
        event_name_entry.grid(row=1, column=1)
        event_type_entry.grid(row=2, column=1)
        event_date_entry.grid(row=3, column=1)
        event_time_entry.grid(row=4, column=1)
        event_pair_entry.grid(row=5, column=1)
        outcomes_entry.grid(row=6, column=1)
        full_line_info_entry.grid(row=7, column=1)
        set_attributes_button.grid(row=8, column=1)

        root.mainloop()
            
       
       
       
class Judge:
    def __init__(self):
        pass 


class  