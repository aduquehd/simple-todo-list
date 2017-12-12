from mongoengine import Document, StringField, BooleanField


class User(Document):
    email = StringField(required=True, max_length=255, unique=True)
    password = StringField(max_length=255)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.email


class TodoList(Document):
    user_id = StringField(required=True, max_length=255)
    description = StringField(required=True, max_length=255)
    status = BooleanField()
