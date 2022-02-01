categoria  = int(input(" digite a categoria do produto:"))
if categoria ==1:
    preço = 20
elif categoria ==2:
        preço = 22
        
elif categoria == 3:
        preço = 45
        
elif categoria ==4:
        preço = 57
else:  
    print("categoria do invalida, digite  um valor entre 1.4!")
    preço = 0
print("o preço do pruduto é : R$8.2f" % preço)            


