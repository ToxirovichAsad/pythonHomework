def check(func):

    def wrapper(a,b): 

        try:

            return func(a,b) #we are keeping original function job
        
        except ZeroDivisionError:

            print("Denominator can't be zero") #we are handling with zero devision error

        except TypeError:

            print("Error: Both inputs must be numbers.") #just in case we are handling type error which user can enter string values as well 


            
    return wrapper
@check
def div(a, b):
   
   return a / b

div(6, 0) #running a function and didn't changed its job returning wrapper function but still function

