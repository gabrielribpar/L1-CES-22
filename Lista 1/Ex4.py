from math import sqrt


def is_prime(n):
    """Verifica se n é primo"""
    primo=True #variavel que retem se o número é primo
    if n<=1:
        return False
    else:
        for i in range(2,int(sqrt(n))+1): #Irá dividindo o número 
            if n%i==0: #Verificação se o número não é primo
                primo=False
                break
    return primo
