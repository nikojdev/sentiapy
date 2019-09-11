"""Assigment - week 2
1. Create a new virtual environment
2. Install the default .pylintrc
3. Create a new main.py
4. Use if __name__ == "__main__":
5. Use requirements.txt to install “requests”
6. Create a function get_site(url) that returns the
contents of that URL
7. Create a function
get_angle_bracket_count(string) that returns
the total amount of <‘s and >’ in that string
8. Create a function replace_str(string, original,
replacement) that replaces all occurrences of
`original` in `string` with `replacement` and
returns the result
9. Pylint should show no problems (including docstring!)
"""
import requests

def get_angle_bracket_count(string):
    """this function counts number of courly brackets that occur in the string
    Arguments:
        string {String} -- content
    Returns:
        number of curly brackets in provided string
    """
    string_count = string.count('<') + string.count('>')
    return string_count


def replace_str(string, original, replacement):
    """replaces all occurances of the string provided with the new one
        and returns the string with new content
    Arguments:
        string {String} -- content
        original {String} -- string to replace
        replacement {String} -- new string
    Returns:
        String -- new content with replaced strings
    """
    new_string = string.replace(original, replacement)
    return new_string

def get_site(url):
    """this function makes GET request for given url, and returns its content as string
    Arguments:
        url {String} -- url address
    Returns:
        String -- url content
    """
    response = requests.get(url)
    return response.text

def main():
    """main function, printing results
    """
    url = "http://example.com"
    content = get_site(url)
    content_length = len(content)
    print(f"Content length: {content_length}")

    number_of_brackets = get_angle_bracket_count(content)
    print(f"Number of brackets: {number_of_brackets}")

    content = replace_str(
        content, "<", "LESS_THAN"
    )
    content = replace_str(
        content, ">", "MORE_THAN"
    )

    content_length = len(content)
    print(f"New content length: {content_length}")


if __name__ == "__main__":
    main()
