
import re

def update_bioswimmer(bioswimmer, command_columns):
    command = command_columns[0]
    # TODO: Continue work from here, I was creating a switch case to handle each command
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)
    return

def read_bioswimmer_data(bioswimmer, serial_data):
    print(serial_data)
    commands = re.findall(r'\{([^}]+)', serial_data)
    print(commands)
    for command in commands:
        print(command)
        command_columns = re.split(r'\W+', command)
        print(command_columns)
    return