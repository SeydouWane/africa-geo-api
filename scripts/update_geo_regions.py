import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import AdministrativeDivision

app = create_app()

def update_geo():
    with app.app_context():
        # Dictionnaire des coordonnées (Latitude, Longitude) des régions
        geo_data = {
            # --- SÉNÉGAL ---
            "Dakar": {"lat": 14.7167, "lon": -17.4677},
            "Thiès": {"lat": 14.7910, "lon": -16.9359},
            "Saint-Louis": {"lat": 16.0244, "lon": -16.4896},
            "Diourbel": {"lat": 14.6500, "lon": -16.2333},
            "Louga": {"lat": 15.6186, "lon": -16.2243},
            "Fatick": {"lat": 14.3581, "lon": -16.4125},
            "Kaolack": {"lat": 14.1499, "lon": -16.0758},
            "Kaffrine": {"lat": 14.1059, "lon": -15.5508},
            "Tambacounda": {"lat": 13.7707, "lon": -13.6673},
            "Kédougou": {"lat": 12.5579, "lon": -12.1743},
            "Kolda": {"lat": 12.8833, "lon": -14.9500},
            "Sédhiou": {"lat": 12.7081, "lon": -15.5569},
            "Ziguinchor": {"lat": 12.5833, "lon": -16.2719},
            "Matam": {"lat": 15.6559, "lon": -13.2554},

            # --- MALI ---
            "District de Bamako": {"lat": 12.6392, "lon": -8.0029},
            "Kayes": {"lat": 14.4469, "lon": -11.4442},
            "Koulikoro": {"lat": 12.8627, "lon": -7.5599},
            "Sikasso": {"lat": 11.3175, "lon": -5.6665},
            "Ségou": {"lat": 13.4317, "lon": -6.2157},
            "Mopti": {"lat": 14.4843, "lon": -4.1830},
            "Tombouctou": {"lat": 16.7666, "lon": -3.0026},
            "Gao": {"lat": 16.2717, "lon": -0.0447},
            "Kidal": {"lat": 18.4411, "lon": 1.4078},
            "Taoudénit": {"lat": 22.6738, "lon": -3.9836},
            "Ménaka": {"lat": 15.9182, "lon": 2.4022},
            "Nioro": {"lat": 15.2333, "lon": -9.5833},
            "Kita": {"lat": 13.0349, "lon": -9.4895},
            "Doïla": {"lat": 12.6739, "lon": -6.7475},
            "Nara": {"lat": 15.1743, "lon": -7.2892},
            "Bougouni": {"lat": 11.4170, "lon": -7.4832},
            "Koutiala": {"lat": 12.3917, "lon": -5.4642},
            "San": {"lat": 13.3034, "lon": -4.8956},
            "Douentza": {"lat": 14.9951, "lon": -2.9517},
            "Bandiagara": {"lat": 14.3501, "lon": -3.6104},
            # --- GAMBIE ---
            "Greater Banjul Area": {"lat": 13.4549, "lon": -16.5790},
            "West Coast Division": {"lat": 13.2833, "lon": -16.5167},
            "North Bank Division": {"lat": 13.5167, "lon": -16.0000},
            "Lower River Division": {"lat": 13.4000, "lon": -15.5833},
            "Central River Division": {"lat": 13.6167, "lon": -14.7500},
            "Upper River Division": {"lat": 13.3833, "lon": -14.2000},
            
            # --- CÔTE D'IVOIRE ---
            "District Autonome d'Abidjan": {"lat": 5.3600, "lon": -4.0083},
            "District Autonome de Yamoussoukro": {"lat": 6.8276, "lon": -5.2767},
            "Bas-Sassandra": {"lat": 4.7561, "lon": -6.6362},
            "Comoé": {"lat": 6.7483, "lon": -3.4833},
            "Denguélé": {"lat": 9.5051, "lon": -7.5643},
            "Gôh-Djiboua": {"lat": 6.1319, "lon": -5.9431},
            "Lacs": {"lat": 6.6472, "lon": -4.7067},
            "Lagunes": {"lat": 5.9281, "lon": -3.9683},
            "Montagnes": {"lat": 7.4125, "lon": -7.5538},
            "Sassandra-Marahoué": {"lat": 6.8774, "lon": -6.4449},
            "Savanes": {"lat": 9.4580, "lon": -5.6295},
            "Vallée du Bandama": {"lat": 7.6897, "lon": -5.0303},
            "Woroba": {"lat": 7.9611, "lon": -6.6719},
            "Zanzan": {"lat": 8.0400, "lon": -2.8000}
        }

        print("Début de la mise à jour des coordonnées...")
        
        count = 0
        for name, coords in geo_data.items():
            # On cherche uniquement les divisions de niveau 1 (Régions/Districts)
            divisions = AdministrativeDivision.query.filter_by(name=name, level=1).all()
            
            for loc in divisions:
                loc.latitude = coords["lat"]
                loc.longitude = coords["lon"]
                count += 1
                print(f"[{count}] Mis à jour : {name} -> Lat: {coords['lat']}, Lon: {coords['lon']}")
        
        db.session.commit()
        print(f"\nTerminé ! {count} régions ont été géo-référencées.")

if __name__ == "__main__":
    update_geo()