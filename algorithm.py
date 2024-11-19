import time
import string
import itertools

class Algorithm:

    def __init__(self, word):
        self.password = word

    # A function to perform a brute-force attempt on a user password
    def brute_force_algorithm(password, mainwindow):
        tic = time.perf_counter()
        # All allowed characters
        characters = string.ascii_lowercase + string.digits
        # Length of the password
        length = len(password)
        if length <= 5:
            # Test all possible combinations of the characters
            for attempt in itertools.product(characters, repeat=length):
                totest = ''.join(attempt)
                mainwindow.print_output(totest)
                if totest == password:
                    toc = time.perf_counter()
                    return totest, toc-tic
            toc = time.perf_counter()
            return None, tic-toc
        else:
            return '0',0
        
    # A wordlist attack with the Top 1 Million passwords
    def wordlist_algorithm(password, mainwindow):
        try:
            tic = time.perf_counter()
            file = mainwindow.get_wordlist()
            with open(file, 'r') as file:
                for row in file:
                    # no spaces
                    row = row.strip()
                    mainwindow.print_output(row)
                    if password == row:
                        toc = time.perf_counter()
                        return row, toc-tic
            toc = time.perf_counter()
            return '0', toc-tic
        except FileNotFoundError:
            print('Datei nicht gefunden')
        except Exception as e:
            print(f'Ein Fehler ist aufgetreten: {e}')

    # Hashfunktionen
    def hash_modulo_algorithm(password, modulo, mainwindow):
        #chars = list(password)
        tic = time.perf_counter()
        hash = 0
        mainwindow.print_output('Starte modulo hash:')
        ascii_values = [ord(char) for char in password]
        for x in ascii_values:
            temp = chr(x)
            x = x%modulo
            mainwindow.print_output(temp + ' becomes ' + str(x))
        for x in ascii_values:
            hash = hash + x
        toc = time.perf_counter()
        return hash, toc-tic        
    
    def hash_modulo_div_algorithm(password, modulo, mainwindow):
        tic = time.perf_counter()
        hash = 0
        length = len(password)
        mainwindow.print_output('Starte modulo hash:')
        ascii_values = [ord(char) for char in password]
        for x in ascii_values:
            temp = chr(x)
            x = x%modulo
            mainwindow.print_output(temp + ' becomes ' + str(x))
        for x in ascii_values:
            hash = hash + x
        mainwindow.print_output('Divide through length of '+ password)
        hash = int(hash / length)
        toc = time.perf_counter()
        return hash, toc-tic 
    
    def hash_modulo_mult_algorithm(password, modulo, mainwindow):
        #chars = list(password)
        tic = time.perf_counter()
        hash = 0
        length = len(password)
        mainwindow.print_output('Starte modulo hash:')
        ascii_values = [ord(char) for char in password]
        for x in ascii_values:
            temp = chr(x)
            x = x%modulo
            mainwindow.print_output(temp + ' becomes ' + str(x))
        for x in ascii_values:
            hash = hash + x
        mainwindow.print_output('Multiply with length of '+ password)
        hash = hash * length
        toc = time.perf_counter()
        return hash, toc-tic 