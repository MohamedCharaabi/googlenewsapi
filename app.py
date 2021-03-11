from flask import Flask, jsonify, request, render_template
from GoogleNews import GoogleNews



app = Flask(__name__)
app.static_folder = 'static'


@app.route('/search/<string:key>', methods=['GET'])
def news(key):
    googlenews = GoogleNews(lang='fr', period='7d')


    googlenews.search(key)

    results = googlenews.results()


    return jsonify(results)






if __name__ == '__main__':

    app.run(debug=True)