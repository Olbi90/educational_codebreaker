# GUI IMPORT
import tkinter as tk
import tkinter.ttk as ttk

# SPECIFIC TK WIDGETS
from tkinter import END, Text
from tkinter import filedialog
from pathlib import Path

# OWN MODULES
from algorithm import Algorithm
from datetime import datetime

class MainWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        # Windowsize
        self.title('Educational Codebreaker')
        window_width = str(int(self.winfo_screenwidth()/2))
        window_height = str(int(self.winfo_screenheight()/2))
        self.geometry(#window_width + 'x' + window_height +
            '+' + str(int(self.winfo_screenwidth()/2)
            - int(int(window_width)/2))
            + '+' + str(int(self.winfo_screenheight()/2)
            - int(int(window_height)/2)))
        self.resizable(False,False)
        
        # Codebreaker
        self.breaker = Algorithm

        # Variables
        self.__var_password = tk.StringVar(self, value='Enter a password (lowercase and digits only)')
        self.__var_solved = tk.StringVar(self)
        self.__var_wordlist_path = tk.StringVar(self, value = str(Path.cwd()) + '/wordlists/10-million-password-list-top-1000000.txt')
        self.__var_time = tk.DoubleVar(self, value = 0.0)
        self.__var_function = tk.StringVar(self, value = 'Bruteforce')
        self.__var_output = tk.StringVar(self, value = 'off')
        self.__var_hash = tk.StringVar(self, value = 'Modulo')
        self.__var_modulo = tk.IntVar(self, value = 0)
        self.__var_mode = tk.StringVar(self, value= 'attack')
        
        # Widgets

        # Label und Entry
        self.frame_entry = ttk.LabelFrame(self, text='Input', relief='groove')
        self.frame_entry.grid(
            row=0, column=0, columnspan=5, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        # Entryfield Password
        self.label_password = tk.Label(self.frame_entry, text='Insert a password: ')
        self.label_password.grid(
            row=0, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5, sticky=tk.W)
        self.password_entry = tk.Entry(
            self.frame_entry, textvariable=self.__var_password, width=40)
        self.password_entry.grid(
            row=0, column=1, columnspan=2, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.password_entry.bind('<FocusIn>', self.on_click)
        # Entryfield Modulo
        self.label_password = tk.Label(self.frame_entry, text='Insert a Modulo: ')
        self.label_password.grid(
            row=0, column=3, padx=(5,5), pady=(5,5), ipadx=5, ipady=5, sticky=tk.W)
        self.modulo_entry = tk.Entry(
            self.frame_entry, textvariable=self.__var_modulo, width=40)
        self.modulo_entry.grid(
            row=0, column=4, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        
        # Frame Attaks 
        self.frame_attack = ttk.LabelFrame(self, text='Attack', relief='groove')
        self.frame_attack.grid(
            row=1, column=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.combo_attack = ttk.Combobox(self.frame_attack, state='readonly',
                                        values=['Bruteforce', 'Wordlist', 'Own Wordlist'])
        self.combo_attack.grid(row=0, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.combo_attack.set(value='Bruteforce')
        self.combo_attack.bind("<<ComboboxSelected>>", self.__select_attack())

        # Frame Modulo
        self.frame_hash = ttk.LabelFrame(self, text='Hashfunction', relief='groove')
        self.frame_hash.grid(
            row=2, column=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.combo_hash = ttk.Combobox(self.frame_hash, state='readonly',
                                        values=['Modulo', 'Modulo Divide', 'Modulo Multiply'])
        self.combo_hash.grid(row=0, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.combo_hash.set(value='Modulo')
        self.combo_hash.bind("<<ComboboxSelected>>", self.__select_hash())   

        # Frame Wordlist
        self.frame_wordlist = ttk.LabelFrame(self, text='Wordlist', relief='groove')
        self.frame_wordlist.grid(
            row=3, column=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        # Entryfield Password
        self.label_password = tk.Label(self.frame_wordlist, text=self.__var_wordlist_path.get().rsplit('/',1)[-1])
        self.label_password.grid(
            row=0, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5, sticky=tk.W)
        
        # Terminalwindow
        self.frame_terminal = ttk.LabelFrame(self, text='Terminal', relief='groove')
        self.frame_terminal.grid(
            row=1, column=0, rowspan=5, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.text_output = tk.Text(
            self.frame_terminal, state='disabled',height=15)
        self.text_output.grid(
            row=0, column=0, columnspan=4, rowspan=5, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.NSEW)
        
        # Options
        self.frame_options = ttk.LabelFrame(self, text='Options', relief='groove')
        self.frame_options.grid(
            row=6, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        
        # Hash, Attack, Scenario
        self.radio_attack = ttk.Radiobutton(
            self.frame_options, text='Attack Mode', variable=self.__var_mode,
            value='attack', command=lambda: self.__mode_change())
        self.radio_attack.grid(
            row=0, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.radio_attack.invoke()
        self.radio_hash = ttk.Radiobutton(
            self.frame_options, text='Hash Mode', variable=self.__var_mode,
            value='hash', command=lambda: self.__mode_change())
        self.radio_hash.grid(
            row=0, column=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.radio_scenario = ttk.Radiobutton(
            self.frame_options, text='Scenario Mode', variable=self.__var_mode,
            value='scenario', command=lambda: self.__mode_change())
        self.radio_scenario.grid(
            row=0, column=2, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        # Button
        self.button_solve = ttk.Button(
            self.frame_options, text='Solve',
            command=lambda: self.__solve())
        self.button_solve.grid(
            row=0, column=3, columnspan=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W + tk.EW)
        self.button_own_list = ttk.Button(
            self.frame_options, text='Upload',
            command=lambda: self.__upload_wordlist())
        self.button_own_list.grid(
            row=0, column=4, columnspan=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W + tk.EW)
        # Checkbutton
        self.check_display = ttk.Checkbutton(self.frame_options, text='Show Output', variable=self.__var_output,
	        command=lambda: self.__print_output(), onvalue='on', offvalue='off')
        self.check_display.grid(
            row=0, column=5, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W + tk.EW)
        
    # METHODS

    def __select_attack(self):
        self.__var_function = self.combo_attack.get()

    def __select_hash(self):
        self.__var_hash = self.combo_hash.get()

    # own wordlist upload
    def __upload_wordlist(self):
        self.__var_wordlist_path = filedialog.askopenfilename(initialdir = str(Path.cwd()), title = 'Select a File', filetypes = (('text files','*.txt'),('all files','*.*')))
        
    def __mode_change(self):
        match self.__var_mode.get():
            case 'attack':
                self.modulo_entry.config(state='disabled')
                self.combo_attack.config(state='readonly')
                self.combo_hash.config(state='disabled')
            case 'hash':
                self.modulo_entry.config(state='normal')
                self.combo_attack.config(state='disabled')
                self.combo_hash.config(state='readonly')
            case 'scenario':
                self.modulo_entry.config(state='disabled')
                self.combo_attack.config(state='disabled')
                self.combo_attack.set(value='Own Wordlist')
                self.combo_hash.config(state='disabled')

    # solve
    def __solve(self):
        time_now = datetime.now()
        stamp = time_now.strftime('%H:%M:%S')
        # BRUTE FORCE
        if self.__var_function.get() == 'Bruteforce':
            self.__var_solved, self.__var_time = self.breaker.brute_force_algorithm(self.__var_password.get(), self)
            # Failes
            if self.__var_solved == '0' and self.__var_time == 0:
                self.text_output.config(state='normal')
                self.text_output.insert(END, ('LOG: [' + stamp + '] : ' + 'Your password has more than five characters. It probably needs the following times: \n'
                                            + '7 chars < 17 minutes \n' + '8 chars < 20 hours \n' + '9 chars < 61 days' + '\n'))
                self.text_output.config(state='disabled')
                self.text_output.see(END)
                self.text_output.update()
            # Complete
            else:
                self.text_output.config(state='normal')
                self.text_output.insert(END, ('LOG: [' + stamp + '] : ' + 'Brute Force complete. Your password is: ' + self.__var_solved + '\n' f'It took {self.__var_time:0.4f} seconds.\n'))
                self.text_output.config(state='disabled')
                self.text_output.see(END)
                self.text_output.update()
        # Wordlist                
        elif self.__var_function.get() == 'Wordlist':
            self.__var_solved, self.__var_time = self.breaker.wordlist_algorithm(self.__var_password.get(), self)
            # Failed
            if self.__var_solved == '0':
                self.text_output.config(state='normal')
                self.text_output.insert(END, ('LOG: [' + stamp + '] : ' + f'Wordlist failed! After {self.__var_time:0.4f} seconds, \n' + 'your password is not on the Top 1.000.000 List.\n'))
                self.text_output.config(state='disabled')
                self.text_output.see(END)
                self.text_output.update()
            # Complete
            else:
                self.text_output.config(state='normal')
                self.text_output.insert(END, ('LOG: [' + stamp + '] : ' + f'Wordlist complete. Your password is: {self.__var_solved} \n' + 'It took {self.__var_time:0.4f} seconds.\n'))
                self.text_output.config(state='disabled')
                self.text_output.see(END)
                self.text_output.update()  
        elif self.__var_function.get() == 'hash_m':
            self.__var_solved, self.__var_time = self.breaker.hash_modulo_algorithm(self.__var_password.get(), self.__var_modulo.get(), self)
            # Complete
            self.text_output.config(state='normal')
            self.text_output.insert(END, ('LOG: [' + stamp + '] : ' + f'Hash completed. Your hash code for \'{self.__var_password.get()}\' is: {self.__var_solved} \n' + f'It took {self.__var_time:0.4f} seconds.\n'))
            self.text_output.config(state='disabled')
            self.text_output.see(END)
            self.text_output.update()  

    # password field clear
    def on_click(self, event):
        self.password_entry.delete(0, 'end')
        #self.password_entry.config(show='*')

    # get path from wordlist
    def get_wordlist(self):
        file = self.__var_wordlist_path.get()
        return file

    # Print on GUI Console
    def print_output(self, word):
        self.text_output.config(state='normal')
        self.text_output.insert(END, (word + '\n'))
        self.text_output.config(state='disabled')
        self.text_output.see(END)
        self.text_output.update()    