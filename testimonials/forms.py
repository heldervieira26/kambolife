from django import forms
from .models import Testimonial



class TestimonialPostForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('title', 'text', 'author', 'affiliation', 'image', 'published_date', 'active')