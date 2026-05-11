let Pizza_size = 0
game.splash("Pizza size?")
Pizza_size = game.askForNumber(Pizza_size)
let Individual_pizza_cost = Pizza_size / 2
game.splash(Individual_pizza_cost)
let _Labour_cost = 0.75 + Individual_pizza_cost
let Price_before_tax = 1 + _Labour_cost
game.splash("Price before tax:")
game.splash(Price_before_tax)
let Price_after_tax = 1.13 * Price_before_tax
game.splash("Price after tax:")
game.splash(Price_after_tax)
game.splash("Price after tax rounded:")
let Rounding = Math.round(100 * Price_after_tax) / 100
game.splash(Rounding)
