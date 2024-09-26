from flask import Flask, request, render_template, redirect, flash, url_for, abort
                # application WSGI

# (interface de serveur web python)
# comportements et méthodes d'un serveur web


app = Flask(__name__)    # instance de classe Flask (en paramètre le nom du module)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!<a href="hello">lien hello</a>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    app.config["TEMPLATES_AUTO_RELOAD"] = True