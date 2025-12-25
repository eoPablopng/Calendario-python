def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_no_mes(ano, mes):
    if mes < 1 or mes > 12:
        return None  
    
    dias_por_mes = [31, 29 if eh_bissexto(ano) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]

def dia_do_ano(ano, mes, dia):
    if mes < 1 or mes > 12:
        return None  
    
    dias_no_mes_atual = dias_no_mes(ano, mes)
    if dia < 1 or dia > dias_no_mes_atual:
        return None  
    
    return sum(dias_no_mes(ano, m) for m in range(1, mes)) + dia


testes = [
    (2020, 1, 1, 1),  
    (2020, 12, 31, 366),  
    (2021, 12, 31, 365),  
    (2020, 2, 29, 60),  
    (2021, 2, 29, None),  
    (2023, 4, 15, 105),  
    (2023, 7, 31, 212),  
    (2023, 13, 1, None), 
    (2023, 0, 10, None),  
    (2023, 6, 0, None),  
    (2023, 6, 31, None)  
]


erro = False
for ano, mes, dia, esperado in testes:
    resultado = dia_do_ano(ano, mes, dia)
    if resultado != esperado:
        print(f"Erro: Ano {ano}, Mês {mes}, Dia {dia} - esperado {esperado}, obtido {resultado}")
        erro = True

if not erro:
    print("Todos os testes passaram!")
