import os
import importlib.util
from app import create_app, db
from app.models import Country

app = create_app()

def run_seed_scripts():
    scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
    if not os.path.exists(scripts_dir):
        return

    scripts = [f for f in os.listdir(scripts_dir) if f.startswith('seed_') and f.endswith('.py')]
    scripts.sort() 

    with app.app_context():
        # --- OPTIMISATION ---
        # Si on a déjà des pays, on considère que le seed a déjà été fait
        if Country.query.first():
            print("✅ Données déjà présentes. On saute le seeding pour démarrer plus vite.")
            return
        # ---------------------

        print(f"🚀 Premier démarrage : Initialisation de {len(scripts)} scripts...")
        for script_file in scripts:
            script_path = os.path.join(scripts_dir, script_file)
            module_name = script_file[:-3]
            try:
                spec = importlib.util.spec_from_file_location(module_name, script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, 'seed_data'):
                    print(f"🔹 Seed: {script_file}")
                    module.seed_data()
            except Exception as e:
                print(f"❌ Erreur {script_file}: {e}")

if __name__ == "__main__":
    # On lance le seeding
    run_seed_scripts()
    
    port = int(os.environ.get("PORT", 10000)) # Render utilise souvent 10000 par défaut
    
    # Utilisation de host 0.0.0.0 est CRITIQUE
    print(f"🌍 Starting server on port {port}...")
    app.run(host="0.0.0.0", port=port)
