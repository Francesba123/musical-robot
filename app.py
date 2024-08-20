from flask import Flask, render_template_string

app = Flask(__name__)

# Inicializar contador de visitantes
visitor_count = 0

@app.route('/')
def home():
    global visitor_count
    visitor_count += 1
    return render_template_string('''
        <html>
            <head>
                <title>Contador de Visitantes</title>
            </head>
            <body>
                <h1>Bem-vindo ao meu site!</h1>
                <p>Número de visitantes: {{ count }}</p>
            </body>
        </html>
    ''', count=visitor_count)

if __name__ == '__main__':
    app.run(debug=True)