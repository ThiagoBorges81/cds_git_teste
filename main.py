import test

def gather_data():
    n1 = input("Primeiro valor: ")
    n2 = input("Segundo valor: ")
    op = input("Operacao: ")
    return n1,n2, op

def main():
    n1,n2,op = gather_data()

    print(eval(n1+op+n2))

    return None



if __main__ == "__main__":
    main()