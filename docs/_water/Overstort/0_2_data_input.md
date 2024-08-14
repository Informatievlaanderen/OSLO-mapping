---
layout: default
title: Data voorbeeld
parent: Overstort
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, voorzien we onderstaand een JSON-LD voorbeeld van een Event. De brondata wordt meteen aangeleverd in JSON-LD-formaat.
Op die manier krijgen we voor overstort:

## Overstorthoogte

```json
{
  "id": "https://aquafin.be/id/observatie/001/gemetenAfstand/2024-07-29T15:00:00Z",
  "type": "Observatie",
  "isVersionOf": "https://aquafin.be/id/observatie/001/gemetenAfstand/2024-07-27T20:00:00Z",
  "modifiedAt": "2024-07-29T15:00:00Z",
  "Observatie.geobserveerdObject": "https://aquafin.be/id/emissiepunt/001",
  "Observatie.geobserveerdKenmerk": "https://data.vlaanderen.be/id/concept/WaterMetingType/gemetenAfstand",
  "Observatie.simpelResultaat": "-10.5",
  "Observatie.resultaat": {
    "type": "KwantitatieveWaarde",
    "KwantitatieveWaarde.waarde": "-10.5",
    "KwantitatieveWaarde.standaardEenheid": "qudt-unit:CentiM"
  },
  "Overstortstatus": "https://data.vlaanderen.be/id/concept/OverstortStatus/nietOverstort",
  "Observatie.resultaatTijd": "2024-07-27T20:00:00Z",
  "Observatie.fenomeentijd": {
    "type": "Moment",
    "inXSDDateTime": "2024-07-27T14:00:00Z"
  },
  "Observatie.gebruikteProcedure": "https://aquafin.be/id/concept/observatieproceduretype/OW19",
  "Observatie.isWaargenomenMet": "https://aquafin.be/id/sensor/001"
}
```

## Temperatuur

```json
{
  "id": "https://aquafin.be/id/observatie/001/temperatuur/2024-07-29T15:00:00Z",
  "type": "Observatie",
  "isVersionOf": "https://aquafin.be/id/observatie/001/temperatuur/2024-07-27T20:00:00Z",
  "modifiedAt": "2024-07-29T15:00:00Z",
  "Observatie.geobserveerdObject": "https://aquafin.be/id/emissiepunt/001",
  "Observatie.geobserveerdKenmerk": "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0030",
  "Observatie.simpelResultaat": "22.5",
  "Observatie.resultaat": {
    "type": "KwantitatieveWaarde",
    "KwantitatieveWaarde.waarde": "22.5",
    "KwantitatieveWaarde.standaardEenheid": "qudt-unit:DEG_C"
  },
  "Observatie.resultaatTijd": "2024-07-27T20:00:00Z",
  "Observatie.fenomeentijd": {
    "type": "Moment",
    "inXSDDateTime": "2024-07-27T14:00:00Z"
  },
  "Observatie.gebruikteProcedure": "https://aquafin.be/id/concept/observatieproceduretype/OW19",
  "Observatie.isWaargenomenMet": "https://aquafin.be/id/sensor/001"
}
```

## Debiet

```json
{
  "id": "https://aquafin.be/id/observatie/001/debiet/2024-07-29T15:00:00Z",
  "type": "Observatie",
  "isVersionOf": "https://aquafin.be/id/observatie/001/debiet/2024-07-27T20:00:00Z",
  "modifiedAt": "2024-07-29T15:00:00Z",
  "Observatie.geobserveerdObject": "https://aquafin.be/id/emissiepunt/001",
  "Observatie.geobserveerdKenmerk": "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0053",
  "Observatie.simpelResultaat": "22.5",
  "Observatie.resultaat": {
    "type": "KwantitatieveWaarde",
    "KwantitatieveWaarde.waarde": "22.5",
    "KwantitatieveWaarde.standaardEenheid": "qudt-unit:CubicMeterPerSecond"
  },
  "Observatie.resultaatTijd": "2024-07-27T20:00:00Z",
  "Observatie.fenomeentijd": {
    "type": "Moment",
    "inXSDDateTime": "2024-07-27T14:00:00Z"
  },
  "Observatie.gebruikteProcedure": "https://aquafin.be/id/concept/observatieproceduretype/OW19",
  "Observatie.isWaargenomenMet": "https://aquafin.be/id/sensor/001"
}
```

## Emissiepunt (Overstortpunt)


```json
{
  "id": "https://aquafin.be/id/emissiepunt/001",
  "type": "Emissiepunt",
  "label": "Overstortpunt 001",
  "geometrie": {
    "type": "Geometrie",
    "wktWGS84": "<http://www.opengis.net/def/crs/EPSG/0/4326> POINT(5.298607495000001 50.948995878)",
    "wktLambert72": "<http://www.opengis.net/def/crs/EPSG/0/31370> POINT(xxx yyy)",
    "lat": "50.948995878",
    "long": "5.298607495000001"
  }
}
```

## Sensor

```json
{
  "id": "https://aquafin.be/id/sensor/001",
  "type": "Sensor",
  "label": "Sensor 001",
  "geometrie": {
    "type": "Geometrie",
    "wktWGS84": "<http://www.opengis.net/def/crs/EPSG/0/4326> POINT(5.298607495000001 50.948995878)",
    "wktLambert72": "<http://www.opengis.net/def/crs/EPSG/0/31370> POINT(xxx yyy)",
    "lat": "50.948995878",
    "long": "5.298607495000001"
  }
  "familieType": "",
  "identifier": "P2046600",
  "eigenaar": "",
  "operationeleStatus": "",
  "serienummer": ""
}
```

https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md

https://www.w3.org/TR/wot-thing-description


## Context
```json
{
  "@context": {
      "@language": "nl",
      "adms": "http://www.w3.org/ns/adms#",
      "qudt-schema": "https://qudt.org/schema/qudt/",
      "terms": "http://purl.org/dc/terms/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "qudt-unit": "https://qudt.org/vocab/unit/",
      "sosa": "http://www.w3.org/ns/sosa/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "schema": "https://schema.org",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "locn": "http://www.w3.org/ns/locn#",
      "wgs84_pos": "http://www.w3.org/2003/01/geo/wgs84_pos#",
      "id": "@id",
      "type": "@type",
      "Observatie": "sosa:Observation",
      "isVersionOf": {
        "@id": "terms:isVersionOf",
        "@type": "@id"
      },
      "createdAt": {
        "@id": "terms:createdAt",
        "@type": "xsd:dateTime"
      },
      "modifiedAt": {
        "@id": "terms:modifiedAt",
        "@type": "xsd:dateTime"
      },
      "Observatie.geobserveerdObject": {
        "@id": "sosa:hasFeatureOfInterest",
        "@type": "@id"
      },
      "Observatie.geobserveerdKenmerk": {
        "@id": "sosa:observedProperty",
        "@type": "@id"
      },
      "Observatie.simpelResultaat": {
        "@id": "sosa:hasSimpleResult",
        "@type": "xsd:decimal"
      },
      "Observatie.resultaat": {
        "@id": "sosa:hasResult",
        "@type": "@id"
      },
      "Observatie.resultaatTijd": {
        "@id": "sosa:resultTime",
        "@type": "xsd:dateTime"
      },
      "Observatie.fenomeentijd": {
        "@id": "sosa:phenomenonTime",
        "@type": "@id"
      },
      "Observatie.gebruikteProcedure": {
        "@id": "sosa:usedProcedure",
        "@type": "@id"
      },
      "KwantitatieveWaarde": "https://schema.org/QuantitativeValue",
      "KwantitatieveWaarde.waarde": {
        "@id": "https://schema.org/value",
        "@type": "xsd:decimal"
      },
      "KwantitatieveWaarde.standaardEenheid": {
        "@id": "https://schema.org/unitCode",
        "@type": "@id"
      },
      "Moment": "time:Instant",
      "inXSDDateTime": "time:inXSDDateTime",
      "overstortStatus": "https://aquafin.be/ns/overstort#overstortStatus",
      "Emissiepunt": "https://data.imjv.omgeving.vlaanderen.be/ns/imjv#Emissiepunt",
      "label": "rdfs:label",
      "geometrie": "locn:geometry",
      "Geometrie": "locn:Geometry",
      "wktWGS84": {
        "@id": "geosparql:asWKT",
        "@type": "geosparql:wktLiteral"
      },
      "wktLambert72": {
        "@id": "geosparql:asWKT",
        "@type": "geosparql:wktLiteral"
      },
      "lat": {
        "@id": "wgs84_pos:lat"
      },
      "long": {
        "@id": "wgs84_pos:long"
      }
  }
}
```