def main():
    """
    Comment
    """


print("-= Homework Lesson 2 =-")
print("")
print("- PROBLEMA 1 -")
print("")
print("Ce valoare o sa contina variabila a după execuția codului ?")
print("")
print("a = 10")
print("a += len(str(a))")
print("a = str(a)")
print("")
a = 10

a += len(str(a))
a = str(a)
print("Răspuns: " + str(a))
print("")
print("Press Enter key to continue...")
enterKey = input()


print("")
print("- PROBLEMA 2 -")
print("")
print("Codul de mai jos conține o eroare, modificați codul astfel încît programul să funcționze corect. ")
print('"In padurea cu alune aveau casa" + 2 + "pitici"')
print("")
print("Explicație   : Trebuie de adus numeralul 2 la tipul string aplicînd fucția str()")
print('Răspuns      : "In padurea cu alune aveau casa" + str(2) + "pitici"')
print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PROBLEMA 3 -")
print("")
print("Ce valoare o sa contina variabila a dupa executia codului ?")
print("a = 10")
print("a + 1")
print("")
print("Explicație   : în al doilea statement rezultatul calcului nu se păstreaza, deaceea valoarea lui a va rămine din statement-ul precedent")
a = 10
a + 1
print("Răspuns      : " + str(a))
print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PROBLEMA 4 -")
print("")
print("Codul de mai jos contine o erroare, Modificati codul ca să nu apară erroare?")
print("a = input()")
print("a += 1")
print("")
print("Explicație   : funcția input returneaza tip String, iar operatorul += este definit pentru int. Pentru corectarea codului urmează de adus variabila 'a' la tipul int aplicînd funcția int()")
print("Răspuns      : a = int(input())")
print("             : a += 1")
print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PROBLEMA 5 -")
print("")
print("Scrieți un program care primește la input numele fisierului (text.txt, program.java) si intoarce extesia lui (txt, java). Puteti sa folositi functia split()")
print("")
print("")
print("Introduceți numele fișierului: ")
denumirea = input()
parsate = denumirea.split(".", 1)
print("Extensia fișierului introdus este: " + parsate[1])
print("")
print("Press Enter key to continue...")
enterKey = input()


print("")
print("- PROBLEMA 6 -")
print("")
print("Fie următoarea listă: a = ['a', 'b', 'c', 'd']")
a = ['a', 'b', 'c', 'd']

print("")
print("- PUNCTUL 6.1 -")
print("Ce valoare are expresia a[int(int('3' * 2) // 11)] ?")
print("ordinea operațiilor este următoarea  1.  '3'*2 = '33'")
print("                                     2.  int('33') = 33 ")
print("                                     3.  33 // 11 = 3 ")
print("                                     4.  int(3) = 3")
print("                                     5.  a[3] = 'd' ")
print("Răspuns:  " + a[int(int('3' * 2) // 11)] )
print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PUNCTUL 6.2 -")
print("Adaugati o valoare nouă în lista a pe prima poziție")
print("")
print("introduceți valoarea elementului de adăugat...")
a.insert(0,input())
print("lista nou creată este: ")
print(a)
print("")
print("Press Enter key to continue...")
enterKey = input()


print("")
print("- PUNCTUL 6.3 -")
print("Ștergeți ultimele 2 valori din lista")
print("")
print("apăsați tasta enter pentru a sterge ultimele doua valori din lista..")
enterKey = input()
print("s-a sters: " + a.pop())
print("s-a sters: " + a.pop())
print("")
print("lista actualizată este: ")
print(a)
print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PUNCTUL 6.4 -")
print("Ordonati lista a descrescator")
print("")
print("lista inițială: ")
print(a)
enterKey = input()
a.sort(reverse=True)
print("lista sortată: " )
print(a)


print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PUNCTUL 6.5 -")
print("Creați o listă nouă b care sa conțină toate elementele din lista a cu excepția primelor 2 elemente")
print("")

print("lista a este")
print(a)
b = a[2:]
print("lista b creată este: ")
print(b)

print("")
print("Press Enter key to continue...")
enterKey = input()

print("")
print("- PROBLEMA 7 -")
print("")
print("Scrieți un program care afișează toate elementele din un invetar si calculează suma lor.")
d = {"scanue": 33, "mese": 22, "fotolii": 11}
print()
print("inventarul este: ")
print(d)
enterKey = input()
print("suma valorilor din inventar este: "+ str(sum(d[item] for item in d)))


enterKey = input()
enterKey = input()
