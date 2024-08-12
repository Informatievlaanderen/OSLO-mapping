---
layout: default
title: Data voorbeeld
parent: Overstort
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, voorzien we onderstaand een JSON-LD voorbeeld van een Event. De brondata wordt meteen aangeleverd in JSON-LD-formaat.
Op die manier krijgen we voor overstort:


```json
      {
  "@context": [
    "https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit/kandidaatstandaard/2023-06-01/context/waterkwaliteit-ap.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/statistiek/kandidaatstandaard/2023-06-01/context/statistiek-ap.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/generiek-basis/zonderstatus/2019-07-01/context/generiek-basis.jsonld",
    {
      "adms": "http://www.w3.org/ns/adms#",
      "qudt-schema": "https://qudt.org/schema/qudt/",
      "dcterms": "http://purl.org/dc/terms/",
      "time": "http://www.w3.org/2006/time#",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "qudt-unit": "https://qudt.org/vocab/unit/",
      "sosa": "http://www.w3.org/ns/sosa/"
    }
  ],
  "@graph": [
    {
      "@id": "_:obv001",
      "@type": "Observatieverzameling",
      "Observatieverzameling.geobserveerdObject": "_:mpt001",
      "Observatieverzameling.geobserveerdKenmerk": [
        "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0030",
        "https://data.vlaanderen.be/id/concept/waterkwaliteit/hoogte",
		"https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0053"
      ],
      "Observatieverzameling.fenomeentijd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "2024-07-29T14:00:00Z"
        }
      },
      "Observatieverzameling.heeftLid": [
        "_:wko001",
        "_:wko002"
      ]
    },
    {
      "@id": "_:wko001",
      "@type": "OverstortMetingParameterObservatie",
      "Observatie.geobserveerdObject": "_:mpt001",
      "OverstortMetingParameterObservatie.geobserveerdKenmerk": {
        "@id": "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0030",
        "skos:prefLabel": "Temperatuur"
      },
      "WaterkwaliteitParameterObservatie.OverstortMetingParameterResultaat": {
        "@type": [
          "Maat",
          "KwantitatieveWaarde"
        ],
        "KwantitatieveWaarde.waarde": 22.5,
        "KwantitatieveWaarde.standaardEenheid": {
          "@type": "qudt-schema:Unit",
          "@id": "qudt-unit:DEG_C"
        }
      },
      "Observatie.fenomeentijd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "2024-07-29T14:00:00Z"
        }
      },
      "Observatie.gebruikteProcedure": {
        "@type": "Observatieprocedure",
        "Observatieprocedure.type": "https://example.com/concept/observatieproceduretype/OW19"
      },
      "Observatie.isWaargenomenMet": "_:P2046600"
    },
    {
      "@id": "_:wko002",
      "@type": "OverstortMetingParameterObservatie",
      "Observatie.geobserveerdObject": "_:mpt001",
      "OverstortMetingParameterObservatie.geobserveerdKenmerk": {
        "@id": "https://data.vlaanderen.be/id/concept/waterkwaliteit/hoogte",
        "skos:prefLabel": "Waterhoogte"
      },
      "OverstortMetingParameterObservatie.OverstortMetingParameterResultaat": {
        "@type": [
          "Maat",
          "KwantitatieveWaarde"
        ],
        "KwantitatieveWaarde.waarde": -0.5,
        "KwantitatieveWaarde.standaardEenheid": {
          "@type": "qudt-schema:Unit",
          "@id": "qudt-unit:Meter"
        }
      },
      "Observatie.fenomeentijd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "2024-07-29T14:00:00Z"
        }
      },
      "Observatie.gebruikteProcedure": {
        "@type": "Observatieprocedure",
        "Observatieprocedure.type": "https://example.com/concept/observatieproceduretype/OW19"
      },
      "Observatie.isWaargenomenMet": "_:P2046600"
    },
	{
      "@id": "_:wko003",
      "@type": "OverstortMetingParameterObservatie",
      "Observatie.geobserveerdObject": "_:mpt001",
      "OverstortMetingParameterObservatie.geobserveerdKenmerk": {
        "@id": "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0053",
        "skos:prefLabel": "Debiet"
      },
      "OverstortMetingParameterObservatie.OverstortmetingParameterResultaat": {
        "@type": [
          "Maat",
          "KwantitatieveWaarde"
        ],
        "KwantitatieveWaarde.waarde": 0.0,
        "KwantitatieveWaarde.standaardEenheid": {
          "@type": "qudt-schema:Unit",
          "@id": "qudt-unit:CubicMeterPerSecond"
        }
      },
      "Observatie.fenomeentijd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "2024-07-29T14:00:00Z"
        }
      },
      "Observatie.gebruikteProcedure": {
        "@type": "Observatieprocedure",
        "Observatieprocedure.type": "https://example.com/concept/observatieproceduretype/OW19"
      },
      "Observatie.isWaargenomenMet": "_:P2046600"
    }
    {
      "@id": "_:P2046600",
      "@type": "sosa:Sensor",
      "dcterms:identifier": "P2046600",
      "sosa:observes": [
		"https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0030",
        "https://data.vlaanderen.be/id/concept/waterkwaliteit/hoogte",
        "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/0053"
		]
    }
  ]
}

```
