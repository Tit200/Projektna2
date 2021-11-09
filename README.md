# Projektna_naloga_2

To je moja projektna naloga pri predmetu Programiranje 1.

Naslov: Analiza frekvence pojavitev določenih besed v knjigi, glede na poglavja in dele.

Podatke bom analiziral iz knjige od avtorja: Jo Nesbø, naslov knjige je pa: Snømannen (Snežak).
Knjigo bom pripel sem v .pdf obliki. 
PDF knjige: [jo_nesbø_Snømannen.pdf](https://github.com/Tit200/Projektna2/files/7374107/jo_nesbo_Snomannen.pdf)

# Ideje:
- Pogledal bom katere besede se največkrat ponovijo skozi celotno knjigo in 
jih prevedel v slovenščino, da dobimo občutek za to, katere besede pogosto uporabljajo,
- preverili bomo katere besede so najpogostejše glede na določena poglavja in to primerjali z naslovom poglavij in
videli, kako tema/naslov poglavja vpliva na rabo besed,
- izčrpali bomo frekvenco pojavitev imen v celotni knjigi ter glede na poglavja in dele knjige (jih je 5),
- razvrstili bomo poglavja in dele glede na količino besed v le-teh,
- preverili bomo koliko krat v tej knjigi se pojavi vsaka izmed črk norveške abecede ter primerjali te podatke s statistiko frekvenc črk, v tem jeziku, po raziskavi:
https://www.sttmedia.com/characterfrequency-norwegian#letters .

# Hipoteze:
- Moja hipoteza glede na najpogostejše besede je, da bo med njimi verjetno beseda "som", ki pomeni "ki/kot" ter morda "Han" ali "Hun", ki pomenita "On" ali "Ona",
- sklepam, da bo tema poglavja vplivala na pojavitve besed in da bo pomen teh besed vezan (vsaj do neke mere) na temo poglavja,
- sklepam, da bo največkrat omenjen "Harry Hole" oz. katerakoli izmed "Harry" in "Hole", saj je to glavni karakter, verjetno bo zelo pogosta tudi beseda "detektiv" (isti pomen v slo.),
- na to katero poglavje vsebuje največ besed ne moram sklepati, lahko pa ugibam, da bo največ besed vseboval Del 4, saj vsebuje največ poglavij,
- sklepam lahko, glede na to, da je knjiga kar obsežna (kriminalni roman), da se bo frekvenca pojavitev črk kar dobro ujemala s predvideno statistiko na zgoraj omenjenem linku.

# Csv datoteke vsebujejo:
- Csv datoteke poimenovane od "csv_file_1_1.csv" do "csv_file_1_6.csv", vsebujejo sto najpogostejših besed, ki se pojavijo v knjigi, kolikokrat se pojavijo v knjigi, ter kolikokrat se te besede pojavijo v petih Delih knjige,
- Csv datoteka poimenovana "csv_file_2.csv", vsebuje številke poglavij, njihove naslove ter število besed, ki so vsebovane v teh poglavjih,
- Csv datoteka poimenovana "csv_file_3.csv", vsebuje črke, ki se pojavijo v knjigi, ter njihovo frekvenco.
