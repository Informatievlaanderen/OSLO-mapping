---
layout: default
title: Input data
parent: Documentatie
grand_parent: Signco
nav_order: 0
---


# Data input

Test data wordt opgehaald via de Signco Swagger API: [](https://devapi.signcoserv.be/swagger/index.html)

## Site voorbeeld Signco 
![Alt text](image.png)
Haalt alle meetpunten op. Uit deze gegevens kunt u de guid halen die u bij de andere dataopvragingen kunt gebruiken.

```json
{
  "itemsCount": 1,
  "data": [
    {
      "code": "Willebroek Dijk",
      "address": {
        "line1": "Jozef de Blockstraat 74",
        "zipCode": "2830",
        "city": "Willebroek",
        "country": "Belgium"
      },
      "coordinate": {
        "latitude": 51.041935,
        "longitude": 4.35714
      },
      "measuringPoints": [
        {
          "guid": "eb58f640-6916-4986-8ded-c7bf5a0fc40d",
          "code": "Willebroek South In",
          "description": "Opposite the buildings",
          "heading": 30,
          "from": "Tisselt",
          "to": "Willebroek",
          "drivingLane": "Single lane",
          "analysisTypeId": "car",
          "owner": "Acme Corporation",
          "isActive": false
        },
        {
          "guid": "ff88e990-5a66-4301-a2cd-e75c897b48a8",
          "code": "Willebroek South Out",
          "heading": 210,
          "from": "Willebroek",
          "to": "Tisselt",
          "drivingLane": "Single lane",
          "analysisTypeId": "car",
          "owner": "Acme Corporation",
          "isActive": false
        }
      ]
    }
  ]
}

```

## Verkeersmeting aantal voertuigen

![Alt text](image-1.png)

Haalt geaggregeerde voertuigen op (som van alle voertuigen). Normaal gesproken wordt de som van de voertuigen per dag geretourneerd. Met behulp van de 'include'-parameters kunt u echter meer gedetailleerde gegevens ophalen door de sommen op te splitsen volgens aanvullende dimensies.

```json
[
  {
    "index": 0,
    "vehicleCount": 1234,
    "date": "2023/09/09",
    "timeSlot": "12:00:00"
  },
  {
    "index": 0,
    "vehicleCount": 978,
    "date": "2023/09/09",
    "timeSlot": "13:00:00"
  }
]
```