from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager

###HACK HACK, should get it from database
mapping = {
  "2": {
    "username" :  "mandyliu0305@gmail.com"
  }
}

class User(UserMixin):
  def __init__(self, **kwargs):
    super(User, self).__init__(**kwargs)
	
@login_manager.user_loader
def load_user(user_id):
  if user_id in mapping:
    user = User()
    user.username = mapping[user_id]["username"]
    return user

  return None
