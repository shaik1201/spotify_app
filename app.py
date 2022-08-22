from flask import Flask, render_template, request
from package import birdy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/birdy',methods=['POST','GET'])
def artist():
    artist_name = request.form.get('birdy')
    if artist_name == 'birdy':
        albums_names = birdy.birdy_albums()
        return render_template('birdy.html', albums=albums_names)
    
    else:
        return '<h1> Artist not found </h1>'


if __name__ == '__main__':
    # app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')
    app.run(debug=True)