import secrets
import string
import random
import calendar
import time
import sys
from datetime import datetime
from zoneinfo import ZoneInfo


class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    CINZA = "\033[90m"


class GeradorSenha:
    @staticmethod
    def gerar(tamanho=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

    @staticmethod
    def eh_segura(senha):
        tem_minuscula = any(c.islower() for c in senha)
        tem_maiuscula = any(c.isupper() for c in senha)
        tem_digito = any(c.isdigit() for c in senha)
        tem_especial = any(c in string.punctuation for c in senha)
        tamanho_ok = len(senha) >= 12
        return all([tem_minuscula, tem_maiuscula, tem_digito, tem_especial, tamanho_ok])

    @classmethod
    def gerar_senha_segura(cls, tamanho=12):
        print("Vamos gerar sua senha segura antes de tudo...")
        tentativas = 0
        while True:
            tentativas += 1
            senha = cls.gerar(tamanho)
            if cls.eh_segura(senha):
                print(f"Senha segura gerada após {tentativas} tentativa(s).")
                return senha
            else:
                print(f"Tentativa {tentativas}: senha '{senha}' não é segura, gerando outra...")


class Calculadora:
    @staticmethod
    def executar():
        print("\n---- CALCULADORA ----\n")
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

        while True:
            operacao = input("Escolha a operação (+, -, *, /): ").strip()
            if operacao in ['+', '-', '*', '/']:
                break
            print("Operação inválida! Digite apenas +, -, * ou /.")

        while True:
            try:
                num2 = float(input("Digite o segundo número: "))
                if operacao == '/' and num2 == 0:
                    print("Erro: divisão por zero não é permitida!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            except KeyboardInterrupt:
                print("\nUsuário saiu!")
                return

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        else:
            resultado = num1 / num2

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}\n")

        while True:
            continuar = input("Deseja continuar na calculadora? (sim/não): ").strip().lower()
            if continuar in ['sim', 's']:
                Calculadora.executar()
                return
            elif continuar in ['não', 'nao', 'n']:
                return
            else:
                print("Resposta inválida! Digite 'sim' ou 'não'.")


class PlataformaJogos:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu(self):
        while True:
            print("\n---- PLATAFORMA DE JOGOS ----\n")
            print("1 - Voltar")
            print("2 - Jogo de adivinhação")
            print("3 - Cara ou Coroa")
            print("4 - Pergunta e resposta")
            print("5 - Jogo da forca")
            print("6 - Roleta russa")

            try:
                opcao = int(input("\nEscolha uma opção (1-6): "))
                if opcao == 1:
                    break
                elif opcao == 2:
                    self.jogo_adivinhacao()
                elif opcao == 3:
                    self.cara_ou_coroa()
                elif opcao == 4:
                    self.pergunta_e_resposta()
                elif opcao == 5:
                    self.jogo_da_forca()
                elif opcao == 6:
                    self.roleta_russa()
                else:
                    print("Opção inválida! Digite um número entre 1 e 6.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            except KeyboardInterrupt:
                print("\nUsuário saiu!!")
                break

    def perguntar_continuar(self, jogo_atual):
        while True:
            print("\n1 - Jogar novamente")
            print("2 - Voltar à plataforma de jogos")
            try:
                escolha = int(input("Escolha uma opção (1-2): "))
                if escolha == 1:
                    jogo_atual()
                    return
                elif escolha == 2:
                    return
                else:
                    print("Opção inválida! Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            except KeyboardInterrupt:
                print("\nUsuário saiu!!")
                return

    def jogo_adivinhacao(self):
        print("\n---- JOGO DE ADIVINHAÇÃO ----\n")
        numero_secreto = random.randint(1, 100)
        tentativas = 0

        while True:
            try:
                chute = int(input("Adivinhe o número entre 1 e 100: "))
                tentativas += 1
                if chute < numero_secreto:
                    print("Muito baixo! Tente novamente.")
                elif chute > numero_secreto:
                    print("Muito alto! Tente novamente.")
                else:
                    print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                    break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            except KeyboardInterrupt:
                print("\nUsuário saiu!!")
                return

        self.perguntar_continuar(self.jogo_adivinhacao)

    def cara_ou_coroa(self):
        print("\n---- CARA OU COROA ----\n")
        print("1 - Cara")
        print("2 - Coroa")

        while True:
            try:
                escolha = int(input("Escolha (1-2): "))
                if escolha in [1, 2]:
                    break
                print("Opção inválida! Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            except KeyboardInterrupt:
                print("\nUsuário saiu!!")
                return

        resultado = random.randint(1, 2)
        print("\nResultado: Cara!" if resultado == 1 else "\nResultado: Coroa!")

        if escolha == resultado:
            print("Você acertou!")
        else:
            print("Você errou!")

        self.perguntar_continuar(self.cara_ou_coroa)

    def pergunta_e_resposta(self):
        print("\n---- PERGUNTA E RESPOSTA ----\n")
        perguntas = [
            {"pergunta": "Qual civilização antiga construiu as pirâmides de Gizé?", "opcoes": {"A": "Mesopotâmia", "B": "Egito", "C": "Grécia", "D": "Roma"}, "resposta": "B"},
            {"pergunta": "Quanto é a raiz quadrada de 144?", "opcoes": {"A": "10", "B": "11", "C": "12", "D": "14"}, "resposta": "C"},
            {"pergunta": "Qual é o símbolo químico do ouro?", "opcoes": {"A": "Ag", "B": "Au", "C": "Fe", "D": "Pb"}, "resposta": "B"},
            {"pergunta": "Qual é a unidade de medida de velocidade no SI?", "opcoes": {"A": "km/h", "B": "m/s", "C": "N", "D": "m/s²"}, "resposta": "B"},
            {"pergunta": "Qual é o maior oceano do mundo?", "opcoes": {"A": "Atlântico", "B": "Índico", "C": "Pacífico", "D": "Ártico"}, "resposta": "C"}
        ]

        random.shuffle(perguntas)
        acertos = 0

        for item in perguntas:
            print("\n" + item["pergunta"])
            for letra in ["A", "B", "C", "D"]:
                print(f"{letra}) {item['opcoes'][letra]}")

            while True:
                try:
                    resposta = input("Resposta (A/B/C/D): ").strip().upper()
                    if resposta in ("A", "B", "C", "D"):
                        break
                    print("Entrada inválida! Digite apenas A, B, C ou D.")
                except KeyboardInterrupt:
                    print("\nUsuário saiu!!")
                    return

            if resposta == item["resposta"]:
                print("Correto!")
                acertos += 1
            else:
                print(f"Errado! A resposta certa era: {item['resposta']}")

        print(f"\nVocê acertou {acertos} de {len(perguntas)} perguntas.")
        self.perguntar_continuar(self.pergunta_e_resposta)

    def jogo_da_forca(self):
        print("\n---- JOGO DA FORCA ----\n")
        palavras = ["python", "programacao", "computador", "teclado", "linux", "terminal"]
        palavra = random.choice(palavras)
        letras_descobertas = ["_"] * len(palavra)
        tentativas_restantes = 6
        letras_tentadas = set()

        while tentativas_restantes > 0 and "_" in letras_descobertas:
            print("\nPalavra: " + " ".join(letras_descobertas))
            print(f"Tentativas restantes: {tentativas_restantes}")

            letra = input("Digite uma letra: ").strip().lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Entrada inválida! Digite apenas uma letra.")
                continue

            if letra in letras_tentadas:
                print("Você já tentou essa letra!")
                continue

            letras_tentadas.add(letra)

            if letra in palavra:
                for i, l in enumerate(palavra):
                    if l == letra:
                        letras_descobertas[i] = letra
            else:
                tentativas_restantes -= 1
                print("Letra incorreta!")

        if "_" not in letras_descobertas:
            print(f"\nParabéns! Você acertou a palavra: {palavra}")
        else:
            print(f"\nVocê perdeu! A palavra era: {palavra}")

        self.perguntar_continuar(self.jogo_da_forca)

    def roleta_russa(self):
        print("\n---- ROLETA RUSSA ----\n")
        print("Regras:")
        print("- Um tambor de 6 posições contém apenas 1 bala.")
        print("- Se você atirar em SI MESMO e NÃO for a bala, você ganha OUTRA JOGADA.")
        print("- Se você atirar em SI MESMO e FOR a bala, você MORRE e perde o jogo.")
        print("- Se você atirar na MÁQUINA e NÃO for a bala, passa a vez para ela.")
        print("- Se você atirar na MÁQUINA e FOR a bala, você VENCE!")
        print("- A máquina seguirá as mesmas regras no turno dela.")
        print("-" * 50)

        bala = random.randint(1, 6)
        posicao_atual = 1
        bala_disparada = False

        while not bala_disparada:
            print(f"\n--- Turno do Jogador ---")
            print(f"O tambor está na posição {posicao_atual} de 6.")

            while True:
                try:
                    escolha = int(input(
                        "Escolha seu alvo:\n[1] Atirar em si mesmo\n[2] Atirar na máquina\nDigite sua opção (1 ou 2): "))
                    if escolha in [1, 2]:
                        break
                    else:
                        print(" Opção inválida! Digite apenas 1 ou 2.")
                except ValueError:
                    print(" Entrada inválida! Por favor, digite um número inteiro (1 ou 2).")

            print("Puxando o gatilho...")
            time.sleep(1)

            if posicao_atual == bala:
                print(" *BANG!*")
                if escolha == 1:
                    print(" A bala estava aqui. Você atirou em si mesmo e morreu. Fim de jogo!")
                else:
                    print(" A bala estava aqui! A máquina levou o tiro e explodiu. VOCÊ VENCEU!")
                return
            else:
                print(" *Clique seco...* Nenhuma bala nesta câmara.")
                if escolha == 1:
                    print(" Sorte sua! Como você atirou em si mesmo e sobreviveu, você joga de novo!")
                    posicao_atual += 1
                    continue
                else:
                    print("A máquina sobreviveu ao seu tiro. Passando a vez...")
                    posicao_atual += 1

            print(f"\n--- Turno da Máquina ---")
            time.sleep(1.5)

            escolha_maquina = random.choice([1, 2])

            if escolha_maquina == 1:
                print(" A máquina decidiu apontar a arma para ELA MESMA!")
            else:
                print(" A máquina apontou a arma para VOCÊ!")

            print("A máquina puxa o gatilho...")
            time.sleep(1)

            if posicao_atual == bala:
                print(" *BANG!*")
                if escolha_maquina == 1:
                    print(" A bala estava na vez dela! A máquina atirou nela mesma e morreu. VOCÊ VENCEU!")
                else:
                    print(" A bala estava na câmara. A máquina atirou em você e você morreu. Fim de jogo!")
                return
            else:
                print(" *Clique seco...* A máquina teve sorte.")
                if escolha_maquina == 1:
                    print("A máquina sobreviveu atirando nela mesma e ganhou mais uma jogada!")
                    posicao_atual += 1
                    continue
                else:
                    print("Você sobreviveu ao tiro da máquina. O jogo continua!")
                    posicao_atual += 1

            if posicao_atual > 6:
                posicao_atual = 1

        self.perguntar_continuar(self.roleta_russa)


class SistemaOperacional:
    def __init__(self, senha_final):
        self.senha_final = senha_final
        self.usuario = "usuario"
        self.hostname = "linux-pc"
        self.inicio_sessao = time.time()
        self.tema_cor = Cores.CIANO
        self.historico_comandos = []

        # Sistema de arquivos virtual em memória
        self.sistema_arquivos = {
            "~": {
                "Arquivos": {
                    "linux-2026.2-installer-amd64.iso": "[Imagem ISO - 4.2 GB]",
                    "pycharm-2026.1.3.tar.gz": "[Pacote Compactado - 680 MB]"
                },
                "Downloads": {
                    "Plataforma_de_Jogos.app": "[Executável - 1.5 GB]",
                    "Calendario.app": "[Executável - 50 MB]"
                },
                "Documentos": {
                    "notas.txt": "Bem-vindo ao Simulador Linux!\nUse 'help' para explorar todos os comandos disponíveis.",
                    "rede.conf": "INTERFACE=wlan0\nIP=192.168.1.42\nDNS=1.1.1.1"
                },
                ".bashrc": "# Configuração do Shell\nalias ll='ls -la'\nexport EDITOR=nano"
            }
        }
        self.caminho_atual = ["~"]

    def obter_diretorio_atual(self):
        ref = self.sistema_arquivos
        for pasta in self.caminho_atual:
            ref = ref[pasta]
        return ref

    def formatar_uptime(self):
        segundos = int(time.time() - self.inicio_sessao)
        horas, resto = divmod(segundos, 3600)
        minutos, seg = divmod(resto, 60)
        return f"{horas}h {minutos}m {seg}s"

    def autenticacao(self):
        print(f"\n{Cores.CIANO}---- TELA DE LOGIN ----{Cores.RESET}")
        for i in range(5):
            try:
                tentativa = input(f"Tentativa {i+1}/5 - Informe sua senha: ")
                if tentativa == self.senha_final:
                    print(f"\n{Cores.VERDE}Acesso concedido!{Cores.RESET}")
                    self.linux()
                    break
                else:
                    print(f"{Cores.VERMELHO}Senha incorreta, tente novamente.{Cores.RESET}")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                return
        else:
            print(f"\n{Cores.VERMELHO}Você excedeu o limite de tentativas.{Cores.RESET}")

    def linux(self):
        while True:
            print(f"\n{Cores.CIANO}---- LINUX ----{Cores.RESET}\n")
            print("1 - Bloquear sessão / Voltar ao login")
            print("2 - Navegador")
            print("3 - Terminal")
            print("4 - Calendário")
            print("5 - Pastas")
            print("6 - Relógio")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    break
                elif opcao == 2:
                    self.navegador()
                elif opcao == 3:
                    self.terminal()
                elif opcao == 4:
                    self.calendario()
                elif opcao == 5:
                    self.pastas()
                elif opcao == 6:
                    self.relogio()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido.")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def navegador(self):
        while True:
            print("\n------ NAVEGADOR ------\n")
            print("1 - Voltar")
            print("2 - Calculadora")
            print("3 - Plataforma de jogos")

            try:
                usuario = int(input("Qual opção deseja ir: "))
                if usuario == 1:
                    break
                elif usuario == 2:
                    Calculadora.executar()
                elif usuario == 3:
                    jogos = PlataformaJogos(self)
                    jogos.menu()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida!")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def _efeito_matrix(self):
        print(f"{Cores.VERDE}Iniciando Matrix (pressione CTRL+C para sair)...{Cores.RESET}")
        time.sleep(0.7)
        caracteres = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ"
        try:
            while True:
                linha = "".join(
                    random.choice(caracteres) if random.random() > 0.65 else " "
                    for _ in range(70)
                )
                print(f"{Cores.VERDE}{linha}{Cores.RESET}")
                time.sleep(0.06)
        except KeyboardInterrupt:
            print(f"\n{Cores.RESET}Matrix encerrada.")

    def terminal(self):
        banner = f"""{self.tema_cor}{Cores.NEGRITO}
╔══════════════════════════════════════════════════════════════╗
║  LINUX TERMINAL v2.6  |  Digite 'help' para ver os comandos  ║
╚══════════════════════════════════════════════════════════════╝{Cores.RESET}"""
        print(banner)

        while True:
            try:
                caminho_str = "/".join(self.caminho_atual)
                prompt = (
                    f"{self.tema_cor}┌──({Cores.NEGRITO}{self.usuario}㉿{self.hostname}{Cores.RESET}"
                    f"{self.tema_cor})-[{Cores.AZUL}{Cores.NEGRITO}{caminho_str}{Cores.RESET}{self.tema_cor}]\n"
                    f"└─$ {Cores.RESET}"
                )
                entrada = input(prompt).strip()
                if not entrada:
                    continue

                self.historico_comandos.append(entrada)
                partes = entrada.split()
                cmd = partes[0].lower()
                args = partes[1:]

                if cmd == "exit":
                    break

                elif cmd == "help":
                    print(f"""
{Cores.NEGRITO}{self.tema_cor}=== COMANDOS DISPONÍVEIS ==={Cores.RESET}
{Cores.AMARELO}Navegação & Arquivos:{Cores.RESET}
  ls [-la]          Lista arquivos e pastas do diretório atual
  pwd               Mostra o caminho completo atual
  cd <pasta>        Entra em uma pasta (use 'cd ..' para voltar ou 'cd ~' para home)
  mkdir <nome>      Cria uma nova pasta
  touch <arquivo>   Cria um arquivo vazio
  cat <arquivo>     Exibe o conteúdo de um arquivo
  echo <txt> > <arq> Escreve texto dentro de um arquivo
  rm <nome>         Remove um arquivo ou pasta

{Cores.AMARELO}Sistema & Personalização:{Cores.RESET}
  neofetch / fetch  Mostra informações detalhadas do sistema
  uname -a          Exibe informações do kernel
  uptime            Mostra há quanto tempo o sistema está ativo
  whoami            Exibe o usuário atual
  passwd            Altera a senha de login da sessão
  theme <cor>       Muda a cor do terminal (ciano, verde, magenta, azul, amarelo)
  history           Mostra o histórico de comandos digitados
  clear             Limpa a tela do terminal

{Cores.AMARELO}Rede & Ferramentas:{Cores.RESET}
  ifconfig / ip     Exibe interfaces de rede e endereço IP
  ping <host>       Testa conectividade com um servidor
  nmap <alvo>       Simula varredura de portas em um alvo
  matrix            Ativa chuva de caracteres estilo Matrix
  calc              Abre a calculadora
  jogos             Abre a plataforma de jogos
  date              Mostra data e hora atuais
  exit              Fecha o terminal
""")

                elif cmd == "pwd":
                    caminho_real = "/home/" + self.usuario + ("/" + "/".join(self.caminho_atual[1:]) if len(self.caminho_atual) > 1 else "")
                    print(caminho_real)

                elif cmd == "ls":
                    dir_atual = self.obter_diretorio_atual()
                    mostrar_ocultos = "-a" in args or "-la" in args or "-al" in args
                    detalhado = "-l" in args or "-la" in args or "-al" in args

                    itens = list(dir_atual.keys())
                    if not mostrar_ocultos:
                        itens = [i for i in itens if not i.startswith(".")]

                    if not itens:
                        print(f"{Cores.CINZA}(diretório vazio){Cores.RESET}")
                        continue

                    for item in itens:
                        eh_pasta = isinstance(dir_atual[item], dict)
                        if eh_pasta:
                            nome_fmt = f"{Cores.AZUL}{Cores.NEGRITO}{item}/{Cores.RESET}"
                            perm = "drwxr-xr-x"
                        elif item.endswith((".app", ".sh")):
                            nome_fmt = f"{Cores.VERDE}{Cores.NEGRITO}{item}{Cores.RESET}"
                            perm = "-rwxr-xr-x"
                        elif item.endswith((".iso", ".tar.gz", ".zip")):
                            nome_fmt = f"{Cores.VERMELHO}{item}{Cores.RESET}"
                            perm = "-rw-r--r--"
                        else:
                            nome_fmt = item
                            perm = "-rw-r--r--"

                        if detalhado:
                            print(f"{Cores.CINZA}{perm}  {self.usuario}  {Cores.RESET}{nome_fmt}")
                        else:
                            print(nome_fmt, end="   ")
                    if not detalhado:
                        print()

                elif cmd == "cd":
                    if not args or args[0] == "~":
                        self.caminho_atual = ["~"]
                    elif args[0] == "..":
                        if len(self.caminho_atual) > 1:
                            self.caminho_atual.pop()
                    else:
                        destino = args[0].rstrip("/")
                        dir_atual = self.obter_diretorio_atual()
                        if destino in dir_atual and isinstance(dir_atual[destino], dict):
                            self.caminho_atual.append(destino)
                        elif destino in dir_atual:
                            print(f"{Cores.VERMELHO}bash: cd: {destino}: Não é um diretório{Cores.RESET}")
                        else:
                            print(f"{Cores.VERMELHO}bash: cd: {destino}: Arquivo ou diretório inexistente{Cores.RESET}")

                elif cmd == "mkdir":
                    if not args:
                        print("mkdir: operando faltando")
                    else:
                        nome = args[0]
                        dir_atual = self.obter_diretorio_atual()
                        if nome in dir_atual:
                            print(f"{Cores.VERMELHO}mkdir: não foi possível criar '{nome}': Arquivo já existe{Cores.RESET}")
                        else:
                            dir_atual[nome] = {}
                            print(f"{Cores.VERDE}Diretório '{nome}' criado.{Cores.RESET}")

                elif cmd == "touch":
                    if not args:
                        print("touch: operando de arquivo faltando")
                    else:
                        nome = args[0]
                        dir_atual = self.obter_diretorio_atual()
                        if nome not in dir_atual:
                            dir_atual[nome] = ""

                elif cmd == "cat":
                    if not args:
                        print("cat: informe o nome do arquivo")
                    else:
                        nome = args[0]
                        dir_atual = self.obter_diretorio_atual()
                        if nome in dir_atual:
                            if isinstance(dir_atual[nome], dict):
                                print(f"{Cores.VERMELHO}cat: {nome}: É um diretório{Cores.RESET}")
                            else:
                                print(dir_atual[nome] if dir_atual[nome] else f"{Cores.CINZA}(arquivo vazio){Cores.RESET}")
                        else:
                            print(f"{Cores.VERMELHO}cat: {nome}: Arquivo ou diretório inexistente{Cores.RESET}")

                elif cmd == "echo":
                    if ">" in args:
                        idx = args.index(">")
                        texto = " ".join(args[:idx]).strip('"').strip("'")
                        if idx + 1 < len(args):
                            arquivo = args[idx + 1]
                            dir_atual = self.obter_diretorio_atual()
                            dir_atual[arquivo] = texto
                        else:
                            print("Erro de sintaxe perto de '>'")
                    else:
                        print(" ".join(args).strip('"').strip("'"))

                elif cmd == "rm":
                    if not args:
                        print("rm: operando faltando")
                    else:
                        nome = args[0].rstrip("/")
                        dir_atual = self.obter_diretorio_atual()
                        if nome in dir_atual:
                            del dir_atual[nome]
                            print(f"{Cores.AMARELO}'{nome}' removido.{Cores.RESET}")
                        else:
                            print(f"{Cores.VERMELHO}rm: não foi possível remover '{nome}': Arquivo ou diretório inexistente{Cores.RESET}")

                elif cmd == "date":
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

                elif cmd == "whoami":
                    print(self.usuario)

                elif cmd == "uname":
                    if "-a" in args:
                        print(f"Linux {self.hostname} 6.11.6-arch1-1 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux")
                    else:
                        print("Linux")

                elif cmd == "uptime":
                    print(f" {datetime.now().strftime('%H:%M:%S')} up {self.formatar_uptime()},  1 user,  load average: 0.14, 0.09, 0.05")

                elif cmd == "history":
                    for idx, item_hist in enumerate(self.historico_comandos, start=1):
                        print(f" {Cores.CINZA}{idx:3d}{Cores.RESET}  {item_hist}")

                elif cmd == "theme":
                    temas = {
                        "ciano": Cores.CIANO,
                        "verde": Cores.VERDE,
                        "magenta": Cores.MAGENTA,
                        "azul": Cores.AZUL,
                        "amarelo": Cores.AMARELO
                    }
                    if args and args[0].lower() in temas:
                        self.tema_cor = temas[args[0].lower()]
                        print(f"{self.tema_cor}Tema alterado para {args[0].lower()}!{Cores.RESET}")
                    else:
                        print("Uso: theme <ciano | verde | magenta | azul | amarelo>")

                elif cmd == "passwd":
                    nova_senha = input("Digite a nova senha (mínimo 8 caracteres): ").strip()
                    if len(nova_senha) >= 8:
                        self.senha_final = nova_senha
                        print(f"{Cores.VERDE}passwd: senha atualizada com sucesso.{Cores.RESET}")
                    else:
                        print(f"{Cores.VERMELHO}Senha muito curta! Operação cancelada.{Cores.RESET}")

                elif cmd == "sudo":
                    print(f"{Cores.VERMELHO}[sudo] senha para {self.usuario}: {Cores.RESET}", end="")
                    input()
                    print(f"{Cores.VERMELHO}{self.usuario} não está no arquivo sudoers. Este incidente será reportado.{Cores.RESET}")

                elif cmd in ["ifconfig", "ip"]:
                    print(f"""{Cores.NEGRITO}lo:{Cores.RESET} flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0

{Cores.NEGRITO}wlan0:{Cores.RESET} flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet {Cores.VERDE}192.168.1.42{Cores.RESET}  netmask 255.255.255.0  broadcast 192.168.1.255
        ether 00:1a:2b:3c:4d:5e  txqueuelen 1000  (Ethernet)""")

                elif cmd == "ping":
                    alvo = args[0] if args else "8.8.8.8"
                    print(f"PING {alvo} ({alvo}) 56(84) bytes de dados.")
                    for seq in range(1, 5):
                        latencia = round(random.uniform(11.2, 28.9), 1)
                        print(f"64 bytes de {alvo}: icmp_seq={seq} ttl=117 tempo={Cores.VERDE}{latencia} ms{Cores.RESET}")
                        time.sleep(0.5)
                    print(f"--- {alvo} estatísticas de ping ---\n4 pacotes transmitidos, 4 recebidos, 0% perda de pacote")

                elif cmd == "nmap":
                    alvo = args[0] if args else "192.168.1.1"
                    print(f"Iniciando Nmap 7.95 em {alvo}...")
                    time.sleep(1)
                    print(f"""PORT     STATE SERVICE
{Cores.VERDE}22/tcp   open  ssh{Cores.RESET}
{Cores.VERDE}80/tcp   open  http{Cores.RESET}
{Cores.VERDE}443/tcp  open  https{Cores.RESET}
{Cores.AMARELO}8080/tcp filtered http-proxy{Cores.RESET}
Nmap concluído: 1 endereço IP (1 host ativo) escaneado em 1.12 segundos.""")

                elif cmd == "matrix":
                    self._efeito_matrix()

                elif cmd == "clear":
                    print("\033[H\033[J", end="")

                elif cmd == "calc":
                    Calculadora.executar()

                elif cmd == "jogos":
                    jogos = PlataformaJogos(self)
                    jogos.menu()

                elif cmd in ["neofetch", "fastfetch", "fetch"]:
                    info = f"""
{self.tema_cor}        .---.          {Cores.NEGRITO}{self.usuario}@{self.hostname}{Cores.RESET}
{self.tema_cor}       /     \\         {Cores.CINZA}----------------{Cores.RESET}
{self.tema_cor}      | ()_() |        {self.tema_cor}OS:{Cores.RESET} Arch Linux Custom x86_64
{self.tema_cor}      |  (_)  |        {self.tema_cor}Kernel:{Cores.RESET} 6.11.6-arch1-1
{self.tema_cor}     /  `---'  \\       {self.tema_cor}Uptime:{Cores.RESET} {self.formatar_uptime()}
{self.tema_cor}    / /       \\ \\      {self.tema_cor}Packages:{Cores.RESET} 1250 (pacman), 15 (flatpak)
{self.tema_cor}   / / |     | \\ \\     {self.tema_cor}Shell:{Cores.RESET} bash 5.2.37
{self.tema_cor}  / /  |     |  \\ \\    {self.tema_cor}WM/DE:{Cores.RESET} Custom Terminal / Python
{self.tema_cor} ( (   |_____|   ) )   {self.tema_cor}CPU:{Cores.RESET} Ryzen 5 5600GT (12) @ 4.40GHz
{self.tema_cor}  \\_\\  /     \\  /_/    {self.tema_cor}Memory:{Cores.RESET} 2048MiB / 16384MiB
{self.tema_cor}    `-'       `-'      {Cores.VERMELHO}███{Cores.VERDE}███{Cores.AMARELO}███{Cores.AZUL}███{Cores.MAGENTA}███{Cores.CIANO}███{Cores.RESET}
"""
                    print(info)
                else:
                    print(f"{Cores.VERMELHO}bash: {cmd}: comando não encontrado. Digite 'help'.{Cores.RESET}")

            except KeyboardInterrupt:
                print(f"\n{Cores.AMARELO}Terminal encerrado.{Cores.RESET}")
                break

    def calendario(self):
        while True:
            print("\n---- CALENDARIO ----\n")
            try:
                mes = int(input("Escolha um mês (1-12): "))
                ano = int(input("Coloque o ano: "))

                if 1 <= mes <= 12:
                    print("\nSeu Calendário:\n")
                    print(calendar.month(ano, mes))
                else:
                    print("Inválido! Selecione meses apenas de 1 a 12.")
                    continue

                print("1 - Voltar ao Linux")
                print("2 - Continuar no Calendário")
                usuario = int(input("Escolha: "))

                if usuario == 1:
                    break
                elif usuario == 2:
                    continue
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Dados informados incorretamente.")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def pastas(self):
        while True:
            print("\n---- PASTAS ----\n")
            print("1 - Home")
            print("2 - Downloads")
            print("3 - Arquivos")
            print("4 - Voltar")
            try:
                pasta = int(input("\nEscolha uma Pasta (1-4): "))
                if pasta == 1:
                    print("Você já está na Home.")
                elif pasta == 2:
                    self.downloads()
                elif pasta == 3:
                    self.arquivos()
                elif pasta == 4:
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida!")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def downloads(self):
        print("\nhome/pastas/downloads")
        while True:
            print("1 - Voltar para Pastas")
            print("2 - Ver info: Plataforma de Jogos")
            print("3 - Ver info: Calendario")
            try:
                usuario = int(input("(1-3): "))
                if usuario == 1:
                    break
                elif usuario == 2:
                    print("\nTamanho: 1.5GB\nDono: Você\nPermissões: Leitura/Escrita\nModificado: Agora\n")
                elif usuario == 3:
                    print("\nResolução: 500x500\nTamanho: 50MB\nDono: Você\nPermissões: Leitura/Escrita\nModificado: Agora\n")
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Dados inválidos!")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def arquivos(self):
        print("\nhome/pastas/arquivos")
        print("\n- linux-2026.2-installer-amd64.iso")
        print("- pycharm-2026.1.3.tar.gz")
        while True:
            try:
                sair = int(input("\nDigite 1 para Sair: "))
                if sair == 1:
                    break
                print("Opção inválida!")
            except ValueError:
                print("Entrada inválida!")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                break

    def relogio(self):
        print("---- RELOGIO ----")
        print("Pressione CTRL+C para parar e voltar.")
        fuso_brasilia = ZoneInfo("America/Sao_Paulo")
        try:
            while True:
                agora = datetime.now(fuso_brasilia)
                hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
                print(f"\rHorário de Brasília: {hora_formatada}", end="", flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nRelógio encerrado com sucesso!")


if __name__ == "__main__":
    senha_final = GeradorSenha.gerar_senha_segura(tamanho=12)
    print(f"\n[SISTEMA] Sua senha de acesso é: {senha_final}\n")

    os_simulado = SistemaOperacional(senha_final)
    os_simulado.autenticacao()