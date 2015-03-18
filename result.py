"""
Rassemble les resultats du fichier resultat.tmp
"""

if __name__ == "__main__" :
    FILE_TMP = "resultats.tmp"
    
    f = open(FILE_TMP,"r")
    tab_result = f.readlines()
    
    pi_value = 0
    for tmp_value in tab_result:
        pi_value = pi_value + float(tmp_value[:-1])

    pi_value = pi_value * 4


    print("PI vaut {0}".format(pi_value))
