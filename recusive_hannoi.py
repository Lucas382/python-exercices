discos = 4

def move_disco(discos, origem, destino, auxiliar):
    if discos == 1:
        print("\nMova o disco da", origem,
                            "para a", destino)
    else:
        move_disco(discos-1, origem,auxiliar ,destino)
        print("\n Mova o disco da ", origem,
                            "para a", destino)
        move_disco(discos-1, auxiliar, destino, origem)


move_disco(discos, "Torre 1", "Torre 3", "Torre 2")