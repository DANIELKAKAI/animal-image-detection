from flask import Flask, render_template, request
from use_model import get_animal

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        image_url = request.form.get('image-url')
        image_file = request.files.get('image-file')
        if image_url:
            result = get_animal(image_url)
        if image_file:
            result = get_animal(image_file.read())
        return render_template('index.html', result=result, image_url=image_url)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
