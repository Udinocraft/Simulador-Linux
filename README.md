# 🐧 Linux Simulator

**A Linux-Inspired Operating Environment Simulated with Python**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Project](https://img.shields.io/badge/Project-Linux%20Simulator-2563eb?style=for-the-badge)](https://github.com/Udinocraft/Simulador-Linux)
[![Interface](https://img.shields.io/badge/Interface-CLI-111827?style=for-the-badge)](https://github.com/Udinocraft/Simulador-Linux)
[![Languages](https://img.shields.io/badge/Languages-PT--BR%20%7C%20EN--UK-16a34a?style=for-the-badge)](#-languages)

---

# 🇧🇷 Português

## 1. Sobre o Projeto

O **Linux Simulator** é um projeto desenvolvido em Python que reproduz, de maneira interativa e educacional, elementos de um ambiente operacional inspirado no Linux.

A aplicação oferece uma interface de linha de comando (CLI), na qual o usuário pode interagir com um sistema virtual, executar comandos, navegar por diretórios, manipular arquivos e utilizar diferentes ferramentas e funcionalidades.

O simulador também reúne recursos complementares, como calculadora, calendário, relógio, gerador de senhas e uma plataforma de jogos.

O desenvolvimento teve como objetivo aplicar e aprofundar conhecimentos de Python, Programação Orientada a Objetos (POO), estruturas de dados, lógica de programação, tratamento de exceções e organização de código.

Além disso, o projeto representa uma evolução prática dos estudos em programação, reunindo diferentes conceitos em uma aplicação interativa.

## 2. Funcionalidades

O ambiente simulado reúne ferramentas organizadas em diferentes áreas.

| Funcionalidade | Descrição |
|---|---|
| 🔐 Autenticação | Sistema de login com validação de senha e limite de tentativas. |
| 💻 Terminal interativo | Interface CLI com comandos inspirados no Linux. |
| 📁 Sistema de arquivos | Criação, navegação, leitura e remoção de arquivos e diretórios virtuais. |
| 🎨 Personalização | Alteração das cores do terminal. |
| 📜 Histórico | Registro dos comandos executados durante a sessão. |
| 🌐 Ferramentas de rede | Simulações de informações de interfaces, conectividade e varredura de portas. |
| 🖥️ Informações do sistema | Exibição de informações fictícias de sistema, kernel e ambiente. |
| 🔑 Gerador de senhas | Geração e validação de senhas utilizando o módulo `secrets`. |
| 🧮 Calculadora | Operações matemáticas básicas. |
| 🎮 Plataforma de jogos | Jogos interativos acessíveis pelo ambiente. |
| 📅 Calendário | Exibição de calendários por mês e ano. |
| 🕐 Relógio | Exibição contínua do horário de Brasília. |
| 📂 Gerenciador de pastas | Navegação por áreas virtuais de arquivos e downloads. |
| 🟢 Efeito Matrix | Animação textual executada no terminal. |

## 3. Terminal e comandos

O terminal é uma das principais partes do projeto. Ele oferece uma experiência inspirada em distribuições Linux, com prompt personalizado, navegação por diretórios, histórico de comandos e ferramentas simuladas.

### Navegação e gerenciamento de arquivos

| Comando | Descrição |
|---|---|
| `help` | Exibe a lista de comandos disponíveis. |
| `pwd` | Exibe o caminho atual. |
| `ls` | Lista arquivos e diretórios. |
| `ls -la` | Exibe arquivos ocultos e informações detalhadas. |
| `cd <pasta>` | Acessa um diretório. |
| `cd ..` | Retorna ao diretório anterior. |
| `cd ~` | Retorna ao diretório inicial. |
| `mkdir <nome>` | Cria um diretório. |
| `touch <arquivo>` | Cria um arquivo vazio. |
| `cat <arquivo>` | Exibe o conteúdo de um arquivo. |
| `echo <texto> > <arquivo>` | Escreve conteúdo em um arquivo. |
| `rm <nome>` | Remove um arquivo ou diretório. |

### Sistema e personalização

| Comando | Descrição |
|---|---|
| `whoami` | Exibe o usuário atual. |
| `uname` | Exibe o nome do sistema simulado. |
| `uname -a` | Exibe informações fictícias do sistema e kernel. |
| `uptime` | Exibe informações simuladas de tempo de atividade. |
| `neofetch` | Exibe informações e uma representação visual do sistema. |
| `fastfetch` | Executa a mesma apresentação simulada de informações do sistema. |
| `fetch` | Exibe informações do ambiente simulado. |
| `passwd` | Permite alterar a senha da sessão. |
| `sudo` | Apresenta uma resposta simulada de autorização. |
| `theme <cor>` | Altera a cor do terminal. |
| `history` | Exibe o histórico de comandos. |
| `clear` | Limpa visualmente o terminal. |
| `date` | Exibe a data e o horário. |
| `exit` | Encerra o terminal. |

**Cores disponíveis:** `ciano`, `verde`, `magenta`, `azul` e `amarelo`.

### Rede e ferramentas

| Comando | Descrição |
|---|---|
| `ifconfig` | Exibe interfaces e configurações de rede fictícias. |
| `ip` | Exibe as mesmas informações de rede simuladas. |
| `ping <host>` | Apresenta respostas de conectividade simuladas. |
| `nmap <alvo>` | Apresenta uma simulação de varredura de portas. |
| `matrix` | Inicia uma animação de caracteres no terminal. |
| `calc` | Abre a calculadora. |
| `jogos` | Abre a plataforma de jogos. |

**Importante:** os comandos de rede não realizam comunicação com hosts reais. As respostas de `ping`, `nmap`, `ifconfig` e `ip` são dados fictícios utilizados para representar visualmente o funcionamento dessas ferramentas.

O terminal também não executa comandos nativos do Linux ou comandos do sistema operacional hospedeiro.

## 4. Sistema de arquivos virtual

O simulador possui um sistema de arquivos próprio, implementado com estruturas de dados do Python.

O ambiente permite:

- Criar diretórios.
- Criar arquivos.
- Navegar entre pastas.
- Listar arquivos e diretórios.
- Consultar conteúdos de arquivos.
- Escrever informações em arquivos.
- Remover arquivos e diretórios.
- Visualizar arquivos ocultos.
- Consultar informações básicas de permissões simuladas.

Os arquivos e diretórios são armazenados em estruturas de dados na memória durante a execução do programa.

Portanto, as alterações não representam modificações no sistema de arquivos real do computador.

## 5. Ferramentas e aplicações complementares

Além do terminal, o Linux Simulator disponibiliza outras funcionalidades acessíveis pelos menus do ambiente.

### 🔑 Gerador de senhas

O projeto utiliza o módulo `secrets` para gerar senhas aleatórias e verificar critérios definidos de segurança.

A validação considera:

- Letras maiúsculas.
- Letras minúsculas.
- Números.
- Caracteres especiais.
- Comprimento mínimo de 12 caracteres.

O gerador repete o processo até obter uma senha que atenda aos critérios implementados.

### 🧮 Calculadora

Implementa operações matemáticas básicas:

- Adição.
- Subtração.
- Multiplicação.
- Divisão.

Também possui validação de entradas e tratamento de divisão por zero.

### 🎮 Plataforma de jogos

O ambiente inclui cinco jogos:

1. Jogo de adivinhação.
2. Cara ou coroa.
3. Perguntas e respostas.
4. Jogo da forca.
5. Roleta russa simulada.

Os jogos utilizam estruturas condicionais, repetição, listas, dicionários e geração de números aleatórios.

A roleta russa é exclusivamente uma simulação textual, sem qualquer interação com armas ou objetos reais.

### 📅 Calendário e relógio

O calendário permite selecionar um mês e um ano para visualizar sua organização.

O relógio apresenta continuamente a data e o horário utilizando o fuso `America/Sao_Paulo`.

## 6. Tecnologias e conceitos utilizados

| Tecnologia / Conceito | Aplicação no projeto |
|---|---|
| Python 3 | Linguagem principal. |
| Programação Orientada a Objetos | Organização das funcionalidades em classes. |
| Funções e métodos | Separação das operações e responsabilidades. |
| Estruturas condicionais | Controle de menus, validações e decisões. |
| Estruturas de repetição | Execução contínua do terminal e das aplicações. |
| Listas e dicionários | Armazenamento e organização de dados. |
| Tratamento de exceções | Gerenciamento de entradas inválidas e interrupções. |
| `secrets` | Geração de senhas. |
| `string` | Conjuntos de caracteres utilizados na geração de senhas. |
| `random` | Mecânicas e resultados dos jogos. |
| `calendar` | Geração de calendários. |
| `datetime` | Manipulação de data e horário. |
| `zoneinfo` | Definição do fuso horário de Brasília. |
| `time` | Controle de intervalos e efeitos visuais. |
| `sys` | Importação disponível no código. |
| CLI | Interface de interação com o usuário. |

## 7. Organização do código

O projeto utiliza Programação Orientada a Objetos para estruturar as principais funcionalidades.

Entre as classes presentes estão:

| Classe | Responsabilidade |
|---|---|
| `Cores` | Define os códigos de cores utilizados na interface. |
| `GeradorSenha` | Gera e valida senhas. |
| `Calculadora` | Executa operações matemáticas. |
| `PlataformaJogos` | Gerencia os jogos disponíveis. |
| `SistemaOperacional` | Controla o ambiente principal, autenticação, terminal, arquivos e aplicações. |

Essa organização permite reunir diferentes funcionalidades em um único ambiente e aplicar conceitos de orientação a objetos em uma aplicação prática.

## 8. Como executar

### Requisitos

- Python 3.9 ou superior.
- Terminal compatível com a execução de aplicações Python.

O projeto utiliza módulos da biblioteca padrão do Python, não exigindo a instalação de dependências externas.

### Clonar o repositório

```bash
git clone https://github.com/Udinocraft/Simulador-Linux.git
```

### Acessar a pasta do projeto

```bash
cd Simulador-Linux/Projetos_python
```

### Executar

```bash
python Linux.py
```

Em algumas distribuições, pode ser necessário utilizar:

```bash
python3 Linux.py
```

Após iniciar, o programa gera uma senha para a sessão e apresenta a tela de autenticação.

## 9. Relatórios e documentação

O repositório possui relatórios técnicos em português e inglês, documentando o desenvolvimento e as tecnologias utilizadas.

### Português

- [Relatório de desenvolvimento](RELATORIOS-PT/DESENVOLVIMENTO.pdf)
- [Relatório de tecnologias](RELATORIOS-PT/TECNOLOGIAS.pdf)

### English

- [Development report](RELATORIOS-ING/DEVELOPMENT.pdf)
- [Technologies report](RELATORIOS-ING/TECHNOLOGIES.pdf)

Os documentos apresentam o processo de desenvolvimento, os recursos implementados, as tecnologias utilizadas, as dificuldades encontradas e os conhecimentos aplicados.

## 10. Aprendizados e conhecimentos aplicados

O desenvolvimento e a atualização do Linux Simulator proporcionaram experiência prática em diferentes áreas da programação:

- Desenvolvimento de aplicações em Python.
- Programação Orientada a Objetos.
- Organização de classes e métodos.
- Construção de interfaces CLI.
- Manipulação de estruturas de dados.
- Implementação de sistemas virtuais.
- Criação de comandos personalizados.
- Validação de entradas.
- Tratamento de exceções.
- Geração de dados aleatórios.
- Utilização de módulos da biblioteca padrão.
- Simulação de ferramentas e conceitos do ambiente Linux.
- Revisão e aprimoramento de código existente.
- Documentação técnica.

## 11. Limitações da simulação

O Linux Simulator é um ambiente educacional desenvolvido em Python. Apesar de utilizar comandos e elementos inspirados no Linux, existem limitações importantes:

- Não é um sistema operacional real.
- Não executa um shell Linux nativo.
- Não realiza comandos diretamente no sistema hospedeiro.
- O sistema de arquivos é virtual e mantido em memória.
- As informações de hardware, kernel e sistema são fictícias.
- As ferramentas de rede apresentam resultados simulados.
- As funcionalidades não substituem ferramentas reais de administração de sistemas ou análise de redes.

Essas limitações fazem parte da proposta do projeto: reproduzir conceitos de maneira controlada, interativa e didática.

## 12. Objetivo educacional

O Linux Simulator foi desenvolvido com foco no aprendizado de Python, na aplicação de Programação Orientada a Objetos e na compreensão de conceitos relacionados ao ecossistema Linux.

O projeto reúne programação, lógica, estruturas de dados e conceitos básicos de sistemas operacionais em uma única aplicação.

Mais do que reproduzir comandos, sua proposta é demonstrar como diferentes funcionalidades podem ser construídas e integradas utilizando Python.

---

# 🇬🇧 English (UK)

## 1. About the Project

**Linux Simulator** is a Python project that provides an interactive and educational representation of a Linux-inspired operating environment.

The application features a Command-Line Interface (CLI), allowing users to interact with a virtual system, execute commands, navigate directories, manage files and access different tools and features.

The simulator also includes additional applications such as a calculator, calendar, clock, password generator and games platform.

The project was developed to apply and improve knowledge of Python, Object-Oriented Programming (OOP), data structures, programming logic, exception handling and code organisation.

It also represents a practical stage in the development of programming skills, bringing different concepts together in a single interactive application.

## 2. Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Login system with password validation and limited attempts. |
| 💻 Interactive terminal | CLI featuring Linux-inspired commands. |
| 📁 File system | Creation, navigation, reading and removal of virtual files and directories. |
| 🎨 Customisation | Terminal colour customisation. |
| 📜 Command history | Records commands executed during the session. |
| 🌐 Network tools | Simulated network interfaces, connectivity and port scanning information. |
| 🖥️ System information | Displays fictional system, kernel and environment information. |
| 🔑 Password generator | Password generation and validation using Python's `secrets` module. |
| 🧮 Calculator | Basic mathematical operations. |
| 🎮 Games platform | Interactive games accessible through the environment. |
| 📅 Calendar | Displays calendars by month and year. |
| 🕐 Clock | Continuously displays Brasília time. |
| 📂 Folder manager | Navigation through virtual downloads and file directories. |
| 🟢 Matrix effect | Text-based terminal animation. |

## 3. Terminal and Commands

The terminal is one of the project's main components. It provides an experience inspired by Linux distributions, featuring a customised prompt, directory navigation, command history and simulated tools.

### Navigation and File Management

| Command | Description |
|---|---|
| `help` | Displays the available commands. |
| `pwd` | Displays the current path. |
| `ls` | Lists files and directories. |
| `ls -la` | Displays hidden files and detailed information. |
| `cd <directory>` | Enters a directory. |
| `cd ..` | Returns to the previous directory. |
| `cd ~` | Returns to the home directory. |
| `mkdir <name>` | Creates a directory. |
| `touch <file>` | Creates an empty file. |
| `cat <file>` | Displays a file's contents. |
| `echo <text> > <file>` | Writes content to a file. |
| `rm <name>` | Removes a file or directory. |

### System and Customisation

| Command | Description |
|---|---|
| `whoami` | Displays the current username. |
| `uname` | Displays the simulated system name. |
| `uname -a` | Displays fictional system and kernel information. |
| `uptime` | Displays simulated system uptime information. |
| `neofetch` | Displays system information with a visual representation. |
| `fastfetch` | Runs the same simulated system information display. |
| `fetch` | Displays information about the simulated environment. |
| `passwd` | Allows the session password to be changed. |
| `sudo` | Displays a simulated authorisation response. |
| `theme <colour>` | Changes the terminal colour. |
| `history` | Displays the command history. |
| `clear` | Visually clears the terminal. |
| `date` | Displays the current date and time. |
| `exit` | Exits the terminal. |

**Available colours:** `ciano`, `verde`, `magenta`, `azul` and `amarelo`.

### Network and Tools

| Command | Description |
|---|---|
| `ifconfig` | Displays fictional network interfaces and configuration. |
| `ip` | Displays the same simulated network information. |
| `ping <host>` | Displays simulated connectivity responses. |
| `nmap <target>` | Displays a simulated port scan. |
| `matrix` | Starts a terminal character animation. |
| `calc` | Opens the calculator. |
| `jogos` | Opens the games platform. |

**Important:** network commands do not communicate with real hosts. The responses from `ping`, `nmap`, `ifconfig` and `ip` are fictional data used to visually represent how these tools work.

The terminal does not execute native Linux commands or commands on the host operating system.

## 4. Virtual File System

The simulator includes its own file system, implemented using Python data structures.

The environment allows users to:

- Create directories.
- Create files.
- Navigate between folders.
- List files and directories.
- Read file contents.
- Write information to files.
- Remove files and directories.
- Display hidden files.
- View basic simulated permission information.

Files and directories are stored in data structures in memory while the programme is running.

Therefore, these operations do not modify the computer's actual file system.

## 5. Additional Tools and Applications

In addition to the terminal, Linux Simulator provides other features accessible through the environment's menus.

### 🔑 Password Generator

The project uses Python's `secrets` module to generate random passwords and validate predefined security criteria.

The validation checks for:

- Uppercase letters.
- Lowercase letters.
- Digits.
- Special characters.
- A minimum length of 12 characters.

The generator repeats the process until a password meets the implemented criteria.

### 🧮 Calculator

Implements basic mathematical operations:

- Addition.
- Subtraction.
- Multiplication.
- Division.

It also includes input validation and division-by-zero handling.

### 🎮 Games Platform

The environment includes five games:

1. Number guessing game.
2. Heads or tails.
3. Questions and answers.
4. Hangman.
5. Simulated Russian roulette.

The games use conditional statements, loops, lists, dictionaries and random number generation.

Russian roulette is exclusively a text-based simulation, with no interaction with real weapons or objects.

### 📅 Calendar and Clock

The calendar allows users to select a month and year to display its layout.

The clock continuously displays the date and time using the `America/Sao_Paulo` time zone.

## 6. Technologies and Concepts

| Technology / Concept | Application |
|---|---|
| Python 3 | Main programming language. |
| Object-Oriented Programming | Organisation of features into classes. |
| Functions and methods | Separation of operations and responsibilities. |
| Conditional statements | Menus, validation and decision-making. |
| Loops | Continuous execution of the terminal and applications. |
| Lists and dictionaries | Data storage and organisation. |
| Exception handling | Management of invalid inputs and interruptions. |
| `secrets` | Password generation. |
| `string` | Character sets used for password generation. |
| `random` | Game mechanics and outcomes. |
| `calendar` | Calendar generation. |
| `datetime` | Date and time handling. |
| `zoneinfo` | Brasília time zone configuration. |
| `time` | Timing intervals and visual effects. |
| `sys` | Imported module available in the code. |
| CLI | User interaction interface. |

## 7. Code Organisation

The project uses Object-Oriented Programming to structure its main features.

The main classes include:

| Class | Responsibility |
|---|---|
| `Cores` | Defines the colour codes used in the interface. |
| `GeradorSenha` | Generates and validates passwords. |
| `Calculadora` | Performs mathematical operations. |
| `PlataformaJogos` | Manages the available games. |
| `SistemaOperacional` | Controls the main environment, authentication, terminal, files and applications. |

This organisation brings different features together in a single environment and demonstrates the practical application of object-oriented programming.

## 8. How to Run

### Requirements

- Python 3.9 or later.
- A terminal capable of running Python applications.

The project uses Python standard library modules and does not require external dependencies.

### Clone the repository

```bash
git clone https://github.com/Udinocraft/Simulador-Linux.git
```

### Enter the project directory

```bash
cd Simulador-Linux/Projetos_python
```

### Run the programme

```bash
python Linux.py
```

On some distributions, you may need to use:

```bash
python3 Linux.py
```

After starting, the programme generates a session password and displays the authentication screen.

## 9. Reports and Documentation

The repository includes technical reports in Brazilian Portuguese and English, documenting the development process and technologies used.

### Portuguese

- [Development report](RELATORIOS-PT/DESENVOLVIMENTO.pdf)
- [Technologies report](RELATORIOS-PT/TECNOLOGIAS.pdf)

### English

- [Development report](RELATORIOS-ING/DEVELOPMENT.pdf)
- [Technologies report](RELATORIOS-ING/TECHNOLOGIES.pdf)

The documents cover the development process, implemented features, technologies, challenges and applied knowledge.

## 10. Learning Outcomes

The development and revision of Linux Simulator provided practical experience in several programming areas:

- Python application development.
- Object-Oriented Programming.
- Class and method organisation.
- CLI development.
- Data structure manipulation.
- Virtual system implementation.
- Custom command development.
- Input validation.
- Exception handling.
- Random data generation.
- Python standard library usage.
- Simulation of Linux environment tools and concepts.
- Code review and improvement.
- Technical documentation.

## 11. Simulation Limitations

Linux Simulator is an educational environment developed in Python. Although it uses commands and elements inspired by Linux, it has several limitations:

- It is not a real operating system.
- It does not execute a native Linux shell.
- It does not run commands directly on the host operating system.
- Its file system is virtual and stored in memory.
- Hardware, kernel and system information is fictional.
- Network tools display simulated results.
- Its features do not replace real system administration or network analysis tools.

These limitations are part of the project's purpose: to represent concepts in a controlled, interactive and educational way.

## 12. Educational Purpose

Linux Simulator was developed to support Python programming education, the practical application of Object-Oriented Programming and the understanding of concepts related to the Linux ecosystem.

The project brings together programming, logic, data structures and basic operating system concepts in a single application.

Its purpose goes beyond reproducing commands: it demonstrates how different features can be developed and integrated using Python.

---

**Project:** Linux Simulator  
**Repository:** [github.com/Udinocraft/Simulador-Linux](https://github.com/Udinocraft/Simulador-Linux)  
**Author:** CyberMota  
**Language:** Python 3  
**Purpose:** Educational Linux-inspired environment simulation
