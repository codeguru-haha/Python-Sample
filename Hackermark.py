def print_logo(thickness):
    c = 'H'
    for i in range(1,2*thickness,2):
        print((c * i).center(thickness*2 ," "))
    for i in range(thickness+1):
        print((c * thickness).center(2*thickness," ").ljust(3*thickness," ")+(c * thickness).center(2*thickness," ").ljust(3*thickness," "))
    for i in range(int((thickness+1)/2)):
        print((c * thickness*5).center(6*thickness," "))
    for i in range(thickness+1):
        print((c * thickness).center(2*thickness," ").ljust(3*thickness," ")+(c * thickness).center(2*thickness," ").ljust(3*thickness," "))
    for i in range(2*thickness - 1,0,-2):
        print(" "*3*thickness + (c * i).center(thickness*2," "))

if __name__ == '__main__':
    thickness = int(input("Enter the thickness: "))
    print_logo(thickness)