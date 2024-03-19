<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gruppenarbeit Gruppe-4</title>
    <link rel="stylesheet" href="Website/styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Gruppenarbeit Gruppe-4 <img src="images/Logo.svg" width="100" ></h1>
            <nav>
                <ul>
                    <li><a href="#einleitung">Einleitung und Übersicht</a></li>
                    <li><a href="#modell">Aufbau des Modells</a></li>
                    <li><a href="#ergebnisse">Ergebnisse</a></li>
                    <li><a href="#ausblick">Ausblick</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container">
        <section id="einleitung">
            <h2>Einleitung</h2>
            <p>Für das Modul Vertiefendes Rechnerpraktikum zur Energietechnik ist das Ziel, einen industriellen Dampferzeugungsprozess zu entwerfen, modellieren und zu simulieren. Dafür wird das Programm TESPy und Ebsilon verwendet. 

In der Grundvariante nutzt der modellierte Dampferzeuger Erdgas und verbrennt diese in einer Brennkammer, um die benötigten Dampfstufen zu erreichen. Es ist eine Gasturbine zwischen der Brennkammer und den Wärmetauscher geschaltet, um elektrische Energie zu erzeugen und die hohen Temperaturen der Abwärme Sinnvoll zu nutzten. In weiteren Modellen wird eine Einbindung einer Wärmepumpe sowie solarthermischer Energie betrachtet und diskutiert ob dies eine Sonnvolle Möglichkeit ist den C02 zu reduzieren. 
</p>
        </section>

        <section id="modell">
            <h2>Aufbau des Modells</h2>
            <p>Beschreibung des Modellaufbaus...
            <p>Vorgaben und Annahmen:
            <p>

            <p> Für das Modell sind die Zielwerte in Tablle 1 zusammengefasst. Diese Zielwerte werden in den erstellten Modellen immer erreicht. 
<!-- Tabelle 1 -->


<table id="tabelle-zielwerte">
  <caption>Tabelle 1: Zielwerte</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Einheit</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hochdruckdampf</td>
      <td>p<sub>H</sub>; m&#775;</td>
      <td>bar; t/h</td>
      <td>40 bar; 90 t/h</td>
    </tr>
    <tr>
      <td>Mitteldruckdampf</td>
      <td>p<sub>M</sub>; m&#775;</td>
      <td>bar; t/h</td>
      <td>14 bar; 360 t/h</td>
    </tr>
    <tr>
      <td>Niederdruckdampf</td>
      <td>p<sub>N</sub>; m&#775;</td>
      <td>bar; t/h</td>
      <td>4 bar; 900 t/h</td>
    </tr>
  </tbody>
</table>

<!-- Tabelle 2 -->


<table>
  <caption>Ausgangswerte</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Einheit</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Druckverlust</td>
      <td>pDV</td>
      <td>bar</td>
      <td>1 bar</td>
    </tr>
    <tr>
      <td>Erdgas</td>
      <td>pEG; TEG</td>
      <td>bar; °C</td>
      <td>30 bar; 15 °C</td>
    </tr>
    <tr>
      <td>Luft</td>
      <td>pLuft; Tluft</td>
      <td>bar; °C</td>
      <td>1 bar; 15 °C</td>
    </tr>
    <tr>
      <td>Luftzusammensetzung</td>
      <td>x</td>
      <td>-</td>
      <td>N2: 0,79; O2: 0,21</td>
    </tr>
  </tbody>
</table>

<!-- Tabelle 3 -->

<table>
  <caption>Gasturbinen</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Einheit</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>isentroper Verdichterwirkungsgrad</td>
      <td>&eta;<sub>is,Verdichter</sub></td>
      <td>-</td>
      <td>90%</td>
    </tr>
    <tr>
      <td>maximale Feuerungstemperatur</td>
      <td>T<sub>max_BK</sub></td>
      <td>°C</td>
      <td>1600 °C</td>
    </tr>
    <tr>
      <td>isentroper Expanderwirkungsgrad</td>
      <td>&eta;<sub>is,Expander</sub></td>
      <td>-</td>
      <td>90%</td>
    </tr>
    <tr>
      <td>mechanischer Wirkungsgrad</td>
      <td>&eta;<sub>m</sub></td>
      <td>-</td>
      <td>99%</td>
    </tr>
  </tbody>
</table>

<!-- Tabelle 4 -->

<table>
  <caption>Pumpen</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Einheit</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>isentroper Wirkungsgrad</td>
      <td>&eta;<sub>is</sub></td>
      <td>-</td>
      <td>80%</td>
    </tr>
    <tr>
      <td>mechanischer Wirkungsgrad</td>
      <td>&eta;<sub>m</sub></td>
      <td>-</td>
      <td>99%</td>
    </tr>
  </tbody>
</table>

<!-- Tabelle 5 -->
<table>
  <caption>Generatoren</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Einheit</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mechanisch-elektrischer Wirkungsgrad</td>
      <td>&eta;<sub>m-el</sub></td>
      <td>-</td>
      <td>98,50%</td>
    </tr>
    <tr>
      <td>mechanischer Wirkungsgrad</td>
      <td>&eta;<sub>m</sub></td>
      <td>-</td>
      <td>100%</td>
    </tr>
  </tbody>
</table>



</p>
        
        <section id="ergebnisse">
            <h2>Ergebnisse</h2>
            <p>Darstellung der Ergebnisse...</p>
        </section>

        <section id="ausblick">
            <h2>Ausblick</h2>        
            <p>Die gestellte Aufgabe wurde erfolgreich bewältigt. Alle Ziele wurden erreicht, darunter die Konzeption, Modellierung und Simulation eines industriellen Dampferzeugungsprozesses. Es wurde untersucht, wie sich die Integration einer Wärmepumpe oder einer Solarthermie auf den Gasverbrauch auswirkt. Dabei hat sich herausgestellt, dass … <p>

<p>Für die Zukunft könnten weitere Integrationen moderner und erneuerbarer Technologien modelliert werden, um einen industriellen Dampferzeugungsprozess zu entwerfen, der unabhängig von fossilen Brennstoffen ist. In den bereits erstellten Modellen sind einige Vereinfachungen vorgenommen worden, wie die Annahme einer konstanten Umgebungs-, Kühlwasser- und Erdgastemperatur sowie die Annahme, dass immer ein konstanter Abnehmer des produzierten Dampfes vorhanden ist. Eine dynamische Betrachtung könnte hier zu realistischeren Ergebnissen führen. Es wurde auch angenommen, dass eine vollständige Verbrennung in der Brennkammer stattfindet und dass im System keine Wärme- und Druckverluste auftreten. Präzisere Annahmen könnten zu genaueren Ergebnissen führen, die die Realität besser widerspiegeln. Die Annahme, dass Erdgas ausschließlich aus reinem Methan besteht, ist ebenfalls unrealistisch. Erdgas besteht aus verschiedenen Komponenten. Ein interessanter Ansatz wäre es auch zu untersuchen, welchen Einfluss eine aktive Beimischung von Wasserstoff hat. Hier besteht das Potenzial, den CO2-Fußabdruck zu reduzieren. Auch die Möglichkeit der Erdgasvorwärmung könnte betrachtet werden, um die Effizienz zu steigern. Es gibt also noch viel Potenzial, um ein stark realitätsnahes Modell zu entwickeln.
</p>
        </section>
   
<footer>
    <div class="footer-content">
        <p>Gruppenarbeit Gruppe-4 © 2024</p>
        <p>Kontakt: info@gruppe4.de</p>
    </div>
</footer>


