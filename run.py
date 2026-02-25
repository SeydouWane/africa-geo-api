import os
import importlib.util
from app import create_app, db
from app.models import Country

app = create_app()

def run_seed_scripts():
    """Détecte et exécute automatiquement tous les scripts dans le dossier /scripts"""
    scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
    
    # On vérifie si le dossier existe
    if not os.path.exists(scripts_dir):
        print(" Dossier /scripts non trouvé.")
        return

    scripts = [f for f in os.listdir(scripts_dir) if f.startswith('seed_') and f.endswith('.py')]
    scripts.sort() 

    with app.app_context():
   

        print(f" Initialisation automatique : {len(scripts)} scripts détectés.")
        
        for script_file in scripts:
            script_path = os.path.join(scripts_dir, script_file)
            module_name = script_file[:-3]

            spec = importlib.util.spec_from_file_location(module_name, script_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'seed_data'):
                print(f"🔹 Exécution de {script_file}...")
                module.seed_data()
            else:
                print(f" {script_file} n'a pas de fonction seed_data().")

if __name__ == "__main__":
    run_seed_scripts()
    
    print("🌍 Serveur démarré sur http://127.0.0.1:5000/docs")
    app.run(debug=True)