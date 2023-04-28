from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
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
  # Get the toys the cat doesn't have...
  # First, create a list of the toy ids that the cat DOES have
  id_list = pokemon.items.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  items_pokemon_doesnt_have = Item.objects.exclude(id__in=id_list)
  move_form = MoveForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'move_form': move_form,
    # Add the toys to be displayed
    'items': items_pokemon_doesnt_have
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'type', 'abilities', 'description']

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


class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items'

def assoc_item(request, pokemon_id, item_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Pokemon.objects.get(id=pokemon_id).items.add(item_id)
  return redirect('detail', pokemon_id=pokemon_id)  