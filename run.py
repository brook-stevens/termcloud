import io
import os
from flask import Flask, send_file, request
import termcloud
import datetime

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/termcloud", methods=['POST'])
def posttermcloud():
    text = request.form['source-text']
    height = int(request.form['height'])
    width = int(request.form['width'])
    no_lemmatization_str = request.form['no_lemmatization']
    if no_lemmatization_str != "":
        no_lemmatization = no_lemmatization_str.split()
    else:
        no_lemmatization = []
    font = request.form['font']
    if(font.lower() == "lato"):
        font_path = "fonts/lato-v14-latin-regular.ttf"

    image = termcloud.generate(text=text,
                               height=height,
                               width=width,
                               no_lemmatization=no_lemmatization,
                               font_path=font_path)
    output = io.BytesIO()
    image.save(output, format='PNG')

    return send_file(
        io.BytesIO(output.getvalue()),
        attachment_filename="termcloud.png",
        last_modified=datetime.datetime.now(),
        cache_timeout=-1,
        mimetype='image/png'
    )


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)