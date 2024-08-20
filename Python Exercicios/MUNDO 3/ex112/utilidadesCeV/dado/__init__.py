def leiavalor(frase):
    num = input(frase).replace(',','.').replace(' ','')
    while not numerico(num):
        print(f'ERRO! "{num}" é um valor inválido.')
        num = input(frase)
    return float(num)


def numerico(string):
    c=0
    for i in string:
        if i not in '1234567890':
            c+=1
        if i in "abcdefghijklmnopqrstuvwxyz;/~´[]-=+º°ª§¬£³²¹/?}{/'!@#$%¨&*()^ ":
            c+=2
        if string[0] in ".," or string[len(string)-1] in ".,":
            c+=2
    if string=='':
        c+=2
    if c>1:
        return False
    else:
        return True
        