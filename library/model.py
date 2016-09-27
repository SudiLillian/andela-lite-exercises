from app import db

class User(db.Model):
  """Create User table details."""

  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))

  def __init__(self, first_name, username, password):
    """Initialize new user."""
    self.first_name = first_name
    self.username = username
    self.password = password

class Post(db.Model):
  """docstring for ClassName"""
  __tablename__ = 'post'
  id = db.Column(db.Integer, primary_key=True)
  post = db.Column(db.String(300))
  post_by = db.Column(db.Integer, db.ForeignKey('user.id'))
  user = db.relationship(User, backref = db.backref('post', lazy = 'dynamic'))
  post_date = db.Column(db.DateTime)

  def __init__(self, post, post_by, post_date):
    """Initialize new user."""
    self.post = post
    self.post_by = post_by
    self.post_date = post_date



class Comments(db.Model):
  """docstring for ClassName"""
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String(300))
  comment_on = db.Column(db.Integer)
  comment_by = db.Column(db.Integer, db.ForeignKey('user.id'))
  user = db.relationship('user', backref=db.backref('comment', lazy = 'dynamic'))

  def __init__(self, comment, comment_on):
    self.comment = comment
    self.comment_on = comment_on
    