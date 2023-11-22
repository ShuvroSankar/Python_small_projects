height = "".join(input('What is the height?(f/m) ').split())
breath = "".join(input('What is the height?(f/m) ').split())


def convert_to_feet(input_string):
    # Separate numbers and characters
    numbers = ''.join(char for char in input_string if char.isdigit())
    numbers = float(numbers)
    characters = ''.join(char for char in input_string if char.isalpha())
    if characters.lower() == 'meters':
        numbers *= 3.28084
    elif characters.lower() == 'feets':
        pass
    else:
        print("Wrong parameter")
    return numbers
def calculate_price(height,breath):
    area = height*breath
    

height_feets = convert_to_feet(height)
breath_feets = convert_to_feet(breath)

print(height)
print(breath)
