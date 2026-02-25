import sys
import os

# Ajout du dossier parent pour l'import des modules de l'app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation du Mali (ID: 223) ---")
        
        ml_id = 223
        ml = Country.query.get(ml_id)
        if not ml:
            ml = Country(id=ml_id, name="Mali", iso_code="ML")
            db.session.add(ml)
            db.session.commit()
            print("Pays Mali créé.")

        # Données complètes des 19 régions + District de Bamako
        # Structure : { "Région": { "Cercle": ["Communes"] } }
        mali_data = {
            "District de Bamako": {
                "Bamako": ["Commune I", "Commune II", "Commune III", "Commune IV", "Commune V", "Commune VI"]
            },
            "Kayes": {
                "Kayes": ["Kayes", "Liberté Dembaya", "Sadiola"],
                "Bafoulabé": ["Bafoulabé", "Mahina", "Diakon"]
            },
            "Koulikoro": {
                "Koulikoro": ["Koulikoro", "Tiénfala", "Dinourou"],
                "Banamba": ["Banamba", "Madina Sacko", "Boron"]
            },
            "Sikasso": {
                "Sikasso": ["Sikasso", "Finkolo", "Gnanadougou"],
                "Kadiolo": ["Kadiolo", "Diou", "Kai"]
            },
            "Ségou": {
                "Ségou": ["Ségou", "Pélengana", "Sébila"],
                "Macina": ["Macina", "Matomo", "Saye"]
            },
            "Mopti": {
                "Mopti": ["Mopti", "Fatoma", "Konna"],
                "Ténenkou": ["Ténenkou", "Diafarabé", "Togoro Kotia"]
            },
            "Tombouctou": {
                "Tombouctou": ["Tombouctou", "Lafia", "Salam"],
                "Goundam": ["Goundam", "Bintagoungou", "Douékiré"]
            },
            "Gao": {
                "Gao": ["Gao", "Gounzoureye", "Soni Ali Ber"],
                "Ansongo": ["Ansongo", "Bara", "Tessit"]
            },
            "Kidal": {
                "Kidal": ["Kidal", "Abeïbara", "Essouk"],
                "Tessalit": ["Tessalit", "Aguel'hoc", "Timtaghène"]
            },
            "Taoudénit": {
                "Taoudénit": ["Taoudénit", "Agorgot"],
                "Foum-Alba": ["Foum-Alba", "Araouane"]
            },
            "Ménaka": {
                "Ménaka": ["Ménaka", "Anéfis"],
                "Andéramboukane": ["Andéramboukane", "Azawak"]
            },
            "Nioro": {
                "Nioro": ["Nioro", "Yéréré", "Youri"],
                "Diéma": ["Diéma", "Béma", "Diangounté Camara"]
            },
            "Kita": {
                "Kita": ["Kita", "Boudofo", "Kokofata"],
                "Séfétó": ["Séfétó", "Kassaro"]
            },
            "Doïla": {
                "Doïla": ["Doïla", "Béléko", "Fana"],
                "Dioïla": ["Dioïla", "Massigui", "Nando"]
            },
            "Nara": {
                "Nara": ["Nara", "Fallou", "Guiré"],
                "Mourdiah": ["Mourdiah", "Niamana"]
            },
            "Bougouni": {
                "Bougouni": ["Bougouni", "Koumantou", "Garalo"],
                "Kolondiéba": ["Kolondiéba", "Kadiana", "Kebila"]
            },
            "Koutiala": {
                "Koutiala": ["Koutiala", "Zangasso", "M'Pessoba"],
                "Yorosso": ["Yorosso", "Koury", "Mahou"]
            },
            "San": {
                "San": ["San", "Somasso", "Tééné"],
                "Tomián": ["Tomián", "Fangasso", "Mandiakuy"]
            },
            "Douentza": {
                "Douentza": ["Douentza", "Débéré", "Gandamia"],
                "Boni": ["Boni", "Haire"]
            },
            "Bandiagara": {
                "Bandiagara": ["Bandiagara", "Sangha", "Dourou"],
                "Bankass": ["Bankass", "Kani Bozon", "Socoura"]
            }
        }

        for reg_name, cercles in mali_data.items():
            # Gestion Niveau 1 (Région)
            region = AdministrativeDivision.query.filter_by(
                name=reg_name, level=1, country_id=ml_id
            ).first()
            if not region:
                region = AdministrativeDivision(name=reg_name, level=1, country_id=ml_id)
                db.session.add(region)
                db.session.flush()
                print(f"-> Ajout Région : {reg_name}")

            for cercle_name, communes in cercles.items():
                # Gestion Niveau 2 (Cercle)
                cercle = AdministrativeDivision.query.filter_by(
                    name=cercle_name, level=2, parent_id=region.id
                ).first()
                if not cercle:
                    cercle = AdministrativeDivision(
                        name=cercle_name, level=2, country_id=ml_id, parent_id=region.id
                    )
                    db.session.add(cercle)
                    db.session.flush()

                for com_name in communes:
                    # Gestion Niveau 3 (Commune)
                    if not AdministrativeDivision.query.filter_by(
                        name=com_name, level=3, parent_id=cercle.id
                    ).first():
                        commune = AdministrativeDivision(
                            name=com_name, level=3, country_id=ml_id, parent_id=cercle.id
                        )
                        db.session.add(commune)
        
        db.session.commit()
        print("\n" + "="*40)
        print("Succès : Les 19 régions du Mali sont à jour !")
        print("="*40)

if __name__ == "__main__":
    seed_data()