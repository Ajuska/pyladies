from random import randrange

from tah import tah


def tah_pc(pole_pc, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if symbol == "o":
        symbol2 = "x"
    else:
        symbol2 = "o"

    assert len(pole_pc) >= 3, "Příliš krátké pole."
    assert "-" in pole_pc, "Nemám kam hrát."

    if ("-"*len(pole_pc)) in pole_pc:
        cislo_policka_pc = len(pole_pc) - 3
    elif symbol+symbol+"-" in pole_pc:  #oo-
        cislo_policka_pc = pole_pc.index(symbol+symbol+"-")+2
    elif "-"+symbol+symbol in pole_pc: #-oo
        cislo_policka_pc = pole_pc.index("-"+symbol+symbol)
    elif symbol2+"-"+symbol2 in pole_pc: #x-x
        cislo_policka_pc = pole_pc.index(symbol2+"-"+symbol2)+1
    elif symbol2+symbol2+"-" in pole_pc: #xx-
        cislo_policka_pc = pole_pc.index(symbol2+symbol2+"-")+2
    elif "-"+symbol2+symbol2 in pole_pc: #-xx
        cislo_policka_pc = pole_pc.index("-"+symbol2+symbol2)
    elif symbol2+"---"+symbol2 in pole_pc: #x---x
        cislo_policka_pc = pole_pc.index(symbol2+"---"+symbol2)+2
    elif symbol+"-" in pole_pc: #o-
        cislo_policka_pc = pole_pc.index(symbol+"-")+1
    elif "-"+symbol in pole_pc: #-o
        cislo_policka_pc = pole_pc.index("-"+symbol)
    elif "-"+symbol2 in pole_pc: #-x
        cislo_policka_pc = pole_pc.index("-"+symbol2)
    elif symbol2+"-" in pole_pc: #x-
        cislo_policka_pc = pole_pc.index(symbol2+"-")+1
    else:
        while True:
            cislo_policka_pc = randrange(0,len(pole_pc))

            if pole_pc[cislo_policka_pc] == "-":
                break

    upravene_pole_pc = tah(pole_pc, cislo_policka_pc, symbol)
    return upravene_pole_pc
