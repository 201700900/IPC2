

def entrada():
    
    correcto = False
    entrada = ""
    while not correcto:
        try:
            entrada = str(
                input(
                    "----------\nIngrese un texto:\n"
                )
            )
            correcto = True
        except ValueError:
            print("Error, intente de nuevo")

    return entrada

def listToString(s): 
        
    str1 = "" 
        
    for ele in s: 
        str1 += ele  
    
    return str1 

def main():
    string_reverso=[]
    str=entrada()
    
    i = len(str)
    while i > 0: 
        string_reverso += str[i-1]
        i = i - 1 # decrement index
    print("El texto invertido es:", listToString(string_reverso)) 
    
    entrada()


main()