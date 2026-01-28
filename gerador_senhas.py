import secrets
import string


def ler_sn(msg: str) -> bool:
    while True:
        r = input(msg).strip().lower()
        if r in ("s", "sim"):
            return True
        if r in ("n", "nao", "não"):
            return False
        print("❌ Responde com 's' ou 'n'.")


def ler_int(msg: str, minimo: int, maximo: int) -> int:
    while True:
        s = input(msg).strip()
        if not s.isdigit():
            print("❌ Insere um número inteiro.")
            continue
        n = int(s)
        if n < minimo or n > maximo:
            print(f"❌ Insere um valor entre {minimo} e {maximo}.")
            continue
        return n


def gerar_senha(tamanho: int, usar_maiusculas: bool, usar_minusculas: bool,
                usar_numeros: bool, usar_simbolos: bool) -> str:
    grupos = []

    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)
    if usar_minusculas:
        grupos.append(string.ascii_lowercase)
    if usar_numeros:
        grupos.append(string.digits)
    if usar_simbolos:
        grupos.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not grupos:
        raise ValueError("Nenhum conjunto de caracteres foi selecionado.")

    # Garantir pelo menos 1 caractere de cada grupo escolhido
    senha = [secrets.choice(g) for g in grupos]

    # Completar o resto com um conjunto combinado
    combinado = "".join(grupos)
    while len(senha) < tamanho:
        senha.append(secrets.choice(combinado))

    # Baralhar para não ficar previsível (ex: 1º sempre maiúscula, etc.)
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)


def main():
    print("=" * 34)
    print("   GERADOR DE SENHAS SEGURAS")
    print("=" * 34)

    tamanho = ler_int("Tamanho da senha (8 a 64): ", 8, 64)

    usar_maiusculas = ler_sn("Incluir letras MAIÚSCULAS? (s/n): ")
    usar_minusculas = ler_sn("Incluir letras minúsculas? (s/n): ")
    usar_numeros = ler_sn("Incluir números? (s/n): ")
    usar_simbolos = ler_sn("Incluir símbolos? (s/n): ")

    try:
        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
        print("Dica: escolhe pelo menos um tipo de caractere.")
        return

    print("\n✅ Senha gerada:")
    print(senha)

    # Extra: força mínima (só informativo)
    tipos = sum([usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos])
    if tipos <= 1:
        print("\n⚠️ Sugestão: ativa 2+ tipos (ex: letras + números + símbolos).")


if __name__ == "__main__":
    main()
