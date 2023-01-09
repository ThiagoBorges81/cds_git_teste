def gather_data():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    return n1,n2

def main():
    n1,n2 = gather_data()

    print(n1*n2)

    return None



if __main__ == "__main__":
    main()