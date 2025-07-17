# py -3 --version // Python 3.13.2 cmd
# py --version // Python 3.13.2 (check python version)
# py -m pip install prettytable // add prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemmon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.field_names = ["Pokemmon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

# +---------------+----------+
# | Pokemmon Name |   Type   |
# +---------------+----------+
# |    Pikachu    | Electric |
# |    Squirtle   |  Water   |
# |   Charmander  |   Fire   |
# +---------------+----------+

# table.align = 'l'
# +---------------+----------+
# | Pokemmon Name | Type     |
# +---------------+----------+
# | Pikachu       | Electric |
# | Squirtle      | Water    |
# | Charmander    | Fire     |
# +---------------+----------+
print(table)

