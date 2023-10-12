---
layout: default
parent: Geomobility
title: Data voorbeeld
nav_order: 3
---

# Data voorbeeld Geomobility

### Voorbeeld site

```json
{
  "id": "05d50e16-2e4e-414a-921a-91a1ea11cb02",
  "name": "Site 38",
  "address": "Noorweegse Kaai",
  "geometry": {
    "type": "Point",
    "coordinates": [3.2421013712883, 51.2257868862067]
  },
  "country": "BE",
  "subdivision": "BE-BRU",
  "origins": [
    {
      "name": "A",
      "geometry": {
        "type": "Point",
        "coordinates": [3.24239104986191, 51.2259355430829]
      }
    },
    {
      "name": "B",
      "geometry": {
        "type": "Point",
        "coordinates": [3.24177950620651, 51.2256331896095]
      }
    }
  ]
}
```

### Voorbeeld meeting

```json
{
  "id": "5ff87dcd9dc02be13c259e28",
  "type": "atc",
  "origin": "A",
  "destination": "B",
  "classification": "fiets",
  "timestamp": "2016-11-22T09:00:00.000Z",
  "count": 5,
  "poiId": "05d50e16-2e4e-414a-921a-91a1ea11cb02",
  "surveyId": "b18222b9-7cd9-4c3c-adbe-41c0c597ee7d"
}
```
