local_carro = 100
velocidade = 50


radar_1 = 60
local_1 = 100
radar_range = 1

condicao_carro_multado_1 =local_carro >=(local_1 - radar_1)
condicao_carro_multado_2 =local_carro <=(local_1 + radar_1)
condicao_carro_multado_3 = velocidade > radar_1

vel_carro_passar_radar_1 = velocidade > radar_1
carro_multado_radar_1 = condicao_carro_multado_1 and condicao_carro_multado_2 and condicao_carro_multado_3


if vel_carro_passar_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
