#Exercise 0 (1 point). Write a function, eval_strint(s, base), which given a 
#string of digits s and a base base, returns its value as an integer.
#That is, this function essentially implements the mathematical object,  
#[[s]]b, which would convert a string s to its numerical value, assuming its 
#digits are given in base b. 


#sample input:
#For example:eval_strint('100111010', base=2) == 314




def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    #
    # YOUR CODE HERE
    #
    the_int = int(s, base)
    
    return(the_int)
    
    
    
    
    
    