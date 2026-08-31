# Kein einzelner Ersatz -- sondern ein ganzes Portfolio an Wasserspeichern

*Ein allgemeinverständliches Begleitdokument zu
`distributed-buffer-resilience-utac` (GenesisAeon P103). Bewusst auf
Deutsch und ohne Fachjargon geschrieben -- die technische Dokumentation
(README, DISCLAIMER, Quellcode) bleibt Englisch für das internationale
Ecosystem.*

## Abstract

Die vorherigen Pakete dieser Serie (P99-P102) haben gezeigt: Gletscher
als natürlicher Wasserpuffer schwinden, künstliche Ersatzinfrastruktur
allein deckt höchstens rund 65 Prozent davon ab, und der Verlust bringt
zusätzliche geologische Risiken mit sich. Dieses Paket zieht die
Konsequenz daraus: Kein einzelner Speichertyp -- weder Stauseen noch
Grundwasser noch Feuchtgebiete allein -- kann einen Gletscher ersetzen.
Was tatsächlich hilft, ist ein **Portfolio** aus verschiedenen Puffern
mit unterschiedlichen Reaktionszeiten, kombiniert. Der stärkste reale
Beleg dafür kommt nicht aus einer Modellrechnung, sondern aus einem
bereits eingetretenen Ereignis: der Schweizer Dürre von 2022.

## Der stärkste Beleg: die Dürre 2022 in der Schweiz

Eine Studie von 2026 untersuchte 88 vergletscherte Einzugsgebiete
während der extremen Dürre 2022 in der Schweiz. Das Ergebnis zeigt
beide Seiten gleichzeitig, real gemessen, nicht projiziert: Die
Gletscherschmelze hat die fehlenden Niederschläge und die fehlende
Schneeschmelze tatsächlich spürbar abgefedert -- der Puffer hat
funktioniert. Gleichzeitig war die absolute Menge an Schmelzwasser im
Sommer bereits in rund zwei Dritteln der untersuchten Gebiete niedriger
als beim vorherigen Extremjahr 2003. Der Puffer wirkt also noch -- aber
er wird gleichzeitig kleiner. Beides ist wahr, zur selben Zeit.

## Wie groß ist das theoretische Ersatzpotenzial weltweit?

Eine Studie von 2019 berechnet: In den eisfrei werdenden Becken weltweit
gäbe es theoretisch Platz für rund 875 Kubikkilometer neuen Wasserspeicher
über etwa 185.000 Gletscher hinweg. Nach einer ersten technischen,
ökologischen und wirtschaftlichen Prüfung bleiben davon aber nur rund 40
Prozent (355 Kubikkilometer) realistisch nutzbar. Auch das ist wichtig,
um die oft zitierte große Zahl richtig einzuordnen: theoretisches
Potenzial und realistisch nutzbares Potenzial sind zwei verschiedene
Dinge.

## Warum "Wassertürme" und wer davon abhängt

Der Begriff "Wasserturm" beschreibt Gebirgsregionen, die Menschen
stromabwärts überproportional mit Wasser versorgen. Eine Studie von 2020
zeigt: weltweit sind etwa 1,9 Milliarden Menschen von solchen Systemen
abhängig -- und einige der wichtigsten Wassertürme (etwa entlang des
Indus, des Amu Darja oder des Tarim) gehören gleichzeitig zu den
verletzlichsten.

## Vorsicht bei "natürlichen Lösungen"

Ein wichtiger, ehrlicher Zusatzbefund: eine systematische Übersichtsstudie
von 2025 zeigt, dass sich Ökosystemleistungen nach Gletscherrückgang
zwar oft positiv entwickeln können (etwa Klimaregulierung, Erosionsschutz)
-- aber uneinheitlich, mit echten Zielkonflikten. Man darf also nicht
automatisch annehmen, dass eine "naturbasierte" Maßnahme hydrologisch
positiv wirkt, nur weil sie natürlich klingt -- das muss vor Ort
tatsächlich gemessen werden.

## Was schwächer belegt ist -- und bewusst getrennt bleibt

Dieses Paket enthält zusätzlich eine eigene Kennzahl ("Glacier Buffer
Replacement Score"), die aus einem Recherchebericht übernommen und in
Code umgesetzt wurde -- sie ist **keine wissenschaftlich begutachtete
Metrik**, sondern eine eigene, im Code durchgehend mit einer Warnung
versehene Umsetzung einer vorgeschlagenen Formel ohne eigenständige
Primärquelle.

## Was wir NICHT behaupten

- Dass ein Portfolio aus Speichern den Verlust der Gletscher
  vollständig ausgleichen kann -- dieselbe physikalische Obergrenze wie
  bei P100 (rund 65 Prozent, unter idealen Bedingungen) gilt weiterhin;
  dieses Paket verbreitert die Werkzeugpalette, hebt die Grenze aber
  nicht auf.
- Dass naturbasierte Maßnahmen automatisch positiv wirken -- das wird
  im Code ausdrücklich verneint und muss lokal überprüft werden.
- Dass der "Glacier Buffer Replacement Score" eine etablierte,
  begutachtete Kennzahl ist -- ist er nicht, siehe oben.
- Dieses Paket enthält bewusst **keine** UTAC/CREP/AFET-Verknüpfung --
  die reale Hydrologie steht für sich.

## Quellen

Vollständige Zitationen (Autor:innen, Journal, DOI) stehen in
[DISCLAIMER.md](DISCLAIMER.md) und [CITATION.cff](CITATION.cff). Der
begleitende Software-Baustein ist auf
[GitHub](https://github.com/GenesisAeon/distributed-buffer-resilience-utac)
veröffentlicht.
