# Fucntion  Example 

#Example 1 : Temperature Conversion

def convert_temp(temp,unit):
    """ This fucntion is convert a temperature"""
    if unit== 'c':
        return temp * 9/5 +32 #convert celsius to farenheit
    elif unit=="f":
        return (temp-32) * 5/9 # Farenheit to celceus
    else:
        return None


print(convert_temp(25,"c"))
print(convert_temp(77,"f"))








#Example 2 : Password Strength checker


# Example 3 : Calculate the Total Cost of Items in a shopping Cart

