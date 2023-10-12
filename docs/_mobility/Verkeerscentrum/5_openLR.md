---
layout: default
parent: Verkeerscentrum
title: OpenLR mapping
nav_order: 6
---

# OpenLR mapping

Om OpenLR compliant te zijn, dienen volgende gegevens geweten te zijn van de verkeersmeting:
-locatieverkeersmeetpunt (x,y);
-coördinaten wegsgement;
-offset (lengte van startpunt naar locatie meetpunt)

Open vraag: zit deze data in de dataset van het verkeerscentrum

Zoniet:
Uit data van het verkeerscentrum halen we momenteel de locatie van het meetpunt. Aan de hand van een GIS functie, wordt het mogelijk om het dichtstbijzijnde wegsegment te vinden. Hierna kan de offset berekend worden.

![Alt text](https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/OpenLR_wegsegment.png)
