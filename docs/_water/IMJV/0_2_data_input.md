---
layout: default
title: Data voorbeeld
parent: IMJV
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, gieten we de input data (relationele views) in een json structuur. Op die manier krijgen we voor water:

```json
      {
        "observation_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/observatie\/01894963000131\/AW9308001\/transfer\/chemische_stof\/RYGMFSIKBFXOCR-UHFFFAOYSA-N\/2021",
        "observatie_label" : "Observatie Koper 2021",
        "year0" : 2021,
        "emissie_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/lozing\/01894963000131\/AW9308001\/2021",
        "emissie_label" : "Lozing in DENDERLAND-MARTIN : LP Industrieel (2021)",
        "emissie_geom" : "POINT (4.042897000000000000 50.983297000000000000)",
        "debiet_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/lozing\/.well-known\/genid\/01894963000131\/AW9308001\/2021\/debiet",
        "debiet_value" : "68877.00000000000000000000",
        "substantie_url" : "https:\/\/data.omgeving.vlaanderen.be\/id\/concept\/chemische_stof\/RYGMFSIKBFXOCR-UHFFFAOYSA-N",
        "substantie_label" : "Koper",
        "concentratie_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/observatie\/.well-known\/genid\/concentratie\/01894963000131\/AW9308001\/obs\/chemische_stof\/RYGMFSIKBFXOCR-UHFFFAOYSA-N\/2021",
        "concentratie_value" : ".02100000000000000000",
        "concentratie_standardUncertainty" : ".02000000000000000000",
        "meetfrequentie" : "18.00000000000000000000",
        "punt_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/lozingspunt\/01894963000131\/AW9308001\/jaar\/2021",
        "punt_label" : "DENDERLAND-MARTIN : LP INDUSTRIEEL (2021)",
        "pH" : "8.10000000000000000000",
        "bepalingsmethode_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/meetgegevens",
        "bepalingsmethode_label" : "meetgegevens",
        "facility_url" : "https:\/\/data.cbb.omgeving.vlaanderen.be\/id\/exploitatie\/01894963000131",
        "facility_geom" : "POINT (4.0429822 50.9851322)",
        "facility_label" : "DENDERLAND-MARTIN",
        "address_url" : "",
        "address_label" : "Nijverheidslaan 8          , 9308 Aalst, België",
        "value0" : "1.44642",
        "unitMeasure_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/eenheid\/kg_per_jaar",
        "unitMeasure_label" : "kg\/jaar",
        "emissie_type_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/geleidelozing",
        "emissie_type_label" : "Geleide lozing",
        "emissie_class_type" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/ns\/imjv#GeleideLozing",
        "activiteit_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/activiteit\/255",
        "activiteit_label" : "DENDERLAND-MARTIN : Textielveredeling",
        "lozingsplaats_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/riool",
        "lozingsplaats_label" : "riool",
        "meetputtype_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/transfer",
        "meetputtype_label" : "transfer",
        "emissie_type_LT_label" : "Geleide lozing - transfer",
        "emissie_type_LT_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/water\/geleidelozing_transfer",
        "Exploitatie_CBB_ID_IMJV" : "01894963000131",
        "Exploitatie_ETRS89_Lengtegraad_IMJV" : 4.042982233000000000,
        "Exploitatie_ETRS89_Breedtegraad_IMJV" : 50.985132184000000000,
        "Meetput_Historiek_ETRS89_Lengtegraad" : "null", // 4.042982233000000000,
        "Meetput_Historiek_ETRS89_Breedtegraad" : "null", // 50.985132184000000000,
        "Exploitatie_ETRS89_Lengtegraad" : 4.0429822,
        "Exploitatie_ETRS89_Breedtegraad" : 50.9851322,
        "modifiedAtUTC" : "2024-06-05T07:14:44.998Z",
        "modifiedAt" : "2024-06-05T07:14:44.998Z",
        "isDeleted" : 0
      }
```
en voor lucht:

```json
    {
        "observation_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/observatie\/01854307000111\/1-1-1\/geleideemissies\/16181\/obs\/chemische_stof\/UGFAIRIUMAVXCW-UHFFFAOYSA-N\/1977",
        "notation_uit_lijst" : "chemische_stof\/UGFAIRIUMAVXCW-UHFFFAOYSA-N",
        "label" : "Observatie Koolstofmonoxide 1977",
        "vracht_value" : 34.047240,
        "vracht_unitMeasure_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/eenheid\/Ton_per_jaar",
        "vracht_unitMeasure_label" : "ton per jaar",
        "year0" : "1977", 
        "substantie_url" : "CO",
        "bepalingsmethode_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/schatting",
        "bepalingsmethode_label" : "Schatting",
        "concentratie_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/observatie\/01854307000111\/1-1-1\/geleideemissies\/16181\/obs\/chemische_stof\/UGFAIRIUMAVXCW-UHFFFAOYSA-N\/1977\/concentratie",
        "concentratie_value" : 300.000000000000000000,
        "concentratie_unitMeasure_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/doc\/concept\/eenheid\/mg_per_Nm3",
        "concentratie_unitMeasure_label" : "milligram per normaal kubieke meter",
        "controleInstantie" : "TNO",
        "debiet_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/observatie\/01854307000111\/1-1-1\/geleideemissies\/16181\/debiet\/1977",
        "debiet_value" : 134800.000000000000000000,
        "debiet_unitMeasure_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/eenheid\/Nm3_per_uur",
        "debiet_unitMeasure_label" : "normaal kubieke meter per uur",
        "emissieContext_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/productieeenheid",
        "emissieContext_label" : "Productie eenheid",
        "emissieDuur_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/emissieduur\/01854307000111\/1-1-1\/geleideemissies\/16181\/1977\/77",
        "emissieDuur_value" : 77,
        "emissieDuur_unitMeasure_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/eenheid\/uur_per_jaar",
        "emissieDuur_unitMeasure_label" : "uur",
        "emissie_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/emissie\/01854307000111\/1-1-1\/geleideemissies\/16181\/1977",
        "emissie_label" : "Emissie in  SCHOORSTEEN(1977)",
        "emissie_class_type" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/ns\/imjv#Emissie",
        "emissie_type_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/concept\/geleideemissies",
        "emissie_type_label" : "Geleide emissie",
        "inDrogeToestandOpgegeven" : 0,
        "periode" : "Januari tot December \/ Dinsdag tot Vrijdag \/ 0 uur tot 24uur",
        "ritme" : "1\/wk - 90min",
        "punt_url" : "https:\/\/data.imjv.omgeving.vlaanderen.be\/id\/emissiepunt\/01854307000111\/1\/1977",
        "punt_label" : " SCHOORSTEEN",
        "punt_geom_x" : 68390.0,
        "punt_geom_y" : 180345.0,
        "punt_geom_lng" : 3.20789873845389, 
        "punt_geom_lat" : 50.92767872455679,
        "site_url" : "https:\/\/data.cbb.omgeving.vlaanderen.be\/id\/exploitatie\/01854307000111",
        "site_label" : "IVIO",
        "site_geom_x" : 68242.9,
        "site_geom_y" : 180398.0,
        "site_geom_lng" : 3.205794868161017,
        "site_geom_lat" : 50.92813442035296,
        "address_url" : 0,
        "address_label" : "Lodewijk de Raetlaan 9,8870 Izegem",
        "modifiedAtUTC" : "2024-05-07T11:16:16.628Z",
        "modifiedAt" : "2024-05-07T11:16:16.628Z",
        "isDeleted" : 0
    }
```
