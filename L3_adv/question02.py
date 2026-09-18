'''a)adade farde byene 30 ta 50 ro print konid
b)adade farde beyne 30 ta 7000 ro beshmorid, begid chantas (print kone y adad -->beeg chanta)
c)adade zoje beyne 60 ta 120 ro joda konid tooye yek list bename zoj_list'''

tedad_f = 0
zoj_list = []
print("a:")
for i in range(30, 50):
    if i%2 != 0:
        print(i)
print("b:")
for h in range(30, 7000):
    if h%2 !=0:
        tedad_f = tedad_f+1
print("adad fard", tedad_f)
print("c:")
for k in range(60, 120):
    if k%2 == 0:
        zoj_list.append(k)
print("zojlist",zoj_list)
        
