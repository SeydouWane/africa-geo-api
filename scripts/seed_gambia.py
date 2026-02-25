import sys
import os

# Ajout du dossier parent pour l'import des modules de l'app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation de la Gambie (ID: 220) ---")
        
        gm_id = 220
        gm = Country.query.get(gm_id)
        if not gm:
            gm = Country(id=gm_id, name="Gambie", iso_code="GM")
            db.session.add(gm)
            db.session.commit()
            print("Pays Gambie créé.")

        # Données des Divisions (Niveau 1) et Districts (Niveau 2)
        # Note : Nous incluons les coordonnées GPS pour les chefs-lieux
        gambia_data = {
            "Greater Banjul Area": {
                "coords": {"lat": 13.4549, "lon": -16.5790},
                "districts": ["Banjul", "Kanifing"]
            },
            "West Coast Division": {
                "coords": {"lat": 13.2833, "lon": -16.5167},
                "districts": ["Kombo North", "Kombo South", "Kombo Central", "Foni Brefet"]
            },
            "North Bank Division": {
                "coords": {"lat": 13.5167, "lon": -16.0000},
                "districts": ["Lower Niumi", "Upper Niumi", "Jokadu", "Lower Badibu"]
            },
            "Lower River Division": {
                "coords": {"lat": 13.4000, "lon": -15.5833},
                "districts": ["Kiang West", "Kiang Central", "Kiang East", "Jarra West"]
            },
            "Central River Division": {
                "coords": {"lat": 13.6167, "lon": -14.7500},
                "districts": ["Lower Saloum", "Upper Saloum", "Nianija", "Niani", "Fulladu West"]
            },
            "Upper River Division": {
                "coords": {"lat": 13.3833, "lon": -14.2000},
                "districts": ["Fulladu East", "Kantora", "Wuli", "Sandu"]
            }
        }

        for reg_name, info in gambia_data.items():
            # Niveau 1 (Divisions/Régions)
            region = AdministrativeDivision.query.filter_by(
                name=reg_name, level=1, country_id=gm_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=reg_name, 
                    level=1, 
                    country_id=gm_id,
                    latitude=info["coords"]["lat"],
                    longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"-> Région : {reg_name}")

            for dist_name in info["districts"]:
                # Niveau 2 (Districts)
                district = AdministrativeDivision.query.filter_by(
                    name=dist_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=dist_name, 
                        level=2, 
                        country_id=gm_id, 
                        parent_id=region.id
                    )
                    db.session.add(district)
        
        db.session.commit()
        print("\n" + "="*45)
        print("Succès : Les données de la Gambie sont à jour !")
        print("="*45)

if __name__ == "__main__":
    seed_data()