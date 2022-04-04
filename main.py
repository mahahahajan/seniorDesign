from flask import Flask, request, jsonify, send_file, make_response, render_template


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

fields = ("img", "device", "info")
data = (
    ("coffeemachine.png", "Coffee Machine", "A coffee machine is on and brewing coffee"),
    ("tv.png", "TV", "A tv is on"),
    ("lamp.png", "Lamp", "A lamp is on in the house")
)



@app.route('/')
def index():
    try:
        return render_template('index.html',  fields=fields, data=data)
    except Exception as e:
        print("error: " + str(e))
        return str(e)


if __name__ == '__main__':
    print('running flask')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(threaded=True, port=8010)
