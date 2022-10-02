from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    This represents the Englsh to French Translation Route
    """

    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    This represents the French to English Route
    """

    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    """
    This renders the file index.html
    """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
