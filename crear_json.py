import json

C_user = input("c_user: ")
XS = input("xs: ")
cookies = {"c_user": C_user,
           "xs": XS}

lista_cookies = []

for nombre, valor in cookies.items():
    lista_cookies.append({
        "name": nombre,
        "value": str(valor),
        "domain": ".facebook.com",
        "path": "/"
    })

nombre = input("escribe nombre que le pondras al archivo: ")

with open(nombre, "w", encoding="utf-8") as archivo:
    json.dump(lista_cookies, archivo, indent=4)
