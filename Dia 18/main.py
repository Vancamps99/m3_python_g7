from  get import obtener_lista_pajaros 
from template import html_template,aves_template

lista_aves=obtener_lista_pajaros()
def lista_a_mostrar():
    lista_vacia=''#
    for ave in lista_aves:
        aves_info=aves_template.substitute(nom_esp=ave["name"]["spanish"],nom_ing=ave["name"]["english"] ,img=ave["images"]["main"])
        lista_vacia+=aves_info #pasar info procesada #+= añade hasta el 205
    html=html_template.substitute(body=lista_vacia)
    with open('aves.html','w', encoding='utf-8' ) as f: #Encoding para mostrar caracteres especiales
        f.write(html)

lista_a_mostrar()
        
#Disculpe profe si ve esto. aún me cuesta . voy a tratar de ejercitar .