#BARNAME FOROSHGAH MAHSOL
'''3 --> yek foroshgah baraye moshtari ebsazi (customer side)
begid salam aya mikhahid kharid konid? age gof yes --> yad dahst mikonm,, 
no -> mamnoon, ag harchi dg -> fght ba yes o no javab bedahid'''

shop = input("salam aya mikhahid kahrid konid?")
if shop == "yes" or shop == "YES":
    print("yaddasht mikonam!") 
elif shop == "no" or shop == "NO": 
    print("mamnoon")
else:
    print("fght ba yes o no javab bedahid")
