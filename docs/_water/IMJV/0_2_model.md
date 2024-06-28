---
layout: default
title: Implementatie model
parent: IMJV
nav_order: 2
---

## Intro

Het OSLO model [`waterkwaliteit`](https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit) werd gebruikt als basis om deze dataset te converteren naar een OSLO compliant dataset.


Concreet werden volgende klasses gebruikt, maar gemapt op SSN/SOSA ipv ISO19156:
* Observatie (sosa:Observation)
* Kenmerktype (sosa:ObservableProperty)
* Object (sosa:FeatureOfInterest)
* Emissie (wk:Emissie)

Een uitbreiding werd gemaakt met volgende klasses:
* Emissiepunt (imjv:Emissiepunt)
* Exploitatie (imjv:Exploitatie)

Het beschrijven van jaar-specifieke versie's van Exploitaties en Emissiepunten werd gedaan met tijdsspecialisaties uit OSLO generiek (`https://data.vlaanderen.be/ns/generiek#isTijdspecialisatieVan`)

<br>
<br>

## Implementatiemodel volgens SSN/SOSA

Met dank aan departement Omgeving werd het implementatiemodel als volgt opgesteld:

![alt text](image-2.png)

Een belangrijk verschil met OSLO waterkwaliteit is dat de specifieke kenmerken en parameters (bruto vracht, concentratie, debiet...) werden uitgemodelleerd op Kenmerktype in plaats van subklasses.

## OSLO Waterkwaliteit

<div id="enlargeImage">
<a href="https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit/kandidaatstandaard/2023-06-01/html/overview.jpg"><img src="https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit/kandidaatstandaard/2023-06-01/html/overview.jpg" width="100%" text-align="center"></a>
</div>