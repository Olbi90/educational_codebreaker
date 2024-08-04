import time
import string
import itertools

class Algorithm:

    def __init__(self, word):
        self.password = word

        

    # A function to perform a brute-force attempt on a user password
    def brute_force_algorithm(password):
        tic = time.perf_counter()
        # All allowed characters
        characters = string.ascii_lowercase + string.digits
        # Length of the password
        length = len(password)
        if length <= 5:
            # Test all possible combinations of the characters
            for attempt in itertools.product(characters, repeat=length):
                totest = ''.join(attempt)
                if totest == password:
                    toc = time.perf_counter()
                    return totest, toc-tic
            toc = time.perf_counter()
            return None, tic-toc
        else:
            return '0',0
        
    # A wordlist attack with the Top 1 Million passwords
    def wordlist_algorithm(password):
        try:
            tic = time.perf_counter()
            with open('./wordlists/10-million-password-list-top-1000000.txt', 'r') as file:
                for row in file:
                    # no spaces
                    row = row.strip()
                    
                    if password == row:
                        toc = time.perf_counter()
                        return row, toc-tic
            toc = time.perf_counter()
            return '0', toc-tic
        except FileNotFoundError:
            print('Datei nicht gefunden')
        except Exception as e:
            print(f'Ein Fehler ist aufgetreten: {e}')
