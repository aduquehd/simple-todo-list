class UserObject:

    def __init__(self, id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_email(self):
        return self.email

    def get_id(self):
        return str(self.id)
