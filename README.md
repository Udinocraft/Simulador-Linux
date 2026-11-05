# 🐧 Linux Simulator

**A Linux-inspired Operating System Simulation Built with Python**

[![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Project](https://img.shields.io/badge/Project-Linux%20Simulator-2563eb?style=for-the-badge)](https://github.com/Udinocraft/Simulador-Linux)
[![Interface](https://img.shields.io/badge/Interface-CLI-111827?style=for-the-badge)](https://github.com/Udinocraft/Simulador-Linux)
[![Languages](https://img.shields.io/badge/Languages-PT--BR%20%7C%20EN--UK-16a34a?style=for-the-badge)](#-languages)

## 🇧🇷 Português

### 1. Sobre o Projeto

O **Linux Simulator** é uma simulação interativa de um ambiente operacional inspirado no Linux, desenvolvida em Python.

O projeto apresenta funcionalidades comuns de um sistema operacional através de uma interface de terminal (CLI), permitindo explorar diferentes recursos de maneira simples e interativa.

Seu desenvolvimento teve como principal objetivo consolidar conhecimentos de Python e Programação Orientada a Objetos (POO), aplicando lógica de programação, estruturas de dados, funções, tratamento de exceções e organização de código.

O projeto foi desenvolvido durante os primeiros meses de estudo em Python, representando uma etapa prática de aprendizado e evolução na programação.

### 2. Funcionalidades

O simulador reúne diferentes recursos em um único ambiente.

| Funcionalidade | Descrição |
|---|---|
| 🔐 Autenticação | Tela de login com senha e limite de tentativas |
| 💻 Terminal | Interface interativa com comandos básicos inspirados no Linux |
| 📁 Pastas | Simulação de gerenciamento de arquivos e diretórios |
| 🌐 Navegador | Ambiente com acesso à calculadora e plataforma de jogos |
| 🧮 Calculadora | Operações matemáticas básicas |
| 🎮 Plataforma de jogos | Jogos interativos executados pelo terminal |
| 📅 Calendário | Exibição de calendários por mês e ano |
| 🕐 Relógio | Exibição de horário em tempo real, utilizando o fuso de Brasília |
| 🔑 Gerador de senhas | Geração de senhas aleatórias com critérios de segurança |

### 3. Terminal e comandos

O terminal simulado permite executar comandos inspirados em ambientes Linux.

| Comando | Descrição |
|---|---|
| `help` | Exibe os comandos disponíveis |
| `ls` | Exibe uma listagem simulada de arquivos e diretórios |
| `date` | Exibe data e horário |
| `whoami` | Exibe o nome do usuário |
| `clear` | Limpa visualmente o terminal |
| `calc` | Abre a calculadora |
| `fetch` | Exibe informações fictícias do sistema |
| `exit` | Encerra o terminal |

Os comandos são implementações educacionais. O terminal não é um shell Linux real e não executa comandos nativos do sistema operacional hospedeiro.

### 4. Plataforma de jogos

O simulador também possui uma área de entretenimento com diferentes jogos:

- Jogo de adivinhação.
- Cara ou coroa.
- Perguntas e respostas.
- Jogo da forca.
- Roleta russa simulada.

Os jogos foram implementados utilizando lógica condicional, estruturas de repetição, listas, dicionários e geração de números aleatórios.

A roleta russa é exclusivamente uma simulação textual dentro do programa, sem qualquer interação com armas ou objetos reais.

### 5. Gerador de senhas

O projeto inclui uma funcionalidade de geração de senhas utilizando o módulo `secrets` do Python.

O gerador utiliza:

- Letras maiúsculas.
- Letras minúsculas.
- Números.
- Caracteres especiais.
- Comprimento mínimo de 12 caracteres para a validação implementada.

A função verifica os critérios definidos e gera outra senha caso a primeira não os satisfaça.

Essa funcionalidade foi incluída como uma aplicação prática de geração aleatória e conceitos básicos de segurança.

### 6. Tecnologias e conceitos utilizados

| Tecnologia / Conceito | Aplicação |
|---|---|
| Python 3 | Linguagem principal |
| Programação Orientada a Objetos | Organização por classes e métodos |
| Funções | Divisão das funcionalidades em componentes |
| Estruturas condicionais | Controle de menus e decisões |
| Estruturas de repetição | Execução contínua de menus e jogos |
| Listas e dicionários | Organização de informações |
| Tratamento de exceções | Gerenciamento de entradas inválidas e interrupções |
| `datetime` e `zoneinfo` | Manipulação de data e horário |
| `calendar` | Exibição de calendários |
| `secrets` | Geração de senhas |
| `random` | Mecânicas dos jogos |
| CLI | Interface de interação com o usuário |

### 7. Organização do código

O projeto utiliza Programação Orientada a Objetos para separar responsabilidades e organizar funcionalidades.

Entre as principais classes estão:

- `SistemaOperacional`: controla o ambiente principal, autenticação, terminal e demais recursos.
- `Calculadora`: executa operações matemáticas.
- `PlataformaJogos`: gerencia os jogos disponíveis.
- `GeradorSenha`: implementa a geração e validação de senhas.

A organização permite compreender como diferentes componentes podem trabalhar juntos dentro de uma aplicação Python.

### 8. Como executar

**Requisitos:**
- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento compatível.

Clone o repositório:

```bash
git clone https://github.com/Udinocraft/Simulador-Linux.git
```

Entre na pasta do projeto:

```bash
cd Simulador-Linux/Projetos_python
```

Execute:

```bash
python Linux.py
```

Dependendo da distribuição, pode ser necessário utilizar `python3 Linux.py`.

O projeto utiliza bibliotecas da distribuição padrão do Python.

### 9. Relatórios e documentação

O repositório também contém relatórios de desenvolvimento e tecnologias em português e inglês.

**Português:**
- [Relatório de desenvolvimento](RELATORIOS-PT/DESENVOLVIMENTO.pdf)
- [Relatório de tecnologias](RELATORIOS-PT/TECNOLOGIAS.pdf)

**English:**
- [Development report](RELATORIOS-ING/DEVELOPMENT.pdf)
- [Technologies report](RELATORIOS-ING/TECHNOLOGIES.pdf)

Os relatórios apresentam informações sobre o desenvolvimento, as tecnologias utilizadas, as dificuldades encontradas e os conhecimentos aplicados.

### 10. Aprendizados

O desenvolvimento do Linux Simulator proporcionou experiência prática em:

- Programação Python.
- Programação Orientada a Objetos.
- Lógica de programação.
- Estruturas de dados.
- Organização de código.
- Tratamento de erros.
- Desenvolvimento de aplicações interativas.
- Resolução de problemas.
- Documentação técnica.

### 11. Melhorias futuras

Algumas possibilidades de evolução incluem:

- Expansão dos comandos do terminal.
- Novos aplicativos e funcionalidades.
- Melhorias no tratamento de exceções.
- Organização do código em módulos.
- Implementação de testes automatizados.
- Interface mais avançada.
- Aprimoramento da simulação do ambiente operacional.

### 12. Objetivo educacional

O Linux Simulator foi desenvolvido para fins educacionais, com foco no aprendizado de Python e na compreensão de conceitos relacionados ao ecossistema Linux.

Ele não é um sistema operacional real, nem substitui uma distribuição Linux.

---

## 🇬🇧 English (UK)

### 1. About the Project

**Linux Simulator** is an interactive simulation of a Linux-inspired operating environment, developed in Python.

The project provides common operating-system-style features through a Command-Line Interface (CLI), allowing users to explore different functionalities in a simple and interactive way.

Its main objective was to consolidate Python programming and Object-Oriented Programming (OOP) knowledge through practical implementation.

The project applies programming logic, data structures, functions, exception handling and code organisation.

### 2. Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Login screen with password validation and limited attempts |
| 💻 Terminal | Interactive terminal with basic Linux-inspired commands |
| 📁 Folders | Simulated file and directory management |
| 🌐 Browser | Environment providing access to the calculator and games platform |
| 🧮 Calculator | Basic mathematical operations |
| 🎮 Games platform | Interactive terminal-based games |
| 📅 Calendar | Calendar display by month and year |
| 🕐 Clock | Real-time clock using Brasília time |
| 🔑 Password generator | Random password generation with security criteria |

### 3. Terminal Commands

| Command | Description |
|---|---|
| `help` | Displays available commands |
| `ls` | Displays a simulated list of files and directories |
| `date` | Displays the current date and time |
| `whoami` | Displays the username |
| `clear` | Visually clears the terminal |
| `calc` | Opens the calculator |
| `fetch` | Displays fictional system information |
| `exit` | Exits the terminal |

These commands are educational implementations. The simulated terminal is not a real Linux shell and does not execute native commands on the host operating system.

### 4. Games Platform

The simulator includes several interactive games:

- Number guessing game.
- Heads or tails.
- Questions and answers.
- Hangman.
- Simulated Russian roulette.

The games use conditional logic, loops, lists, dictionaries and random number generation.

The Russian roulette feature is exclusively a text-based simulation within the programme.

### 5. Password Generator

The project includes a password generator using Python's `secrets` module.

It uses uppercase letters, lowercase letters, digits and special characters, with a minimum length of 12 characters for the implemented validation.

The generator checks the defined criteria and generates another password when necessary.

### 6. Technologies and Concepts

| Technology / Concept | Application |
|---|---|
| Python 3 | Main programming language |
| Object-Oriented Programming | Classes and methods |
| Functions | Feature organisation |
| Conditional statements | Menus and decision-making |
| Loops | Repeated operations |
| Lists and dictionaries | Data organisation |
| Exception handling | Invalid inputs and interruptions |
| `datetime` and `zoneinfo` | Date and time handling |
| `calendar` | Calendar generation |
| `secrets` | Password generation |
| `random` | Game mechanics |
| CLI | User interaction |

### 7. Code Organisation

The project uses Object-Oriented Programming to separate responsibilities.

Main classes include:

- `SistemaOperacional`: manages the main environment, authentication, terminal and other features.
- `Calculadora`: performs mathematical operations.
- `PlataformaJogos`: manages the available games.
- `GeradorSenha`: implements password generation and validation.

### 8. How to Run

**Requirements:**
- Python 3.
- A compatible terminal or development environment.

Clone the repository:

```bash
git clone https://github.com/Udinocraft/Simulador-Linux.git
```

Enter the project directory:

```bash
cd Simulador-Linux/Projetos_python
```

Run the programme:

```bash
python Linux.py
```

Depending on the distribution, `python3 Linux.py` may be required.

No external Python packages are required.

### 9. Reports and Documentation

The repository includes development and technology reports in Brazilian Portuguese and English.

- [Development report](RELATORIOS-ING/DEVELOPMENT.pdf)
- [Technologies report](RELATORIOS-ING/TECHNOLOGIES.pdf)

### 10. Key Takeaways

This project provided practical experience in:

- Python programming.
- Object-Oriented Programming.
- Programming logic.
- Data structures.
- Code organisation.
- Exception handling.
- Interactive application development.
- Problem-solving.
- Technical documentation.

### 11. Future Improvements

Potential improvements include:

- Expanding terminal commands.
- Adding new applications.
- Improving exception handling.
- Modularising the codebase.
- Implementing automated tests.
- Developing a more advanced interface.
- Improving the operating environment simulation.

### 12. Educational Purpose

Linux Simulator was developed for educational purposes, focusing on Python programming and concepts related to the Linux ecosystem.

It is not a real operating system and does not replace a Linux distribution.

---

**Project:** Linux Simulator  
**Repository:** [github.com/Udinocraft/Simulador-Linux](https://github.com/Udinocraft/Simulador-Linux)  
**Author:** CyberMota  
**Language:** Python 3  
**Purpose:** Educational Python and Linux environment simulation
