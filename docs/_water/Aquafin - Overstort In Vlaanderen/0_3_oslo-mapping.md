---
layout: default
title: Stap voor stap
parent: Overstort
nav_order: 3
---

# Intro

Voor het mappen van de brondata in JSON-format naar een Linked Data graph volgens OSLO wordt gewerkt met een SPARQL CONSTRUCT mapping die JSON-brondata herstructureert in het implementatiemodel.

In onderstaande voorbeelden wordt meegegeven hoe de transformatie plaatsvindt.

# Voorbeeld event

## Ruwe data

Onderstaand nogmaals de data zoals ze ontvangen wordt door de LDIO workbench in JSON-formaat.

```json
{
	"type":"Event",
	"start_timestamp":"2025-02-18T08:31:00.000Z",
	"end_timestamp":"2025-02-18T08:41:00.000Z",
	"measurement_location":"P_000000181521",
	"status":"WerkingOnbekend",
	"is_observed_with":"P1037143",
	"modified_at":"2025-02-18T10:21:17.979Z",
	"is_deleted":"false"
}
```

## OSLO mapping

Op basis van de brondata kunnen we een OSLO mapping uitwerken worden aan de hand van SPARQL CONSTRUCT queries. 

### WHERE

Bovenstaande brondata wordt gebruikt als input in de WHERE-clausule:

```
CONSTRUCT {
  ...
} WHERE {
	 ?s aquafin:start_timestamp ?start_timestamp .
	 ?s aquafin:end_timestamp ?end_timestamp .
	 ?s aquafin:modified_at ?modified_at .
     OPTIONAL {?s aquafin:measurement_location ?measurement_location . }
	 ?s aquafin:status ?status .
	 ?s aquafin:is_observed_with ?is_observed_with .
	 ?s aquafin:is_deleted ?is_deleted .

	 BIND(IRI(CONCAT("https://aquafin.be/id/concept/OverstortStatus/", ?status)) AS ?measurement_status_bind)
	 FILTER(?status != "InWerkingDroogWeer")

	 BIND(IRI(CONCAT("https://aquafin.be/id/event/", STRUUID())) AS ?event)

	 BIND(xsd:dateTime(?start_timestamp) AS ?start_timestamp_bind)
	 BIND(xsd:dateTime(?end_timestamp) AS ?end_timestamp_bind)
	 BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)

	 BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_bind)
	 BIND(MD5(?is_observed_with) AS ?is_observed_with_bind)

	}
}
```

### Prefix

Voor de leesbaarheid worden volgende prefices gebruikt:

```
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX ssn: <http://www.w3.org/ns/ssn/>
        PREFIX aquafin: <https://aquafin.be/ns#>
        PREFIX qudt: <http://qudt.org/schema/qudt/>
        PREFIX schema: <http://schema.org/>
```

### CONSTRUCT

#### Versie

Nu kunnen we starten met het mappen naar OSLO.
De versionering gebeurt automatisch door de LDIO Workbench pipeline en wordt toevoegd aan de eindmapping. 
Het versioneren wordt hier wel in de mapping gedaan adhv de modifiedAt-waarde om te vermijden dat het aantal _url kolommen verdubbelt.

```
        CONSTRUCT {
			?event a sosa:Observation ;
				aquafin:event_start_time ?start_timestamp_bind ;
				aquafin:event_end_time ?end_timestamp_bind ;
				purl:modified ?modified_at_bind ;
				sosa:hasFeatureOfInterest ?measurement_location_bind ;
				sosa:hasResult ?measurement_status_bind;
				sosa:observedProperty <https://aquafin.be/id/concept/Kenmerk/Overstort> ;
				sosa:madeBySensor ?is_observed_with_bind ;
				aquafin:is_deleted ?is_deleted .
			}
			WHERE {
				?s aquafin:start_timestamp ?start_timestamp .
				?s aquafin:end_timestamp ?end_timestamp .
				?s aquafin:modified_at ?modified_at .
				OPTIONAL {?s aquafin:measurement_location ?measurement_location . }
				?s aquafin:status ?status .
				?s aquafin:is_observed_with ?is_observed_with .
				?s aquafin:is_deleted ?is_deleted .

				BIND(IRI(CONCAT("https://aquafin.be/id/concept/OverstortStatus/", ?status)) AS ?measurement_status_bind)
				FILTER(?status != "InWerkingDroogWeer")

				BIND(IRI(CONCAT("https://aquafin.be/id/event/", STRUUID())) AS ?event)

				BIND(xsd:dateTime(?start_timestamp) AS ?start_timestamp_bind)
				BIND(xsd:dateTime(?end_timestamp) AS ?end_timestamp_bind)
				BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)

				BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_bind)
				BIND(MD5(?is_observed_with) AS ?is_observed_with_bind)

			}
          ...
}
```

# Voorbeeld Sensor

## Ruwe data

Onderstaand nogmaals de data zoals ze ontvangen wordt door de LDIO workbench in JSON-formaat.

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
	"quality_label":"A01",
	"valid_from":"2025-04-11T13:31:56.947Z",
	"valid_to":"9999-12-31T23:59:59.000Z",
	"modified_at":"2025-04-11T13:31:56.947Z",
	"is_deleted":false
}
```

## OSLO mapping

Op basis van de brondata kunnen we een OSLO mapping uitwerken worden aan de hand van SPARQL CONSTRUCT queries. 

### WHERE

Bovenstaande brondata wordt gebruikt als input in de WHERE-clausule:

```
CONSTRUCT {
  ...
} WHERE {
          ?s aquafin:id  ?id .
          ?s aquafin:valid_from ?valid_from .
          ?s aquafin:modified_at ?modified_at . 


          OPTIONAL { ?s aquafin:device_type ?device_type . }
          OPTIONAL { ?s aquafin:name ?name . }
          OPTIONAL { ?s aquafin:owner ?owner . }
          OPTIONAL { ?s aquafin:supplier ?supplier . }
          OPTIONAL { ?s aquafin:brand ?brand . }
	      OPTIONAL {
			?s aquafin:serial_number ?serial_number .
            BIND(MD5(?serial_number) AS ?hashed_serial_number)
  		  }
		  OPTIONAL { ?s aquafin:device_state ?device_state . }
          OPTIONAL { ?s aquafin:lat_WGS84 ?lat_WGS84 . }
          OPTIONAL { ?s aquafin:long_WGS84 ?long_WGS84 . }
          OPTIONAL { ?s aquafin:lat_Lambert72 ?lat_Lambert72 . }
          OPTIONAL { ?s aquafin:long_Lambert72 ?long_Lambert72 . }
          OPTIONAL {
            ?s aquafin:measurement_location ?measurement_location .          BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_name)        }
          OPTIONAL { ?s aquafin:quality_label ?quality_label . }
          OPTIONAL { ?s aquafin:valid_to ?valid_to . }
          OPTIONAL { ?s aquafin:is_deleted ?is_deleted . }

		  BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", STRUUID())) AS ?sensor)
          BIND(MD5(?id) AS ?hashed_id)
		  BIND(xsd:dateTime(?valid_from) AS ?valid_from_bind)
          OPTIONAL {
            ?s aquafin:valid_to ?valid_to .
            BIND(xsd:dateTime(?valid_to) AS ?valid_to_bind)
          }
          OPTIONAL {
            ?s aquafin:modified_at ?modified_at .
            BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)
    }
}
```

### Prefix

Voor de leesbaarheid worden volgende prefices gebruikt:

```
        PREFIX so: <http://schema.org/>
        PREFIX sc: <http://purl.org/science/owl/sciencecommons/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>
        PREFIX ssn: <http://www.w3.org/ns/ssn/>
        PREFIX aquafin: <https://aquafin.be/ns#>
        PREFIX schema: <https://schema.org/>
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX environment: <https://smartdatamodels.org/dataModel.Environment/>
        PREFIX sdm: <https://smartdatamodels.org/>
```

### CONSTRUCT

#### Versie

Nu kunnen we starten met het mappen naar OSLO.
De versionering gebeurt automatisch door de LDIO Workbench pipeline en wordt toevoegd aan de eindmapping. 
Het versioneren wordt hier wel in de mapping gedaan adhv de modifiedAt-waarde om te vermijden dat het aantal _url kolommen verdubbelt.

```
        CONSTRUCT {
          ?sensor a sosa:Sensor ;
                  dcterms:identifier ?hashed_id ;
                  environment:deviceId ?hashed_id ;                  
                  dcterms:description ?name ;
                  dcterms:type ?device_type ;
                  sdm:owner ?owner ;
                  schema:seller ?supplier ;
                  environment:deviceModel ?brand ;
                  schema:serialNumber ?hashed_serial_number ;
                  environment:deviceStatus ?device_state ;
                  geo:lat ?lat_WGS84 ;
                  geo:long ?long_WGS84 ;
                  aquafin:lat_Lambert72 ?lat_Lambert72 ;
                  aquafin:long_Lambert72 ?long_Lambert72 ;
                  environment:deviceName ?name ;
                  sosa:hasFeatureOfInterest ?measurement_location_name ;
				  aquafin:valid_from ?valid_from_bind ;
                  aquafin:valid_to ?valid_to_bind ;
                  aquafin:is_deleted ?is_deleted;
                  dcterms:modified ?modified_at_bind .
        }
        WHERE {
          ?s aquafin:id  ?id .
          ?s aquafin:valid_from ?valid_from .
          ?s aquafin:modified_at ?modified_at . 


          OPTIONAL { ?s aquafin:device_type ?device_type . }
          OPTIONAL { ?s aquafin:name ?name . }
          OPTIONAL { ?s aquafin:owner ?owner . }
          OPTIONAL { ?s aquafin:supplier ?supplier . }
          OPTIONAL { ?s aquafin:brand ?brand . }
	      OPTIONAL {
			?s aquafin:serial_number ?serial_number .
            BIND(MD5(?serial_number) AS ?hashed_serial_number)
  		  }
		  OPTIONAL { ?s aquafin:device_state ?device_state . }
          OPTIONAL { ?s aquafin:lat_WGS84 ?lat_WGS84 . }
          OPTIONAL { ?s aquafin:long_WGS84 ?long_WGS84 . }
          OPTIONAL { ?s aquafin:lat_Lambert72 ?lat_Lambert72 . }
          OPTIONAL { ?s aquafin:long_Lambert72 ?long_Lambert72 . }
          OPTIONAL {
            ?s aquafin:measurement_location ?measurement_location .          BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_name)        }
          OPTIONAL { ?s aquafin:quality_label ?quality_label . }
          OPTIONAL { ?s aquafin:valid_to ?valid_to . }
          OPTIONAL { ?s aquafin:is_deleted ?is_deleted . }

		  BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", STRUUID())) AS ?sensor)
          BIND(MD5(?id) AS ?hashed_id)
		  BIND(xsd:dateTime(?valid_from) AS ?valid_from_bind)
          OPTIONAL {
            ?s aquafin:valid_to ?valid_to .
            BIND(xsd:dateTime(?valid_to) AS ?valid_to_bind)
          }
          OPTIONAL {
            ?s aquafin:modified_at ?modified_at .
            BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)
    }

  ...
}
```

