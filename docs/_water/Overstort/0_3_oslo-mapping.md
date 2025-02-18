---
layout: default
title: Stap voor stap
parent: Overstort
nav_order: 3
---

# Intro

Voor het mappen van de brondata in JSON-format naar een Linked Data graph volgens OSLO wordt gewerkt met een SPARQL CONSTRUCT mapping die JSON-brondata herstructureert in het implementatiemodel.

Bij deze alvast een voorbeeld.

# Voorbeeld hoogte overstort

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

Merk op dat kolom `modified_at` ook gebruikt wordt. Dit is domeinonafhankelijk en wordt gebruikt bij het versioneren van de data.

## OSLO mapping

Op basis van de brondata kunnen we een OSLO mapping uitwerken worden adhv SPARQL CONSTRUCT queries. 

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

Belangrijk bij het mappen is dat de objecten van triples correct getypeerd worden: datatypes worden verrijkt met `STRDT` en bijhorende xsd type, instanties van een klasse met `URI`.

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

#### Resultaat en tijd - STILL TO DO

```
CONSTRUCT {
  ...
  ?observation_versie sosa:phenomenonTime ?observation_versie_fenomeentijd ;
    sosa:hasResult ?observation_versie_result ;
    sosa:hasSimpleResult ?vracht_value_with_datatype .

  ?observation_versie_fenomeentijd a time:Instant ;
    rdfs:label ?year0 ;
    time:inXSDgYear ?year_with_datatype .

  ?observation_versie_result a schema:QuantitativeValue, sosa:Result ;
    schema:unitCode ?vracht_unitMeasure ;
    schema:unitText ?unitMeasure_label ;
    schema:value ?vracht_value_with_datatype ;
    rdfs:label ?vracht_value_label .
    ...
} WHERE {
    ...
    BIND(URI(concat(str(?observation_versie), "/fenomeentijd/0001")) as ?observation_versie_fenomeentijd) 
    BIND(URI(concat(str(?observation_versie), "/result/0001")) as ?observation_versie_result)

    BIND(STRDT(?year0, xsd:gYear) as ?year_with_datatype)
    BIND(URI(?unitMeasure_url) as ?vracht_unitMeasure)
    BIND(STRDT(?value0, xsd:decimal) as ?vracht_value_with_datatype)

    BIND(if(bound(?unitMeasure_label), concat(?value0, ' (', ?unitMeasure_label, ')'), concat(?value0, ' (eenheid onbekend)')) as ?vracht_value_label)
  ...
}
```



