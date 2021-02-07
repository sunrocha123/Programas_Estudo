import pytest

class Carros:

    def __init__ (self, marca_do_carro, modelo_do_carro, ano_do_carro, velocidade_maxima_do_carro):
        self.marca_do_carro = marca_do_carro
        self.modelo_do_carro = modelo_do_carro
        self.ano_do_carro = ano_do_carro
        self.velocidade_maxima_do_carro = velocidade_maxima_do_carro

    def __str__ (self):
        if self.velocidade_maxima_do_carro > 200:
            s = 'O carro ' + self.marca_do_carro + " " + self.modelo_do_carro + ' é um raioooooo!'
        elif self.velocidade_maxima_do_carro >= 150 and self.velocidade_maxima_do_carro <= 200:
            s = 'O carro ' + self.marca_do_carro + " " + self.modelo_do_carro + ' até que é rápido!'
        else:
            s = 'O carro ' + self.marca_do_carro + " " + self.modelo_do_carro + ' é lerdo!'

        return s

    def validar_velocidade(self):
        if self.velocidade_maxima_do_carro < 150:
            print(self)
        else:
            print(self)

class Test:

    @pytest.mark.parametrize("marca_do_carro, modelo_do_carro, ano_do_carro, velocidade_maxima_do_carro, resposta_esperada",[
        ('Volkswagen','Fusca', 1972, 136, 'O carro Volkswagen Fusca é lerdo!'),
        ('Volkswagen','Brasília', 1973, 132, 'O carro Volkswagen Brasília é lerdo!'),
        ('Lamborghini','Aventador SVJ Roadster', 2020, 350, 'O carro Lamborghini Aventador SVJ Roadster é um raioooooo!')
    ])
    def test(self, marca_do_carro, modelo_do_carro, ano_do_carro, velocidade_maxima_do_carro, resposta_esperada):
        Carros(marca_do_carro, modelo_do_carro, ano_do_carro, velocidade_maxima_do_carro) == resposta_esperada
        



