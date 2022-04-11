from flask import Flask, request, redirect, url_for, jsonify, send_file, make_response, render_template

no_device = ("noDevice.png", "No devices found", "Hm.. it doesn't look like you have anything plugged in", "noDevice")
lamp = ("lamp.png", "Lamp", "A lamp is on in the house", "")
fridge = ("fridge.png", "Fridge", "This is a fridge", "")
hairdryer = ("hairdryer.png", "Hairdryer", "Time to style your harir", "")
television = ("tv.png", "TV", "A tv is on", "")
coffee = ("coffeemachine.png", "Coffee Machine", "A coffee machine is on and brewing coffee", "")




app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

fields = ("img", "device", "info")
data = (
    ("coffeemachine.png", "Coffee Machine",
     "A coffee machine is on and brewing coffee"),
    ("tv.png", "TV", "A tv is on"),
    ("lamp.png", "Lamp", "A lamp is on in the house")
)

data2 = '22'

@app.route('/getData', methods=['GET', 'POST'])
def get_data():
    print(request.headers)
    reqData = request.get_json()
    print(reqData)
    # data2.append(reqData['value'])
    global data2
    data2 = reqData['value']
    print("NEw data2: " + str(data2))
    return "got data"

#     noise 1
# 'lamp' 2
# 'fridge' 3
# 'hairdryer' 4
# 'television' 5
# 'coffee' 6
# 'fridge', 'lamp' 7
# 'hairdryer', 'lamp' 8
# 'lamp', 'television' 9
# 'coffee', 'lamp' 10
# 'fridge', 'hairdryer' 11
# 'fridge', 'television' 12
# 'coffee', 'fridge' 13
# 'hairdryer', 'television' 14
# 'coffee', 'hairdryer' 15
# 'coffee', 'television' 16
# 'fridge', 'hairdryer', 'lamp' 17
# 'fridge', 'lamp', 'television' 18
# 'coffee', 'fridge', 'lamp' 19
# 'hairdryer', 'lamp', 'television' 20
# 'coffee', 'hairdryer', 'lamp' 21
# 'coffee', 'lamp', 'television' 22
# 'fridge', 'hairdryer', 'television' 23
# 'coffee', 'fridge', 'hairdryer' 24
# 'coffee', 'fridge', 'television' 25
# 'coffee', 'hairdryer', 'television' 26
# 'fridge', 'hairdryer', 'lamp', 'television' 27
# 'coffee', 'fridge', 'hairdryer', 'lamp' 28
# 'coffee', 'fridge', 'lamp', 'television' 29
# 'coffee', 'hairdryer', 'lamp', 'television' 30
# 'coffee', 'fridge', 'hairdryer', 'television' 31
# 'coffee', 'fridge', 'hairdryer', 'lamp', 'television' 32


def convert_num_to_devices(num):
    if num == '0':
        return (no_device, )
    elif num == '1':
        return (no_device, )
    elif num == '2':
        # lamp
        data = (lamp,)
        return data
    elif num == '3':
        # fridge
        data = (fridge,)
        return data
        return "fridge"
    elif num == '4':
        # hairdryer
        data = (hairdryer,)
        return data
    elif num == '5':
        data = (television,)
        return data
    elif num == '6':
        data = (coffee,)
        return data
    elif num == '7':
        data = (fridge, lamp)
        return data
    elif num == '8':
        data = (hairdryer, lamp)
        return data
    elif num == '9':
        data = (lamp, television)
        return data
    elif num == '10':
        data = (coffee, lamp)
        return data
    elif num == '11':
        data = (fridge, hairdryer)
        return data
    elif num == '12':
        data = (fridge, television)
        return data
    elif num == '13':
        data = (coffee, fridge)
        return data
    elif num == '14':
        data = (hairdryer, television)
        return data
    elif num == '15':
        data = (coffee, hairdryer)
        return data
    elif num == '16':
        data = (coffee, television)
        return data
    elif num == '17':
        data = (fridge, hairdryer, lamp)
        return data
    elif num == '18':
        data = (fridge, lamp, television)
        return data
    elif num == '19':
        data = (coffee, fridge, lamp)
        return data
    elif num == '20':
        data = (hairdryer, lamp, television)
        return data
    elif num == '21':
        data = (coffee, hairdryer, lamp)
        return data
    elif num == '22':
        data = (coffee, lamp, television)
        return data
    elif num == '23':
        data = (fridge, hairdryer, television)
        return data
    elif num == '24':
        data = (coffee, fridge, hairdryer)
        return data
    elif num == '25':
        data = (coffee, fridge, television)
        return data
    elif num == '26':
        data = (coffee, hairdryer, television)
        return data
    elif num == '27':
        data = (fridge, hairdryer, lamp, television)
        return data
    elif num == '28':
        data = (coffee, fridge, hairdryer, lamp)
        return data
    elif num == '29':
        data = (coffee, fridge, lamp, television)
        return data
    elif num == '30':
        data = (coffee, hairdryer, lamp, television)
        return data
    elif num == '31':
        data = (coffee, fridge, hairdryer, television)
        return data
    elif num == '32':
        data = (coffee, fridge, hairdryer, lamp, television)
        return data
    else:
        return "not sure"


@app.route('/updateData', methods=['GET', 'POST'])
def update_data():
    print("Data 2 is " + data2)
    data2_json = {"value": data2}
    # index()
    return data2_json


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        print(data2)
        data = convert_num_to_devices(data2)
        # print("Data is " + data[0][1])
        return render_template('index.html',  fields=fields, data=data, data2=data2)
    except Exception as e:
        print("error: " + str(e))
        return str(e)


if __name__ == '__main__':
    print('running flask')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8010, debug=True)
