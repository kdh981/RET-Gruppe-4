<h1>Gruppenarbeit Gruppe-4 <img src="images/Logo Gruppe 4.png" width="100"></h1>

## Ziel
Für das Modul Vertiefendes Rechnerpraktikum zur Energietechnik ist das Ziel, einen industriellen Dampferzeugungsprozess zu entwerfen, modellieren und zu simulieren.

Für mehr Informationen über den Aufbau unseres Modells besuchen Sie gerne unsere [Internetwebseite](https://kdh981.github.io/RET-Gruppe-4/).

## Installation
TESPy steht für Thermal Engineering Systems in Python und ist eine Bibliothek zur Simulation und Berechnung thermodynamischer Kreisläufe und Prozesse. Sie ermöglicht Anwendern, maßgeschneiderte Lösungen für komplexe energietechnische Systeme wie Kraftwerke und Wärmepumpen zu entwickeln, indem sie eine flexible und intuitive Modellierungsumgebung bietet. Für eine funktionierende Modellierung eines Dampferzeugers ist TESPy erforderlich. Dafür muss TESPy mit folgendem Befehl installiert werden:

```bash
pip install tespy
```
CoolProp ist eine Python-Bibliothek, die genaue Daten über thermodynamische Eigenschaften verschiedener Stoffe liefert. Sie ist besonders nützlich für Ingenieure, Wissenschaftler und studierende in verschiedenen Bereichen, wie Kraftwerkstechnik, Klimatechnik und Verfahrenstechnik, da sie umfassende Informationen für die Modellierung von Prozessen und die Analyse von Stoffeigenschaften bietet. Zur Modellbildung muss CoolProp installiert werden:

```bash
pip install CoolProp
```

## Modell: Dampferzeuger
### Fließbild
Hier ist die Abbildung des einfachen modellierten Dampferzeugers, welches die Dampferzeugung rein über die Gasverbrennung bereitstellt:
<img src="docs/Fließbild.PNG" width="300">

## Ergebnis
Ziel ist ein funktionierendes Modell mit TESPy zu erstellen und drei verschiedene Varianten zu betrachten welche der drei Varianten theoretisch den niedrigsten Gasverrbauch aufweist. Das Modell gibt in Tabellenform die benötigen Informationen wieder. Welches Modell den niedrigsten Gas verbrauch aufweist kann man unter unsere [Internetwebseite](https://kdh981.github.io/RET-Gruppe-4/) gerne herausfinden.

## Ausblick
Es können weitere Verbesserungen des Codes und somit ein genaueres Modell erstellt werden, einige Verbesserungen können sein:

### Dynamische Betrachtung
Eine dynamische Betrachtung könnte hier zu realistischeren Ergebnissen führen, da in den bereits erstellten Modellen einige Vereinfachungen vorgenommen worden sind. Diese Annahmen beinhalten unteranderem konstante Umgebungs-, Kühlwasser- und Erdgastemperatur sowie die Annahme, dass immer ein konstanter Abnehmer des produzierten Dampfes vorhanden ist.

### Zukünftige Entwicklungen
Für die Zukunft könnten weitere Integrationen moderner und erneuerbarer Technologien modelliert werden, um einen industriellen Dampferzeugungsprozess zu entwerfen, der unabhängig von fossilen Brennstoffen ist. 

### Elektrifizierung
Intersannt könnte Btrachtung der Elektrifizierung des Dampferzeugers sein. Unter dem Motto Power to Heat. Hier könnte unter der einbindung verschiedener erneuerbaren Energien und ein e-Heizstab eine intersannte Möglichkeit sein den Gasverbrauch auf null zu reduzieren und dabei realistische Werte für den Strommarktpreis für das Modell zu verwenden. 




