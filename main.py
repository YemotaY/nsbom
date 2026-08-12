# SBOM (Software Bill of Materials) Klasse für NPM + Python venv's
# Utilisiert für npm -> "npm ls --json" & python -> "pip list --format=json"
# Das Ergebnis wird als JSON geparst und kann als kleine Webanwendung hirarchisch begutachtet werden
# Erweiterungsideen: Versionierung & Vergleiche, Exporte in gängige Formate, einfache Schwachstellensuche
# !!! npm muss immer global installiert sein fuer die nutzung !!!
# letzte Änderungen am 09.09.2025 von SBO

# Standardimporte
import time
import json
from pathlib import Path
import platform
import subprocess
import sys

# Eigene Exceptions
from exceptions.invalider_typ_exception import InvaliderTypException
from exceptions.illegaler_pfad_exception import IllegalerPfadException


class SBOM:
    
    # Initialisierungsparameter:
    # projekt_typ(str) -> einer der verfuegbaren projekttypen
    # pfad(pathlib.Path) -> ist standard auf den Lokalen Ordner der Programmausführung gerichtet
    # kann aber auf einen Projekt Oberordner gerichtet werden via pathlib.Path

    def __init__(self, projekt_typ, pfad=None):

        #Kann dynamisch erweitert werden...
        self.verfuegbare_projekte = [{"id":"npm","command":["npm.cmd", "ls", "--json"]}, {"id":"python","command":["pip", "list", "--format=json"]}]
        self.id = time.time_ns()
        self.projekt_typ = self.validiere_projekt(projekt_typ)
        self.selber_pfad = None 
        self.pfad = self.validiere_pfad(pfad)
        self.host_bs = platform.system()   
                             
        if self.host_bs == "":
            raise Exception("Kein Betriebssystem erkannt.")
        
        #Hier holen wir uns den Baum als JSON. 
        print(self.scanne_baum())


    def scanne_baum(self):
        #Jetzt wissen wir projekttyp und ordner! Jetzt starten wir mit dem lesen des Baumes
        try:
            match self.selber_pfad:
                case True:
                    #Selber Ordner jetzt unterscheiden nach projekttyp
                    for i in range(0,len(self.verfuegbare_projekte)):
                        if(self.verfuegbare_projekte[i]["id"] == self.projekt_typ):
                            self.roh_ergebnis = subprocess.run(
                                self.verfuegbare_projekte[i]["command"],
                                capture_output=True,
                                text=True,
                                check=True
                            )
                            geparst = json.loads(self.roh_ergebnis.stdout)
                            return geparst
                case False:
                    #Benutzerdefinierter Ordner
                    for i in range(0,len(self.verfuegbare_projekte)):
                        if(self.verfuegbare_projekte[i]["id"] == self.projekt_typ):

                            self.roh_ergebnis = subprocess.run(
                                self.verfuegbare_projekte[i]["command"],
                                capture_output=True,
                                cwd=self.pfad,
                                text=True,
                                check=True
                            )
                            geparst = json.loads(self.roh_ergebnis.stdout)
                            return geparst

        except Exception as e:
            print("Bem parsen des Baumes trat folgender fehler auf " + str(e))
            sys.exit()

    def validiere_pfad(self, pfad):
        if pfad is None:
            self.selber_pfad = True
            return Path.cwd()
        try:
            self.selber_pfad = False
            pfad_obj = Path(pfad).resolve(strict=True)
            return pfad_obj
        except Exception:
            raise IllegalerPfadException(pfad)

    def validiere_projekt(self, projekt_typ):
        if not isinstance(projekt_typ, str):
            raise InvaliderTypException("projekt_typ", str, type(projekt_typ))
        ungueltig = True
        for i in range(0,len(self.verfuegbare_projekte)):
            if(self.verfuegbare_projekte[i]["id"] == projekt_typ):
                ungueltig = False
        if ungueltig:
            raise ValueError(
                f"Ungültiger Projekttyp '{projekt_typ}'. Erlaubt sind: {self.verfuegbare_projekte}"
            )
        return projekt_typ


# Testbereich
try:
    #bei python muss es direkt auf das venv zeigen ohne /pip.exe
    #C:\Users\admin\Desktop\nsbom\testvenv\Scripts
    #bei npm nur der ordner des package.json
    test_Klasse = SBOM("npm",pfad=r"C:\Users\admin\Desktop\nsbom")
except Exception as e:
    print(e)
