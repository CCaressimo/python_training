def format_name(f_name, l_name):
    """Convert string to title case"""
    if f_name == "" or l_name == "":
        return "You did not provide a valid input"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

formated_string = format_name(input("What is your first name?\n"), input("What is your last name?\n"))
print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)
