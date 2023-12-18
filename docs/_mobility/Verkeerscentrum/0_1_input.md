---
layout: default
title: Input data
parent: Verkeerscentrum
nav_order: 0
---

# Data voorbeeld Verkeerscentrum



De dataset die dient gemapt te worden op bestaande OSLO standaarden, is opgesplitst in 2 datasets. Eén dataset bevat de verkeersmetingen van 1 dag met aggregatieniveau 15 minuten. Deze dataset is beperkt tot de essentiële velden, namelijk:
* locpost: identificatie van de meetpost (doorsnede van de weg)
* Time_measured: begintijdstip van het interval
* int_niet_vracht: intensiteit niet-vrachtverkeer ('auto')
* int_vracht: intensiteit vrachtverkeer
* Vh_niet_vracht: gemiddelde snelheid niet-vrachtverkeer (harmonisch gemiddelde)
* Vh_vracht: gemiddelde snelheid vrachtverkeer (harmonisch gemiddelde)
* rec_kl_gaten: percentage data gereconstrueerd op basis van interpolatie
* rec_geslvak: percentage data gereconstrueerd op basis van een redundante meetpost
* rec_typed: percentage data gereconstrueerd op basis van een type dag
 



## Data voorbeeld

```

locpost	TIME_MEASURED	int_niet_vracht	int_vracht	Vh_niet_vracht	Vh_vracht	rec_kl_gaten	rec_geslvak	rec_typed
100105	2023-09-07  0:00:00.000	8	1	82	62	0	0	0
100105	2023-09-07  0:15:00.000	3	0	87	NULL	0	0	0
100105	2023-09-07  0:30:00.000	1	0	120	NULL	0	0	0
100105	2023-09-07  0:45:00.000	3	2	65	66	0	0	0
100105	2023-09-07  1:00:00.000	0	0	NULL	NULL	0	0	0
100105	2023-09-07  1:15:00.000	1	1	99	63	0	0	0
100105	2023-09-07  1:30:00.000	0	2	NULL	64	0	0	0
100105	2023-09-07  1:45:00.000	3	0	79	NULL	0	0	0
100105	2023-09-07  2:00:00.000	0	4	NULL	62	0	0	0
100105	2023-09-07  2:15:00.000	1	2	79	58	0	0	0

```

## Meetpunten voorbeeld

```json
            "Post": {
                "LocPost": 100105,
                "Offset": 14,
                "Segmentdeel": {
                    "Begin": {
                        "X": 85255.6517999992,
                        "Y": 196641.521899998
                    },
                    "Eind": {
                        "X": 85207.9952000007,
                        "Y": 196729.535599999
                    },
                    "Lengte": 101.904619949324,
                    "SD_ID": 3101004522
                },
                "X": 85217.3483000025,
                "Y": 196719.535100002
            }
```
