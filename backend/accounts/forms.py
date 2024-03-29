from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username','email',)

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email',)