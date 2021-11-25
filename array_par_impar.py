
#Separe an array in two other arrays, odd and even.
def main():
    array_completo = [1,3,35,40,85,123,121,209,200,305,350]
    def par(array):
        par = []
        for item in array:
            if item %2 == 0:
                par.append(item)
        return par


    def impar(array):
        impar = []
        for item in array:
            if item %2 != 0:
                impar.append(item)
        return impar


    print(f'Array completo {array_completo}')
    print(f'Separação Par {par(array_completo)}')
    print(f'Separação Impar {impar(array_completo)}')


if __name__ == '__main__':
    main()