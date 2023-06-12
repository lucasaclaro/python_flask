from flask import Flask, render_template

# criação do site
app = Flask(__name__)

# criação da 1ª página. Toda página tem route (qual link vai abrir qual página. Nome após o nome do domínio) e função (conteúdo)

@app.route("/") # a / representa a homepage. Caso fosse outra página, seria o nome dela
def homepage():
    return render_template('index.html')




# site no ar
if __name__ == '__main__':
    app.run(debug=True) #todas as edições serão exibidas de forma automática