foods = {'butternut squash soup':[45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.'],
        'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                '4. Mixed them thoroughly'],
        'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}


class Food:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe
        
    def show(self):
        print("Name:", self.name)
        self.recipe.show_recipe()
        print("***", '\n')

class FoodType:
    def __init__(self, food_type, is_vegie, cuisine):
        self.food_type = food_type
        self.is_vegie = is_vegie
        self.cuisine = cuisine
        
    def show_food(self):
        print("Is Veggie?", 'Yes' if self.is_vegie else "No")
        print("Food Type:", self.food_type)
        print("Cuisine:", self.cuisine)
    
        
class Recipe:
    def __init__(self, recipe, prep_time, food_type, ingredients):
        self.recipe = recipe
        self.prep_time = prep_time
        self.food_type = food_type
        self.ingredients = ingredients
        
    def show_recipe(self):
        print("Prep time:",self.prep_time, "mins")
        self.food_type.show_food()
        self.ingredients.show_ingredients()
        print("recipe", self.recipe)


class Ingredients:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def show_ingredients(self):
        print('Ingredients: ')
        for item in value[4]:
            print(item, end=', ')
        print()
    
    
list_of_food = []
        
for key, value in foods.items():
    
    ingredients = Ingredients(value[4])
    food_type = FoodType(value[2], value[1], value[3])
    recipe = Recipe(value[5], value[0], food_type, ingredients)

    food = Food(key, recipe)
    food.show()
    list_of_food.append(food)