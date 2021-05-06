from flask import Flask, render_template, abort
import json
app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def inicio():
    with open("books.json") as libros:
        lista=json.load(libros)
  
    return render_template("index.html",lista=lista)

@app.route('/libro/<isbn>')
def libro(isbn):
    with open("books.json") as libros:
        todos_isbn=[]
        lista=json.load(libros)
        for i in lista:
            isbn_libro=i.get("isbn")
            todos_isbn.append(isbn_libro)
        if isbn not in todos_isbn:
            abort(404)
        
        
    return render_template("hola.html",lista=lista,isbn=isbn)

app.run(debug=True)
