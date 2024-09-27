def count_a(string):
    """
    Conta o numero de ocorrencias da letra 'a' (maiuscula ou minuscula) em uma
    string fornecida.

    A funcao percorre cada caractere da string e verifica se ele corresponde a
    letra 'a'.

    Args:
        string (str): A string na qual se deseja contar a letra 'a'.

    Returns:
        int: O numero de ocorrencias da letra 'a' na string.
    """
    counter = 0
    for char in string:
        if char.lower() == 'a':
            counter += 1
    
    return counter

def main():
    string = str(input("Please give any input: "))
    a_count = count_a(string)

    if a_count == 0:
        print(f"{string} doesn't have any letter 'a'")
    else:
        print(f"{string} has {a_count} letter 'a'")

if __name__ == "__main__":
    main()