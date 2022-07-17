from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import user

# Visible Routes
@app.route('/')
def index():
    users = user.User.get_all_users()
    print(users)
    return render_template('read_all_users.html', all_users = users)

@app.route('/users')
def redirect_users():
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/users/<int:id>/')
def view_user(id):
    data = {
        "id": id
    }
    return render_template('read_one_user.html', id=id, one_user = user.User.get_one_user(data))




@app.route('/users/<int:id>/edit')
def edit_page(id):
    data = {
        "id": id
    }
    one_user = user.User.get_one_user(data)
    return render_template('edit_user.html', id=id, one_user=one_user)


# Hidden Routes
@app.route('/process_user_form', methods=['POST'])
def process_user_form():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    id = user.User.save_user(data)
    return redirect(f'/users/{id}')


@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        "id": id
    }
    user.User.delete_one_user(data)
    return redirect('/')


@app.route('/clear')
def clear():
    user.User.clear_users()
    user.User.reset_ids()
    return redirect('/')


@app.route('/users/<int:id>/process_edit_user', methods=['POST'])
def process_edit_user(id):
    data = {
        "id": id,
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    user.User.edit_user(data)
    return redirect(f'/users/{id}')