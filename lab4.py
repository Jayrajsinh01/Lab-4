
from ast import pattern
from importlib.resources import path

from sys import *
def main():

    path = '/Users/jayrajsinh/Desktop/gateway.log'

    return


# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):

    import re

    with open(r'/Users/jayrajsinh/Desktop/gateway.log', 'r') as file:
        pattern:re.compile(r"/Users/jayrajsinh/Desktop/gateway.log ", re.IGNORECASE, re.DOTALL, re.MULTILINE)
    return pattern.match
    

    for line in file:
        match = re.search
        print(line,end='')

    return

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()