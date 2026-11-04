# Non-metal Information Finder
from pyscript import display, document


def symbol_search(e):
    document.getElementById('result').innerHTML = ' '
    element = document.getElementById('element_symbol').value

    nonmetals = {
    "H": {'Symbol': 'H', 'Name': 'Hydrogen', 'Number': '11', 'Mass': '1.008'},
    "He":{'Symbol': 'He', 'Name': 'Helium', 'Number': '2', 'Mass': '4.003'},
    "C": {'Symbol': 'C', 'Name': 'Carbon', 'Number': '6', 'Mass': '12.01'},
    "N": {'Symbol': 'N', 'Name': 'Nitrogen', 'Number': '7', 'Mass': '14.01'},
    "O": {'Symbol': 'O', 'Name': 'Oxygen', 'Number': '8', 'Mass': '16.00'},
    "F": {'Symbol': 'F', 'Name': 'fluorine', 'Number': '9', 'Mass': '19.00'},
    "Ne": {'Symbol': 'Ne', 'Name': 'Neon', 'Number': '10', 'Mass': '20.18'},
    "P": {'Symbol': 'P', 'Name': 'phosphorus', 'Number': '15', 'Mass': '30.97'},
    "S": {'Symbol': 'S', 'Name': 'sulfur', 'Number': '16', 'Mass': '32.07'},
    "Cl": {'Symbol': 'Cl', 'Name': 'Chlorine', 'Number': '17', 'Mass': '35.45'},
    "A": {'Symbol': 'A', 'Name': 'Argon', 'Number': '18', 'Mass': '39.95'},
    "Se": {'Symbol': 'Se', 'Name': 'Selenium', 'Number': '34', 'Mass': '78.96'},
    "Br": {'Symbol': 'Br', 'Name': 'Bromine', 'Number': '35', 'Mass': '79.90'},
    "Kr": {'Symbol': 'Kr', 'Name': 'Krypton', 'Number': '36', 'Mass': '83.80'},
    "I": {'Symbol': 'I', 'Name': 'Iodine', 'Number': '53', 'Mass': '126.9'},
    "Xe": {'Symbol': 'Xe', 'Name': 'Xenon', 'Number': '54', 'Mass': '131.3'},
    "Rn": {'Symbol': 'Rn', 'Name': 'Radon', 'Number': '86', 'Mass': '(222)'}}

    info_finder = element in nonmetals
    display_message = (f'That is not in our list of Non-metals', f'({nonmetals.get(element)})')

    document.getElementById('results').innerHTML = (display_message[info_finder])
