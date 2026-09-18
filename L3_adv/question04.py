'''4--> while
oon masaleye foroshgah k miporsid aya mahsoli mikhahid?

agar goft yes --> begid befarmaeeid 
agar goft no --> begid besiar awli

agar harchize dige goft (n yes , na no) --> aval begid bayad ba yeso no javab bdi
mojadad -> aya mahsoli mikhahid?

va inkar ro onghdr anjam bdid ta benevise yes ya no

ta zamani k yes ya no nanevehst --> (ba yes o no javab bede) mahsol mikhahi?

'''


while True:
    question = input('aya mahsooli mikhahid?')
    if question == 'yes' or question == 'YES':
        print('welcome')
        break
    elif question == 'NO' or question == 'no':
        print('besiar awli')
        break
    else:
        print('faghat ba yes/no javab bedahid.')
