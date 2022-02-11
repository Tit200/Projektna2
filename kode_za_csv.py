import vzorci_za_knjigo
import csv 
#=======================PRVA TABELA================================#
#==================================================================#

with open('csv_file_1_1.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v celotni knjigi'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.sorted_frekvenca_besed_prvih_sto:
        writer.writerow(vrstica)

with open('csv_file_1_2.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v DELU I'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.seznam_1:
        writer.writerow(vrstica)
    
with open('csv_file_1_3.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v DELU II'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.seznam_2:
        writer.writerow(vrstica)
    
with open('csv_file_1_4.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v DELU III'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.seznam_3:
        writer.writerow(vrstica)

with open('csv_file_1_5.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v DELU IV'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.seznam_4:
        writer.writerow(vrstica)

with open('csv_file_1_6.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['Top sto besed', 'Frekvenca besed v DELU V'] 
    writer.writerow(header)
    for vrstica in vzorci_za_knjigo.seznam_5:
        writer.writerow(vrstica)

#===================================================================#

#=======================DRUGA TABELA================================#
#==================================================================#

with open('csv_file_2.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    header = ['St. poglavja', 'Naslov poglavja', 'St. besed v poglavju'] 
    writer.writerow(header)
    for triple in vzorci_za_knjigo.seznam_triplov:
        writer.writerow(triple)


#=======================TRETJA TABELA==============================#
#==================================================================#

with open('csv_file_3.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    header = ['Crka', 'Frekvenca crke v knjigi'] 
    writer.writerow(header)
    for tuple in vzorci_za_knjigo.seznam_tuplov:
        writer.writerow(tuple)
    
with open('csv_file_4.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    header = ['Crka', 'Procent crke v knjigi'] 
    writer.writerow(header)
    for tuple in vzorci_za_knjigo.seznam_tuplov_2:
        writer.writerow(tuple)