#BARNAME FOROSHGAH MAHSOL
"""5---> vaghty k taraf nvsht yes kochik bozorg faslee --> ag
javabesh yes bood (takmil tarin halat) , mahsol ro az taraf begire 
yek listi dahste bashid bename
products --> b tahe in list ezafe konidesh

yes --> esme mahsolo bego -> esme mahsolo minevise--> berizid tahe yek list (products)"""

shop = input("salam aya mikhahid kahrid konid?")
a = shop.lower()
b = a.strip()
products = []
if b == "yes":
    name = input('esm mahsool ra vared konid : ')
    products.append(name)
elif b == "no": 
    print("mamnoon")
else:
    print("fght ba yes o no javab bedahid")
