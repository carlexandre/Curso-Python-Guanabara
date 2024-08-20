import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('O site pudim não está funcionando no momento.')
else:
    print('O site pudim está livre para ser acessado.')