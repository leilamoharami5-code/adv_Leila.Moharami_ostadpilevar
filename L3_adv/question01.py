#سوال ۱ — Password

#Az user password begirid va faghat dar sorati be user begid:

'''ba movafaghiat sabt shod'''

#ke password shoroot ra dashte bashe:

'''andazash bishtar az 8 bashe
hatman tarkibi az adad va horof bashe
hatman tarkibi az horofe bozorg va kochak bashe'''

num = 0
up = 0
low = 0
pass_word = input('enter your password : ')
for i in pass_word:
    if i.isupper():
        up = up+1
    if i.islower():
        low = low+1
    if i.isdigit():
        num = num+1
if len(pass_word)>0 and num>0 and up>0 and low>0:
    print("ba movafaghiat sabt shod")
else:
    raise ValueError("password is invalid")