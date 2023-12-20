---
layout: default
parent: LUCAS
title: Aanpak
nav_order: 2
---

# Aanpak

Aangezien we zowel ligging, als diepte naast de effectieve geometrie (puntlocatie) willen beschrijven, starten we vanuit een  BoRuimtelijkBemonsteringsobject.

![Alt text](image-3.png)

`BoRuimtelijkBemonsteringsobject` is een `bemonsteringsobject`, hierdoor kunnen we de unieke identificator POINT_ID en het type beschrijven:

```json

"@id": "_:bmo001",
"@type": "BoRuimtelijkBemonsteringsobject",
"Bemonsteringsobject.identificator": {
    "@type": "Identificator",
    "Identificator.identificator": {
        "@value": "47862690",
        "@type": "cl-idt:bemonsteringsobjectid"
    }
},
"Bemonsteringsobject.type": "composite sample",
```

De diepte van de bemonstering kan via "BoRuimtelijkBemonsteringsobject.diepte" beschreven worden:

```json
"BoRuimtelijkBemonsteringsobject.diepte": {
    "@type": "KwantitatieveWaarde",
    "KwantitatieveWaarde.standaardEenheid": {
        "@type": "qudt-schema:Unit",
        "@id": "qudt-unit:M"
    },
    "KwantitatieveWaarde.waarde": 0.2
}
```



Willen we het tijdstip van de effectieve bemonstering toevoegen, dan doen we dit via "Bemonstering.bemonsteringstijdstip":

![Alt text](image-4.png)

```json

            "Bemonsteringsobject.isResultaatVan": {
                "@type": "Bemonstering",
                "Bemonstering.bemonsteringstijdstip": {
                    "@type": "time:Instant",
                    "time:inXSDDateTime": {
                        "@type": "xsd:dateTime",
                        "@value": "2018-07-06"
                    }
                }
            }
```






            "RuimtelijkBemonsteringsobject.geometrie": {
                "@type": "Punt",
                "Geometrie.gml": {
                    "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>16.13421178,47.15023795</gml:coordinates><gml:Point>",
                    "@type": "geosparql:gmlliteral"
                }
            },
            "Bemonsteringsobject.bemonsterdObject": "",
            "Bemonsteringsobject.geassocieerdeObservatie": [
                "_:Crbn001",
                "_:pH_CaCl2_001",
                "_:pH_H2O_001"
            ]
        },





        {
            "@id": "_:Crbn001",
            "@type": "Meting",
            "Observatie.identificator": {
                "@type": "Identificator",
                "Identificator.identificator": {
                    "@value": "1",
                    "@type": "cl-idt:observatieid_Crbn001"
                }
            },
            "Observatie.resultaat": {
                "@type": "Maat",
                "Maat.maat": {
                    "@type": "KwantitatieveWaarde",
                    "KwantitatieveWaarde.waarde": 12.4,
                    "KwantitatieveWaarde.standaardEenheid": {
                        "@type": "qudt-schema:Unit",
                        "@id": "qudt-unit:GM-PER-KiloGM"
                    }
                }
            },
            "Observatie.geobserveerdKenmerk": "http://inspire.ec.europa.eu/codelist/SoilDerivedObjectParameterNameValue/organicCarbonContent",
            "Observatie.gebruikteProcedure": {
                "@type": "Observatieprocedure",
                "Observatieprocedure.specificatie": "https://www.iso.org/standard/18782.html"
            }
        },



        {
            "@id": "_:pH_CaCl2_001",
            "@type": "Meting",
            "Observatie.identificator": {
                "@type": "Identificator",
                "Identificator.identificator": {
                    "@value": "1",
                    "@type": "cl-idt:observatieid_pH_CaCl2"
                }
            },
            "Observatie.resultaat": {
                "@type": "Maat",
                "Maat.maat": {
                    "@type": "KwantitatieveWaarde",
                    "KwantitatieveWaarde.waarde": 4.1,
                    "KwantitatieveWaarde.standaardEenheid": {
                        "@type": "qudt-schema:Unit",
                        "@id": "qudt-unit:PH"
                    }
                }
            },
            "Observatie.geobserveerdKenmerk": "http://inspire.ec.europa.eu/codelist/SoilDerivedObjectParameterNameValue/pHValue",
            "Observatie.gebruikteProcedure": {
                "@type": "Observatieprocedure",
                "Observatieprocedure.specificatie": "https://www.iso.org/standard/40879.html"
            }
        },



        {
            "@id": "_:pH_H2O_001",
            "@type": "Meting",
            "Observatie.identificator": {
                "@type": "Identificator",
                "Identificator.identificator": {
                    "@value": "1",
                    "@type": "cl-idt:observatieid_pH_H2O"
                }
            },
            "Observatie.resultaat": {
                "@type": "Maat",
                "Maat.maat": {
                    "@type": "KwantitatieveWaarde",
                    "KwantitatieveWaarde.waarde": 4.81,
                    "KwantitatieveWaarde.standaardEenheid": {
                        "@type": "qudt-schema:Unit",
                        "@id": "qudt-unit:PH"
                    }
                }
            },
            "Observatie.geobserveerdKenmerk": "http://inspire.ec.europa.eu/codelist/SoilDerivedObjectParameterNameValue/pHValue",
            "Observatie.gebruikteProcedure": {
                "@type": "Observatieprocedure",
                "Observatieprocedure.specificatie": "https://www.iso.org/standard/40879.html"
            }