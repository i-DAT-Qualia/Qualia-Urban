from django import forms
from leaflet.forms.widgets import LeafletWidget
from django.forms.widgets import CheckboxSelectMultiple, Select
from django.forms import ModelForm
from django.db.models import Q

from models import *


class TreeForm(forms.ModelForm):

    class Meta:
        model = Tree
        fields = [
            'name',
            'info',
            'gps',
            'species',
            'age',
            'org',
            'dataset'
        ]

        widgets = {
            'gps': LeafletWidget(),
        }


class ReadingForm(forms.ModelForm):

    class Meta:
        model = Reading
        fields = [
            'author',
            'type',
            'value'
        ]


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = [
            'author',
            'image',
        ]


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = [
            'author',
            'info',
        ]


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = [
            'author',
            'type',
            'info'
        ]
