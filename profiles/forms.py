from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(Field("name"))

    class Meta:
        model = User
        fields = ["name"]


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            HTML("<h4>Teacher Incharge</h4>"),
            Field("t1"),
            Field("t2"),
            Field("t3"),
            HTML("<h4>Student Incharge</h4>"),
            Field("s1"),
            Field("s2"),
            Field("t3"),
        	HTML("<h4>EXQUISITE - <span class = 'gg'>Hackathon</span></h4>"),
            Field("hack1"),
            Field("hack2"),
            Field("hack3"),
        	HTML("<h4>TECH EXULT - <span class = 'gg'>Quiz</span></h4>"),
        	Field("quiz1"),
            Field("quiz2"),
        	HTML("<h4>X-WORD - <span class = 'gg'>Crossword</span></h4>"),
        	Field("cross1"),
            Field("cross2"),
            Field("cross3"),
            Field("cross4"),
        	HTML("<h4>EXECUTE.EXE - <span class = 'gg'>Programming</span></h4>"),
        	Field("prog1"),
        	HTML("<h4>X-86 - <span class = 'gg'>Hardware</span></h4>"),
        	Field("hard1"),
            Field("hard2"),
        	HTML("<h4>EXCLUSIVE - <span class = 'gg'>Surprise</span></h4>"),
        	Field("surp1"),
            Field("surp2"),
            Field("surp3"),
            Field("surp4"),
            HTML("<h4>X-VISION - <span class = 'gg'>AV</span></h4>"),
            Field("av1"),
            Field("av2"),
            HTML("<h4>PIXELS - <span class = 'gg'>Photography</span></h4>"),
            Field("photo1"),
            Field("photo2"),
            Field("photo3"),
            Field("photo4"),
            Submit("update", "Update", css_class="button2"),
        )

    class Meta:
        model = models.Profile
        fields = ["hack1","hack2","hack3","quiz1",'quiz2','cross1','cross2','cross3','cross4','prog1','hard1','hard2','surp1','surp2','surp3','surp4','av1','av2','photo1','photo2','photo3','photo4','t1','t2','t3','s1','s2','s3']
