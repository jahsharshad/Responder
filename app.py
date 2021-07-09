from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        # new_task = Todo(content=task_content)

        print("You posted")

        try:
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        return render_template('index.html')
