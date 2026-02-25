import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():
        print("--- Initialisation du Sénégal (221) ---")
        sn_id = 221
        sn = Country.query.get(sn_id)
        if not sn:
            sn = Country(id=sn_id, name="SENEGAL", iso_code="SN")
            db.session.add(sn)
            db.session.commit()

        # Structure : { "Région": { "Département": ["Commune1", "Commune2"] } }
        africa_data = {
            "Dakar": {
                "Dakar": ["Plateau", "Médina", "Fann-Point E", "Gorée", "Yoff", "Ngor", "Ouakam"],
                "Pikine": ["Pikine Est", "Pikine Ouest", "Thiaroye Gare", "Mbao", "Yeumbeul"],
                "Guédiawaye": ["Golf Sud", "Sam Notaire", "Ndiarème Limamoulaye", "Wakhinane Nimzatt"],
                "Rufisque": ["Rufisque Est", "Rufisque Ouest", "Rufisque Nord", "Sébikotane", "Diamniadio"],
                "Keur Massar": ["Keur Massar Nord", "Keur Massar Sud", "Jaxaay-Parcelles"]
            },
            "Thiès": {
                "Thiès": ["Thiès Nord", "Thiès Est", "Thiès Ouest", "Khombole", "Pout"],
                "Mbour": ["Mbour", "Saly Portudal", "Sandiara", "Joal-Fadiouth", "Somone"],
                "Tivaouane": ["Tivaouane", "Meckhé", "Mboro", "Pir Goureye"]
            },
            "Saint-Louis": {
                "Saint-Louis": ["Saint-Louis", "Mpal", "Fass Ngom"],
                "Dagana": ["Dagana", "Richard-Toll", "Rosso Sénégal", "Gae", "Ross Béthio"],
                "Podor": ["Podor", "Ndioum", "Golléré", "Niandane", "Mboumba"]
            },
            "Diourbel": {
                "Diourbel": ["Diourbel", "Ndindi", "Ndoulo"],
                "Bambey": ["Bambey", "Baba Garage", "Ngogom"],
                "Mbacké": ["Mbacké", "Touba Mosquée", "Sadio", "Dalla Ngabou"]
            },
            "Louga": {
                "Louga": ["Louga", "Nguersane", "Coki"],
                "Linguère": ["Linguère", "Dahra", "Mbeuleukhé"],
                "Kébémer": ["Kébémer", "Guéoul", "Ndande"]
            },
            "Fatick": {
                "Fatick": ["Fatick", "Dioffior", "Niakhar"],
                "Foundiougne": ["Foundiougne", "Sokone", "Karang Poste", "Passy"],
                "Gossas": ["Gossas", "Colobane", "Mbar"]
            },
            "Kaolack": {
                "Kaolack": ["Kaolack", "Kahone", "Ndoffane"],
                "Nioro du Rip": ["Nioro du Rip", "Keur Madiabel", "Paos Koto"],
                "Guinguinéo": ["Guinguinéo", "Fass", "Mboss"]
            },
            "Kaffrine": {
                "Kaffrine": ["Kaffrine", "Nganda"],
                "Birkelane": ["Birkelane", "Mabo"],
                "Koungheul": ["Koungheul", "Missirah Wadene"],
                "Malem Hodar": ["Malem Hodar", "Sagna"]
            },
            "Tambacounda": {
                "Tambacounda": ["Tambacounda", "Missirah"],
                "Bakel": ["Bakel", "Diawara", "Kidira"],
                "Goudiry": ["Goudiry", "Kothiary"],
                "Koupentoum": ["Koupentoum", "Payar"]
            },
            "Kédougou": {
                "Kédougou": ["Kédougou", "Bandafassi"],
                "Salemata": ["Salemata", "Dakately"],
                "Saraya": ["Saraya", "Bembou"]
            },
            "Kolda": {
                "Kolda": ["Kolda", "Saré Yoba Diéga"],
                "Vélingara": ["Vélingara", "Kounkané"],
                "Médina Yoro Foulah": ["Médina Yoro Foulah", "Pata"]
            },
            "Sédhiou": {
                "Sédhiou": ["Sédhiou", "Marsassoum"],
                "Bounkiling": ["Bounkiling", "Madina Wandifa"],
                "Goudomp": ["Goudomp", "Tanaff"]
            },
            "Ziguinchor": {
                "Ziguinchor": ["Ziguinchor", "Niaguis"],
                "Bignona": ["Bignona", "Thionck-Essyl", "Abéné"],
                "Oussouye": ["Oussouye", "Cap Skirring"]
            },
            "Matam": {
                "Matam": ["Matam", "Ourossogui"],
                "Kanel": ["Kanel", "Waoundé", "Hamady Ounaré", "Semmé"],
                "Ranérou-Ferlo": ["Ranérou"]
            }
        }

        for reg_name, depts in africa_data.items():
            # Créer/Récupérer Région (Level 1)
            region = AdministrativeDivision.query.filter_by(name=reg_name, level=1).first()
            if not region:
                region = AdministrativeDivision(name=reg_name, level=1, country_id=sn_id)
                db.session.add(region)
                db.session.flush()

            for dept_name, communes in depts.items():
                # Créer/Récupérer Département (Level 2)
                dept = AdministrativeDivision.query.filter_by(name=dept_name, level=2, parent_id=region.id).first()
                if not dept:
                    dept = AdministrativeDivision(name=dept_name, level=2, country_id=sn_id, parent_id=region.id)
                    db.session.add(dept)
                    db.session.flush()

                for com_name in communes:
                    # Créer Commune (Level 3)
                    if not AdministrativeDivision.query.filter_by(name=com_name, level=3, parent_id=dept.id).first():
                        commune = AdministrativeDivision(name=com_name, level=3, country_id=sn_id, parent_id=dept.id)
                        db.session.add(commune)
        
        db.session.commit()
        print("Insertion terminée : 14 Régions, 45 Départements et les communes principales ajoutées.")

if __name__ == "__main__":
    seed_data()