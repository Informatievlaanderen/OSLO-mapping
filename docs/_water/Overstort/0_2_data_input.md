---
layout: default
title: Data voorbeeld
parent: Overstort
nav_order: 1
---

# Data voorbeeld

Om alles overzichtelijk te maken, gieten we de input data (triple store views) in een json structuur. Op die manier krijgen we voor overstort:

TOEVOEGEN:JSON-LD

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
