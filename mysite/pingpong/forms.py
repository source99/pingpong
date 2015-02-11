from django import forms
from pingpong.models import Player, Match
import datetime

class PlayerForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="'Please Enter your name.")

    class Meta:
        model = Player
        fields = ('name',)


class MatchForm(forms.ModelForm):
    player_1_id = forms.ModelChoiceField(queryset=Player.objects.all(), required=True)
    player_2_id = forms.ModelChoiceField(queryset=Player.objects.all(), required=True)
    player_1_score = forms.IntegerField(initial=0, required=True)
    player_2_score = forms.IntegerField(initial=0, required=True)
    date = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Match
        fields = ('player_1_id','player_2_id','player_1_score','player_2_score','date')


class RecordForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['player_1_id', 'player_2_id']

