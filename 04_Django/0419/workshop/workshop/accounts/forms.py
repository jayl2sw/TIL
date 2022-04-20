from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationFrom(UserCreationForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('profile_image','nickname',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
