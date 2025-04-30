from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .models import System, Game, Accessory
from .forms import SystemForm, GameForm, AccessoryForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('systems_index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def systems_index(request):
    systems = System.objects.filter(user=request.user)
    return render(request, 'systems/index.html', {'systems': systems})

@login_required
def systems_create(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.user = request.user
            system.save()
            return redirect('systems_index')
    else:
        form = SystemForm()
    return render(request, 'systems/create.html', {'form': form})

@login_required
def systems_detail(request, system_id):
    system = get_object_or_404(System, id=system_id, user=request.user)
    games = Game.objects.filter(system=system, user=request.user)
    accessories = Accessory.objects.filter(system=system, user=request.user)
    return render(request, 'systems/detail.html', {
        'system': system,
        'games': games,
        'accessories': accessories
    })

@login_required
def games_create(request, system_id):
    system = get_object_or_404(System, id=system_id, user=request.user)
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.system = system
            game.user = request.user
            game.save()
            return redirect('systems_detail', system_id=system_id)
    else:
        form = GameForm()
    return render(request, 'games/create.html', {'form': form, 'system': system})

@login_required
def games_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'games/detail.html', {'game': game})

@login_required
def games_update(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if game.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this game.")
    
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games_detail', game_id=game_id)
    else:
        form = GameForm(instance=game)
    return render(request, 'games/update.html', {'form': form, 'game': game})

@login_required
def games_delete(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if game.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this game.")
    
    if request.method == 'POST':
        system_id = game.system.id
        game.delete()
        return redirect('systems_detail', system_id=system_id)
    return render(request, 'games/confirm_delete.html', {'game': game})

@login_required
def accessories_create(request, system_id):
    system = get_object_or_404(System, id=system_id, user=request.user)
    if request.method == 'POST':
        form = AccessoryForm(request.POST)
        if form.is_valid():
            accessory = form.save(commit=False)
            accessory.system = system
            accessory.user = request.user
            accessory.save()
            return redirect('systems_detail', system_id=system_id)
    else:
        form = AccessoryForm()
    return render(request, 'accessories/create.html', {'form': form, 'system': system})

@login_required
def accessories_detail(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    return render(request, 'accessories/detail.html', {'accessory': accessory})

@login_required
def accessories_update(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    if accessory.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this accessory.")
    
    if request.method == 'POST':
        form = AccessoryForm(request.POST, instance=accessory)
        if form.is_valid():
            form.save()
            return redirect('accessories_detail', accessory_id=accessory_id)
    else:
        form = AccessoryForm(instance=accessory)
    return render(request, 'accessories/update.html', {'form': form, 'accessory': accessory})

@login_required
def accessories_delete(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    if accessory.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this accessory.")
    
    if request.method == 'POST':
        system_id = accessory.system.id
        accessory.delete()
        return redirect('systems_detail', system_id=system_id)
    return render(request, 'accessories/confirm_delete.html', {'accessory': accessory})

@login_required
def account(request):
    systems_count = System.objects.filter(user=request.user).count()
    games_count = Game.objects.filter(system__user=request.user).count()
    accessories_count = Accessory.objects.filter(system__user=request.user).count()
    
    context = {
        'systems_count': systems_count,
        'games_count': games_count,
        'accessories_count': accessories_count,
    }
    return render(request, 'account.html', context)
