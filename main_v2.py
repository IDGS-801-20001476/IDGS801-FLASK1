
from flask import Flask

app=Flask (__name__)
#ruta base
@app.route("/")
def index():
    return "Hola mundo Flask cambios nuevos"

#crear una ruta
#ejemplo 1
@app.route("/hola")
def hola():
    return "Hola desde hola"

#ejemplo 2
@app.route("/nueva")
def nueva():
    return "Hola desde Nueva"

if __name__=="__main__":
    app.run(debug=True,port=3000)


