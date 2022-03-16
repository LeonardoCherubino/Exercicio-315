#Calcular tempo de vida de um fumante

tempo_fumando = int(input('Você fuma há quantos anos? '))
dias_fumando = tempo_fumando * 365
print('Você já fumou por {} dias'.format(dias_fumando))
quantidade_de_cigarros_dia = int(input('Quantos cigarros por dia? '))
print('A cada cigarro que você fuma você perde 10 minutos da sua vida. ')
quantidade_de_cigarros_ano = quantidade_de_cigarros_dia * 365
print('Você fuma por ano {} cigarros'.format(quantidade_de_cigarros_ano))
tempo_perdido_em_minutos_por_ano = quantidade_de_cigarros_ano * 10
print('Em um ano você perdeu {} minutos da sua vida por causa do cigarro'.format(tempo_perdido_em_minutos_por_ano))
a = tempo_perdido_em_minutos_por_ano / 60
print('O que equivalem a {} horas'.format(a))
b = a / 24
print('O que equivalem a {} dias'.format(b))
#dias_perdidos_em_um_ano = tempo_perdido_em_minutos_por_ano / 365
#print('Por ano você perde {} dias da sua vida'.format(dias_perdidos_em_um_ano))
#anos_perdidos_de_vida = dias_perdidos_em_um_ano * tempo_fumando
#print('Você já perdeu {} anos da sua vida com o cigarro'.format(anos_perdidos_de_vida))

#rint('Você fuma por ano')
#quantidade_cigarros_ano = tempo_fumando * quantidade_de_cigarros



#tempo_de_vida = quantidade_de_cigarros * 10
#print('Você já perdeu {} minutos da sua vida'.format(tempo_de_vida))