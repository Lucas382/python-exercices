#Ccalculate the height of a building based
# on the given number of floors and height of each floor.
def main():
    numero_andar = int(input("Qual número de andares possui o edificio?"))
    altura_andar = int(input("Qual a altura de cada andar? "))


    def calcula_altura(altura, num_andar):
        return altura * num_andar


    print(f'O edificio possui {calcula_altura(numero_andar,altura_andar)} metros de altura')


if __name__ == '__main__':
    main()