from flask import Flask, render_template, abort
import json
app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def inicio():
    with open("books.json") as libros:
        lista=json.load(libros)
  
    return render_template("index.html",lista=lista)

app.run(debug=True)
