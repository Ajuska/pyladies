def precti_znaky(soubor):
    "Vezme soubor a nacte z neho spravne znaky bez mezer a koncu radku"
    with open(soubor, encoding='utf-8') as soubor:
        list_znaku = list()
        list_iterovany = list(soubor.read())
        for znak in list_iterovany:
            if znak is not '\n':
                list_znaku.append(znak)
    return list_znaku

list_hiragana = precti_znaky('hiragana.txt')
list_katakana = precti_znaky('katakana.txt')

print(list_hiragana)
print(list_katakana)


with open('rozsypanycaj.txt', encoding='utf-8') as soubor:
    retezec = soubor.read()
    pocet_hiragany = 0
    pocet_katakany = 0
    for znak in retezec:
        if znak in list_hiragana:
            pocet_hiragany = pocet_hiragany + 1
        if znak in list_katakana:
            pocet_katakany = pocet_katakany + 1

    print(pocet_hiragany)
    print(pocet_katakany)
