---
layout: default
title: Stap voor stap
parent: Documentatie
grand_parent: Telraam
nav_order: 2
---

# Stap voor stap


## Wegsegment

```json
"geometry": {
        "type": "MultiLineString",
        "coordinates": [
          [
            [
              4.04451041920408,
              50.9346197016993
            ],
            [
              ...
            ]
          ]
        ]
      }
```


```json
   {
      "@id": "_:wgs001",
      "@type": "Wegsegment",
      "Wegsegment.geometriemiddenlijn": {
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.9346197016993 4.04451041920408,50.9346499094883 4.04468516398887,50.9346736897766 4.04476128017613, 50.9347048165154 4.04486091154096,50.9347897018035 4.0450104190652,50.9348297017355 4.04508041942127,50.9349798325647 4.04536795581668,50.9350979049717 4.04561050090522, 50.9351073291995 4.04563353497237,50.9351797011571 4.04581042002322</gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      },
      "Wegsegment.beginknoop": "_:wgkn001",
      "Wegsegment.eindknoop": "_:wgkn002"
    }
```

## Wegknoop
```json
{
    "@id": "_:wgkn001",
    "@type": "Wegknoop",
    "Wegknoop.geometrie": {
    "@type": "Punt",
    "Geometrie.gml": {
        "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.9346197016993 4.0445104192040</gml:coordinates><gml:Point>",
        "@type": "geosparql:gmlLiteral"
    }
    }
}
```

## Verkeersmeting

```json
{
    "@id": "_:vkmfiets001",
    "@type": "Verkeersmeting",
    "Verkeersmeting.geobserveerdKenmerk": {
    "@type": "Verkeerskenmerk",
    "Verkeerskenmerk.type": "cl-vkt:aantal",
    "Verkeerskenmerk.voertuigType": "cl-vrt:fiets"
    },
    "Verkeersmeting.geobserveerdObject": "_:mpt001",
    "Verkeersmeting.fenomeenTijd": ":_fenomtime001",
    "Verkeersmeting.resultaat": 33.3209922251018,
    "Verkeersmeting.uitgevoerdMet": "_:mti001",
    "dct:memberOf": "_:dataset001"
}
```

## Verkeersmeetpunt
```json
{
    "@id": "_:mpt001",
    "@type": "Verkeersmeetpunt",
    "Verkeersmeetpunt.geometrie": {
    "@type": "Punt",
    "Geometrie.gml": {
        "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>virtual_x,virtual_y</gml:coordinates><gml:Point>",
        "@type": "geosparql:gmlLiteral"
    }
    },
    "Verkeersmeetpunt.netwerkreferentie": {
    "@type": "Puntreferentie",
    "Puntreferentie.opPositie": {
        "@type": "Lengte",
        "KwantitatieveWaarde.waarde": "300",
        "KwantitatieveWaarde.standaardEenheid": {
        "@value": "m",
        "@type": "ucum:ucumunit"
        }
    }
    },
    "Verkeersbemonsteringsobject.bemonsterdObject": "_:wgs001"
}
```

## fenomeenTijd
```json
{
    "@id": "_:fenomtime001",
    "Verkeersmeting.fenomeenTijd": {
    "@type": "time:ProperInterval",
    "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
        "@type": "xml-schema:dateTime",
        "@value": "20210930T06:00:00.000"
        }
    },
    "time:hasEnd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
        "@type": "xml-schema:dateTime",
        "@value": "20210930T07:00:00.000"
        }
    }
    }
}
```

## Sensor
```json
{
    "@id": "_:mti001",
    "@type": "Sensor",
    "Systeem.type": "cl-mit:telraam",
    "Sensor.implementeert": {
    "@type": "Observatieproceduretype",
    "Observatieprocedure.type": "cl-op:type"
}
}
```



