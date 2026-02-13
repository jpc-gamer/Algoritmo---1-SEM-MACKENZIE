print(
    f"""
Cliente: {input("Nome do cliente: ")}
CPF: {input("CPF: ")}
Produto: {input("Produto: ")}
Qnts.: {input("Quantidade: ")}
Preço: {float(input("Preço: "))}
Confirme o valor total para recibo.: {input("Quantidade: ")}
""" )
print(f"""
===========================================
{"LOJA PYTHON S.A.":^43}
{"Rua dos Códigos, 101":^43}
===========================================
""")
print ( f"""
CLIENTE: {input("Cliente: ")}
CPF:     {input("CPF):    ")}

-------------------------------------------
ITEM              QTD        PREÇO
{input("Item: "):.<18} {input("Qtd: "):<10} R$ {input("Preço: ")}

-------------------------------------------
SUBTOTAL:                 R$ {input("Subtotal: ")}
IMPOSTO (10%):             R$ calc...
===========================================
        OBRIGADO PELA PREFERÊNCIA!
===========================================

        """
)




    
