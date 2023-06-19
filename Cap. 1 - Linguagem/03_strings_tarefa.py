# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "Isso é uma String"
    print(s)

    # TODO: Tente juntar os dois.
    
    #print(b + s)

    # TODO: Bytes e strings precisam ser apropriadamente encoded
    
    print(s + b.decode('utf-8'))

    # TODO: Faça o encode da string como UTF-32
    print(s.encode('utf-32') + b)

if __name__ == "__main__":
    main()
