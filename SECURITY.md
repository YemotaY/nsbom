# Security Policy

## Unterstützte Versionen

Wir unterstützen die folgenden Versionen mit Sicherheitsupdates:

| Version | Unterstützt        |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Sicherheitslücken melden

Wir nehmen die Sicherheit von NSBOM ernst. Falls Sie eine Sicherheitslücke entdecken, melden Sie diese bitte verantwortungsvoll.

### Meldung von Sicherheitslücken

**Bitte melden Sie Sicherheitslücken NICHT über öffentliche GitHub Issues.**

Senden Sie stattdessen eine E-Mail an: [security@example.com] (ersetzen Sie dies mit Ihrer tatsächlichen E-Mail)

Fügen Sie folgende Informationen hinzu:
- Typ der Sicherheitslücke
- Vollständige Pfade der betroffenen Quelldateien
- Ort der Sicherheitslücke (so spezifisch wie möglich)
- Schritt-für-Schritt-Anweisungen zur Reproduktion
- Proof-of-Concept oder Exploit-Code (falls möglich)
- Potenzielle Auswirkungen der Sicherheitslücke

### Antwortzeit

Wir werden uns bemühen, innerhalb von 48 Stunden zu antworten und ein geschätztes Datum für einen Fix anzugeben.

### Verantwortungsvolle Offenlegung

Wir bitten Sie:
- Geben Sie uns angemessene Zeit, das Problem zu beheben
- Vermeiden Sie den Zugriff auf oder die Änderung von Daten anderer
- Melden Sie das Problem nicht öffentlich, bis wir eine Lösung veröffentlicht haben
- Handeln Sie stets in gutem Glauben

### Sicherheitsfeatures

NSBOM enthält bereits einige Sicherheitsfeatures:

#### PowerShell-Sicherheits-Scanner
- Erkennt bekannte Malware-Signaturen in NPM-Paketen
- Scannt den Pattern `const _0x112fa8` (bekannter Kompromittierungs-Indikator)
- Rekursive Durchsuchung aller node_modules Dateien

#### Eingabe-Validierung
- Pfad-Validierung verhindert Directory Traversal
- Projekttyp-Validierung verhindert Code Injection
- Exception Handling für sichere Fehlerbehandlung

#### Subprocess-Sicherheit
- Verwendung von `subprocess.run()` mit expliziten Argumenten
- Keine Shell-Injection möglich durch feste Kommando-Arrays
- Timeout-basierte Ausführung (kann in Zukunft implementiert werden)

### Bekannte Sicherheitsüberlegungen

#### NPM-spezifisch
- Das Tool führt `npm ls` aus, was package.json und node_modules liest
- Keine Ausführung von package scripts oder hooks
- Nur Lesezugriff auf Abhängigkeitsinformationen

#### Python-spezifisch
- Das Tool führt `pip list` aus, was installierte Pakete auflistet
- Kein Import oder Ausführung von Python-Paketen
- Nur Metadaten-Zugriff auf installierte Pakete

#### Allgemein
- Das Tool benötigt Lesezugriff auf Projektverzeichnisse
- Schreibt keine Dateien (außer optionale Logs)
- Führt keine Remote-Anfragen aus

## Sicherheits-Roadmap

Geplante Sicherheitsverbesserungen:
- [ ] CVE-Datenbank-Integration für Schwachstellenerkennung
- [ ] Digitale Signierung von SBOM-Outputs
- [ ] Sandbox-Modus für unsichere Umgebungen
- [ ] Audit-Logging für alle Operationen
- [ ] Rate-Limiting für API-Aufrufe
- [ ] Input-Sanitization für alle Benutzereingaben

Vielen Dank, dass Sie zur Sicherheit von NSBOM beitragen!
