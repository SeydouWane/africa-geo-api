import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation de la Guinée-Bissau (ID: 245) ---")
        
        gb_id = 245
        gb = Country.query.get(gb_id)
        if not gb:
            gb = Country(id=gb_id, name="Guinée-Bissau", iso_code="GW")
            db.session.add(gb)
            db.session.commit()
            print("Pays Guinée-Bissau créé.")

        gb_data = {
            "Sector Autónomo de Bissau": {
                "coords": {"lat": 11.8632, "lon": -15.5843},
                "sectors": ["Bissau Centre", "Antula", "Milière"]
            },
            "Bafatá": {
                "coords": {"lat": 12.1667, "lon": -14.6667},
                "sectors": ["Bafatá", "Bambadinca", "Contuboel", "Galomaro", "Gã-Mamudo", "Xitole"]
            },
            "Biombo": {
                "coords": {"lat": 11.8333, "lon": -15.8333},
                "sectors": ["Quinhámel", "Safim", "Prábis"]
            },
            "Bolama-Bijagós": {
                "coords": {"lat": 11.5833, "lon": -16.0000},
                "sectors": ["Bolama", "Bubaque", "Caravela", "Uno"]
            },
            "Cacheu": {
                "coords": {"lat": 12.2667, "lon": -16.1667},
                "sectors": ["Cacheu", "Canchungo", "Calequisse", "Caió", "Bula", "São Domingos"]
            },
            "Gabú": {
                "coords": {"lat": 12.2833, "lon": -14.2167},
                "sectors": ["Gabú", "Pirada", "Pitche", "Sonaco", "Boe"]
            },
            "Oio": {
                "coords": {"lat": 12.2500, "lon": -15.2500},
                "sectors": ["Farim", "Mansôa", "Bissorã", "Nhacra", "Mansabá"]
            },
            "Quinara": {
                "coords": {"lat": 11.7500, "lon": -15.1667},
                "sectors": ["Buba", "Empada", "Fulacunda", "Tite"]
            },
            "Tombali": {
                "coords": {"lat": 11.2500, "lon": -15.0000},
                "sectors": ["Catió", "Como", "Bedanda", "Cacine", "Quebo"]
            }
        }

        for region_name, info in gb_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=gb_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, 
                    level=1, 
                    country_id=gb_id,
                    latitude=info["coords"]["lat"],
                    longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"-> Région : {region_name}")

            for sector_name in info["sectors"]:
                sector = AdministrativeDivision.query.filter_by(
                    name=sector_name, level=2, parent_id=region.id
                ).first()
                if not sector:
                    sector = AdministrativeDivision(
                        name=sector_name, level=2, country_id=gb_id, parent_id=region.id
                    )
                    db.session.add(sector)
        
        db.session.commit()
        print("\n" + "="*45)
        print("Succès : Les données de la Guinée-Bissau sont à jour !")
        print("="*45)

if __name__ == "__main__":
    seed_data()