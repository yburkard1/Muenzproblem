def geldboerse():
    """ der Geldbeutel wird definiert """

    gesamt = 0

    #Geldbeutel
    bargeld = {
        0.01:3,
        0.02:3,
        0.05:3,
        0.1:3,
        0.2:3,
        0.5:3,
        1:3,
        2:3
        }

    for k,v in bargeld.items():
        gesamt = gesamt + k * v

    return gesamt, bargeld


def ausgeben(betrag, bargeld):
    """ Für den Betrag wird das passende Kleingeld zusammengesucht """

    bezahlen = 0
    muenzen = []
    anzahl = []

    #Bargeld wird aufgespalten in 2 Listen, muenzen und anzahl
    #Es wird solange Geld hinzugefügt, bis der Betrag gedeckt ist 
    for k,v in bargeld.items():
        muenzen.insert(0, k)
        anzahl.insert(0, v)
        bezahlen = bezahlen + k * v
        if bezahlen >= betrag:
            break

    aussortieren = bezahlen
    laenge = len(muenzen)

    #Die Liste wird jetzt korrigiert, da (meistens) noch zu viel Geld darin ist.
    #Dazu wird von oben nach unten geschaut, wieviel (anzahl) von bestimmten Münzen/Scheinen (muenzen)
    #man aus der Liste entfernen muss, um möglichst viele Münzen/Scheine abzugeben, aber ohne unter den 
    #Zahlbetrag zu kommen.
    for x in range(laenge):
        if betrag <= (aussortieren - muenzen[x]):
            for y in range(anzahl[x]):
                if betrag <= (aussortieren - muenzen[x]):
                    aussortieren = aussortieren - muenzen[x]
                    anzahl[x] = anzahl[x] - 1
                    if anzahl[x] == 0:
                        break

    laufen = True
    x = 0

    #Die Liste wird jetzt bereinigt, d. h. alle Münzen/Scheine mit Anzahl 0 werden gelöscht.
    while laufen == True:
        if anzahl[x] == 0:
            del muenzen[x]
            del anzahl[x]
            x = x - 1
        x = x + 1
        laenge = len(anzahl)
        if x == laenge:
            laufen  = False

    bargeld = {}
    
    #Die einzelne Werte werden in ein lesbares Format gebracht.
    for x in range(laenge):
        if muenzen[x] == 0.01:
            bargeld["1Cent"] = anzahl[x]
        elif muenzen[x] == 0.02:
            bargeld["2Cent"] = anzahl[x]
        elif muenzen[x] == 0.05:
            bargeld["5Cent"] = anzahl[x]
        elif muenzen[x] == 0.1:
            bargeld["10Cent"] = anzahl[x]
        elif muenzen[x] == 0.2:
            bargeld["20Cent"] = anzahl[x]
        elif muenzen[x] == 0.5:
            bargeld["50Cent"] = anzahl[x]
        elif muenzen[x] == 1:
            bargeld["1Euro"] = anzahl[x]
        elif muenzen[x] == 2:
            bargeld["2Euro"] = anzahl[x]

    return bargeld


if __name__ == "__main__":

    #zählt das Geld im Portmonaie und gibt es aus
    gesamt, bargeld = geldboerse()
    print("Guthaben:{}".format(gesamt))

    #zu zahlender Betrag wird eingegeben
    betrag = float(input("Betrag:"))

    #Nach der Prüfung, ob zu wenig oder genau richtig viel Geld im Geldbeutel ist
    #wird die passende Zusammensetzung des Kleingelds gesucht, um möglichst viele Münzen loszuwerden
    if betrag > gesamt:
        print("Nicht genug Geld.")
    elif betrag == gesamt:
        print("Alles")
    else:
        bezahlen = ausgeben(betrag, bargeld)
        print(bezahlen)