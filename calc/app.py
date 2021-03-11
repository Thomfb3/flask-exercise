# Put your app in here.
from flask import Flask, request, redirect
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <html>
        <body>
            <h1>Do some Math</h1>
            <form method="POST">
                <select name="operation" >
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select>
                
                <input type='number' placeholder='a' name='a' />
                <input type='number' placeholder='b' name='b' />
                <button>Submit</button>
            </form>
        </body>
    </html>
    """
    return html


@app.route('/', methods=["POST"])
def go_to_math():
    operation = request.form["operation"]
    a = request.form["a"]
    b = request.form["b"]
    return redirect(f'/math/{operation}/a={a}&b={b}')



@app.route('/math/<operation>/a=<a>&b=<b>')
def do_math(operation, a, b):
    a = int(a)
    b = int(b)

    if operation == "add":
        return f"{add(a,b)}"
    elif operation == "subtract":
        return f"{sub(a,b)}"
    elif operation == "multiply":
        return f"{mult(a,b)}"
    elif operation == "divide":
        return f"{div(a,b)}"

