from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
from .forms import MoveForm



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', {
    'pokemons': pokemons
  })

def pokemons_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  # instantiate FeedingForm to be rendered in the template
  move_form = MoveForm()
  return render(request, 'pokemons/detail.html', {
    # include the cat and feeding_form in the context
    'pokemon': pokemon, 'move_form': move_form
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type','abilities','description']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons'  

def add_move(request, pokemon_id):
  form = MoveForm(request.POST)
  if form.is_valid():
    new_move = form.save(commit=False)
    new_move.pokemon_id = pokemon_id
    new_move.save()
    return redirect('detail', pokemon_id=pokemon_id)
