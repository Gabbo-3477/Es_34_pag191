prenotazioni=[]
lettera_sì=[]
lettera_no=[]

while True:
    dati_pren=input("Scrivi nome e cognome del partecipante: (Scrivi STOP per interrompere la lista) ")
    if dati_pren=="STOP":
        break
    else:
        prenotazioni.append(dati_pren)
        richesta_lettera=input("Il partecipante deve ricevere una lettera di conferma? ")
        if richesta_lettera=="Sì":
            lettera_sì.append(dati_pren)
        elif richesta_lettera=="No":
            lettera_no.append(dati_pren)

print("I partecipanti che devono ricevere una lettera di conferma sono:", lettera_sì)  