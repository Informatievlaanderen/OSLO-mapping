---
layout: default
title: Stap voor stap
parent: VMM
nav_order: 2
---

# Context

De @context sleutel definieert de context waarin de termen in het document worden geïnterpreteerd. Hier worden zowel naar externe contexten (URL's) als codelijsten verwezen.

Externe contexten: De eerste twee URL's verwijzen naar applicatieprofielen die specifieke termen en definities bevatten voor sensoren, bemonstering, observaties en metingen.

Codelijsten: Dit is een lijst van prefixen die worden gebruikt om termen in het document korter en leesbaarder te maken. Bijvoorbeeld, time verwijst naar het W3C Time Ontology, en qudt-schema verwijst naar het QUDT schema voor eenheden en dimensies.

# Graph 

De @graph sleutel bevat een lijst van objecten die de daadwerkelijke data van het document vertegenwoordigen. Elk object heeft een @type dat het type van het object aangeeft.


<table border="0">
 <tr>
<td>input</td>
<td>output</td>

 </tr>
 <tr>
 <td>
{% highlight json %}
{
    "@context": [
        "https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit/kandidaatstandaard/2022-10-17/context/waterkwaliteit-ap.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/statistiek/kandidaatstandaard/2022-10-17/context/statistiek-ap.jsonld",
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
            "qudt-unit": "https://qudt.org/vocab/unit/"
        }
    ]}
{% endhighlight %}
</td>
 <td>
{% highlight json %}
{
    "@context": [
        "https://data.vlaanderen.be/doc/applicatieprofiel/waterkwaliteit/kandidaatstandaard/2022-10-17/context/waterkwaliteit-ap.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/statistiek/kandidaatstandaard/2022-10-17/context/statistiek-ap.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/generiek-basis/zonderstatus/2019-07-01/context/generiek-basis.jsonld",
        {
{% endhighlight %}
</td>

 </tr>
</table>