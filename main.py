from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    Esta función captura TODAS las solicitudes y las redirige
    permanentemente (código 301) a https://www.macal.cl/
    """
    return redirect("https://www.macal.cl/", code=301)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))