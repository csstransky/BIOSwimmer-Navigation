
import re

def read_bioswimmer_data(bioswimmer, serial_data):
    print(serial_data)
    commands = re.findall(r'\{([^}]+)', serial_data)
    print(commands)
    return