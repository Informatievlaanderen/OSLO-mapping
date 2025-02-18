---
layout: default
title: Data voorbeeld
parent: Overstort
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, voorzien we onderstaand een voorbeeld in JSON-formaat van een eventbericht en een metadatabericht van een sensor. 
Dit is ook meteen het formaat waarin de brondata wordt aangeleverd om later ter beschikking gesteld te worden via LDES.


## Event
In de events wordt niet de data vastgelegd die op een specifiek moment wordt opgemeten, maar is een berekening van de overstortduur
Onderstaand een json-voorbeeld

```json
{
	"type":"Event",
	"start_timestamp":"2025-02-18T08:31:00.000Z",
	"end_timestamp":"2025-02-18T08:41:00.000Z",
	"measurement_location":"P_000000181521",
	"status":"WerkingOnbekend",
	"is_observed_with":"P1037143",
	"modified_at":"2025-02-18T10:21:17.979Z",
	"end_timestamp_known":true,
	"sent_to_evh":false 
}
```

## Sensor
In de Sensordata-json wordt alle relevante metadata per sensor doorgestuurd. 
Indien er wijzigingen optreden in de status, locatie of kwaliteit van de sensor, wordt een nieuwe versie beschikbaar gemaakt op de LDES Server die de meest versie van de sensormetadata bevat.


```json
{
	"id":"P2050378",
	"device_type":"Overstortmeter",
	"name":"Overstortmeter Ijinus US LTE",
	"owner":"AQUAFIN",
	"brand":"Ijinus",
	"supplier":"ELSCOLAB",
	"serial_number":"IJA0102-00004425",
	"device_state":"ACTIEF",
	"lat_WGS84":51.04243219340782,
	"long_WGS84":5.594445509825586,
	"lat_Lambert72":193183.8663904309,
	"long_Lambert72":235956.9331605651,
	"measurement_location":"P_000000217952",
	"load_timestamp_utc":"2025-02-16T22:01:04.229Z",
	"change_timestamp_utc":"2024-12-29T05:52:09.343Z",
	"quality_label":"0",
	"scd_update_timestamp":"2025-02-14T08:46:50.202Z"
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
      "sc": "http://purl.org/science/owl/sciencecommons",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "qudt-unit": "https://qudt.org/vocab/unit/",
      "sosa": "http://www.w3.org/ns/sosa/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "schema": "https://schema.org",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "locn": "http://www.w3.org/ns/locn#",
      "geo" : "http://www.w3.org/2003/01/geo/wgs84_pos#",
      "prov": "http://www.w3.org/ns/prov#",
      "sosa": "http://www.w3.org/ns/sosa/",
      "ssn": "http://www.w3.org/ns/ssn/",
      "aquafin": "https://aquafin.be/ns#",
      "dcterms": "http://purl.org/dc/terms/",
      "environment": "https://smartdatamodels.org/dataModel.Environment/",
      "sdm": "https://smartdatamodels.org/",
 
      }
  }
}

