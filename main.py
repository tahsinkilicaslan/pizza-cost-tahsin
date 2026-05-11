Pizza_size = 0
Price_before_tax = 0
game.splash("Pizza size?")
Pizza_size = game.ask_for_number(Pizza_size)
Individual_pizza_cost = Pizza_size / 2
game.splash(Individual_pizza_cost)
_Labour_cost = 0.75 + Individual_pizza_cost
Price_before_tax = 1 + _Labour_cost
game.splash("Price before tax:")
game.splash(Price_before_tax)
Price_after_tax = 1.13 * Price_before_tax
game.splash("Price after tax:")
game.splash(Price_after_tax)
game.splash("Price after tax rounded:")
Rounding = Math.round(100 * Price_after_tax) / 100
game.splash(Rounding)