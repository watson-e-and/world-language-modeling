#extracting L1 and L2 speakers from dataset using regex

import os, glob

def populations(txt):
    i = 0
    txt = txt.split(" ")
    total, l1, l2 = 0, 0, 0
    while i < len(txt):
        #change the numerical commas value to an integer
        word = txt[i]
        parse = word.replace(",","")
        if word == "L1":
            j = i+1
            while j < len(txt) and True:
                next_word = txt[j]
                parse = next_word.replace(",","")
                if parse.isdigit():
                    l1 = int(parse)
                    break
                j = j + 1 
            i = j
        elif word == "L2":
            j = i+1
            while j < len(txt) and True:
                next_word = txt[j]
                parse = next_word.replace(",","")
                if parse.isdigit():
                    l2 = int(parse)
                    break
                j = j + 1 
            i = j
        else:
            if parse.isdigit():
                total = int(parse)
        i = i + 1
    return (total, l1, l2)
    
 
def main():
    editions = ['16','17','18','19','20','21','22','23','25']
    languages = ['eng', 'fra','hin','ind','jpn','pcm','por','rus','spa','urd','arz','ben','cmn','deu']
    
    language_dict = {}
    for language in languages:
        language_dict[language] = {} #each key store a dictionary with all the countries and the year
        for i in range(len(editions)):
            fi = open(f'./data/{editions[i]}{language}.txt', 'r')
            for line in fi:
                [country, txt] = line.split("\t")
                if country in language_dict[language]:
                    language_dict[language][country][i] = populations(txt)
                else:
                    language_dict[language][country] = [0]*len(editions)
                    language_dict[language][country][i] = populations(txt)
            fi.close()
            
    output_fi = open('populations.tsv', 'a')
    for lang in language_dict.keys():
        for cntry in language_dict[lang]:
            li = f'{lang}\t{cntry}\t'
            for j in language_dict[lang][cntry]:
                li = li + f'{j}\t'
            li = li + "\n"
            output_fi.write(li)
    output_fi.close()
    return    
if __name__ == "__main__":
    main()