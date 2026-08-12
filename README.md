# NSBOM - Node.js & Python SBOM Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/node.js-required-green.svg)](https://nodejs.org/)

Ein Tool zur automatischen Generierung von Software Bill of Materials (SBOM) für Node.js NPM-Projekte und Python Virtual Environments.

## Features

- **Dual Support**: Unterstützt sowohl NPM- als auch Python-Projekte
- **Automatische Erkennung**: Scannt Abhängigkeiten automatisch
- **JSON Output**: Strukturierte Ausgabe für weitere Verarbeitung
- **Cross-Platform**: Funktioniert auf Windows, macOS und Linux
- **Flexible Pfade**: Kann lokale oder benutzerdefinierte Projektpfade verwenden
- **Sicherheits-Scanner**: Enthält PowerShell-Script zur Erkennung kompromittierter Pakete

## Voraussetzungen

### System Requirements
- Python 3.8 oder höher
- Node.js und NPM (für NPM-Projekte)
- PowerShell (für Sicherheits-Scans)

### Python Dependencies
- Keine externen Dependencies erforderlich (nutzt nur Standard-Bibliothek)

## 🛠Installation

1. Repository klonen:
```bash
git clone https://github.com/yourusername/nsbom.git
cd nsbom
```

2. Python Virtual Environment erstellen (empfohlen):
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. Dependencies installieren (falls erforderlich):
```bash
pip install -r requirements.txt
```

## Verwendung

### Grundlegende Verwendung

```python
from main import SBOM

# NPM-Projekt scannen
npm_sbom = SBOM("npm", pfad=r"C:\path\to\your\npm\project")

# Python Virtual Environment scannen
python_sbom = SBOM("python", pfad=r"C:\path\to\your\venv\Scripts")

# Aktuelles Verzeichnis scannen
local_sbom = SBOM("npm")  # oder "python"
```

### Kommandozeilen-Verwendung

```bash
# NPM-Projekt
python main.py

# Mit angepasstem Code für CLI-Parameter
python main.py --type npm --path /path/to/project
```

### Sicherheits-Scan

Führe den PowerShell-Scanner aus, um kompromittierte Pakete zu finden:

```powershell
.\scan.ps1
```

## 🏗Projektstruktur

```
nsbom/
├── main.py                 # Haupt-SBOM-Klasse
├── scan.ps1               # PowerShell-Sicherheits-Scanner
├── package.json           # NPM-Konfiguration für Tests
├── exceptions/            # Custom Exception Classes
│   ├── __init__.py
│   ├── illegaler_pfad_exception.py
│   └── invalider_typ_exception.py
├── testvenv/             # Test Virtual Environment
└── README.md
```

## API-Referenz

### SBOM Klasse

#### Constructor
```python
SBOM(projekt_typ, pfad=None)
```

**Parameter:**
- `projekt_typ` (str): "npm" oder "python"
- `pfad` (str, optional): Pfad zum Projekt. Standard: aktuelles Verzeichnis

#### Methoden

##### `scanne_baum()`
Scannt das Projekt und gibt die Abhängigkeiten als JSON zurück.

**Returns:** Dict mit allen gefundenen Abhängigkeiten

##### `validiere_pfad(pfad)`
Validiert und konvertiert den gegebenen Pfad.

**Parameters:**
- `pfad` (str): Zu validierender Pfad

**Returns:** Path-Objekt

**Raises:** `IllegalerPfadException` bei ungültigem Pfad

##### `validiere_projekt(projekt_typ)`
Validiert den Projekttyp.

**Parameters:**
- `projekt_typ` (str): Zu validierender Projekttyp

**Returns:** String des validierten Projekttyps

**Raises:** 
- `InvaliderTypException` bei falschem Typ
- `ValueError` bei ungültigem Projekttyp

## Exception Handling

Das Projekt verwendet custom Exceptions für bessere Fehlerbehandlung:

- `IllegalerPfadException`: Wird ausgelöst bei ungültigen Pfaden
- `InvaliderTypException`: Wird ausgelöst bei falschen Datentypen

## Testing

```bash
# Teste mit NPM-Projekt
python -c "from main import SBOM; SBOM('npm')"

# Teste mit Python-Projekt
python -c "from main import SBOM; SBOM('python')"
```

## Sicherheit

Das `scan.ps1` Script sucht nach bekannten Malware-Signaturen in node_modules:
- Erkennt den Pattern `const _0x112fa8` (bekannter Malware-Indikator)
- Scannt rekursiv alle Dateien im node_modules Verzeichnis

## Contributing

Beiträge sind willkommen! Bitte:

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/nsbom.git
cd nsbom
python -m venv dev-env
source dev-env/bin/activate  # Windows: dev-env\Scripts\activate
```

## Roadmap

- [ ] **Versionierung & Vergleiche**: SBOM-Versionen vergleichen
- [ ] **Export-Funktionen**: Export in gängige SBOM-Formate (SPDX, CycloneDX)
- [ ] **Schwachstellensuche**: Integration mit CVE-Datenbanken
- [ ] **Web-Interface**: Hierarchische Darstellung als Webanwendung
- [ ] **CLI-Interface**: Vollständige Kommandozeilen-Unterstützung
- [ ] **Docker Support**: Container-basierte Scans
- [ ] **CI/CD Integration**: GitHub Actions, GitLab CI Support

## Verwandte Projekte

- [SPDX Tools](https://github.com/spdx/tools-python)
- [CycloneDX Python](https://github.com/CycloneDX/cyclonedx-python)
- [npm-audit](https://docs.npmjs.com/cli/v6/commands/npm-audit)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) Datei für Details.

## Autor

**YemotaY** - Initial work

## Danksagungen

- NPM-Team für die `npm ls --json` Funktionalität
- Python-Team für die `pip list --format=json` Funktionalität
- Open Source Community für Inspiration und Tools

## Status

Aktueller Status: **Beta** - Grundfunktionalität implementiert, weitere Features in Entwicklung.

Letzte Aktualisierung: 09.09.2025
