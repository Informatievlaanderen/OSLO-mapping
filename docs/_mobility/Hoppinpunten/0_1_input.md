---
layout: default
title: Input data
parent: Hoppinpunten
nav_order: 0
---

## Input data

Een synthetische dataset werd gecreëerd voor een hoppinpunt wat de combinatie is van alle bestaande hoppinpunten. Op die manier is de OSLO mapping toepasbaar voor alle bestaande Hoppinpunten, doordat dit synthetische Hoppinpunt alle gebruikte datavelden bevat.

```json
"1-Aalst Station" : {
"Locatie" : {
"CRS" : "EPSG:31370",
"Geometrie" : "POLYGON ((126966 181444,126958.387953251 181405.731656763,126936.710678119 181373.289321881,126904.268343237 181351.612046749,126866 181344,126827.731656763 181351.612046749,126795.289321881 181373.289321881,126773.612046749 181405.731656763,126766 181444,126773.612046749 181482.268343236,126795.289321881 181514.710678119,126827.731656763 181536.387953251,126866 181544,126904.268343237 181536.387953251,126936.710678119 181514.710678119,126958.387953251 181482.268343236,126966 181444))"
},
"Attributen" : {
    "ID": "1",
    "Naam": "Aalst Station",
    "Provincie": "Oost-Vlaanderen",
    "VVR": "Aalst",
    "Gemeente": "Aalst",
    "Status": "Goedgekeurd",
    "Categorie BVR": "Interregionaal",
    "Beheer": [
        "Lokaal bestuur"
    ],
    "Mobiliteitsaanbod": {
            "Deelsystemen": [
               {
                  "Naam" : "Cambio",
                  "Aanbod" : [ "Deelwagens" ],
                  "Logo" : "https://cambio.png",
                  "URL" : "www.cambio.be"
               }
            ],
            "Lijnbus halte": "true",
            "Tramhalte": "true",
            "Kernnet": "true",
            "Aanvullend net": "true",
            "Functioneel net": "true",
            "Metrohalte": "true",
            "Treinstation": "true",
            "VOM flex halte": "true",
            "Deelwagen VOM": "true",
            "Deelfiets VOM": "true",
            "Fietslockers": "true",
            "Deelsteps": "true",
            "Fietspomp": "true",
            "Park and ride": "true",
            "Kiss and ride": "true",
            "Fietsenstalling": [
                {
                    "Overdekt": "true",
                    "Beveiligd": "true",
                    "Toegankelijk buitenmaatse fietsen": "true"
                }
            ],
            "Aantal laadpunten EV": "1",
            "Aantal laadpunten E-bike": "1",
            "Aantal parkeerplaatsen carpool": "1",
            "Aantal parkeerplaatsen wagens": "89",
            "Aantal parkeerplaatsen beperking": "6",
            "Aantal laadpunten EV deelwagens buiten VOM": "2",
            "Aantal parkeerplaatsen deelwagens buiten VOM": "2",
            "Aantal laadpunten E-bike deelfietsen buiten VOM": "1"
        
    },
    "Aanvullend aanbod": {
            "Wachtaccomodatie": "true",
            "Vuilnisbak": "true",
            "Pakketautomaat": "true",
            "Bagagelocker": "true",
            "Fietshersteldienst": "true",
            "Sanitair": "true",
            "Rode brievenbus": "true",
            "AED": "true",
            "Geld automaat": "true",
            "Wifi": "true",
            "Oplaadpunt smartphones": "true",
            "Drinkerwatervoorziening": "true",
            "Vergaderruimte": "true",
            "Voedings-en krantenwinkel": "true",
            "Eet- en drankgelegenheid": "true",
            "Uitleenpunt kinderwagens": "true",
            "Spin-off centrumdiensten": "true"
    },
    "Hoppinzuil": [
        {
            "Locatie": {
                "CRS": "EPSG:31370",
                "Geometrie": "POINT (156579.64 216540.27)"
            },
            "Attributen": {
                "ID": "10",
                "Type": "Interactief"
            }
        }
    ],
    "Adres": "N73 Peerderbaan x N715 Lommelsebaan; 3940 Hechtel-Eksel",
    "Toegankelijkheid": [
        "VisualImpairment",
        "MotorDisability"
    ]
}
}

```