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
In de events vind je telkens een berekening terug van de start- en eindtijd van elk event, gevolgd door de specificatie over welk type event het gaat. Een event kan nl. een overstorting zijn, maar even goed de afwezigheid van een overstorting of een foutmelding. 

Onderstaand een json-voorbeeld

```json
{
	"type":"Event", --Type Event
	"start_timestamp":"2025-02-18T08:31:00.000Z", -- Tijdstip waarop het event startte
	"end_timestamp":"2025-02-18T08:41:00.000Z", -- Tijdstip waraop het event eindigde
	"measurement_location":"P_000000181521", --unieke identifier van de locatie waar de meting werd uitgevoerd. P-nummers op basis van de Rioolinventaris
	"status":"WerkingOnbekend", --Status van het event. Werd er overstort vastgesteld, geen overstort vastgesteld of was er een verstoord signaal (WerkingOnbekend)
	"is_observed_with":"P1037143", -- unieke identifier van het toestel waarmee de meting werd uitgevoerd
	"modified_at":"2025-02-18T10:21:17.979Z", --Tijdstip waarop het event werd verstuurd
	"is_deleted":"false" -- Is dit event nog geldig of werd deze verwijderd en vervangen door een nieuw en verbeterd event? 
}
```

## Sensor
In de Sensordata-json wordt alle relevante metadata per sensor doorgestuurd. 
Indien er wijzigingen optreden in de status, locatie of kwaliteit van de sensor, wordt een nieuwe versie beschikbaar gemaakt op de LDES Server die de meest recente versie van de sensormetadata bevat.


```json
{
	"id":"P2050378", -- Unieke identifier van het toestel waarmee de meting werd uitgevoerd
	"device_type":"Overstortmeter", --type van het toestel
	"name":"Overstortmeter Ijinus US LTE", --niet-unieke naam van het toestel
	"owner":"AQUAFIN", -- eigenaar van het toestel
	"brand":"Ijinus", -- merk van het toestel
	"supplier":"ELSCOLAB", -- verkoper van het toestel 
	"device_state":"ACTIEF", --status van het toestel (Actief / Inactief / uit dienst)
	"lat_WGS84":51.04243219340782, --Lengte-coördinnaat van de locatie van het toestel volgens WGS84-normen
	"long_WGS84":5.594445509825586, --breedte- coördinnaat van de locatie van het toestel volgens WGS84-normen
	"lat_Lambert72":193183.8663904309, -- lengte-coördinnaat van de locatie van het toestel volgens Lambert72-normen
	"long_Lambert72":235956.9331605651, -- breedte-coördinnaat van de locatie van het toestel volgens Lambert72-normen
	"measurement_location":"P_000000217952", --unieke identifier van de locatie waar de meting werd uitgevoerd. P-nummers op basis van de Rioolinventaris
	"quality_label":"A00", --kwaliteitskenmerk van het toestel
	"valid_from":"2025-04-11T13:31:56.947Z", --start geldigheidsdatum waarop dit record valide was
	"valid_to":"9999-12-31T23:59:59.000Z" -- einde geldigheidsdatum waarop dit record valide was
	"modified_at":"2025-04-11T13:31:56.947Z" --datum laatste wijziging van dit record
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
      "sdm": "https://smartdatamodels.org/"
      }
  }
```
