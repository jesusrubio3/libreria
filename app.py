from flask import Flask, render_template, abort
app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def inicio():
    f=open("books.json")
    lista=f.read()
    f.close()

    return render_template("index.html",lista=lista)

app.run(debug=True)