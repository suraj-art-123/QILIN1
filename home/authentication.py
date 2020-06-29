from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
class EmailAuthBackend():
    def authenticate(self, username=None, password=None,**kwargs):
        if username is None or password is None:
            return
        UserModel=get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return  user
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None