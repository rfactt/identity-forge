import os
import random as rd


def gerar_sugestoes(nome_usuario, tema_usuario, estilo, quantidade):
    sugestoes = gerar_sugestoes(nome_usuario, tema_usuario, estilo, quantidade)

    return sugestoes
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 30)
    print("     IDENTIFY FORGE")
    print("=" * 30)

    while True:
        
        nome_usuario = input("Digite o nome do usuário: ").strip()

        if nome_usuario:
            break
        else:
            print("O nome do usuário não pode estar vazio. Por favor, tente novamente.")
    while True:        
        tema_usuario = input("Digite um tema para sua identidade: ").strip()
        if tema_usuario:
            break

        else:
            print("O tema para a identidade não pode estar vazio. Por favor, tente novamente.")

    while True:
        print("\nEstilos Disponíveis:")
        print("- Hacker")
        print("- Clean")
        print("- Profissional")
        print("- Criativo")
        estilo = input("Escolha um estilo para sua identidade: ").lower().strip()
        if estilo in ["hacker", "clean", "profissional", "criativo"]:
            break
        else:
            print("Estilo inválido. Por favor, escolha um dos estilos disponíveis.")

    nome_usuario =nome_usuario.lower().strip()

    tema_usuario = tema_usuario.lower().strip()

    estilo = estilo.lower().strip()

    while True:
        try:
            quantidade = int(input("Quantas sugestões de identidade você deseja? "))
            if quantidade <= 0:
                print("Por favor, insira um número positivo.")
                continue
            break
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


    if estilo == "hacker":
        prefixos = ["Dark", "Sys", "root", "Cyber", "Shadow", "null"]
        sufixos = ["fx", "core", "404", "byte", "exe", "link", "byte"]
        separadores = ["_", ".", "-", ""]

    elif estilo == "clean":
        prefixos = ["neo", "mini", "simple", "pure", "just"]
        sufixos = ["lab", "flow", "line", "studio", "space"]
        separadores = ["_", ".", "-", ""]


    elif estilo == "profissional":
        prefixos = ["dev", "code", "tech", "mr", "pro"]
        sufixos = ["solutions", "consulting", "group", "services", "digital", "works"]
        separadores = ["_", ".", "-", ""]


    elif estilo == "criativo":
        prefixos = ["meta", "encho", "nova", "pixel", "volt"]
        sufixos = ["wave", "spark", "lab", "zone", "vibe", "fusion", "motion"]
        separadores = ["_", ".", "-", ""]

    else:
        prefixo = ["neo", "dev", "byte"]
        sufixos = ["lab", "core", "flow"]
        separadores = ["_", ".", "-", ""]

    sugestao = []

    while len(sugestao) < quantidade:
        prefixo = rd.choice(prefixos)
        sufixo = rd.choice(sufixos)
        separador = rd.choice(separadores)

        modelo = rd.choice([
            nome_usuario + separador + sufixo,
            prefixo + separador + nome_usuario,
            nome_usuario + separador + tema_usuario,
            tema_usuario + separador + nome_usuario,
            prefixo + nome_usuario,
            nome_usuario + sufixo,
            tema_usuario + sufixo,
            prefixo + tema_usuario,
        ])
        if modelo not in sugestao:
            sugestao.append(modelo)

    print("\nGerando sugestões de identidade...")

    print(f"\nSugestões de identidade ({quantidade}):\n")
    for i, nome in enumerate(sugestao, start=1):
        print(f"{i}. {nome}")

    if estilo == "hacker":
        print("\n Identidade gerada com perfil mais obscuro e tecnológico.")

    elif estilo == "clean":
        print("\n Identidade gerada com perfil mais minimalista e moderno.")

    elif estilo == "profissional":
        print("\n Identidade gerada com perfil mais séria e confiavel.")

    elif estilo == "criativo":
        print("\n Identidade gerada com energia original e experimental.")

    print("\nIdentidade gerada com sucesso!")

    repetir = input("\nDeseja gerar mais sugestões? (s/n): ").lower().strip()

    
    if repetir != 's':
        print("\n Encerrando o Identify Forge. Até a próxima!...")
        break
