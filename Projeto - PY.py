import math
import random
import statistics
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def converter_CDI_anual(taxa_anual):
    return (1 + taxa_anual) ** (1/12) - 1


def calcular_total_investido(capital, aporte, meses):
    return capital + (aporte * meses)


def calcular_cdb(capital, aporte, meses, percentual_cdb):

    cdi_mensal = converter_CDI_anual(cdi_anual)
    
    taxa = cdi_mensal * percentual_cdb

    montante = capital * (1 + taxa) ** meses
    montante += aporte * (((1 + taxa) ** meses - 1) / taxa)

    total = calcular_total_investido(capital, aporte, meses)
    lucro = montante - total

    dias = meses * 30

    if dias <= 180:
        ir = 0.225
    elif dias <= 360:
        ir = 0.20
    elif dias <= 720:
        ir = 0.175
    else:
        ir = 0.15

    imposto = lucro * ir

    return montante - imposto


def calcular_lci(capital, aporte, meses, cdi_mensal, percentual_lci):

    taxa = cdi_mensal * percentual_lci

    montante = capital * (1 + taxa) ** meses
    montante += aporte * (((1 + taxa) ** meses - 1) / taxa)

    return montante


def calcular_poupanca(capital, aporte, meses):

    taxa = 0.005

    montante = capital * (1 + taxa) ** meses
    montante += aporte * (((1 + taxa) ** meses - 1) / taxa)

    return montante


def calcular_fii(capital, aporte, meses, taxa_fii):

    base = capital * (1 + taxa_fii) ** meses + aporte * (((1 + taxa_fii) ** meses - 1) / taxa_fii)

    v1 = base * (1 + random.uniform(-0.03, 0.03))
    v2 = base * (1 + random.uniform(-0.03, 0.03))
    v3 = base * (1 + random.uniform(-0.03, 0.03))
    v4 = base * (1 + random.uniform(-0.03, 0.03))
    v5 = base * (1 + random.uniform(-0.03, 0.03))

    media = statistics.mean((v1, v2, v3, v4, v5))
    mediana = statistics.median((v1, v2, v3, v4, v5))
    desvio = statistics.stdev((v1, v2, v3, v4, v5))

    return media, mediana, desvio


def calcular_datas(meses):
    hoje = datetime.date.today()
    resgate = hoje + datetime.timedelta(days=meses * 30)
    return hoje, resgate


def formatar(valor):
    return locale.currency(valor, grouping=True)


def validar(capital, aporte, meses):

    if capital <= 0:
        print("Erro: capital inválido")
        return False

    elif aporte < 0:
        print("Erro: aporte inválido")
        return False

    elif meses <= 0:
        print("Erro: prazo inválido")
        return False

    else:
        return True


def barra(valor, maior):
    tamanho = int((valor / maior) * 50)
    return "█" * tamanho


def melhor(cdb, lci, poup, fii):

    if cdb >= lci and cdb >= poup and cdb >= fii:
        return "CDB"
    elif lci >= cdb and lci >= poup and lci >= fii:
        return "LCI/LCA"
    elif poup >= cdb and poup >= lci and poup >= fii:
        return "Poupança"
    else:
        return "FII"



capital = float(input("Capital inicial (R$): "))
aporte = float(input("Aporte mensal (R$): "))
meses = int(input("Prazo(meses): "))
cdi_anual = float(input("CDI anual (%): ")) / 100
perc_cdb = float(input("Percentual CDI no CDB(%): ")) / 100
perc_lci = float(input(" Percentual CDI na LCI (%): ")) / 100
taxa_fii = float(input(" Rentabilidade mensal esperada do FII (%): ")) / 100
meta = float(input("Meta financeira desejada (R$): "))

