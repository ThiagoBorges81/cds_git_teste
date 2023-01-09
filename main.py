def gather_data():
    n1 = input("Primeiro valor: ")
    n2 = input("Segundo valor: ")

    return n1,n2, op

def print_message(n1,n2):
    print(f'Os valores{n1} e {n2} somados dão {n1+n2}')

    return None
    

def main():
    n1,n2,op = gather_data()

    print(eval(n1+op+n2))

    return None



if __main__ == "__main__":
    main()