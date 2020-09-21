"""|Algoritmo de criptografia Calango|


Criado por: Filipefilia"""

import random

def encrypt_calango(msg):
    #Conjunto de listas e variáveis que serão utilizadas para criptografar a mensagem
    encrypt_calango1 = list(msg)
    encrypt_calango2 = []
    encrypt_calango3 = []
    encrypt_calango4 = ""
    cont = 0
    key = random.randint(199, 299)
    #fake_key é um conjunto de números aleatórios que são adicionados à chave para mantê-la em segredo
    fake_key = str(key) + str(random.randint(1111111, 9999999))
    
    #Inverte a mensagem de trás pra frente
    while len(encrypt_calango1) > 0:
        encrypt_calango2.extend(encrypt_calango1[-1:])
        encrypt_calango1.pop()
    
    #Transforma os caracteres em algarismos com base na tabela ASC ii e multiplica cada um deles pelo número gerado aleatoriamente pela variável 'key'
    for i in encrypt_calango2:
        i = int(ord(i)) * key
        encrypt_calango3.append(str(i))
    
    #Verifica o tamanho dos blocos, caso um dos blocos possua menos que 5 dígitos um '0' é adicionado no início dele
    while cont < len(encrypt_calango3):
        if len(encrypt_calango3[cont]) < 5:
            aux = '0' + encrypt_calango3[cont]
            encrypt_calango3[cont] = aux
        cont += 1
    for i in encrypt_calango3:
        encrypt_calango4 += i
    return encrypt_calango4, fake_key


def decrypt_calango(encrypt_msg, encrypt_key):
    #Listas e variáveis que serão utilizadas para decriptografar a mensagem
    decrypt_calango1 = list(encrypt_msg)
    decrypt_calango2 = []
    decrypt_calango3 = []
    decrypt_calango4 = []
    decrypt_calango5 = ""
    cont = 0
    aux = ""
    key = int(encrypt_key[0:3])
    
    #Separa a mensagem criptografada em uma lista com blocos de 5 dígitos (que são o resultado da criptografia)
    while len(decrypt_calango1) > 0:
        decrypt_calango2.append(decrypt_calango1[0:5])
        del decrypt_calango1[0:5]
    
    #Verifica se os blocos iniciam em '0', se sim, esse '0' é removido
    while cont < len(decrypt_calango2):
        if decrypt_calango2[cont][0] == '0':
            del decrypt_calango2[cont][0]
        cont += 1
    
    #Realiza a concatenação dos elementos produzidos na lista anterior, faz a operação matemática inversa (dividindo o algarismo gerado pela chave) e transforma o resultado em caracteres
    for i in decrypt_calango2:
        for j in i:
            aux += j
        decrypt_calango3.extend(chr(int(int(aux)/key)))
        aux = ""
    
    #Reordena a mensagem que havia sido invertida
    while len(decrypt_calango3) > 0:
        decrypt_calango4.extend(decrypt_calango3[-1:])
        decrypt_calango3.pop()
    
    #Transforma a lista final em uma string
    for i in decrypt_calango4:
        decrypt_calango5 += i
    return decrypt_calango5

#Método que roda o programa, chamando os métodos de criptografia e descriptografia
def play():
    while True:
        print("Criptografia com o método Calango")
        print("\t1.Encripta\t2.Decripta\t3.Encerra")
        choice = input("Entre com a opção desejada:")
        if choice == '1':
            msg, key = encrypt_calango(input("Digite a mensagem a ser criptografada:"))
            print("Resultado da cifra:\n--->{}" .format(msg))
            print("\nChave para descriptografia:\n--->{}\n\n" .format(key))
        elif choice == '2':
            encrypt_msg = decrypt_calango(input("\nInsira mensagem:"), input("\nInsira a chave:"))
            print("\n\nMensagem descriptografada:\n--->{}\n\n" .format(encrypt_msg))
        elif choice == '3':
            break
        else:
            print("Opção Inválida\n\n")

play()