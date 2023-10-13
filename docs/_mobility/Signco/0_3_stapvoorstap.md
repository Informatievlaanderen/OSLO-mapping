---
layout: default
title: Stap voor stap
parent: Signco
nav_order: 2
---

# Stap voor stap

## Rijrichting

```json
{
      "@id": "_:rri001",
      "@type": "Rijrichting",
      "Rijrichting.netwerkreferentie": {
        "@type": "Linkreferentie",
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:inDirection"
      },
      "Rijrichting.rijrichting": "cl-trt:inDirection"
    }
    ```
  
```json
    {
      "@id": "_:rri002",
      "@type": "Rijrichting",
      "Rijrichting.netwerkreferentie": {
        "@type": "Linkreferentie",
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:inOppositeDirection"
      },
      "Rijrichting.rijrichting": "cl-trt:inOppositeDirection"
    }
```

## Wegsegment

```json
{
  "@id": "_:wgs001",
  "@type": "Wegsegment",
  "Wegsegment.beginknoop": "_:wgkn001",
  "Wegsegment.eindknoop": "_:wgkn002",
  "Wegsegment.geometriemiddenlijn": {
    "@type": "LineString",
    "Geometrie.wkt": {
      "@value": "<http://www.opengis.net/def/crs/EPSG/0/4326> LINESTRING (30 10, 10 30, 40 40)",
      "@type": "geosparql:wktLiteral"
    }
  }
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
      "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>",
      "@type": "geosparql:gmlLiteral"
    }
  }
}
```


## Verkeersmeting
```json

    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Verkeersmeting.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Verkeersmeting.geobserveerdObject": "_:mpt001",
      "Verkeersmeting.fenomeenTijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 30,
      "Verkeersmeting.uitgevoerdMet": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:Signco001"
    }
```



```json

    {
      "@id": "_:fenomtime001",
      "Verkeersmeting.fenomeenTijd": {
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20161122T09:00:00.000Z"
          }
        },
        "time:hasEnd": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20161122T10:00:00.000Z"
          }
        }
      }
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
      "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>51.041935,4.35714</gml:coordinates><gml:Point>",
      "@type": "geosparql:gmlLiteral"
    }
  },
  "Verkeersmeetpunt.netwerkreferentie": "_:pr001",
  "Verkeersbemonsteringsobject.bemonsterdObject": "_:rri001"
}
```
## Puntreferentie

```json
{
    "@id": "_:pr001",
    "@type": "Puntreferentie",
    "Puntreferentie.opPositie": {
      "@type": "Lengte",
      "KwantitatieveWaarde.waarde": "300",
      "KwantitatieveWaarde.standaardEenheid": {
        "@value": "m",
        "@type": "ucum:ucumunit"
      }
    },
    "Linkreferentie.toepassingsRichting": "cl-trt:bothDirections"
}
```

## Sensor
```json
{
  "@id": "_:mti001",
  "@type": "Sensor",
  "Systeem.type": "cl-mit:atc",
  "Sensor.implementeert": {
    "@type": "Observatieproceduretype",
    "Observatieprocedure.type": "cl-op:type"
  }
}
```