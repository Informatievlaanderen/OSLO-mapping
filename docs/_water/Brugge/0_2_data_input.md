---
layout: default
title: Data voorbeeld
parent: Waterkwaliteit Brugge
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, gieten we de input data (staalname documenten) in een json structuur. Op die manier krijgen we dit:

```json
{
"Waterkwaliteit":
{
    "pH": 7.8,
    "Opgeloste_zuurstof": 65.1,
    "Temperatuur(water)": 3.6,
    "Temperatuur(pH)": 4.2,
},
"Locatie":{
    "lat":"51°13'4.2126",
    "lon":"3°13'45.1626"
},
"plaatsnaam": "Ter Duinenbrug",
"datum staalname":"11/01/2021",
"Organisatie":"BVP/KD",
"Methode": "staalnamekooi/fles",
"weer":"zon/bewolkt"
"procedure":"https://reflabos.vito.be/2022/WAC_I_A_003.pdf"


}
```
