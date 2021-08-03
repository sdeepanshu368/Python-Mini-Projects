from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
     return 'Hello, World!'


@app.route('/arm/<int:num>')
def armn(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
        # return "True"
        result = {
            "Number": num,
            "Armstrong": True,
            "Server IP": "127.0.0.1.0",
            "ListOfNumbers": [0, 1, 153, 5885]
        }
    else:
        print(num, "is not an Armstrong number")
        # return "False"
        result = {
            "Number": num,
            "Armstrong": False,
            "Server IP": "127.0.0.1.0",
            "ListOfNumbers": [0, 1, 153, 5885]
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
