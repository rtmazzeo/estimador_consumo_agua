from datetime import datetime
import pandas as pd

tarifa = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
          'Valor da Agua': [29.63, 4.13,6.29,7.56],
          'Valor do Esgoto':[26.67,3.72,5.66,6.80]
          }
tarifa = pd.DataFrame(data=tarifa)

class Dias:

    def __init__(self,none):
        self._dias = none

    @property
    def dias(self):
        return self._dias

class Leitura:

    def __init__(self,none):
        self._leitura = none

    @property
    def leitura(self):
        return self.leitura

class Consumo_dia:

    def __init__(self,none):
        self._consumo_dia = self._consumo/self._dias

    @property
    def consumo_d(self):
        return self.consumo_d

class Lance:
  def __init__(self,usuario,valor):
      self.dias = dias
      self.leitura = leitura
      self.consumo_d = consumo_d

n_dias = Dias(((datetime.strptime(input('Qual a data da leitura informada pelo usuário? (hoje) '),"%d/%m/%Y") - 
        datetime.strptime(input('Qual a data da última leitura valida? '),"%d/%m/%Y")).days))
n_leitura = Leitura(float(input('Qual a leitura atual? ').strip()) - float(input('Qual a ultima leitura válida? ').strip()))

consumo_diario = n_leitura.leitura/n_dias.dias
consumo_mes = float(round(consumo_diario*30,0))
consumo = consumo_mes

tarifa = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
          'Valor da Agua': [29.63, 4.13,6.29,7.56],
          'Valor do Esgoto':[26.67,3.72,5.66,6.80]
          }
tarifa = pd.DataFrame(data=tarifa)


consumo_10 = tarifa.at[0,'Valor da Agua'] + tarifa.at[0,"Valor do Esgoto"] # seleciona somente o valor da colular Valor agua linha 1
consumo_20 = tarifa.at[1,'Valor da Agua']*(consumo-10) + tarifa.at[1,"Valor do Esgoto"]*(consumo-10) + (consumo_10-0.03)
consumo_30 = tarifa.at[2,'Valor da Agua']*(consumo-20) + tarifa.at[2,"Valor do Esgoto"]*(consumo-20) + 134.80
consumo_50 = tarifa.at[3,'Valor da Agua']*(consumo-50) + tarifa.at[3,"Valor do Esgoto"]*(consumo-50) + 493.30 +0.11

consumo10 = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
         '':['','','',''],
         'Total':[56.30, 0, 0,0]}
consumo10d = pd.DataFrame(data=consumo10)
tarifa10 = pd.merge(tarifa,consumo10d)

consumo20 = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
         '':['','','',''],
         'Total':[56.30, consumo_20-56.30, 0,0]}
consumo20d = pd.DataFrame(data=consumo20)
tarifa20 = pd.merge(tarifa,consumo20d)

consumo30 = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
         '':['','','',''],
         'Total':[56.30, 134.77, consumo_30-191.10,0]}
consumo30d = pd.DataFrame(data=consumo30)
tarifa30 = pd.merge(tarifa,consumo30d)

consumo50 = {'Faixa de Consumo': ['Consumo 00 à 10','Consumo 11 à 20','Consumo 21 à 50','Consumo acima 50' ],
         '':['','','',''],
         'Total':[56.30, 134.77, 493.30,consumo_50-684.37]}
consumo50d = pd.DataFrame(data=consumo50)
tarifa50 = pd.merge(tarifa,consumo50d)

print()
print(f'Nos últimos {(n_dias.dias)} dias, o consumo foi de {(n_leitura.leitura)} m³.')
print()
print(f'O consumo por dia foi: {(n_leitura.leitura/n_dias.dias)} m³/dia')
print()
print(f'A projeção de consumo para os próximos 30 dias é de: {(consumo_mes)} m³.')
print()

#mostra Valor conta
if consumo <= 10:
    print(f'Valor Estimado para os próximos 30 dias é de R$ {consumo_10:.2f}')
    print()
    print(tarifa10)
elif 20>=consumo>10:
    print(f'Valor Estimado para os próximos 30 dias é de R$ {consumo_20:.2f}')
    print()
    print(tarifa20)
elif 50>=consumo>20:
    print(f'Valor Estimado para os próximos 30 dias é de R$ {consumo_30:.2f}')
    print()
    print(tarifa30)
else:
    print(f'Valor Estimado para os próximos 30 dias é de R$ {consumo_50:.2f}')
    print()
    print(tarifa50)
