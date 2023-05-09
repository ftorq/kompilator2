import os
import re
from collections import Counter
from colorama import Fore, Style

# Funkcja do wczytywania pliku i wypisywania numerów linii
def print_file_with_line_numbers(file_name):
    if not os.path.isfile(file_name):
        print(Fore.RED + f"Plik {file_name} nie istnieje." + Style.RESET_ALL)
        return
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            print(f"{i}: {line}", end="")
            
# Funkcja do znajdowania 10 najczęściej występujących słów w Biblii
def find_top_10_words(file_name):
    if not os.path.isfile(file_name):
        print(Fore.RED + f"Plik {file_name} nie istnieje." + Style.RESET_ALL)
        return
    with open(file_name) as f:
        words = re.findall(r'\b\w+\b', f.read().lower())
        return Counter(words).most_common(10)

# Wyrażenie regularne odpowiadające potędze 2 w zapisie binarnym
binary_power_of_2_regex = r'^(0|(1(00)*))$'

# Wyrażenie regularne sprawdzające poprawność adresu IP
ip_address_regex = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'

# Skaner (lekser), który wstawia odstęp po kropce i przecinku, chyba że taki odstęp już tam jest
def lexer_add_spaces(text):
    return re.sub(r'(?<=[.,])(?=[^\s])', ' ', text)

# Definicje tokenów
tokens = [
    ("IF",     r"if"),
    ("ELSE",   r"else"),
    ("WHILE",  r"while"),
    ("INT",    r"\d+"),
    ("ZMIENNA",     r"[a-zA-Z_]\w*"),
    ("PLUS",   r"\+"),
    ("MINUS",  r"-"),
    ("POMNOŻYĆ",  r"\*"),
    ("PODZIELIĆ", r"/"),
    ("LEWY_NAWIAS", r"\("),
    ("PRAWY_NAWIAS", r"\)"),
    ("DWUKROPEK", r"\:"),
    ("WIEKSZE", r"\>"),
    ("MNIEJSZE", r"\<"),
    ("ROWNE", r"\="),
    ("NOWA_LINIA", r"\n"),
    ("WCIECIE", r"\s+")
]

# Funkcja skanująca wejście i zwracająca listę tokenów
def lex_jezyk(input_string):
    tokens_found = []
    position = 0
    while position < len(input_string):
        match = None
        for token in tokens:
            pattern = token[1]
            regex = re.compile(pattern)
            match = regex.match(input_string, position)
            if match:
                text = match.group(0)
                tokens_found.append((token[0], text))
                position = match.end(0)
                break
        if not match:
            raise ValueError(f"Nieznany znak: {input_string[position]}")
    return tokens_found

# Menu wyboru
while True:
    print("\nWybierz jedną z opcji:")
    print("1. Wyrażenie regularne odpowiadające potędze 2 w zapisie binarnym")
    print("2. Wyrażenie regularne sprawdzające poprawność adresu IP")
    print("3. Skaner (lekser), który wypisze plik wejściowy z numerami linii")
    print("4. Skaner (lekser), który wstawia odstęp po każdej kropce i przecinku, chyba że taki odstęp już tam jest")
    print("5. Skaner (lekser), który znajdzie dziesięć najczęściej występujących słów w Biblii")
    print("6. Skaner (lekser) dokonujący analizy leksykalnej zaprojektowanego przez siebie języka programowania")
    print("0. Wyjście z programu")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        # Wyrażenie regularne odpowiadające potędze 2 w zapisie binarnym
        print("Podaj ciąg binarny:")
        binary_string = input()
        if re.match(binary_power_of_2_regex, binary_string):
            print(f"{binary_string} jest potęgą 2 w zapisie binarnym.")
        else:
            print(f"{binary_string} nie jest potęgą 2 w zapisie binarnym.")
    elif choice == "2":
        # Wyrażenie regularne sprawdzające poprawność adresu IP
        print("Podaj adres IP:")
        ip_address = input()
        if re.match(ip_address_regex, ip_address):
                       print(f"{ip_address} jest poprawnym adresem IP.")
        else:
            print(f"{ip_address} nie jest poprawnym adresem IP.")
    elif choice == "3":
        # Skaner (lekser), który wypisze plik wejściowy z numerami linii
        print("Podaj nazwę pliku:")
        file_name = input()
        print_file_with_line_numbers(file_name)
    elif choice == "4":
        # Skaner (lekser), który wstawia odstęp po każdej kropce i przecinku, chyba że taki odstęp już tam jest
        print("Podaj tekst:")
        text = input()
        print(lexer_add_spaces(text))
    elif choice == "5":
        # Skaner (lekser), który znajdzie dziesięć najczęściej występujących słów w Biblii
        file_name = "biblia.txt"
        top_10_words = find_top_10_words(file_name)
        print(f"10 najczęściej występujących słów w Biblii:")
        for word, count in top_10_words:
            print(f"{word}: {count}")
    elif choice == "6":
        # Skaner (lekser), kaner (lekser) dokonujący analizy leksykalnej zaprojektowanego przez siebie języka programowania
        input_string = "if x > 0: y = 2 * (3 + z)"
        tokens = lex_jezyk(input_string)
        print(tokens)          
    elif choice == "0":
        # Wyjście z programu
        break
    else:
        print(Fore.RED + "Nieprawidłowa opcja." + Style.RESET_ALL)