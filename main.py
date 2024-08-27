decimal_to_roman = {1 : 'I', 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX"}

change = []   
def roman_number(number):
    while True:
        if number >= 1000:
            change.append("M")
            number -= 1000
        
        elif number >= 900:
            change.append("CM")
            number -= 900
            
        elif number >= 500:
            change.append("D")
            number -= 500
        
        elif number >= 400:
            change.append("CD")
            number -= 400
            
        elif number >= 100:
            change.append("C")
            number -= 100
        
        elif number >= 90:
            change.append("XC")
            number -= 90
            
        elif number >= 50:
            change.append("L")
            number -= 50
       
        elif number >= 40:
            change.append("XL")
            number -= 40
        
        elif number >= 10:
            change.append("X")
            number -= 10
        
        elif number <= 9 and number != 0:
            change.append(decimal_to_roman.get(number))
            number = 0
        
        elif number == 0:
            return change   

number = int(input("Enter number: "))
roman = roman_number(number)
print(f"\nRoman number is:{''.join(roman)}")                 
            
    