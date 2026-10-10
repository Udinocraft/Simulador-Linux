import secrets
import string
import random
import calendar
import time
from datetime import datetime
from zoneinfo import ZoneInfo


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

            try:
                opcao = int(input("\nEscolha uma opção (1-5): "))
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
                else:
                    print("Opção inválida! Digite um número entre 1 e 5.")
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
        palavras = ["python", "programacao", "computador", "teclado"]
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


class SistemaOperacional:
    def __init__(self, senha_final):
        self.senha_final = senha_final

    def autenticacao(self):
        print("\n---- TELA DE LOGIN ----")
        for i in range(5):
            try:
                tentativa = input(f"Tentativa {i+1}/5 - Informe sua senha: ")
                if tentativa == self.senha_final:
                    print("\nAcesso concedido!")
                    self.linux()
                    break
                else:
                    print("Senha incorreta, tente novamente.")
            except KeyboardInterrupt:
                print("\nUsuário saiu.")
                return
        else:
            print("\nVocê excedeu o limite de tentativas.")

    def linux(self):
        while True:
            print("\n---- LINUX ----\n")
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

    def terminal(self):
        print("\n---- TERMINAL (Digite 'help' para ajuda ou 'exit' para sair) ----")
        while True:
            try:
                comando = input("[usuario@linux ~]$ ").strip().lower()
                if comando == "exit":
                    break
                elif comando == "help":
                    print("Comandos disponíveis: ls, date, whoami, clear, calc, exit")
                elif comando == "ls":
                    print("Arquivos/\tlinux-2026.2-installer-amd64.iso\tpycharm-2026.1.3.tar.gz\tDownloads\tPlataforma de Jogos\tCalendario")
                elif comando == "date":
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                elif comando == "whoami":
                    print("usuario")
                elif comando == "clear":
                    print("\n" * 50)
                elif comando == "calc":
                    Calculadora.executar()
                elif comando in ["neofetch", "fastfetch", "fetch"]:
                    info = """
                       .---.         usuario@linux-pc
                      /     \\        ----------------
                     | ()_() |       OS: Linux Generic x86_64
                     |  (_)  |       Kernel: 6.8.0-generic
                    /  `---'  \\      Uptime: 2 hours, 15 mins
                   / /       \\ \\     Packages: 1250 (pacman), 15 (flatpak)
                  / / |     | \\ \\    Shell: bash 5.2.26
                 / /  |     |  \\ \\   WM/DE: Custom Terminal / Python
                ( (   |_____|   ) )  CPU: Generic Quad-Core Processor @ 2.40GHz
                 \\_\\  /     \\  /_/   Memory: 2048MiB / 8192MiB
                    `-'       `-'    
                            """
                    print(info)
                else:
                    print(f"bash: {comando}: comando não encontrado. Digite 'help'.")
            except KeyboardInterrupt:
                print("\nTerminal encerrado.")
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
    # Geração inicial de segurança
    senha_final = GeradorSenha.gerar_senha_segura(tamanho=12)
    print(f"\n[SISTEMA] Sua senha de acesso é: {senha_final}\n")

    # Inicialização do Sistema Operacional
    os_simulado = SistemaOperacional(senha_final)
    os_simulado.autenticacao()