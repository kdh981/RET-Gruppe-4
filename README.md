<h1>Gruppenarbeit Gruppe-4 <img src="images/Logo Gruppe 4.png" width="100"></h1>

## Ziel:
Das Ziel des Projekts ist es, ein Energiesystemmodell zu entwickeln, das flexibel am dem fluktuierenden Strommarkt operiert, um maximalen Gewinn aus Stromverkäufen zu erzielen, während gleichzeitig der schwankende Wärmebedarf erfüllt wird.

Vor Beginn der eigentlichen Modellentwicklung werden fünf verschiedene Übungsaufgaben gelöst, um die mathematische Formulierung, insbesondere die Zielfunktion und die Nebenbedingungen, zu üben. Dabei geht es auch um die Reduktion des Optimierungsproblems sowie um den Einsatz verschiedener Optimierungstools und deren praktische Anwendung.

Für mehr Informationen wie unser Modell aufgebaut ist, besucht gerne unsere [Internetwebseite](https://kdh981.github.io/RET-Gruppe-4/).


## Installation
Es wird für eine funktionierende Modellierung eines Dampferzeugers TESPy benötigt. Dafür muss TESPy mit folgendem Befehl installiert werden:  

Zur Modellbildung und Optimierung muss Pyomo und Python-Optimierungstools Gurobi installiert werden, die mit den folgenden Befehl installiert werden können:
```bash
pip install tespy
```
CoolProp ist eine Python-Bibliothek, die genaue Daten über thermodynamische Eigenschaften verschiedener Stoffe liefert. Sie ist besonders nützlich für Ingenieure, Wissenschaftler und studierende in verschiedenen Bereichen, wie Kraftwerkstechnik, Klimatechnik und Verfahrenstechnik, da sie umfassende Informationen für die Modellierung von Prozessen und die Analyse von Stoffeigenschaften bietet. Zur Modellbildung muss CoolProp installiert werden:
```bash
pip install CoolProp
```
