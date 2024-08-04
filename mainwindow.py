import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsgbox
from algorithm import Algorithm

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
        self.__var_time = tk.DoubleVar(self, value=0.0)
        self.__var_function = tk.StringVar(self, value='brute')
        
        # Widgets
        self.password_entry = tk.Entry(
            self, textvariable=self.__var_password, width=40)
        self.password_entry.grid(
            row=0, column=0, columnspan=2, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.password_entry.bind('<FocusIn>', self.on_click)
        
        # Radiobuttons
        self.radio_brute_force = ttk.Radiobutton(
            self, text='Brute Force',
            variable=self.__var_function, value='brute')
        self.radio_brute_force.grid(
            row=1, column=0, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)
        self.radio_brute_force.invoke()
        self.radio_wordlist = ttk.Radiobutton(
            self, text='Top 1 Million', variable=self.__var_function,
            value='word')
        self.radio_wordlist.grid(
            row=1, column=1, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W)

        # Button
        self.button_solve = ttk.Button(
            self, text='Solve',
            command=lambda: self.__solve())
        self.button_solve.grid(
            row=2, column=0, columnspan=2, padx=(5,5), pady=(5,5), ipadx=5, ipady=5,
            sticky=tk.W + tk.EW)
        
    # Methods
    def __solve(self):
        if self.__var_function.get() == 'brute':
            self.__var_solved, self.__var_time = self.breaker.brute_force_algorithm(self.__var_password.get())
            if self.__var_solved == '0' and self.__var_time == 0:
                tkmsgbox.showinfo(title='Solution Brute Force', message='Your password has more than five characters.\n' 
                    + 'It probably needs the following times:\n'
                    + '7 chars < 17 minutes \n 8 chars < 20 hours \n 9 chars < 61 days')
            else:
                tkmsgbox.showinfo(title='Solution Brute Force', message=f'Your password is: {self.__var_solved} \n It took {self.__var_time:0.4f} seconds.')
        elif self.__var_function.get() == 'word':
            self.__var_solved, self.__var_time = self.breaker.wordlist_algorithm(self.__var_password.get())
            if self.__var_solved == '0':
                tkmsgbox.showinfo(title='Solution Wordlist', message=f'After {self.__var_time:0.4f} seconds, \n your password is not on the Top 1.000.000 List.')
            else:
                tkmsgbox.showinfo(title='Solution Wordlist', message=f'Your password is: {self.__var_solved} \n It took {self.__var_time:0.4f} seconds.')

    def on_click(self, event):
        self.password_entry.delete(0, 'end')
        self.password_entry.config(show='*')