class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def has_access(self, resource):
        if resource in self.role:
            return True
        return False

admin = ['resource1', 'resource2', 'resource3']
guest = ['resource1']

admin_user = User('admin', admin)
guest_user = User('guest', guest)

print(admin_user.has_access('resource2'))  # True
print(guest_user.has_access('resource2'))  # False
