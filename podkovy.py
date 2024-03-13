def podkovy(p,k):
        x = p - (k*4)

        if x > 0:
            print("Počet přebývajících podkov:", x)

        elif x < 0:
            print("Počet chybějících podkov:", -x)
            
        else:
            print("Počet podkov vychází přesně.")
        
