import pdfplumber

pot = 'jo_nesbø_Snømmanen.pdf'

with pdfplumber.open(pot) as pdf:
    with open('prebrana_knjiga.txt', 'a', encoding='utf-8') as dat:
        for page_number in range(905):
            st_dela = 0
            if (page_number + 1) not in {193, 362, 485, 767}:
                dat.write(f'({page_number + 1})')
                dat.write('\n')
                dat.write(pdf.pages[page_number].extract_text(x_tolerance=3, y_tolerance=3))
                dat.write('\n')
            else:
                slovar_posebnih_strani = {193: 1, 362: 2, 485: 3, 767: 4}
                dat.write(f'({page_number + 1})')
                dat.write('\n')
                dat.write(pdf.pages[page_number].extract_text(x_tolerance=3, y_tolerance=3))
                dat.write('\n')
                dat.write(f'KONEC DELA {slovar_posebnih_strani[page_number + 1]}')
                dat.write('\n')
with open('prebrana_knjiga.txt', 'a', encoding='utf-8') as dat:
    dat.write('KONEC')