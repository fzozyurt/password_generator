from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
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
        return render_template_string(template, password=password)

    return render_template_string(template)

template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Password Generator</title>
  </head>
  <body>
    <h1>Password Generator</h1>
    <form method="post">
      <label for="length">Password Length:</label>
      <input type="number" id="length" name="length" min="1" required><br><br>
      <input type="checkbox" id="uppercase" name="uppercase">
      <label for="uppercase">Include Uppercase Letters</label><br>
      <input type="checkbox" id="lowercase" name="lowercase">
      <label for="lowercase">Include Lowercase Letters</label><br>
      <input type="checkbox" id="digits" name="digits">
      <label for="digits">Include Digits</label><br>
      <input type="checkbox" id="special" name="special">
      <label for="special">Include Special Characters</label><br><br>
      <input type="submit" value="Generate Password">
    </form>
    {% if password %}
    <h2>Your Generated Password:</h2>
    <p>{{ password }}</p>
    {% endif %}
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)