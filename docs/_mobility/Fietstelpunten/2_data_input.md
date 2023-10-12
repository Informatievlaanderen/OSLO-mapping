---
layout: default
parent: Fietstelpunten
title: data voorbeeld
nav_order: 2
---


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





