---
layout: default
title: Input data
parent: Fietstelpunten
nav_order: 0
---

## Input data

Gegevens komen van een tellus van AWV. Datasets worden in bulk gepubliceerd via [](https://opendata.apps.mow.vlaanderen.be/fietstellingen/index.html)

Hierover dit:
Meetpunt (blauwe pin op de kaart) ligt langs een fietsbrug in Machelen en meer bepaald langs Wegsegment https://data.vlaanderen.be/id/wegsegment/662242:

![Wegsegment](https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/wegsegment_fietstellus.png)

Coordinaatinfo van deze fietsbrug vinden we hier https://api.basisregisters.dev-vlaanderen.be/v1/wegsegmenten/662242, waaruit we kunnen afleiden dat het beginpunt rechtsonder
ligt en het eindpunt rechtsboven, het meetpunt ligt dus aan de kant vd weg die gelijkloopt met de digitalisatierichting.

Brucargo ligt in het oosten, Machelen in het westen. De IN en OUT bij de rijrichtingen matchen dus resp met de gelijklopende wegkant en de tegengestelde wegkant.

Er rijden tussen 7u45 en 8u op 1/8/2019 dus 7 fietsers richting Machelen en 4 richting Brucargo.


# Data voorbeeld fietstellus

Om de bron data overzichtelijk te maken, plaatsen we dit in een json structuur:

```json
{
"data":
[
{
"site ID": 1,
"richting" : "OUT",
"type": "FIETSERS",
"van":"2023-06-01 00:00:00.0",
"tot": "2023-06-01 00:15:00.0",
"aantal": 1
},
{
"site ID": 1,
"richting" : "OUT",
"type": "FIETSERS",
"van":"2023-06-01 00:00:00.0",
"tot": "2023-06-01 00:15:00.0",
"aantal": 0
}],

"sites":
[
{
    "site ID" : "1",
    "site nr" : "100046096",
    "long": 4.456121776137429,
    "lang": 50.91618331151478,
    "naam": "Machelen",
    "domein" : "Vlaamse Overheid A. Wegen enVerkeer",
    "wegnr": "T2110002",
    "district": "AWV212",
    "gemeente" : "Machelen",
    "interval":"15",
    "datum_van":"2019-08-22"

}],

"richtingen":[
    {
"site ID":1,
"richting": "IN",
"naam":"Machelen Cyclists rich. Brucargo"},
{
"site ID":1,
"richting": "Out",
"naam":"Machelen Cyclists richting Machelen"}
]
}

```

