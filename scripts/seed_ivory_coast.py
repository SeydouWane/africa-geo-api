import sys
import os

# Ajout du dossier parent pour l'import des modules de l'app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation de la Côte d'Ivoire (ID: 225) ---")
        
        ci_id = 225
        ci = Country.query.get(ci_id)
        if not ci:
            ci = Country(id=ci_id, name="Côte d'Ivoire", iso_code="CI")
            db.session.add(ci)
            db.session.commit()
            print("Pays Côte d'Ivoire créé.")

        # Données des Districts (Niveau 1), Régions (Niveau 2) et Départements/Communes (Niveau 3)
        ivory_coast_data = {
            "District Autonome d'Abidjan": {
                "Abidjan": ["Cocody", "Plateau", "Abobo", "Adjamé", "Yopougon", "Treichville", "Marcory"]
            },
            "District Autonome de Yamoussoukro": {
                "Yamoussoukro": ["Yamoussoukro Commune", "Attiégouakro"]
            },
            "Bas-Sassandra": {
                "Nawa": ["Soubré", "Buyo", "Méagui"],
                "San-Pédro": ["San-Pédro", "Tabou"],
                "Gboklè": ["Sassandra", "Fresco"]
            },
            "Comoé": {
                "Indénié-Djuablin": ["Abengourou", "Agnibilékrou", "Bettié"],
                "Sud-Comoé": ["Aboisso", "Adiaké", "Grand-Bassam", "Tiapoum"]
            },
            "Denguélé": {
                "Kabadougou": ["Odienné", "Gbéléban", "Madinani"],
                "Folon": ["Minignan", "Kaniasso"]
            },
            "Gôh-Djiboua": {
                "Gôh": ["Gagnoa", "Oumé"],
                "Lôh-Djiboua": ["Divo", "Lakota", "Guitry"]
            },
            "Lacs": {
                "Bélier": ["Toumodi", "Didiévi", "Djékanou", "Tiebissou"],
                "Iffou": ["Daoukro", "M'Bahiakro", "Prikro"],
                "Moronou": ["Bongouanou", "Arrah", "M'Batto"],
                "N'Zi": ["Dimbokro", "Bocanda", "Kouassi-Kouassikro"]
            },
            "Lagunes": {
                "Agnéby-Tiassa": ["Agboville", "Sikensi", "Tiassalé"],
                "Grands-Ponts": ["Dabou", "Grand-Lahou", "Jacqueville"],
                "La Mé": ["Adzopé", "Akoupé", "Alépé"]
            },
            "Montagnes": {
                "Tonkpi": ["Man", "Danané", "Biankouma", "Zouan-Hounien"],
                "Guémon": ["Duékoué", "Bangolo", "Facobly"],
                "Cavally": ["Guiglo", "Bloléquin", "Taï"]
            },
            "Sassandra-Marahoué": {
                "Haut-Sassandra": ["Daloa", "Issia", "Vavoua"],
                "Marahoué": ["Bouaflé", "Sinfra", "Zuénoula"]
            },
            "Savanes": {
                "Poro": ["Korhogo", "Sinématiali", "Dikodougou"],
                "Tchologo": ["Ferkessédougou", "Ouangolodougou"],
                "Bagoué": ["Boundiali", "Kouto", "Tengréla"]
            },
            "Vallée du Bandama": {
                "Gbêkê": ["Bouaké", "Béoumi", "Sakassou"],
                "Hambol": ["Katiola", "Dabakala", "Niakaramandougou"]
            },
            "Woroba": {
                "Worodougou": ["Séguéla", "Kani"],
                "Bafing": ["Touba", "Koro", "Ouaninou"],
                "Béré": ["Mankono", "Dianra", "Kounahiri"]
            },
            "Zanzan": {
                "Gontougo": ["Bondoukou", "Koun-Fao", "Sandégué"],
                "Bounkani": ["Bouna", "Doropo", "Nassian"]
            }
        }

        for dist_name, regions in ivory_coast_data.items():
            # Niveau 1 (Districts)
            district = AdministrativeDivision.query.filter_by(
                name=dist_name, level=1, country_id=ci_id
            ).first()
            if not district:
                district = AdministrativeDivision(name=dist_name, level=1, country_id=ci_id)
                db.session.add(district)
                db.session.flush()
                print(f"-> District : {dist_name}")

            for reg_name, subdivisions in regions.items():
                # Niveau 2 (Régions)
                region = AdministrativeDivision.query.filter_by(
                    name=reg_name, level=2, parent_id=district.id
                ).first()
                if not region:
                    region = AdministrativeDivision(
                        name=reg_name, level=2, country_id=ci_id, parent_id=district.id
                    )
                    db.session.add(region)
                    db.session.flush()

                for sub_name in subdivisions:
                    # Niveau 3 (Départements/Communes)
                    if not AdministrativeDivision.query.filter_by(
                        name=sub_name, level=3, parent_id=region.id
                    ).first():
                        sub = AdministrativeDivision(
                            name=sub_name, level=3, country_id=ci_id, parent_id=region.id
                        )
                        db.session.add(sub)
        
        db.session.commit()
        print("\n" + "="*45)
        print("Succès : Les données de Côte d'Ivoire sont à jour !")
        print("="*45)

if __name__ == "__main__":
    seed_data()