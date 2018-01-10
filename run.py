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
def simple():
    text = request.form['source-text']
    image = termcloud.generate(text=text, font_path="fonts/lato-v14-latin-regular.ttf")
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