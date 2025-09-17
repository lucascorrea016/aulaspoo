from Car import Chave
from Car import Carro

ch = Chave("FIAT")
ch1 = Chave("Volks")
car1 = Carro("Uno", 1998, "Da Firma", 1.0, "SQ007", ch)

car1.LigarCarro()

car1.AbrirCarro(ch)

car1.LigarCarro()

for i in range(2):
    car1.AceleraCarro()

for i in range(3):
    car1.FreiarCarro()

print(car1.chave.marca)