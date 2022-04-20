from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model # 현재 활성화되어 있는 유저의 모델을 가져다 줌





class CustomUserChangeForm(UserChangeForm):
    # password = None
    class Meta:
        model = get_user_model() # User
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)