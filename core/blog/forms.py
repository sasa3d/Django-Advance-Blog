from django import forms
from .models import Post


# class ContactForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass
class PostForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for MODELNAME."""
        model = Post
        #fields = ['author','title', 'content', 'status','category','published_date']
        fields = ['title', 'content', 'status','category','published_date'] #author is not editable because it is automatically 
                  # set to the current user when the form is saved 
        
        verbose_name = 'MODELNAME'
        verbose_name_plural = 'MODELNAMEs'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        pass

