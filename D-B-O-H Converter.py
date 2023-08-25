def print_formatted(number):
    leng = len(bin(number).replace("0b",""))
    for each in range(1, number + 1):
        print(str(each).rjust(leng," "), format(each,'o').replace("0o","").rjust(leng," "), f'{each:X}'.rjust(leng," "), format(each,'b').rjust(leng," "))
        
    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
