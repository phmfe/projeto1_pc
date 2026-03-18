import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = float(input('Prazo(meses)'))
cdi_anual = float(input('CDI anual (%): '))/100
perc_cdb = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('Rentabilidade do FII (%):'))/100
meta = float(input('Meta financeira (R$): '))

#conversao XDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1
#total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb),meses))+(aporte * meses)
lucro_cdb = montante_cdb - total_investido 
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI/LCI
taxa_lci =  cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#poupaça 
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses))
+(aporte*meses)

# FII
valor_fii_base = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * (math.pow((1 + taxa_fii), meses) - 1) / taxa_fii)

s1 = valor_fii_base * (1 + random.uniform(-0.03, 0.03))
s2 = valor_fii_base * (1 + random.uniform(-0.03, 0.03))
s3 = valor_fii_base * (1 + random.uniform(-0.03, 0.03))
s4 = valor_fii_base * (1 + random.uniform(-0.03, 0.03))
s5 = valor_fii_base * (1 + random.uniform(-0.03, 0.03))

lista_fii = [s1, s2, s3, s4, s5]
media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)

# Data de resgate
data_atual = datetime.datetime.now()
data_resgate = data_atual + datetime.timedelta(days=meses * 30)

# Saída
barra_cdb = "█" * int(montante_cdb_liquido / 1000)
barra_lci = "█" * int(montante_lci / 1000)
barra_poup = "█" * int(montante_poupanca / 1000)
barra_fii = "█" * int(media_fii / 1000)

# Print final
print("-" * 30)
print("Data de Resgate:", data_resgate.strftime('%d/%m/%Y'))
print("Total Investido:", locale.currency(total_investido, grouping=True))
print("-" * 30)

print(f"CDB Líquido: {locale.currency(montante_cdb_liquido, grouping=True)}")
print(f"Grafico: {barra_cdb}")

print(f"\nLCI/LCA: {locale.currency(montante_lci, grouping=True)}")
print(f"Grafico: {barra_lci}")

print(f"\nPoupança: {locale.currency(montante_poupanca, grouping=True)}")
print(f"Grafico: {barra_poup}")

print(f"\nFII Média: {locale.currency(media_fii, grouping=True)}")
print(f"Grafico: {barra_fii}")

print("-" * 30)
print("FII Mediana:", locale.currency(mediana_fii, grouping=True))
print("FII Desvio Padrão:", locale.currency(desvio_fii, grouping=True))

if media_fii >= meta:
    print("Meta alcançada!")
else:
    print("Meta não alcançada.")

