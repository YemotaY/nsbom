# CHANGELOG

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [Unreleased]

### Geplant
- Web-Interface für hierarchische SBOM-Darstellung
- Export in SPDX und CycloneDX Formate
- CVE-Schwachstellenintegration
- CLI-Interface
- Docker Support

## [1.0.0] - 2025-09-09

### Hinzugefügt
- Grundlegende SBOM-Generierung für NPM-Projekte
- Grundlegende SBOM-Generierung für Globales Python + Virtual Environments
- Eigene Exception Behandlung (`IllegalerPfadException`, `InvaliderTypException`, weitere folgen)
- Automatische Pfad-Validierung
- Projekttyp-Validierung
- JSON-Output für alle Scans
- Cross-Platform-Unterstützung (Windows, macOS, Linux)
- Deutsche Dokumentation und Kommentare

### Technische Details
- Nutzt `npm ls --json` für NPM-Abhängigkeiten
- Nutzt `pip list --format=json` für Python-Abhängigkeiten
- Subprocess-basierte Ausführung für maximale Kompatibilität
- Path-Objekt-basierte Pfad-Behandlung

### Getestet
- Windows 11 mit PowerShell
- Python 3.8+
- Node.js 16+
- NPM 8+

[Unreleased]: https://github.com/yourusername/nsbom/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/nsbom/releases/tag/v1.0.0
