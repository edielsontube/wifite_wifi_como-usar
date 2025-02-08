def filter_wordlist():
    filename = input("Digite o nome da wordlist (com extensão .txt): ")
    try:
        with open(filename, "r", encoding="latin-1") as file:
            lines = file.readlines()
        
        filtered_lines = [line for line in lines if len(line.strip()) >= 8]
        
        with open(filename, "w", encoding="latin-1") as file:
            file.writelines(filtered_lines)
        
        print("Wordlist filtrada com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    filter_wordlist()
