import sys
import os

# Ajout du dossier parent pour l'import des modules de l'app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation de la Guinée (ID: 224) ---")
        
        gn_id = 224
        gn = Country.query.get(gn_id)
        if not gn:
            gn = Country(id=gn_id, name="Guinée", iso_code="GN")
            db.session.add(gn)
            db.session.commit()
            print("Pays Guinée créé.")

        # Données des Régions (Niveau 1), Préfectures (Niveau 2) et Sous-préfectures (Niveau 3)
        guinea_data = {
            "Zone Spéciale de Conakry": {
                "coords": {"lat": 9.5092, "lon": -13.7122},
                "prefectures": {
                    "Conakry": ["Kaloum", "Dixinn", "Ratoma", "Matam", "Matoto", "Kassa"]
                }
            },
            "Boké": {
                "coords": {"lat": 10.9321, "lon": -14.2905},
                "prefectures": {
                    "Boké": ["Boké Centre", "Kamsar", "Sangaredi"],
                    "Boffa": ["Boffa Centre", "Koba", "Douprou"],
                    "Fria": ["Fria Centre", "Baguinet"],
                    "Gaoual": ["Gaoual Centre", "Kounsitel"],
                    "Koundara": ["Koundara Centre", "Youkounkoun"]
                }
            },
            "Kindia": {
                "coords": {"lat": 10.0569, "lon": -12.8658},
                "prefectures": {
                    "Kindia": ["Kindia Centre", "Friguiagbé", "Mambia"],
                    "Coyah": ["Coyah Centre", "Manéah", "Kouriah"],
                    "Dubréka": ["Dubréka Centre", "Tanènè"],
                    "Forécariah": ["Forécariah Centre", "Maferinyah"],
                    "Télimélé": ["Télimélé Centre", "Sogolon"]
                }
            },
            "Mamou": {
                "coords": {"lat": 10.3739, "lon": -12.0915},
                "prefectures": {
                    "Mamou": ["Mamou Centre", "Ouré-Kaba", "Dounet"],
                    "Dalaba": ["Dalaba Centre", "Ditinn"],
                    "Pita": ["Pita Centre", "Timbi-Madina", "Bantignel"]
                }
            },
            "Labé": {
                "coords": {"lat": 11.3175, "lon": -12.2833},
                "prefectures": {
                    "Labé": ["Labé Centre", "Popodara", "Diari"],
                    "Koubia": ["Koubia Centre", "Matakaou"],
                    "Mali": ["Mali Centre", "Yembering"],
                    "Lélouma": ["Lélouma Centre", "Balaya"],
                    "Tougué": ["Tougué Centre", "Kansangui"]
                }
            },
            "Faranah": {
                "coords": {"lat": 10.0410, "lon": -10.7449},
                "prefectures": {
                    "Faranah": ["Faranah Centre", "Tiro", "Beindou"],
                    "Dabola": ["Dabola Centre", "Bissikrima"],
                    "Dinguiraye": ["Dinguiraye Centre", "Lansanaya"],
                    "Kissidougou": ["Kissidougou Centre", "Albadariah"]
                }
            },
            "Kankan": {
                "coords": {"lat": 10.3854, "lon": -9.3057},
                "prefectures": {
                    "Kankan": ["Kankan Centre", "Batè-Sidié", "Milo"],
                    "Kérouané": ["Kérouané Centre", "Banankoro"],
                    "Kouroussa": ["Kouroussa Centre", "Kiniéro"],
                    "Siguiri": ["Siguiri Centre", "Doko", "Kourémalé"],
                    "Mandiana": ["Mandiana Centre", "Koundian"]
                }
            },
            "Nzérékoré": {
                "coords": {"lat": 7.7562, "lon": -8.8179},
                "prefectures": {
                    "Nzérékoré": ["Nzérékoré Centre", "Pale", "Bounouma"],
                    "Beyla": ["Beyla Centre", "Boola"],
                    "Guéckédou": ["Guéckédou Centre", "Tekoulo"],
                    "Lola": ["Lola Centre", "Bossou"],
                    "Macenta": ["Macenta Centre", "Sérédou"],
                    "Yomou": ["Yomou Centre", "Diecké"]
                }
            }
        }

        for region_name, info in guinea_data.items():
            # Niveau 1 (Région)
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=gn_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, 
                    level=1, 
                    country_id=gn_id,
                    latitude=info["coords"]["lat"],
                    longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"-> Région : {region_name}")

            for pref_name, sous_prefs in info["prefectures"].items():
                # Niveau 2 (Préfecture)
                prefecture = AdministrativeDivision.query.filter_by(
                    name=pref_name, level=2, parent_id=region.id
                ).first()
                if not prefecture:
                    prefecture = AdministrativeDivision(
                        name=pref_name, level=2, country_id=gn_id, parent_id=region.id
                    )
                    db.session.add(prefecture)
                    db.session.flush()

                for sp_name in sous_prefs:
                    # Niveau 3 (Sous-préfecture/Commune)
                    if not AdministrativeDivision.query.filter_by(
                        name=sp_name, level=3, parent_id=prefecture.id
                    ).first():
                        sp = AdministrativeDivision(
                            name=sp_name, level=3, country_id=gn_id, parent_id=prefecture.id
                        )
                        db.session.add(sp)
        
        db.session.commit()
        print("\n" + "="*45)
        print("Succès : Les données de la Guinée sont à jour !")
        print("="*45)

if __name__ == "__main__":
    seed_data()