"""
Calcul d'une partie du nombre pi
Stockera le resultat dans un fichier tmp_result{numero de l'unité de calcul}
"""
import sys

if __name__ == "__main__" :
    starting_value = int(sys.argv[1])
    step_value = int(sys.argv[2])
    max_value = int(sys.argv[3])
    FILE_TMP = "tmp_result" + str(starting_value)


    print("START from {0} with {1} steps".format(starting_value,step_value))
    
    result = 0
    i = starting_value
    while(i<max_value):
        etape1 = (-1)**i
        etape2 = (2 * i) + 1
        result = result + (etape1 / etape2)
        i = i + step_value
    
    f = open(FILE_TMP, "a")
    f.write("%s\n" % result)
