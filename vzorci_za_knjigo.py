import re
import operator

#===============================================#
#=====Grozem seznam izjem za črke in besede=====#
#======ki jih ločimo od seznama vseh besed======#
#===============================================#

grozen_seznam_izjem = {",",
".","?","!","«","»",":",";","(",")",
"0","1","2","3","4","5","6","7","8",
"9","-","&","'","–","/", "’","…",""}

#===================================#
#=======VSE BESEDE IZ KNJIGE:=======#
#===================================#


with open('prebrana_knjiga.txt', 'r', encoding='utf-8') as dat:

    vsebina = dat.read().lower()
    seznam_hecnih_besed = vsebina.split("\n")
    seznam_besed_s_problemom = " ".join(str(element) for element in seznam_hecnih_besed).split(" ")

    #==Odpravitev problema, kjer se je beseda razcepila zaradi preloma v novo vrstico==#

    i = 0
    while i < len(seznam_besed_s_problemom):
        beseda = seznam_besed_s_problemom[i]
        if beseda.endswith("-"):
            seznam_besed_s_problemom[i] = beseda[:-1] + seznam_besed_s_problemom[i + 1]
            del seznam_besed_s_problemom[i + 1]
        i += 1

    #==Odpravljanje nepotrebnih pik, vejic ter narekovajev v besedah==#

    i = 0
    while i < len(seznam_besed_s_problemom):
        beseda = seznam_besed_s_problemom[i]
        for znak in beseda:
            if znak in grozen_seznam_izjem:
                seznam_besed_s_problemom[i] = seznam_besed_s_problemom[i].replace(znak, "")
        i += 1

    #==Odpravitev objekta "" iz klasifikacije besede==#

    seznam_besed_s_problemom_2 = []
    for beseda_prob in seznam_besed_s_problemom:
        if beseda_prob != "":
            seznam_besed_s_problemom_2.append(beseda_prob)

    seznam_vseh_besed = seznam_besed_s_problemom_2
    



    kolicina_vseh_besed = len(seznam_vseh_besed)

    #==!!! Vse crke v knjigi !!!==#

    seznam_vseh_crk = []
    for element in seznam_vseh_besed:
        for crka in element:
            seznam_vseh_crk.append(crka)


    #==Slovar besed ter stevilo pojavitev te besede v celotni knjigi==#

    frekvenca_besed = {}
    frekvenca_crk = {}

    kolicina_vseh_crk = len(seznam_vseh_crk)

    for beseda in seznam_vseh_besed:
        if beseda in frekvenca_besed:
            frekvenca_besed[beseda] += 1
        else: 
            frekvenca_besed[beseda] = 1

    for crka in seznam_vseh_crk:
        if crka in frekvenca_crk:
            frekvenca_crk[crka] += 1
        else:
            frekvenca_crk[crka] = 1

    procent_vsake_crke_v_besedilu = {}

    for crka in frekvenca_crk:
        procent_vsake_crke_v_besedilu[crka] = round((frekvenca_crk[crka]/kolicina_vseh_crk) * 100, 2) 

   
   

    #==Seznam sto najpogostejših besed v knjigi ter njihova frekvenca==#
    
    sorted_frekvenca_besed = dict( sorted(frekvenca_besed.items(), key=operator.itemgetter(1),reverse=True))
    sorted_frekvenca_crk = dict( sorted(frekvenca_crk.items(), key=operator.itemgetter(1),reverse=True))

    sorted_delez_crk = dict( sorted(procent_vsake_crke_v_besedilu.items(), key=operator.itemgetter(1),reverse=True))
    
 



    sorted_frekvenca_besed_prvih_sto = []
    n = 0
    for element in sorted_frekvenca_besed.items():
        n += 1
        if n <= 100:
            sorted_frekvenca_besed_prvih_sto.append(element)
        else:
            break

    
    top_sto = []
    for tuple in sorted_frekvenca_besed_prvih_sto:
        top_sto.append(tuple[0])

   
   
    
    

    #==Prvih sto besed po pogostosti. (brez frekvence)==#

    top_sto_besed = top_sto
    



#===================================#
#======VZOREC PO DELIH KNJIGE:======#
#===================================#

#==Regularni izraz za zaznavanje DELOV 1-5==#

vzorec_dela = re.compile(
    r'\(\w*?\)\n' 
    r'DEL (?P<st_dela>\w*)'
    r'.*?'
    r'KONEC',
    flags=re.DOTALL)

with open('prebrana_knjiga.txt', 'r', encoding='utf-8') as dat:
    vsebina = dat.read()


#==============================================================#
#======SEZNAM, v katerem so nizi vseh petih DELOV knjige:======#
#==============================================================#

nizi_delov = []

nepomemben_objekt_1 = vzorec_dela.finditer(vsebina)
for thing in nepomemben_objekt_1:
    nizi_delov.append(thing.group(0))

seznam_seznamov_besed_v_delih = []
seznam_seznamov_crk_v_delih = []

seznam_frekvenc_besed = []
seznam_frekvenc_crk = []

seznam_stevila_besed_v_delih = []
seznam_stevila_crk_v_delih = []

seznam_procentov_crk_po_delih = []

seznam_sorted_frekvenca_besed_po_delih = []
seznam_sorted_frekvenca_crk_po_delih = []
seznam_sorted_procentov_crk_po_delih = []
seznam_sorted_frekvenca_besed_prvih_sto_po_delih = []

seznam_top_sto_po_delih = []



for del_knjige in nizi_delov:

    seznam_hecnih_besed_del = del_knjige.lower().split("\n")
    seznam_besed_s_problemom_del = " ".join(str(element) for element in seznam_hecnih_besed_del).split(" ")

  
    #==Odpravitev problema, kjer se je beseda razcepila zaradi preloma v novo vrstico==#

    i = 0
    while i < len(seznam_besed_s_problemom_del):
        beseda = seznam_besed_s_problemom_del[i]
        if beseda.endswith("-"):
            seznam_besed_s_problemom_del[i] = beseda[:-1] + seznam_besed_s_problemom_del[i + 1]
            del seznam_besed_s_problemom_del[i + 1]
        i += 1

    #==Odpravljanje nepotrebnih pik, vejic ter narekovajev v besedah==#

    i = 0
    while i < len(seznam_besed_s_problemom_del):
        beseda = seznam_besed_s_problemom_del[i]
        for znak in beseda:
            if znak in grozen_seznam_izjem:
                seznam_besed_s_problemom_del[i] = seznam_besed_s_problemom_del[i].replace(znak, "")
        i += 1

    #==Odpravitev objekta "" iz klasifikacije besede==#
 
    seznam_besed_s_problemom_2_del = []
    for beseda_prob in seznam_besed_s_problemom_del:
        if beseda_prob != "":
            seznam_besed_s_problemom_2_del.append(beseda_prob)

    seznam_vseh_besed_del = seznam_besed_s_problemom_2_del

    seznam_seznamov_besed_v_delih.append(seznam_vseh_besed_del)
    


    kolicina_vseh_besed_del = len(seznam_vseh_besed_del)

    seznam_stevila_besed_v_delih.append(kolicina_vseh_besed_del)

    #==!!! Vse crke v knjigi !!!==#

    seznam_vseh_crk_del = []
    for element in seznam_vseh_besed_del:
        for crka in element:
            seznam_vseh_crk_del.append(crka)

    seznam_seznamov_crk_v_delih.append(seznam_vseh_crk_del)

    #==Slovar besed ter stevilo pojavitev te besede v celotni knjigi==#

    frekvenca_besed_del = {}
    frekvenca_crk_del = {}

    kolicina_vseh_crk_del = len(seznam_vseh_crk_del)

    seznam_stevila_crk_v_delih.append(kolicina_vseh_crk_del)


    for beseda in seznam_vseh_besed_del:
        if beseda in frekvenca_besed_del:
            frekvenca_besed_del[beseda] += 1
        else: 
            frekvenca_besed_del[beseda] = 1

    for crka in seznam_vseh_crk_del:
        if crka in frekvenca_crk_del:
            frekvenca_crk_del[crka] += 1
        else:
            frekvenca_crk_del[crka] = 1

    seznam_frekvenc_besed.append(frekvenca_besed_del)
    seznam_frekvenc_crk.append(frekvenca_crk_del)



    procent_vsake_crke_v_besedilu_del = {}

    for crka in frekvenca_crk_del:
        procent_vsake_crke_v_besedilu_del[crka] = round((frekvenca_crk_del[crka]/kolicina_vseh_crk_del) * 100, 2) 

    seznam_procentov_crk_po_delih.append(procent_vsake_crke_v_besedilu_del)
   

    #==Seznam sto najpogostejših besed v knjigi ter njihova frekvenca==#
    
    sorted_frekvenca_besed_del = dict( sorted(frekvenca_besed_del.items(), key=operator.itemgetter(1),reverse=True))
    sorted_frekvenca_crk_del = dict( sorted(frekvenca_crk_del.items(), key=operator.itemgetter(1),reverse=True))

    sorted_delez_crk_del = dict( sorted(procent_vsake_crke_v_besedilu_del.items(), key=operator.itemgetter(1),reverse=True))
    
 



    sorted_frekvenca_besed_prvih_sto_del = []
    n = 0
    for element in sorted_frekvenca_besed_del.items():
        n += 1
        if n <= 100:
            sorted_frekvenca_besed_prvih_sto_del.append(element)
        else:
            break

    
    top_sto_del = []
    for tuple in sorted_frekvenca_besed_prvih_sto_del:
        top_sto_del.append(tuple[0])

   
    seznam_sorted_frekvenca_besed_po_delih.append(sorted_frekvenca_besed_del)
    seznam_sorted_frekvenca_crk_po_delih.append(sorted_frekvenca_crk_del)
    seznam_sorted_procentov_crk_po_delih.append(sorted_delez_crk_del)
    seznam_sorted_frekvenca_besed_prvih_sto_po_delih.append(sorted_frekvenca_besed_prvih_sto_del)
    seznam_top_sto_po_delih.append(top_sto_del)


#========================================================================#
#==================SEZNAM NIZOV VSEH POGLAVIJ============================#
#========================ZA CELO KNJIGO==================================#
#========================================================================#

nizi_poglavij = []

vzorec_poglavij = re.compile(
    r"(el (?P<st_poglavja>\d+).*?Kapitt)"
    r"|(el (?P<st_poglavja_2>\d+).*KONEC)",
    flags=re.DOTALL)

nepomemben_objekt_2 = vzorec_poglavij.finditer(vsebina)
for thing in nepomemben_objekt_2:
    nizi_poglavij.append(thing.group(0))

#====STEVILO BESED NA POGLAVJE====#

seznam_seznamov_besed_v_poglavju = []
seznam_stevila_besed_v_poglavje = []

for poglavje in nizi_poglavij:

    seznam_hecnih_besed_poglavje = poglavje.split("\n")
    seznam_besed_s_problemom_poglavje = " ".join(str(element) for element in seznam_hecnih_besed_poglavje).split(" ")

  
    #==Odpravitev problema, kjer se je beseda razcepila zaradi preloma v novo vrstico==#

    i = 0
    while i < len(seznam_besed_s_problemom_poglavje):
        beseda = seznam_besed_s_problemom_poglavje[i]
        if beseda.endswith("-"):
            seznam_besed_s_problemom_poglavje[i] = beseda[:-1] + seznam_besed_s_problemom_poglavje[i + 1]
            del seznam_besed_s_problemom_poglavje[i + 1]
        i += 1

    #==Odpravljanje nepotrebnih pik, vejic ter narekovajev v besedah==#

    i = 0
    while i < len(seznam_besed_s_problemom_poglavje):
        beseda = seznam_besed_s_problemom_poglavje[i]
        for znak in beseda:
            if znak in grozen_seznam_izjem:
                seznam_besed_s_problemom_poglavje[i] = seznam_besed_s_problemom_poglavje[i].replace(znak, "")
        i += 1

    #==Odpravitev objekta "" iz klasifikacije besede==#
 
    seznam_besed_s_problemom_2_poglavje = []
    for beseda_prob in seznam_besed_s_problemom_poglavje:
        if beseda_prob != "":
            seznam_besed_s_problemom_2_poglavje.append(beseda_prob)

    seznam_vseh_besed_poglavje = seznam_besed_s_problemom_2_poglavje

    seznam_seznamov_besed_v_poglavju.append(seznam_vseh_besed_poglavje)
    


    kolicina_vseh_besed_poglavje = len(seznam_vseh_besed_poglavje)

    seznam_stevila_besed_v_poglavje.append(kolicina_vseh_besed_poglavje)

#========================================================================#
#=======NABORI VSEH SEZNAMOV/SLOVARJEV, KI SEM JIH ZE ZGORAJ DOBIL=======#
#==========================ZA CELO KNJIGO================================#
#========================================================================#
#
# SEZNAMI VSEH BESED / CRK V KNJIGI IN 
#
seznam_vseh_besed
seznam_vseh_crk
top_sto_besed
#
# ST. POJAVITEV BESED / CRK
#
frekvenca_besed
frekvenca_crk
#
# UREJENI SLOVARJI, PO PADANJU (DESCENDING) FREKVENC POJAVITVE OBJEKTOV
#
sorted_frekvenca_besed
sorted_frekvenca_crk
sorted_frekvenca_besed_prvih_sto
#
# ST. POJAVITEV TEH CRK
#
sorted_delez_crk
procent_vsake_crke_v_besedilu
#
# KOLICINA OBJEKTOV (DOLZINA)
#
kolicina_vseh_besed
kolicina_vseh_crk
#
#
#
#========================================================================#
#======SEZNAMI, V KATERIH SO DEFINIRANI OBJEKTI ZA POSAMEZNE DELE.=======#
#============================ZA DELE OD 1-5==============================#
#========================================================================#
#
# TO SO NIZI DELOV 1-5
#
nizi_delov
#
# SEZNAMI, V KATERIH SO SEZNAMI BESED, CRK V DELIH OD 1-5, ter stevilo vseh besed v DELIH 1-5
#
seznam_seznamov_besed_v_delih
seznam_seznamov_crk_v_delih
#
# FREKVENCE POJAVITEV BESED IN CRK V DELIH 1-5 (!!! NEUREJENO !!!)
#
seznam_frekvenc_besed
seznam_frekvenc_crk
#
# STEVILO BESED IN STEVILO CRK V DELIH 1-5 (LENGHT SEZNAMA NA BESEDAH / CRKAH)
#
seznam_stevila_besed_v_delih
seznam_stevila_crk_v_delih
#
# PROCENT, KOLIKOKRAT SE CRKA POJAVI V DELU 1-5 GLEDE NA STEVILO BESED V DELIH 1-5
#
seznam_procentov_crk_po_delih
#
# SORTIRANI SEZNAMI PO PADANJU FREKVENCE BESED IN CRK PO DELIH 1-5, PADANJU PROCENTOV (!!! UREJENO !!!)
#
seznam_sorted_frekvenca_besed_po_delih
seznam_sorted_frekvenca_crk_po_delih
seznam_sorted_procentov_crk_po_delih
#
# ANALIZA PRVIH 100, FREKVENCA NAJPOGOSTEJSIH 100 BESED, SEZNAM TOP 100 BESED, OBOJE PO DELIH 1-5
#
seznam_sorted_frekvenca_besed_prvih_sto_po_delih
seznam_top_sto_po_delih
#============================================================
#
#
#========================================================================#
#======================NIZI POGLAVIJ 1-38================================#
#========================================================================#
#
nizi_poglavij
#
#
# STEVILO BESED V VSAKEM POGLAVJU OD 1.-38.
# 
seznam_stevila_besed_v_poglavje
#
#========================================================================#


regular_svetih_stirih= re.compile(r"Kapittel (?P<st_poglavja>\w*)"
"\n(?P<cas_dogajanja>.*)\.\n(?P<naslov>.*)")

naslovi_poglavij = []
nepomemben_objekt_3 = regular_svetih_stirih.finditer(vsebina)
for thing in nepomemben_objekt_3:
    naslovi_poglavij.append(thing.groupdict())




regular_ostalih = re.compile(r"Kapittel (?P<st_poglavja>\w*)"
"\nDag (?P<st_dneva>\w*?)\. (?P<naslov>.*)")
 
nepomemben_objekt_4 = regular_ostalih.finditer(vsebina)
for thing in nepomemben_objekt_4:
    naslovi_poglavij.append(thing.groupdict())


naslovi_poglavij.append({'st_poglavja': '38', 'cas_dogajanja': 'Desember 2004', 'naslov': 'Svanene'})
naslovi_poglavij.append({'st_poglavja': '5', 'cas_dogajanja': '4. november 1992', 'naslov': 'Totempælen'})


seznam_1 = []
for beseda in top_sto_besed:
    seznam_1.append((beseda, seznam_frekvenc_besed[0][beseda.lower()]))

seznam_2 = []
for beseda in top_sto_besed:
    seznam_2.append((beseda, seznam_frekvenc_besed[1][beseda.lower()]))

seznam_3 = []
for beseda in top_sto_besed:
    seznam_3.append((beseda, seznam_frekvenc_besed[2][beseda.lower()]))

seznam_4 = []
for beseda in top_sto_besed:
    seznam_4.append((beseda, seznam_frekvenc_besed[3][beseda.lower()]))

seznam_5 = []
for beseda in top_sto_besed:
    seznam_5.append((beseda, seznam_frekvenc_besed[4][beseda.lower()]))




seznam_triplov = []

k = 1
for slovar in naslovi_poglavij:
    seznam_triplov.append((int(slovar['st_poglavja']), slovar['naslov'], seznam_stevila_besed_v_poglavje[int(slovar['st_poglavja']) - 1]))
    k += 1

seznam_triplov.sort()


seznam_tuplov = []
for key in sorted_frekvenca_crk:
    seznam_tuplov.append((key, sorted_frekvenca_crk[key]))


#________________________________________
#REGULAR ZA NASLOV POGLAVJA: 1, 2, 33
#________________________________________
# 
#
#
#
#
#   |----------->  Kapittel (?P<st_poglavja>\w*)\n(?P<cas_dogajanja>.*)\.\n(?P<naslov>.*)
#     
#
#
#
#
#       <st_dneva> pri 2 poglavju je = 1 (izjema)
#
#_________________________________________
#REGULAR ZA NASLOV POGLAVJA: 38 (POSEBENO)
#_________________________________________
#
#
#
#
#   |----------->  Kapittel 38\n(?P<cas_dogajanja>.*) (?P<naslov>.*)
#
#
#
#
#_________________________________
#REGULAR ZA NASLOVE: VSEH OSTALIH (razen 5)
#_________________________________
#
#
#
#   |----------->  Kapittel (?P<st_poglavja>\w*)\nDag (?P<st_dneva>\w*?)\. (?P<naslov>.*)
#
#
#
#
#
#
#  !!!  <cas_dogajanja> je datum, v katerem se poglavje odvija
#  !!!  <st_dneva> je stevilo dneva v katerem se odvija zgodba, zacne se z dnevom 1 (poglavja 1,5,33,38) nimajo določenega stevila dneva
#  !!!  <naslov> je cisto pri vseh naslov poglavja











