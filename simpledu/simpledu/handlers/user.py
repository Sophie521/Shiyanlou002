from flask import Blueprint,render_template
from simpledu.models import User

user = Blueprint('user',__name__,url_prefix = '/user/<username>')

@user.route('/')
def user_index(username):
    return render_template('user.html',user=User.query.first())

