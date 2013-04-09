# -*- coding: utf-8 -*-

import io, sys

__author__ = 'vchemiere@elanz.fr'


def main(argv):
    """ Parse the log file in parameter

    argv -- log file path
    """
    #ouverture du fichier de log passé en paramètre
    with open(argv[0], 'r') as log:
        line = log.readline()
        result = ""
        #lecture ligne par ligne tant que l'on ne tombe pas sur une ligne vide
        while line != "" :
            #mise a jour d'un module
            if ' 1 modules...' in line:
                result = ""
            #nom du fichier de test chargé
            if 'TEST' in line and 'openerp.modules.loading' in line:
                result += 'File loaded: ' + line.split('module ')[1] + '\n'
            #erreur déclenchée par le test
            if 'ERROR' in line and 'yaml_import' in line:
                result += '/!\\' + line.split('yaml_import:')[1] + '\n'
            #infos sur une assertion échouée
            if 'test:' in line or 'values:' in line:
                result += '\t' + line + '\n'
            line = log.readline()

    #résumé du log de test
    nberror = result.count('/!\\')
    result += 'There is ' + str(nberror) + ' test(s) failed'
    print result

if __name__ == "__main__":
    main(sys.argv[1:])
