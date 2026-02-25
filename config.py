import os

class Config:
    # On récupère l'URL de Render s'il existe, sinon on utilise le local (SQLite ou Postgres local)
    # Note : Render fournit souvent l'URL via la variable DATABASE_URL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "postgresql://africaapigeo_user:rXrL6PDIP43vknCyqnZLyUR8jCCpVPK7@dpg-d6ffenma2pns73div780-a.oregon-postgres.render.com/africaapigeo"
    )
    
    # Correction pour les versions récentes de SQLAlchemy/Render (remplace postgres:// par postgresql://)
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key récupérée du serveur ou valeur de secours pour le dev
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-africa-geo-99221")

class ProductionConfig(Config):
    """Configuration spécifique à la production"""
    DEBUG = False
    # En prod, on force souvent le SSL pour Postgres sur Render
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "sslmode": "require"
        }
    }

class DevelopmentConfig(Config):
    """Configuration spécifique au développement local"""
    DEBUG = True
    # Ici vous pouvez mettre votre URL locale si vous voulez alterner
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:aipenpass123@localhost:5432/africaapigeo"
