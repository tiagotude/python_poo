from frota import *

def operar_carro(carro: Carro):
    print('1-ligar motor')
    print('2-desligar motor')
    print('3-Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro1.ligar()
    elif op == 2:
        carro1.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro1.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro1)
    print(carro2)


if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('quanto tem no tanque?'))
    consumo_medio = float(input('qual o consumo medio?'))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0,False, litros, consumo_medio)

    print('cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('quanto tem no tanque?'))
    consumo_medio = float(input('qual o consumo medio?'))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, consumo_medio)
    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and carro1.tanque > 0 or carro2.tanque > 0:
        try:
            op = 0
            while op not in(1,2):
                op = int(input('qual carro[1,2]'))

                if op == 1:
                    operar_carro(carro1)
                else:
                    operar_carro(carro2)

        except Exception as e:
            print('Erro!')
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
    print('Parar para trocar óleo!!!')

