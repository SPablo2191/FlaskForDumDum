from wtforms import Form
from wtforms import StringField,TextAreaField,EmailField

class CommentForm(Form):
    username = StringField('username:')
    email = EmailField('correo:')
    comment = TextAreaField('comentario:')