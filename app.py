from flask import Flask, request, render_template, jsonify
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            length = data.get('length')
            if length is None:
                return jsonify(error="Length is required"), 400
            length = int(length)
            use_uppercase = data.get('uppercase', False)
            use_lowercase = data.get('lowercase', False)
            use_digits = data.get('digits', False)
            use_special = data.get('special', False)
        else:
            length = request.form.get('length')
            if not length:
                return "Length is required", 400
            length = int(length)
            use_uppercase = 'uppercase' in request.form
            use_lowercase = 'lowercase' in request.form
            use_digits = 'digits' in request.form
            use_special = 'special' in request.form

        characters = ''
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            return "Please select at least one character set."

        password = ''.join(random.choice(characters) for _ in range(length))

        if request.is_json:
            return jsonify(password=password)
        else:
            return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)