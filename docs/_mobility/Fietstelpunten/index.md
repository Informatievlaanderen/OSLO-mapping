---
layout: default
title: Fietstelpunten
has_children: true
---

# Fietstelpunten

<div style="text-align: left;">

De telpunten langs belangrijke fietsverbindingen verzamelen heel wat nuttige informatie. Dankzij deze fietstelpunten brengen we het verplaatsingsgedrag van fietsers in kaart. Zo maken we het fietsbeleid slimmer en accurater.

De fietstelpunten zijn fietstelpalen met display, maar ook onzichtbare fietstellussen. Hiermee kunnen we op een eenvoudige manier belangrijke info verzamelen:

* hoeveel fietsers rijden er per jaar?
* Wat is het aantal op piekmomenten?
* Wanneer zijn die piekmomenten?
* Wordt de route ook ‘s nachts gebruikt?

<img src="https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/Fietstelpunt.jpg" width="200" alt="My Image" id="hp"/>

Fietstelpalen hebben ook een motiverende en sensibiliserende functie, fietsers weten dat ze niet alleen zijn en ook de omgeving ziet dat mensen bewust een mobiliteitskeuze maken. De data die we hieruit verkrijgen helpt ons het fietsbeleid te optimaliseren.

</div>

<p align="center"><img src="https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/Fietstellus_schets.jpg" width="60%" text-align="center"></p>


## Input data

Gegevens komen van een tellus van AWV. Datasets worden in bulk gepubliceerd via [](https://opendata.apps.mow.vlaanderen.be/fietstellingen/index.html)

Hierover dit:
Meetpunt (blauwe pin op de kaart) ligt langs een fietsbrug in Machelen en meer bepaald langs Wegsegment https://data.vlaanderen.be/id/wegsegment/662242:

![Wegsegment](https://raw.githubusercontent.com/samuvack/OSLO-mapping/main/docs/images/wegsegment_fietstellus.png)

Coordinaatinfo van deze fietsbrug vinden we hier https://api.basisregisters.dev-vlaanderen.be/v1/wegsegmenten/662242, waaruit we kunnen afleiden dat het beginpunt rechtsonder
ligt en het eindpunt rechtsboven, het meetpunt ligt dus aan de kant vd weg die gelijkloopt met de digitalisatierichting.

Brucargo ligt in het oosten, Machelen in het westen. De IN en OUT bij de rijrichtingen matchen dus resp met de gelijklopende wegkant en de tegengestelde wegkant.

Er rijden tussen 7u45 en 8u op 1/8/2019 dus 7 fietsers richting Machelen en 4 richting Brucargo.

## Aanpak

We maken twee Verkeersmetingen, vrm001 en vrm002, één per Rijrichting.
Het geobserveerdKenmerk "\_:mpt001" is voor beide metingen hetzelfde, nl het aantal fieters waarbij "Aantal" het type kenmerk is en "Fiets" het voertuigtype. Deze waarden komen uit codelijsten die worden opgesteld in het kader van de implementatie van de Mobility dataspace.

Resultaat is in beide gevallen een integer.
De meting is uitgevoerdMet mti001, we veronderstellen dat dit een Sensor is vh type "PneumatischeTelslang" en dat deze "Assentelling" als Observatieprocedure implementeert. Hier verwijzen we naar de codelijst: [](https://data.vlaanderen.be/doc/concept/VkmMeetInstrumentType/rubberslang)

De fenomeentijd is voor beide metingen dezelfde, nl een periode op 1/8/2019 tussen 7u45 en 8u.
We zouden de metingen rechtstreeks kunnen koppelen aan de Rijrichtingen waarop ze slaan (geobserveerdObject is Rijrichting x), maar we kiezen er hier voor om het
Verkeersmeetpunt als geobserveerdObject op te geven, dat deze Rijrichtingen bemonstert.

{: .note }
Deze werkwijze benadert meer de OpenLR-aanpak waarmee we compatibel willen zijn.

We maken hiervoor twee inline Verkeersmeetpunten, één per Rijrichting die we bemonsteren.

{: .warning }
Beide Rijrichtingen worden eigenlijk met hetzelfde Verkeersmeetpunt gemonitord (telslang over de ganse weg). Probleem is dat we dan met twee bemonsterdeObjecten zitten voor eenzelfde Verkeersmeting en dus niet meer duidelijk is op welke Rijrichting het ultiem geobserveerdObject is van de Verkeersmeting.

{: .note }
ISO O&M laat dus niet toe om een Bemonsteringsobject ruimer te definiëren dan het object waarop de meting slaat. Oplossing die het zelf aanbiedt is om dmv de associatie geassocieerdBemonsteringsobject en de klasse Bemonsteringsobjectcomplex een omvattend Bemonsteringsobject te creëren.

{: .note }
Het omvattend Verkeersmeetpunt correspondeert met de site vermeld in de data en toevoeging daarvan aan het datavoorbeeld zou meteen het probleem oplossen dat de gegevens daarvan (situering, beheerder, datum inGebruikname etc) momenteel ontbreken.

Om de twee inline Verkeersmeetpunten te situeren langs het Wegsegment maken we een Puntreferentie aan, ttz we geven aan waar het punt ligt door de afstand op te geven (offset in OpenLR) tov het begin vd geometrie van het Wegsegment.

{: .note }
Alternatief zou zijn om de ligging van beide meetpunten gewoon dmv de coördinaten van het omvattend meetpunt te beschrijven, deze coördinaten staan ook in de aangeleverde data. Hier wordt
•
Toepassingsrichting is "bothDirections" omdat de meetpunten beide wegkanten monitoren (telslang over de ganse weg). Alternatief zou twee aparte netwerkreferenties omvatten,
een per richting.

{: .note }
opPositie is momenteel niet gekend, moet berekend worden uit de geometrie vh Wegsegment, rekening houdend met de ligging vh startpunt vd geometrie. Wat we alvast wel weten is dat het startpunt in het oosten ligt en we dus van daaruit de afstand moeten bepalen.

We beschrijven beide Rijrichting elk met hun ligging tov het Wegsegment, de richting naar Brucargo loopt west-oost en heeft dus als richting "inOpppositeDirection", de andere richting
loopt oost-west en heeft "inDirection" als richting.

{: .note }
we bepaalde dit manueel op basis van de richting van het Wegsegment en de beschrijving, maar in praktijk zal dit automatisch moeten gebeuren op basis van de IN en OUT waarden bij richting en data.

Merk op dat we in al de netwerkreferenties referen naar Wegsegment https://data.vlaanderen.be/id/wegsegment/662242 verwijzen en niet Wegsegment T2110002.
Hoogstwaarschijnlijk gaat het echter over hetzelfde Wegsegment. TODO: te verifiëren.

