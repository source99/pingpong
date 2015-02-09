from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from pingpong.forms import PlayerForm, MatchForm, RecordForm
from pingpong.models import Match
from itertools import chain

def index(request):
    context_dict = {'boldmessage' : "I am bold font from the context"}
    return render(request, 'pingpong/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage' : "I am bold font from the context"}
    return render(request, 'pingpong/about.html', context_dict)


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = PlayerForm()

    return render(request,'pingpong/add_player.html',{'form' : form, 'page_title' : "Add Player"})

def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = MatchForm()

    return render(request,'pingpong/add_match.html',{'form' : form})


def show_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)

        if form.is_valid():
            print "form cleaned data = {}".format(form.cleaned_data)
            #query: player1 = id1 && player2 = id2 
            #<h2>{{record.player_1_id.name}}</h2>
            matches1 = Match.objects.filter(player_1_id__name=form.cleaned_data['player_1_id'].name).filter(player_2_id__name=form.cleaned_data['player_2_id'].name)
            matches2 = Match.objects.filter(player_1_id__name=form.cleaned_data['player_2_id'].name).filter(player_2_id__name=form.cleaned_data['player_1_id'].name)
            matches = list(chain(matches1, matches2))
            print matches            
            return render(request,'pingpong/show_record.html',{'form' : form, 'matches' : matches})
        else:
            print form.errors
    else:
        form = RecordForm()

    return render(request,'pingpong/show_record.html',{'form' : form})


