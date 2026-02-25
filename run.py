import os
import importlib.util
from app import create_app, db
from app.models import Country

# Initialisation de l'application Flask
app = create_app()

def run_seed_scripts():
    """
    Détecte et exécute automatiquement tous les scripts 'seed_*.py' 
    situés dans le dossier /scripts.
    """
    # Définition du chemin absolu vers le dossier scripts
    scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
    
    # Vérification de l'existence du dossier
    if not os.path.exists(scripts_dir):
        print("⚠️ Dossier /scripts non trouvé.")
        return

    # Liste et tri des scripts commençant par 'seed_'
    scripts = [f for f in os.listdir(scripts_dir) if f.startswith('seed_') and f.endswith('.py')]
    scripts.sort() 

    with app.app_context():
        # --- ÉTAPE CRUCIALE POUR LA PROD (RENDER) ---
        # Crée les tables si elles n'existent pas encore dans PostgreSQL
        print("🛠️ Vérification et création des tables de la base de données...")
        db.create_all()
        # --------------------------------------------

        print(f"🚀 Initialisation automatique : {len(scripts)} scripts détectés.")
        
        for script_file in scripts:
            script_path = os.path.join(scripts_dir, script_file)
            module_name = script_file[:-3] # Enlever l'extension .py

            try:
                # Chargement dynamique du script python
                spec = importlib.util.spec_from_file_location(module_name, script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Appel de la fonction seed_data() contenue dans le script
                if hasattr(module, 'seed_data'):
                    print(f"🔹 Exécution de {script_file}...")
                    module.seed_data()
                else:
                    print(f"⚠️ {script_file} ignoré : pas de fonction seed_data() trouvée.")
            
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de {script_file} : {e}")

if __name__ == "__main__":
    # Exécution du seeding avant le lancement du serveur
    run_seed_scripts()
    
    # Configuration du port dynamique pour Render (défaut 5000 en local)
    port = int(os.environ.get("PORT", 5000))
    
    print(f"🌍 Application démarrée sur le port {port}")
    
    # Lancement de l'application (host 0.0.0.0 impératif pour Render)
    app.run(host="0.0.0.0", port=port)
