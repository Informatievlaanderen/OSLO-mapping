---
layout: default
title: Hoppinpunten
has_children: true
---

# Verkeerscentrum - Meten-in-Vlaanderen (MIV)

<div style="text-align: left;"><img src="https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/verkeerscentrum.jpg" width="200" alt="My Image" id="hp"></div>

- Deze gegevens zijn afkomstig van dubbele meetlussen, hoofdzakelijk op snelwegen in het Vlaams gewest.
- Verantwoordelijken voor deze gegevens zijn het [Agentschap Wegen en Verkeer (AWV)](http://www.wegenenverkeer.be) en het [Vlaams Verkeerscentrum (VVC)](http://www.verkeerscentrum.be).
- De gegevens bevatten o.a. aantallen voertuigen en gemiddelde snelheden, opgedeeld in 5 voertuigklassen, per minuut geaggregeerd en de bijhorende locaties van de meetlussen.
- De gegevens worden elke minuut geüpdatet.
- Rijstroken logica:
  - R: rijstrook
  - B: Bijzonder Overrijdbare Bedding (BOB) of busbaan
  - TR: meting van het verkeer in inOppositeDirectione richting (meestal bij Tunnels) op de R-rijstrook
  - P: Pechstrook
  - W: parking of andere weg
  - S: spitsstrook
  - A: meetpunt op een gearceerd gedeelte van de weg

De nummering start bij R10 voor de eerste reguliere rijstrook op de hoofdrijbaan. De nummering stijgt van rechts/trager naar links/sneller.

Rijstroken met 09, 08, 07, ... liggen hier dan rechts van en stellen meestal op- en afritten, invoegstroken, net bijgekomen rijstroken, spitsstroken of BOB's voor.

Rijstroken 11, 12, 13, ... liggen dan links van de rijstrook R10.

Het nummer 00 wordt gebruikt voor een meetpunt op de pechstrook (P00).

De TR-rijstrook is identiek aan de overeenkomstige R-rijstrook (TR10=R10,TR11=R11,TR12=R12,...), alleen geeft het meetpunt enkel de minuutdata van het "spookverkeer" door.

(De meetgegevens voor TR10 zijn afkomstig van dezelfde meetlussen als deze voor R10.)

Data set meetpunten: [Meetpunten Verkeerscentrum](https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/%C2%B4meetpunten_verkeerscentrum.json)
Data set verkeersmeting: [Verkeersmeting Verkeerscentrum](https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/verkeerscentrum.json)

<p align="center"><img src="https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/Verkeerscentrum_schets.jpg" width="60%" text-align="center"></p>
