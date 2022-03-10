def is_palindrome(palavra):
    palindromo=True #Variável que guarda se a palavra é um palindromo
    for i in range(int(len(palavra)/2)): #Loop para verificar se é palindromo
        if palavra[i]!=palavra[-1-i]:#verificar o inicio e o final da palavra
            palindromo=False
    return palindromo
