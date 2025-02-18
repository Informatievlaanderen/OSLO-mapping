---
layout: default
parent: Overstort   
title: Examples Overstort
nav_order: 4
---

#Prefices 

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

#### Eindresultaat op de LDES Server


```

<https://aquafin.be/id/event/61443dd0-e8a5-4d60-aa59-91d2ade86150/2025-02-06T07:02:14.284989010>
        rdf:type              <http://www.w3.org/ns/sosa/Event>;
        dct:isVersionOf       <https://aquafin.be/id/event/61443dd0-e8a5-4d60-aa59-91d2ade86150>;
        prov:generatedAtTime  "2025-02-06T07:02:14.284Z"^^xsd:dateTime;
        <http://www.w3.org/ns/sosa/event_end_time>
                "2025-02-05T16:30:00.000Z"^^xsd:dateTime;
        <http://www.w3.org/ns/sosa/event_start_time>
                "2025-02-05T16:16:00.000Z"^^xsd:dateTime;
        <http://www.w3.org/ns/sosa/hasFeatureOfInterest>
                <https://aquafin.be/id/meetpunt/P_000000582719>;
        <http://www.w3.org/ns/sosa/madeBySensor>
                <https://aquafin.be/id/sensor/P1035782>;
        <http://www.w3.org/ns/sosa/modified_at>
                "2025-02-06T06:34:13.273Z"^^xsd:dateTime;
        <http://www.w3.org/ns/ssn/status>
                "WerkingOnbekend";
        <https://aquafin.be/ns#endTimestampKnown>
                true .
}
