#!/usr/bin/python3
import random

def tamanhoJogo(jogos):
    """
    Função que retorna o tamanho de cada jogo
    """
    tamanho = {}
    j = 0
    for i in jogos:
        tamanho[j] = len(i)
        j += 1

    lista = []
    for i in range(3):
        menor = min(tamanho,key=tamanho.get)
        lista.append(menor)
        tamanho.pop(menor)

    return lista

def main():
    """
    Função principal
    """
    # lista com os numeros em sequencia [1-25]
    list_num = list(range(1,26))

    # recebe os 5 num para exclusao da lista
    list_remove = []
    for i in range(1,6):
        while 1:
            n = int(input('Digite o {}º Número [1-25]: '.format(i)))
            # verifica se o num digitado está entre 1-25
            if n <= 25:
                # verifica se o num já foi digitado anteriormente
                if n not in list_remove:
                    list_remove.append(n)
                    break
                else:
                    print('O Número {} já foi digitado, Escolha outro número...'.format(n))
                
            else:
                print('O Número precisa ser menor ou igual a 25, Digite novamente...')

    # exibe os num escolhidos
    print('Os números escolhidos para exclusão foram {}'.format(list_remove))

    # remove os 5 num escolhidos da lista de 25 num
    for i in list_remove:
        list_num.remove(i)

    # jogos com lista de 4 sequencias
    jogos = [[],[],[],[]]

    # 3 primeiras sequencias a serem preenchidas / gerado aleatoriamente
    id_jogo = random.sample(range(0,4),3)

    for i in list_num:
        # gera a primeira sequencia de jogos
        if len(id_jogo) > 0:
            for j in id_jogo:
                jogos[j].append(i)
            id_jogo = []
        else:
            menor = tamanhoJogo(jogos)
            for k in menor:
                jogos[k].append(i)


    print("Jogos Gerados:")
    n = 1
    for j in jogos:
        print("Jogo Nº{} -> {}".format(n,j))
        n += 1

# executa a função principal
main()