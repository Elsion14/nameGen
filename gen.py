#générateur de syllabes/noms

from random import *
import os


def main(path):
    list_voyelles, list_consonnes, list_syllabes = fileReader(path);

    isto_list = create_list(list_voyelles, list_consonnes);
    
    fichier = open(path[:-4]+"2syl.txt","w");
    for i in range(0,100):
        fichier.write(create_name(isto_list,2)+"\n");
    fichier.close();

    fichier = open(path[:-4]+"3syl.txt","w");
    for i in range (0,100):
        fichier.write(create_name(isto_list,3)+"\n");
    fichier.close();

    print("Done");


def syllabe(voyelles, consonnes): #génère une syllabe à partir de lettres choisies aléatoirement parmis des lettres données

    alea_voyelle = randint(0,len(voyelles)-1);
    voyelle = voyelles[alea_voyelle];
    nb_lettres = randint(0,3);
    res = "";
    voyelle_in = False;

    while nb_lettres > 0:
        alea_consonne = randint(0,len(consonnes)-1);
        consonne = consonnes[alea_consonne];

        if not voyelle_in:
            v = randint(0,1);
            if v == 1:
                res += voyelle;
                voyelle_in = True;
                nb_lettres = nb_lettres - 1;
                continue
        res += consonne;
        nb_lettres = nb_lettres - 1;

    cpt_consonnes = 0;
    for i in range(len(res)):
        for j in range(len(consonnes)):
            if res[i] == consonnes[j]:
                cpt_consonnes += 1
    if cpt_consonnes == len(res):
        res = syllabe(voyelles, consonnes);
        return res;

    return res;


def test_syllabe(syl, voyelles, consonnes): #test si la chaine passée en arguement est une syllabe

    if len(syl) == 1:
        if syl[0] in voyelles:
            return True;
        else:
            return False;
    
    elif len(syl) == 2:
        if syl[0] in voyelles or syl[1] in voyelles:
            return True;
        else:
            return False;
    else:
        for i in range(len(syl)):
            if syl[i] in voyelles:
                return True;
        return False;


def create_list(voyelles, consonnes):
    syllabes = [];
    nb_syllabes = 50;
    for i in range(nb_syllabes):
        syl = syllabe(voyelles, consonnes);
        test = test_syllabe(syl, voyelles, consonnes);
        if test:
            syllabes.append(syl);
    return syllabes;

    
def create_name(syllabes, i):
    name = "";

    for i in range(0,i):
        choix_syl = randint(0,len(syllabes)-1);
        name += syllabes[choix_syl];
        
    return name;


def fileReader(path):
    file = open(path,"r");
    line = file.readline();
    list_voyelles = [];
    list_consonnes = [];
    list_syllabes = [];
    while line != "END":
        if line[0] == "#":
            line = file.readline();
            continue;
        elif line[0] == "~":
            if line[1:] == "letters\n":
                line = file.readline();
                list_voyelles = list(line.split("-")[0]);
                list_consonnes = list(line.split("-")[1]);
                if list_consonnes[-1] == "\n":
                    del list_consonnes[-1];
            elif line[1:] == "syllabes\n":
                line = file.readline();
                if line != "/NONE/\n":
                    list_syllabes = line.split("-");
                    tmp = list(list_syllabes[-1])
                    if tmp[-1] == "\n":
                        del tmp[-1];
                        list_syllabes[-1] = "".join(tmp);
        line = file.readline();
    file.close();
    return list_voyelles, list_consonnes, list_syllabes;
    


main("resources/generate.txt");
