import random as rd



def main():
    nome = obter_nome()

    tema = obter_tema()
    
    estilo = obter_estilo()

    quantidade = obter_quantidade()

    sugestoes = gerar_sugestoes(
        nome,
        tema,
        estilo,
        quantidade
    )

    exibir_sugestoes(sugestoes)



def obter_nome():

    while True:

        nome = input("Digite um nome de usuario:").strip()

        if nome:
            return nome
        print("O nome nao pode estar vazio")


def obter_tema():

    while True:

        tema = input("Escolha um tema:").strip().lower()

        if tema:
            return tema
        print("O tema não pode estar vazio")


def obter_estilo():

    estilos_validos = [
        "hacker",
        "clean",
        "profissional",
        "criativo"
    ]

    while True:
        print("\nEstilos Disponiveis")
        print("- Hacker")
        print("- Clean")
        print("- Profissional")
        print("- Criativo")

        estilo = input("Escolha um estilo:").strip().lower()
        if estilo in estilos_validos:
            return estilo
        
        print("Estilo inválido.")

def obter_quantidade():

    while True:

        try:

            quantidade = int(
                input("Quantas sugestões deseja criar?:")
                )
            if quantidade > 0:
                return quantidade

            print("Digite um numero positivo")

        except ValueError:
            print("Digite apenas numeros inteiros.")


def gerar_sugestoes(
    nome,
    tema,
    estilo,
    quantidade
):
    
    match estilo:

        case "hacker":
            prefixos= [
                "Dark",
                "Sys",
                "root",
                "Cyber",
                "Shadow",
                "null"
            ]

            sufixos = [
                "fx",
                "core",
                "404",
                "byte",
                "exe",
                "link"
            ]

        case "clean":

            prefixos = [
                "neo",
                "mini",
                "simple",
                "pure",
                "just"
            ]

            sufixos = [
                "lab",
                "flow",
                "line",
                "studio",
                "space"
            ]

        case "profissional":
            
            prefixos = [
                "dev",
                "code",
                "tech",
                "mr",
                "pro"
            ]

            sufixos = [
                "solutions",
                "consulting",
                "group",
                "services"
            ]

        case "criativo":

            prefixos = [
                 "meta",
                "echo",
                "nova",
                "pixel",
                "volt"
            ]

            sufixos = [
                "wave",
                "spark",
                "lab",
                "zone",
                "vibe"
            ]

        case _:

            prefixos = ["neo"]
            sufixos = ["lab"]


    separadores = [
        "_",
        ".",
        "-",
        ""
    ]

    sugestoes = [

    ]

    while len(sugestoes) < quantidade:

        prefixo = rd.choice(prefixos)

        sufixo = rd.choice(sufixos)

        separador = rd.choice(separadores)

        modelo = rd.choice([
             nome + separador + sufixo,

            prefixo + separador + nome,

            nome + separador + tema,

            tema + separador + nome,

            prefixo + nome,

            nome + sufixo,

            tema + sufixo,

            prefixo + tema,
        ])

        if modelo not in sugestoes:

            sugestoes.append(modelo)

    return sugestoes


def exibir_sugestoes(sugestoes):

    print("\n Sugestões geradas")

    for i, nome in enumerate(sugestoes, start=1):

        print(f"{i}. {nome}")


if __name__ == "__main__":
    main()