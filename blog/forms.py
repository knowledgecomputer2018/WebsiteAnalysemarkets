from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
         )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
#####widget
#You’ll also notice an argument widget has been passed to both the fields.
#The author field has the forms.TextInput widget.
#This tells Django to load this field as an HTML text input element in the templates.
