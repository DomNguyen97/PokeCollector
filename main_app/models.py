from django.db import models
from django.urls import reverse

ELEMENTS = (
    ('F', 'Fire'),
    ('W', 'Water'),
    ('L', 'Lighting')
)

# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  abilities = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pokemon_id': self.id})  

class Move(models.Model):
  name = models.CharField(max_length=50)
  element = models.CharField(
    max_length=1,
      choices=ELEMENTS,
      default=ELEMENTS[0][0]
  )
  pokemon = models.ForeignKey(
    Pokemon, 
    on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.get_element_display()} on {self.name}"
  