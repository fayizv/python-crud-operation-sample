from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("first_name","last_name","username", "email", "password1", "password2")
		
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']

		if commit:
			user.save()
		return user


class EditProfileForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email']
        help_texts={
            'username': None
        }	

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email']
        help_texts={
            'username': None
        }	


        
