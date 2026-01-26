---
layout: default
parent: Overstort   
title: Examples Overstort
nav_order: 4
---

# Voorbeelden Overstort

## Prefices 

```
PREFIX dcat:                             <http://www.w3.org/ns/dcat#>
PREFIX dct:                              <http://purl.org/dc/terms/>
PREFIX foaf:                             <http://xmlns.com/foaf/0.1/>
PREFIX geo:                              <http://www.opengis.net/ont/geosparql#>
PREFIX ldes:                             <https://w3id.org/ldes#>
PREFIX m8g:                              <http://data.europa.eu/m8g/>
PREFIX overstort-event-cleansed:         <https://ldes-overstort.test.az.aquafin.be/ldes/overstort-event-cleansed/>
PREFIX overstort-event-cleansed-by-page: <https://ldes-overstort.test.az.aquafin.be/ldes/overstort-event-cleansed/overstort-event-cleansed-by-page/>
PREFIX owl:                              <http://www.w3.org/2002/07/owl#>
PREFIX prov:                             <http://www.w3.org/ns/prov#>
PREFIX rdf:                              <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:                             <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sh:                               <http://www.w3.org/ns/shacl#>
PREFIX shsh:                             <http://www.w3.org/ns/shacl-shacl#>
PREFIX skos:                             <http://www.w3.org/2004/02/skos/core#>
PREFIX tree:                             <https://w3id.org/tree#>
PREFIX xsd:                              <http://www.w3.org/2001/XMLSchema#>
```

#### Eindresultaat Overstort Sensor op de LDES Server

```
<https://aquafin.be/id/sensor/cfe90f61-ac58-4950-a414-e98fcf5bc97c/2025-08-26T08:48:44.580544355>
        rdf:type                     <http://www.w3.org/ns/sosa/Sensor>;
        dct:description              "OSM OSgr. R. De Cuyperst. 11, S-M-Bodeg";
        dct:identifier               "738d3a70cbc10bee4be120f70e377bc0";
        dct:isVersionOf              <https://aquafin.be/id/sensor/cfe90f61-ac58-4950-a414-e98fcf5bc97c>;
        dct:modified                 "2025-06-04T16:28:58.057Z"^^xsd:dateTime;
        dct:type                     "Overstortmeter";
        <http://www.w3.org/2003/01/geo/wgs84_pos#lat>
                5.08685000001277E1;
        <http://www.w3.org/2003/01/geo/wgs84_pos#long>
                4.238606314746391E0;
        prov:generatedAtTime         "2025-08-26T08:48:44.58Z"^^xsd:dateTime;
        <http://www.w3.org/ns/sosa/hasFeatureOfInterest>
                <https://aquafin.be/id/meetpunt/P_000000599187>;
        <https://aquafin.be/ns#is_deleted>
                false;
        <https://aquafin.be/ns#lat_Lambert72>
                1.731325603766878E5;
        <https://aquafin.be/ns#long_Lambert72>
                1.408385979174557E5;
        <https://aquafin.be/ns#quality_label>
                "E00";
        <https://aquafin.be/ns#valid_from>
                "2025-03-11T20:39:06.182Z"^^xsd:dateTime;
        <https://aquafin.be/ns#valid_to>
                "2025-04-12T04:02:49.429Z"^^xsd:dateTime;
        <https://schema.org/seller>  "ELSCOLAB";
        <https://smartdatamodels.org/dataModel.Environment/deviceId>
                "738d3a70cbc10bee4be120f70e377bc0";
        <https://smartdatamodels.org/dataModel.Environment/deviceModel>
                "Ijinus";
        <https://smartdatamodels.org/dataModel.Environment/deviceName>
                "OSM OSgr. R. De Cuyperst. 11, S-M-Bodeg";
        <https://smartdatamodels.org/dataModel.Environment/deviceStatus>
                "ACTIEF";
        <https://smartdatamodels.org/owner>
                "AQUAFIN" .
```

#### Eindresultaat Overstort Event op de LDES Server


```

<https://aquafin.be/id/event/4004f4ea-117d-4e01-9b7d-6b6af865ad52/2025-08-26T08:49:13.965604961>
        rdf:type              <http://www.w3.org/ns/sosa/Observation>;
        dct:isVersionOf       <https://aquafin.be/id/event/4004f4ea-117d-4e01-9b7d-6b6af865ad52>;
        dct:modified          "2025-08-05T17:29:19.457Z"^^xsd:dateTime;
        prov:generatedAtTime  "2025-08-26T08:49:13.965Z"^^xsd:dateTime;
        <http://www.w3.org/ns/sosa/hasFeatureOfInterest>
                <https://aquafin.be/id/meetpunt/P_000000350733>;
        <http://www.w3.org/ns/sosa/hasResult>
                <https://aquafin.be/id/concept/OverstortStatus/NietInWerking>;
        <http://www.w3.org/ns/sosa/madeBySensor>
                "4c314f066bea53f212495cb8c1eaca0b";
        <http://www.w3.org/ns/sosa/observedProperty>
                <https://aquafin.be/id/concept/Kenmerk/Overstort>;
        <https://aquafin.be/ns#event_end_time>
                "2024-02-18T20:46:00.000Z"^^xsd:dateTime;
        <https://aquafin.be/ns#event_start_time>
                "2024-02-18T20:45:00.000Z"^^xsd:dateTime;
        <https://aquafin.be/ns#is_deleted>
                false .
```
