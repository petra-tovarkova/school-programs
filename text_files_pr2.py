with open ("Dokument.txt", encoding="utf-8") as file:
#task a
    print("Křestní jména obsahující dvě a/A:")
    for line in file:
        jmeno, prijmeni, prumer = line.split()
        if ('a' in jmeno or 'A' in jmeno) and len(jmeno) == 2:
            print(jmeno)

#task b
    print("Průměr žáku s příjmením na S:")
    for line in file:
        if ('S' in prijmeni):
            print(prumer)

#task c
    print(("Chcete do dokumentu přidat dalšího žáka?"))
    x = input("Odpovídejte ano/ne:")
    ano = ["ano","Ano"]
    if x.strip() in ano:
        with open ("Dokument.txt", mode="a", encoding="utf-8") as file:
            print("Zadejte jméno, příjmení a průměr žáka:")
            file.write(print())
            file.write(input())
    print("Celý seznam studentů:")
    for line in file:
        print(jmeno, prijmeni, prumer)
    
#task d
    if ('ch' in jmeno or 'Ch' in jmeno) or ('ch' in prijmeni or 'Ch' in prijmeni):
        print("Údaje o žácích s ch ve jméně:")
        print(jmeno, prijmeni, prumer)
        print()
    