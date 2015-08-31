#! /usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from misslove.models import NewUser
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
	class Meta():
		model = get_user_model()
		fields = ('username', 'email',)
		lables = {
			'username': u'用户名',
			'email': u'邮箱',
		}

class InfoEdit(forms.ModelForm):
	class Meta():
		model = get_user_model()
		fields = ('username','email', 'gender', 'whats_up', 'avatar', )



