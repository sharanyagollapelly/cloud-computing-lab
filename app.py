from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>Hello!! RGUKT</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)











# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# def home():
#    <html>
#    <body>
#    <h1>Hello!! RGUKT</h1>
#    </body>
#    </html>
#    return "flask application running successfully"
# if __name__ == "__main__":
#     app.run(debug=True)
