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

Onderstaand nogmaals de data zoals ze ontvangen wordt de LDIO workbench in JSON-formaat.

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

Merk op dat kolom `change_timestamp_utc` ook gebruikt wordt. Dit is domeinonafhankelijk en wordt gebruikt bij het versioneren van de data.

## OSLO mapping

Op basis van de brondata kunnen we een OSLO mapping uitwerken worden adhv SPARQL CONSTRUCT queries. 

### WHERE

Bovenstaande brondata wordt gebruikt als input in de WHERE-clausule:

```
CONSTRUCT {
  ...
} WHERE {
                ?s aquafin:id  ?id .
                ?s aquafin:devicetype ?device_type .
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
Eerst zorgen we ervoor dat de observatie correct geversioneerd en gelabeled is.
De ?observation_url kolom wordt als persistente identificator van een observatie gebruikt en dus niet de ?obs die door de pipeline wordt ingevuld.
De bedoeling is om de Linked Data zo dicht mogelijk in de bron te houden. Dit houdt in dat de URI's van resources best worden beschreven in de view adhv `_url`
 kolommen en niet in de mapping. Het versioneren wordt hier wel in de mapping gedaan adhv de modifiedAt-waarde om te vermijden dat het aantal _url kolommen verdubbelt.

Belangrijk bij het mappen is dat de objecten van triples correct getypeerd worden: datatypes worden verrijkt met `STRDT` en bijhorende xsd type, instanties van een klasse met `URI`.

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
                  environment:deviceName ?devicename ;
                  sosa:hasFeatureOfInterest ?measurement_location_name ;
                  aquafin:quality_label ?quality_label 
              }
              WHERE {
                ?s aquafin:id  ?id .
                ?s aquafin:devicetype ?device_type .
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

  ...
}
```

#### Resultaat en tijd

![alt text](image-3.png)

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

#### Kenmerken

![alt text](image-4.png)

```
CONSTRUCT {
  ...
  ?observation_versie sosa:observedProperty ?observed_property_emissievrachtagens .

  ?observed_property_emissievrachtagens a sosa:ObservableProperty , imjv:EmissieVrachtAgens ;
              wk:agens ?agens ;
              rdfs:label ?observed_property_emissievrachtagens_label ;
              rdfs:comment ?observed_property_emissievrachtagens_comment .
            
            ?agens a skos:Concept ;
              rdfs:label ?substantie_url_with_lang .
    ...
} WHERE {
    ...
    BIND(URI(str(?substantie_url)) as ?agens)
    BIND(STRLANG(?substantie_url, "nl") as ?substantie_url_with_lang)

    BIND(STRLANG(concat("vracht ", ?substantie_label), "nl") as ?observed_property_emissievrachtagens_label)
    BIND(STRLANG(concat("De vracht ", ?substantie_label, " van een emissie."), "nl") as ?observed_property_emissievrachtagens_comment)
  ...
}
```

#### Geobserveerd Object



![alt text](image-5.png)

```
CONSTRUCT {
  ...
  ?observation_versie sosa:hasFeatureOfInterest ?emissie .
    ...
} WHERE {
  ...
  BIND(URI(?emissie_url) as ?emissie)
  ...
}
```
