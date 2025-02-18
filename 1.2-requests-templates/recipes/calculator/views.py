from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'tost': {
         'хлеб, ломтик': 1,
         'масло сливочное, г': 0.01,
         'сыр, г': 0.05,
    },
}


# Обработчик, который передает в templates рецепт блюда, рассчитанный на n персон.
# По умолчанию n = 1.
# Источник данных для рецептов словарь DATA.
def select_recipe(request, recipe_name=None):
  recipe = DATA.get(recipe_name) if recipe_name else None
  servings = 1
  if recipe:
    servings_str = request.GET.get('servings', None)
    
    if servings_str and servings_str.isdigit():
      servings = int(servings_str)
      adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    else:
      adjusted_recipe = recipe
  else:
    adjusted_recipe = None

  title_recipe = 'РЕЦЕПТ БЛЮДА:'
  title_persons = 'Число персон:'
  
  context = {
    'pages': {
      'Рецепты': reverse('index')
    },
    'recipe': adjusted_recipe,
    'unknown_recipe': recipe_name,
    'new_title': title_recipe,
    'dish': recipe_name,
    'new_persons': title_persons,
    'persons': servings
  }

  return render(request, 'calculator/index.html', context)


# Обработчик с инструкцией по поиску рецептов для стартовой страницы.
# Запускается при вводе в адресную строку браузера http://127.0.0.1:8000 
def index_view(request, recipe_name=None):
  recipe = DATA.get(recipe_name) if recipe_name else None
  pages = {
    'Рецепты': reverse('index')
  }
  
  context = {
    'pages': pages,
    'unknown_recipe': None,
    'check': recipe
  }
  return render(request, 'calculator/index.html', context)