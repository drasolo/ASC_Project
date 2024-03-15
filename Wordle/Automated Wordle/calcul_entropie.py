from words import words
import math
import copy

helperwords = words.copy()

def algorithm():
    
    global helperwords

    #citirea celor 2 string-uri

    f = open("fisier.txt", "r")
    bestword = f.readline()
    fb = f.readline() 
    f.close()
    
    #aici am taiat \n

    bestword = bestword[:5]
    
    def words_out(xd, feedback):
        newlistt = []
        for i in xd:
            a = letter_by_letter_words_out(bestword, i, feedback)
            if a!= 0:
                newlistt.append(a)
        return newlistt

    def letter_by_letter_words_out(bestword, given_word, feedbackk):
        formation = ""
        for y in range(5):
            if given_word[y] == bestword[y]:
                formation += '3'
            elif bestword[y] in given_word:
                formation += '2'
            else:
                formation += '1'
        if formation == feedbackk:
            return given_word
        else:
            return 0

    # Aici se termina
    # Are acelasi mecanism ca si facutul tuturor posibilitatilor, doar ca aici stie ce posibilitate sa caute si scoate toate cuvintele care sunt asa si le baga intr-o lista noua.
    # 1.END





    # 4.START
    def letter_by_letter(given_word, random_word):
        formation = ""
        # Initializez un string gol pe care urmeaza sa il umplu cu cate o cifra pt fiecare litera din cuvant.
        # Iau fiecare litera in parte din cuvantul incercat si vede daca e gri, galben sau verde in joc.
        # Daca este gri, ii dau valoarea 1
        # Daca este galben, ii dau valoarea 2
        # Daca este verde, ii dau valoarea 3
        # Tehnica functioneaza pentru ca initializez un vector de frecventa cu fiecare posibila formatie de culori(fiecare litera din cuvant are culoarea gri,galben sau verde si am facut un vector cu fiecare din posibilitatile astea)
        for y in range(5):
            if given_word[y] == random_word[y]:
                formation += '3'
            elif random_word[y] in given_word:
                formation += '2'
            else:
                formation += '1'
        helper = int(formation)
        # Number_of_posibilities este vectorul de frecventa cu fiecare posibilitate de asezat culorile, urmand ca acesta sa fie criteriul prin care dau afara cuvintele cand primesc feedback ul de la programul lui Iustin
        Number_of_posibilities[helper] += 1
    #4.END


    # 3.START
    def table(the_word):
        # Iau fiecare cuvant pe rand si ii fac formatia de litere in functie de cuvantul preselectat.
        for x in range(number_of_words):
            letter_by_letter(the_word, helperwords[x])
        return entropy()
    # 3.END 
    

    # 5.START
    def entropy():
        # Calculeaza entropia in functie de toate posibilitatile de culori care se pot forma dupa formula de entropie.
        entropy = 0
        for i in range(33334):
            pi = Number_of_posibilities[i] / (number_of_words*1.0)
            if pi != 0:
                entropy += pi * math.log(1/pi,2)
        return entropy
    # 5.END


    Number_of_posibilities = [int(0)] * 33334 
    max_entropy = -1
    word_with_max = ""
    actual_entropy= -1
    newlist = []
    newlist = words_out(helperwords, fb)
    helperwords = copy.deepcopy(newlist)
    
    newlist.clear()
    number_of_words = len(helperwords)
    
    # 2.START
    for k in range(number_of_words):
        
        # Iau cuvant cu cuvant si calculez entropia lui
        actual_entropy = table(helperwords[k])
        # Retin entropia maxima si cuvantul care o are.
        if max_entropy < actual_entropy:
            max_entropy = actual_entropy
            word_with_max = helperwords[k]
        # Resetez vectorul de frecventa ca sa nu se suprapuna cu calculele de la celelalte cuvinte   
        Number_of_posibilities = [int(0)] * 33334 
    # 2.END
    
    #afisarea celui mai bun cuvant
   
    f = open("fisier.txt","w")
    f.write(word_with_max)
    f.close()
