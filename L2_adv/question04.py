#BARNAME FOROSHGAH MAHSOL
"""4----> hamin mesale foroshgah fanavari (User side) --> yek moshkel dare

do ta moshkel
moshkel ro hal konid

4.1--> yes --> Yes --> javab
4.2--> fasele yes --> javabe gahalt
"""

shop = input("salam aya mikhahid kahrid konid?")
a = shop.lower()
b = a.strip()
if b == "yes":
    print("yaddasht mikonam!") 
elif b == "no": 
    print("mamnoon")
else:
    print("fght ba yes o no javab bedahid")
