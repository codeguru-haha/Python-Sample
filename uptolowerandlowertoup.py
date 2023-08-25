def swap_case(string):
    swapped = ''
    for char in string:
        # if char.islower():
        #     swapped += char.upper()
        if char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped
s = "0x1A15B231E8f96924AB9174567b3a8335463872Ae"
ss=""
print(swap_case(s))
print(len(ss))