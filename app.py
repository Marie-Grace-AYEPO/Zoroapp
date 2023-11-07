from flask import Flask, render_template, url_for, flash, request, redirect
import pyodbc as odbc


DSN = 'Driver={SQL Server};Server=DESKTOP-DU03FQL\\SQLEXPRESS;Database=Gestion_des_Magasins;'
conn = odbc.connect(DSN)
cursor = conn.cursor()
# uid = <username>;
# pwd = <password>; 


app = Flask(__name__)
app.config['SECRET_KEY']='clés_flash'

@app.route("/")
def Connexion():
    return render_template("Connexion.html")


@app.route("/Accueil")
def Accueil():
    return render_template("Accueil.html")


if __name__ == "__main__":
    app.run(debug=True)