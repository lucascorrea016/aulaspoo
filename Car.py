class Chave:
    def __init__(self, marca):
        self.marca = marca
        self.ativa = False

class Carro:
    def __init__(self, modelo: str, ano, cor, potencia, placa, chave: Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = 0

    def AbrirCarro(self, chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            print('O carro está aberto!')
        else:
            print('O carro já está aberto, ligado ou a chave está errada.')
            
    def LigarCarro(self):
        if not self.ligado and self.aberto:
            self.ligado = True
            print('O carro está ligado! RUUUUUUMMM tssss')
        else:
            print('O carro está ligado ou não está aberto. \nVerifique isso!')

    def AceleraCarro(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade +=5
            print(f'O carro {self.modelo} está andando a {self.velocidade} km/h.')
        else:
            print(f'O carro {self.modelo} está desligado. \nPrecisa ligá-lo primeiro.')

    def FreiarCarro(self):
        if self.ligado and self.velocidade >= 1:
            self.velocidade -= 5
            print(f'*Freiando* \nO carro {self.modelo} está reduzindo e está a {self.velocidade} km/h.')
        elif self.velocidade == 0:
            print('Carro parado.')
        else:
            print('O carro está desligado!')