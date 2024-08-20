class Carro:
    modelo : str
    marca : str
    cor : str
    odometro = 0.0
    motor_on = False
    tanque: float
    consumo_medio: float
    velocidade: float
    tempo: float

    def __init__(self,consumo_medio: float, tanque: float, modelo: str, marca: str, cor: str,
                       odometro : float, motor : bool):

        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor
        self.consumo_medio = consumo_medio
        self.tanque = tanque

    def ligar(self):
        if not self.motor_on and self.tanque > 0:
            self.motor_on = True
        else:
             raise Exception("Erro: Motor já ligado ou tanque vazio.")

    def acelerar(self, velocidade : float, tempo : float):

        if self.motor_on and self.tanque > 0:
            km = self.velocidade * self.tempo
            litros = km / self.consumo_medio

            if self.tanque >= litros:
                self.odometro += km
                self.tanque -= litros
                self.motor_on = False
            else:
                km = self.tanque * self.consumo_medio
                self.odometro += km
                self.tanque = 0
        else:
            raise Exception("Erro: nao e possivel acelerar! motor desligado.")

    def desligar(self):

        if self.motor_on:
            self.motor_on = False
        else:
             raise Exception("Erro: nao e possivel acelerar! motor desligado.")

    def __str__ (self):

        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}'
                f'consumo medio{self.consumo_medio} km/l'
                f'nivel do tanque {self.tanque}l')
        return info





