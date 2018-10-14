#générateur de syllabes/noms

from random import *
import os


isto_voyelles = ["a","e","i","o","y"]
isto_consonnes = ["c","d","l","m","n","r","s","t","v"]
isto_syl = ["ter", "les", "las", "yl", "ac", "ni"];


def main():
    isto_list = create_list(isto_voyelles, isto_consonnes);
    
    fichier = open("resources/2syl.txt","w");
    for i in range(0,100):
        fichier.write(create_name(isto_list,2)+"\n");
    fichier.close();

    fichier = open("resources/3syl.txt","w");
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


main();
