# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



from prettytable import PrettyTable
table = PrettyTable() #object created
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["ELectric","Water","Fire"])
table.align = "l"
print(table)