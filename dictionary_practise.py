foods = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}
NBA_players = {"Lebron James": 23 , "Kevin Durant": 25, "Kobe Bryant" : 24,
 "Stephen Curry": 30, "Damian Lillard": 0, "Michael Jordan": 23 }

chicken_price = foods["chicken"]
print(chicken_price)

beef_price = foods["beef"]
print(beef_price)

cheese_price = foods["cheese"]
print(cheese_price)

milk_price = foods["milk"]
print(milk_price)

james_num = NBA_players["Lebron James"]
print(james_num)

shoes = {"Jordan_13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 
5, "SB Dunk": 4}


def food_total(food1, food2):
    total = food1 + food2
    return total
print( food_total(foods["chicken"], foods["beef"]))

def food_total(food1, food2):
    total = food1 - food2
    return total
print( food_total(foods["milk"], foods["cheese"]))

def restock(shoe, num):
    shoes[shoe] = shoes[shoe] * num
    stock = shoes
    return stock
print( restock("Air Max", 4) )

def clearance_sale(shoe, num):
    shoes[shoe] = shoes[shoe] / num
    stock=shoes
    return stock
print( clearance_sale("SB Dunk", 5))

def players_mean(player1, player2, player3, player4, player5, player6):
    mean = player1 + player2 + player3 + player4 + player5 + player6 / 6
    return mean
print(  players_mean("Lebron James", "Kevin Durant", "Kobe Bryant",
 "Stephen Curry", "Damian Lillard", "Micheal Jordan")  )
