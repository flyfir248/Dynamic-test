from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define a list of user objects (for demonstration purposes only)
users = [
  {'id': 1, 'username': 'Alice'},
  {'id': 2, 'username': 'Bob'},
  {'id': 3, 'username': 'Charlie'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    # Create a new user with the given username and add it to the list of users
    user_id = len(users) + 1
    new_user = {'id': user_id, 'username': username}
    users.append(new_user)
    # Redirect the user back to the index page
    return redirect('/')

@app.route('/users/delete', methods=['POST'])
def delete_user():
    user_id = int(request.form['user_id'])
    # Find the user with the given ID and remove it from the list of users
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            break
    # Redirect the user back to the index page
    return redirect('/')

if __name__ == '__main__':
    app.run()