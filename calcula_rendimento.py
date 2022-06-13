import pandas as pd
import math


def calcula_vf(vp, j, periodos, **kwargs):
    lista_rendimento = [vp]
    periodos = math.modf(periodos)
    p_resgate = kwargs.get('p_resgate', None)
    v_resgate = kwargs.get('v_resgate', None)

    for p in list(range(int(periodos[1]))):
        if p == p_resgate:
            calc = lista_rendimento[p] * j + lista_rendimento[p] - v_resgate
            lista_rendimento.append(round(calc, 2))
        else:
            calc = lista_rendimento[p] * j + lista_rendimento[p]
            lista_rendimento.append(round(calc, 2))

    decimal = lista_rendimento[-1] * (1+(j/100)) ** periodos[0]
    if decimal != lista_rendimento[-1]:
        lista_rendimento.append(round(decimal, 2))

    return lista_rendimento


def gerar_df_vf(vp,j,s,p, **kwargs):
    periodos = math.modf(p)
    p_list = list(range(0,int(periodos[1])+1))
    p_dec = periodos[0]
    if p_dec > 0:
        p_list.append(p_dec)
    r = []
    for rendimento in s:
        r.append(rendimento*j)

    p_resgate = kwargs.get('p_resgate', None)
    v_resgate = kwargs.get('v_resgate', None)

    df = pd.DataFrame(data={'Investimento':vp,
                            'Juros':f'{j*100}%',
                            'Rendimento': r,
                            'Periodo': p_list,
                            'Resgate': 'x',
                            'Saldo': s
                            },
                        index=p_list)

    if p_resgate:
        df.loc[p_resgate,  'Resgate'] = v_resgate

    print(df)


def main():
    taxa_juros = float(input("Digite a taxa de Juros:"))/100
    periodos = float(input("Digite a quantidade de periodos:"))
    valor_presente = float(input("Digite o valor Investido:"))
    resgate = int(input("Digite em qual periodo será o resgate(0 se não houver resgate):"))

    if resgate > 0:
        valor_resgate = float(input("Digite a quantidade do resgate: "))
        vf_rendimentos = calcula_vf(valor_presente, taxa_juros, periodos, p_resgate=resgate, v_resgate=valor_resgate)
        gerar_df_vf(valor_presente,taxa_juros, vf_rendimentos, periodos, p_resgate=resgate, v_resgate=valor_resgate)

    else:
        vf_rendimentos = calcula_vf(valor_presente, taxa_juros, periodos)
        gerar_df_vf(valor_presente,taxa_juros, vf_rendimentos, periodos)



    print('-' * 24)

if __name__ == '__main__':
    main()