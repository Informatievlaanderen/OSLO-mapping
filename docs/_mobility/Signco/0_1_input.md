---
layout: default
title: Input data
parent: Signco
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

## Surveys

```json
{
  "id": "903e2e28-919e-4fcf-8a68-8a46bc3c9b94",
  "reference": "131 21376 Bruges (May 2023)",
  "timezone": "Europe/Brussels",
  "createdAt": "2023-07-27T14:51:23.000Z",
  "pois": [
    {
      "name": "Site 1",
      "address": "Pater Damiaanstraat",
      "id": "5ed752d5-a754-415c-97a1-0ca27cff1a81",
      "type": "site",
      "geometry": {
        "type": "Point",
        "coordinates": [
          3.2148652151227,
          51.2095512122563
        ]
      },
      "country": "BE",
      "subdivision": "BE-BRU",
      "origins": [
        {
          "id": "db3859a7-b60d-4688-92fb-00a6038788c2",
          "name": "A",
          "geometry": {
            "type": "Point",
            "coordinates": [
              3.21470361202955,
              51.209493870826
            ]
          }
        },
        {
          "id": "26f39f88-fa0e-4c7e-aed0-f698490a0dce",
          "name": "B",
          "geometry": {
            "type": "Point",
            "coordinates": [
              3.21502950042486,
              51.2096106540299
            ]
          }
        }
      ]
    },
    {
      "name": "Site 2",
      "address": "Roompotstraat",
      "id": "bcb2c52e-f4b2-4265-9e85-84df06bfd1a5",
      "type": "site",
      "geometry": {
        "type": "Point",
        "coordinates": [
          3.21467377245426,
          51.2099479793909
        ]
      },
      "country": "BE",
      "subdivision": "BE-BRU",
      "origins": [
        {
          "id": "8b93be49-3be6-4b1b-b4cc-f378f28879e3",
          "name": "A",
          "geometry": {
            "type": "Point",
            "coordinates": [
              3.21448434144259,
              51.2098786661622
            ]
          }
        },
        {
          "id": "be6c5883-4f0d-4b55-a00f-097a0636df06",
          "name": "B",
          "geometry": {
            "type": "Point",
            "coordinates": [
              3.21487192064524,
              51.2100202330697
            ]
          }
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