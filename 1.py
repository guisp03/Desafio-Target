def is_it_in_fibonacci_sequence(num):
    """
    Verifica se um numero dado pertence a sequencia de Fibonacci.

    A sequencia de Fibonacci começa com 0 e 1, e cada numero subsequente e 
    a soma dos dois numeros anteriores. Esta funcao calcula os numeros de 
    Fibonacci ate que o valor gerado seja igual ou maior que o numero 
    fornecido.

    Args:
        num (int): O numero a ser verificado.

    Returns:
        bool: Retorna True se o numero estiver na sequencia de Fibonacci, 
        caso contrario, retorna False.
    """
    if num < 0:
        return False
    
    if num == 0 or num == 1:
        return True
    
    prev_values = [0, 1]
    curr_value = 1
    while num > curr_value:
        prev_values[0] = prev_values[1]
        prev_values[1] = curr_value
        curr_value += prev_values[0]
    
    if num == curr_value:
        return True
    
    return False
        

def main():
    while True:
        try:
            num = int(input("Please enter an integer: "))
            break
        except:
            print("Please input a valid integer!")
    
    result = is_it_in_fibonacci_sequence(num)
    print(f"{num} is it in fibonacci sequence? "
      f"{'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()