def no_c(my_string):
    new_string = " "
    for char in my_string:
        if char not in ('c', 'C'):
            new_string += char
        return new_string
        
        
        
        
        
        
        #if char != 'c' and char != 'C':
            #new_string = char
    #return new_string


#print(no_c("Chicago"))
#print(no_c("C is fun!"))