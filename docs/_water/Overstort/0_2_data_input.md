---
layout: default
title: Data voorbeeld
parent: Overstort
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, voorzien we onderstaand een JSON voorbeeld van een event en sensordata. 
De brondata wordt telkens aangeleverd in JSON-formaat.


## Event
In de events wordt niet de data vastgelegd die op een specifiek moment wordt opgemeten, maar is een berekening van de overstortduur
Onderstaand een json-voorbeeld

```json
{
	"type": "event",
	"event_start_time": "2024-07-27T14:00:00Z",
        "event_end_time": "2024-07-27T14:30:00Z",
	"modifiedAt": "2024-07-27T14:00:00Z", 
	"measurement_location":"K_000003850759", 
	"overstort_in_werking": "InWerking", 
	"is_observed_with": "418858" 
}
```

## Sensor
In de Sensordata-json wordt alle relevante metadata per sensor doorgestuurd. Dit gaat over slowly changing data. 

```json
{
   "id": "415987",
   "device_type": "Sensor",
   "name": "Overstortmeter Ijinus RD LTE",
   "owner": "Aquafin",
   "brand": "IJINUS",
   "supplier": "ELSCOLAB",
   "serial_number": "XAA0102-00001999",
   "device_state": "Actief",
   "lat_WGS84": "50.948995878",
   "long_WGS84": "5.298607495000001", 
   "lat_Lambert72": "xxx", 
   "long_Lambert72": "yyy", 
   "measurement_location":"K_000003850759"
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

