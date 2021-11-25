import numpy as np

#Get a user-supplied array and sort them in descending order using numpy.
def main():
    arr =[]
    aux = []
    for i in range(5):
        arr.append(int(input(f'Digite o {i+1}º número: ')))

    for item in range(len(arr)):
        maior = max(arr)
        aux.append(maior)
        arr.remove(maior)
    print(aux)


if __name__ == '__main__':
    main()