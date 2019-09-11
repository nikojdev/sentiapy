"""
Assignmet week 3
"""
from os_resources import OsResources
from utilities import Utilities

def main():
    """Main function
    """
    #data vars
    output_data = {}
    output_stdout = []

    #parse user input
    user_input = Utilities.parse_arguments()

    #get the requested data based on user input and store it
    if not user_input.no_cpu:
        output_data["cpu"] = OsResources.get_cpu()
        output_stdout.append(f"CPU: {output_data['cpu']}")
    if not user_input.no_memory:
        output_data["mem_free_mb"] = OsResources.get_free_mem_mb()
        output_data["mem_free_perc"] = OsResources.get_free_mem_perc()
        output_stdout.append(f"Free memory: {output_data['mem_free_mb']}MB "
                             f"({output_data['mem_free_perc']}%)")

    #store file to json if there is any data for output
    if bool(output_data):
        Utilities.write_json(output_data)

    #check if user opted for output
    if user_input.stdout:
        for string in output_stdout:
            print(string)


if __name__ == "__main__":
    main()
