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
	"end_timestamp_known":true,
	"sent_to_evh":false 
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
          ?s aquafin:measurement_location ?measurement_location .
          ?s aquafin:status ?status .
          ?s aquafin:is_observed_with ?is_observed_with .
          ?s aquafin:end_timestamp_known ?end_timestamp_known .
          # ?s aquafin:type ?type.

          BIND(IRI(CONCAT("https://aquafin.be/id/event/", STRUUID())) AS ?event)

          BIND(xsd:dateTime(?start_timestamp) AS ?start_timestamp_bind)
          BIND(xsd:dateTime(?end_timestamp) AS ?end_timestamp_bind)
          BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)

          BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_bind)
          BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", COALESCE(?is_observed_with, "unknown"))) AS ?is_observed_with_bind)
          # BIND(IRI(CONCAT("Event",COALESCE(?type,"unknown"))) AS ?message_type)
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
          ?event a sosa:Event ;
            sosa:event_start_time ?start_timestamp_bind ;
            sosa:event_end_time ?end_timestamp_bind ;
            sosa:modified_at ?modified_at_bind ;
            sosa:hasFeatureOfInterest ?measurement_location_bind ;
            ssn:status ?status ;
            sosa:madeBySensor ?is_observed_with_bind ;
            aquafin:endTimestampKnown ?end_timestamp_known ;
            # aquafin:type ?type .
        }
        WHERE {
          ?s aquafin:start_timestamp ?start_timestamp .
          ?s aquafin:end_timestamp ?end_timestamp .
          ?s aquafin:modified_at ?modified_at .
          ?s aquafin:measurement_location ?measurement_location .
          ?s aquafin:status ?status .
          ?s aquafin:is_observed_with ?is_observed_with .
          ?s aquafin:end_timestamp_known ?end_timestamp_known .
          # ?s aquafin:type ?type.

          BIND(IRI(CONCAT("https://aquafin.be/id/event/", STRUUID())) AS ?event)

          BIND(xsd:dateTime(?start_timestamp) AS ?start_timestamp_bind)
          BIND(xsd:dateTime(?end_timestamp) AS ?end_timestamp_bind)
          BIND(xsd:dateTime(?modified_at) AS ?modified_at_bind)

          BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_bind)
          BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", COALESCE(?is_observed_with, "unknown"))) AS ?is_observed_with_bind)
          # BIND(IRI(CONCAT("Event",COALESCE(?type,"unknown"))) AS ?message_type)
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
	"load_timestamp_utc":"2025-02-16T22:01:04.229Z",
	"change_timestamp_utc":"2024-12-29T05:52:09.343Z",
	"quality_label":"A01",
	"scd_update_timestamp":"2025-02-14T08:46:50.202Z"
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
         ?s aquafin:name ?name .
         ?s aquafin:owner ?owner .
         ?s aquafin:supplier ?supplier .
         ?s aquafin:brand ?brand .
         ?s aquafin:serial_number ?serial_number .
         ?s aquafin:device_state ?device_state .      
         ?s aquafin:lat_WGS84 ?lat_WGS84 .
         ?s aquafin:long_WGS84 ?long_WGS84 .
         ?s aquafin:lat_Lambert72 ?lat_Lambert72 .
         ?s aquafin:long_Lambert72 ?long_Lambert72 .
         ?s aquafin:measurement_location ?measurement_location .    
         ?s aquafin:load_timestamp_utc ?load_timestamp_utc .             
         ?s aquafin:change_timestamp_utc ?change_timestamp_utc . 
         ?s aquafin:quality_label ?quality_label .
         ?s aquafin:scd_update_timestamp ?scd_update_timestamp .

         BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", STRUUID())) AS ?sensor)
         BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_name)

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
                  dcterms:identifier ?id ;
                  environment:deviceId ?id ;                  
                  dcterms:description ?name ;
                  dcterms:type ?device_type ;
                  sdm:owner ?owner ;
                  schema:vendor ?supplier ;
                  environment:deviceModel ?brand ;
                  schema:serialNumber ?serial_number ;
                  environment:deviceStatus ?device_state ;
                  geo:lat ?lat_WGS84 ;
                  geo:long ?long_WGS84 ;
                  aquafin:lat_Lambert72 ?lat_Lambert72 ;
                  aquafin:long_Lambert72 ?long_Lambert72 ;
                  environment:deviceName ?name ;
                  sosa:hasFeatureOfInterest ?measurement_location_name ;
                  aquafin:load_timestamp_utc ?load_timestamp_utc ;
                  aquafin:change_timestamp_utc ?change_timestamp_utc ;
                  aquafin:quality_label ?quality_label ;
        }
        WHERE {
	 ?s aquafin:id  ?id .
         ?s aquafin:name ?name .
         ?s aquafin:owner ?owner .
         ?s aquafin:supplier ?supplier .
         ?s aquafin:brand ?brand .
         ?s aquafin:serial_number ?serial_number .
         ?s aquafin:device_state ?device_state .      
         ?s aquafin:lat_WGS84 ?lat_WGS84 .
         ?s aquafin:long_WGS84 ?long_WGS84 .
         ?s aquafin:lat_Lambert72 ?lat_Lambert72 .
         ?s aquafin:long_Lambert72 ?long_Lambert72 .
         ?s aquafin:measurement_location ?measurement_location .    
         ?s aquafin:load_timestamp_utc ?load_timestamp_utc .             
         ?s aquafin:change_timestamp_utc ?change_timestamp_utc . 
         ?s aquafin:quality_label ?quality_label .
         ?s aquafin:scd_update_timestamp ?scd_update_timestamp .

         BIND(IRI(CONCAT("https://aquafin.be/id/sensor/", STRUUID())) AS ?sensor)
         BIND(IRI(CONCAT("https://aquafin.be/id/meetpunt/", COALESCE(?measurement_location, "unknown"))) AS ?measurement_location_name)

        }  

  ...
}
```

