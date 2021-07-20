from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm): # auth\forms.py의 UserCreationForm 상속
    # override, super method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # username이라는 이름의 필드를 찾고, disabled 속성 True로.
        self.fields['username'].disabled = True
