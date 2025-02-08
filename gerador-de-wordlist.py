from itertools import product
from collections import Counter
import time

def is_valid_string(string, max_repeats):
    count = Counter(string)
    return all(v <= max_repeats for v in count.values())

def generate_wordlist():
    banner = """
    \033[1;32m###########################################
    #         GERADOR DE WORDLIST         #
    ###########################################\033[0m
    """
    print(banner)
    
    filename = input("\033[1;34mDigite o nome do arquivo para salvar a wordlist (com extensão .txt): \033[0m")
    min_length = int(input("\033[1;34mDigite o número mínimo de caracteres: \033[0m"))
    max_length = int(input("\033[1;34mDigite o número máximo de caracteres: \033[0m"))
    
    char_types = {
        "1": "abcdefghijklmnopqrstuvwxyz",  # Letras minúsculas
        "2": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # Letras maiúsculas
        "3": "0123456789",  # Números
        "4": "!@#$%^&*()-_=+[]{}|;:'",  # Caracteres especiais
        "5": " "  # Espaço
    }
    
    print("\033[1;36mEscolha os tipos de caracteres que deseja incluir:\033[0m")
    print("\033[1;33m1 - Letras minúsculas")
    print("2 - Letras maiúsculas")
    print("3 - Números")
    print("4 - Caracteres especiais")
    print("5 - Espaço\033[0m")
    choices = input("\033[1;34mDigite os números correspondentes separados por vírgula (ex: 1,3,4): \033[0m").split(",")
    
    charset = "".join(char_types[c.strip()] for c in choices if c.strip() in char_types)
    
    max_repeats = int(input("\033[1;34mQuantas vezes um mesmo caractere pode se repetir no máximo por linha? \033[0m"))
    
    prefix = input("\033[1;34mDeseja adicionar uma palavra no início de cada linha? (Deixe vazio para não) \033[0m")
    suffix = input("\033[1;34mDeseja adicionar uma palavra no final de cada linha? (Deixe vazio para não) \033[0m")
    
    total_combinations = sum(len(charset) ** length for length in range(min_length, max_length + 1))
    processed = 0
    
    with open(filename, "w", encoding="latin-1") as file:
        for length in range(min_length, max_length + 1):
            for combo in product(charset, repeat=length):
                generated_string = "".join(combo)
                if is_valid_string(generated_string, max_repeats):
                    file.write(f"{prefix}{generated_string}{suffix}\n")
                    processed += 1
                    percentage = (processed / total_combinations) * 100
                    print(f"\033[1;32mProgresso: {percentage:.2f}% concluído\033[0m", end="\r")
    
    print("\n\033[1;32mWordlist gerada com sucesso!\033[0m")

if __name__ == "__main__":
    generate_wordlist()
