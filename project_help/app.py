# TODO Fill the package and the functions

from _ import _, _, _, _, _

app = _(__name__)

# List to store tasks
tasks = []

@app.route('/')
def home():
    # TODO Fill the file name with extension
    template_name = _
    return _(template_name, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = _.form['task']
    tasks.append(task)
    return _(_('home'))

if __name__ == '__main__':
    app.run(debug=True)