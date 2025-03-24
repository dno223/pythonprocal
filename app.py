from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate(num1, num2, operation):
    try:
        num1, num2 = float(num1), float(num2)
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return "Error! Division by zero." if num2 == 0 else num1 / num2
    except ValueError:
        return "Invalid input!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_api():
    data = request.json  # Get JSON data from frontend
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")
    result = calculate(num1, num2, operation)
    return jsonify({"result": result})  # Return JSON response

if __name__ == "__main__":
    app.run(debug=True)
