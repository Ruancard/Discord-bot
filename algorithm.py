from urllib.request import urlopen
from bs4 import BeautifulSoup
from unidecode import unidecode
import discord

def __obthtml__(nome):
    url = (f'https://soundcloud.com/search?q={nome}')
    response = urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def __caminho__(soup):
    search = soup.find('div', id = 'app')
    search = search.find_all('ul')
    if len(search) > 1 :
        search = search[1].find_all('li')
        return search
    else:
        print('error [nothing found]')
        __main__()

def __obturl__(search):
    links = {}
    num = 1
    for l in search:
        l = l.find('h2')
        l = l.find('a')
        l = l['href']
        l =  'https://soundcloud.com/' + l
        links[num] = l
        num += 1
    return links

def __obtnomes__(search, links):
    lista  = (1,2,3,4,5,6,7,8,9,10)
    num = 1
    for n in search:   
        n = n.find('h2')
        n = n.find('a')
        n = n.get_text()
        print(f'{num}  =  {n}')
        num += 1 
    change = int(input('change a opcion: '))
    if change in lista:
        musica = links[change]
        return musica
    else:
        print('type a valid number')
        __obtnomes__(search)

def __change__():
    opc = int(input('0 = break\n1 = continue\n'))
    if opc == 0:
        print('Bye')
    elif opc == 1:
        __main__()
    else:
        print('type a valid number')
        __change__()

def __main__():
    nome = __pesquisar__()
    nome = nome.replace (" ", "-")
    nome = (unidecode(nome))
    soup = __obthtml__(nome)
    search = __caminho__(soup)
    links = __obturl__(search)
    musica = __obtnomes__(search,links)
    print(musica)
    __change__()


def __pesquisar__():
    nome = input('type the name of music:')
    return nome

__main__()