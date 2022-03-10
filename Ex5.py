def verifica_palindromo(palavra):
    """Verifica se a palavra é um palindromo"""
    palindromo=True #Variável que guarda se a palavra é um palindromo
    for i in range(int(len(palavra)/2)): #Loop até o meio da palavra
        if palavra[i]!=palavra[-1-i]:#verifica os extremos
            palindromo=False
            break 
    return palindromo
