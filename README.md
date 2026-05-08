# Identify Forge

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

Gerador de usernames e identidades digitais desenvolvido em Python com foco em modularização, organização de código e geração procedural.

---

## Preview

```bash
=================================
        IDENTIFY FORGE
=================================

Digite um nome de usuario: rafael
Escolha um tema: python
Escolha um estilo: hacker
Quantas sugestões deseja criar?: 5
```

### Resultado

```bash
1. Dark_rafael
2. python404
3. Cyber-rafael
4. Shadow.python
5. rootpython
```

---

## Funcionalidades

- Geração procedural de usernames
- Diferentes estilos de identidade
- Sistema modularizado
- Validação de entrada do usuário
- Evita sugestões repetidas
- Uso de `match case`
- Estrutura organizada e escalável

---

## Estilos Disponíveis

| Estilo | Descrição |
|---|---|
| Hacker | Identidades obscuras e tecnológicas |
| Clean | Estilo minimalista e moderno |
| Profissional | Identidades mais sérias e corporativas |
| Criativo | Combinações originais e experimentais |

---

## Conceitos Aplicados

O projeto foi desenvolvido como prática de:

- Modularização
- Separação de responsabilidades
- Arquitetura básica de aplicações
- Estruturas de repetição
- Tratamento de exceções
- Validação de dados
- `match case`
- Organização de fluxo principal
- Refatoração de código

---

## Estrutura do Projeto

```python
main()
│
├── obter_nome()
├── obter_tema()
├── obter_estilo()
├── obter_quantidade()
├── gerar_sugestoes()
└── exibir_sugestoes()
```

---

## Tecnologias Utilizadas

- Python 3.10+
- Biblioteca `random`
- Git
- GitHub
- VSCode

---

## Instalação

### Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/identity-forge.git
```

### Entre na pasta do projeto

```bash
cd identity-forge
```

### Execute o programa

```bash
python main.py
```

---

## Exemplo de Geração

```bash
Dark_rafael
Cyber.python
root-dev
meta.wave
neo_studio
```

Cada execução gera combinações diferentes utilizando listas, separadores e modelos aleatórios.

---

## Evolução do Projeto

O projeto começou como um script procedural simples e foi refatorado para uma arquitetura mais limpa e modular.

Principais melhorias implementadas:

- Separação em funções
- Fluxo principal desacoplado
- Organização de responsabilidades
- Uso de `match case`
- Melhor legibilidade
- Estrutura mais escalável

---

## Melhorias Futuras

- Interface gráfica
- Versão web
- Sistema de exportação
- Mais estilos de identidade
- Histórico de usernames
- Sistema de favoritos

---

## Autor

Desenvolvido por Rafael Gama.

---

## Contribuição

Sinta-se livre para abrir issues, sugerir melhorias ou fazer forks do projeto.
