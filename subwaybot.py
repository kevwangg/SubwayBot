
import random
import discord
sandwiches = ['Cali Fresh Turkey', 'Cali Fresh Steak', 'All American', 'Black Forest Ham', 'Buffalo Chicken', 'Cold Cut Combo', 'Italian BMT', 'Meatball Marinara', 'Oven Roasted Turkey', 'Spicy Italian', 'Sweet Onion Chicken Teriyaki', 'Tuna']
breads = ['Artisan Italian', 'Multigrain', 'Herbs & Cheese']
cheeses = ['American', 'Cheddar', 'Pepperjack', 'Provolone', 'Swiss']
vegetables = ['Lettuce', 'Tomatoes', 'Cucumbers', 'Green Peppers', 'Red Onions', 'Spinach', 'Pickles', 'Black Olives', 'Jalepenos', 'Banana Peppers']
sauces = ['Mayonnaise', 'Yellow Mustard', 'Honey Mustard', 'Caesar', 'Buffalo Sauce', 'Ranch', 'Marinara', 'Sweet Onion']
randVeggieSample = random.randint(5,10)
randSauceSample = random.randint(1, 2)

sandwich = random.choice(sandwiches)
bread = random.choice(breads)
cheese = random.choice(cheeses)
veggieList = random.sample(vegetables, randVeggieSample)
veggies = ', '.join(veggieList)
sauceList = random.sample(sauces, randSauceSample)
sauce = ', '.join(sauceList)

previousSandwich = []
favouriteSandwiches = []

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$subway'):
      sandwichList = [sandwich, bread, cheese, veggies, sauce]
      await message.channel.send(f' Sandwich: {sandwichList[0]}\nBread: {sandwichList[1]}\nCheese: {sandwichList[2]}\nVeggies: {sandwichList[3]}\nSauce: {sandwichList[4]}')
      previousSandwich = sandwichList

    
    if message.content.startswith('$fav'):
      favouriteSandwiches.append(previousSandwich)
    

    if message.content.startswith('$favlist'):
      for oldSandwich in favouriteSandwiches:
        await message.channel.send(oldSandwich)
    
    if message.content.startswith('$favremove'):
      pass
    

    if message.content.startswith('$help'):
      pass