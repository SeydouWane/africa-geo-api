from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from app.models import Country, AdministrativeDivision
from sqlalchemy import func
import math

main_bp = Blueprint('main', __name__)

# Configuration de Swagger sur /docs
api = Api(main_bp, 
          doc='/docs', 
          title='Africa Geo API', 
          description='API de découpage administratif de l\'Afrique avec support Géographique',
          version='1.0')

# --- Modèles pour la documentation (Sérialisation) ---

country_model = api.model('Country', {
    'id': fields.Integer(description='Indicatif téléphonique (ex: 221)'),
    'name': fields.String(description='Nom du pays'),
    'iso': fields.String(attribute='iso_code', description='Code ISO (ex: SN)')
})

division_model = api.model('Division', {
    'id': fields.Integer,
    'name': fields.String,
    'level': fields.Integer(description='1=Région/District, 2=Cercle/Département, 3=Commune'),
    'latitude': fields.Float,
    'longitude': fields.Float,
    'parent_id': fields.Integer,
    'country_id': fields.Integer
})

# Modèles pour l'arborescence récursive (Tree)
commune_tree = api.model('CommuneTree', {
    'id': fields.Integer,
    'name': fields.String,
    'level': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float
})

dept_tree = api.model('DeptTree', {
    'id': fields.Integer,
    'name': fields.String,
    'level': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'communes': fields.List(fields.Nested(commune_tree), attribute='sub_divisions')
})

region_tree = api.model('RegionTree', {
    'id': fields.Integer,
    'name': fields.String,
    'level': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'departments': fields.List(fields.Nested(dept_tree), attribute='sub_divisions')
})

full_tree_model = api.model('FullTree', {
    'id': fields.Integer,
    'name': fields.String,
    'iso': fields.String(attribute='iso_code'),
    'hierarchy': fields.List(fields.Nested(region_tree), attribute='divisions')
})

stats_model = api.model('Stats', {
    'country': fields.String,
    'regions_count': fields.Integer,
    'departments_count': fields.Integer,
    'communes_count': fields.Integer
})

# --- Endpoints ---

@api.route('/countries')
class CountryList(Resource):
    @api.marshal_list_with(country_model)
    def get(self):
        """Liste tous les pays d'Afrique enregistrés"""
        return Country.query.all()

@api.route('/countries/<int:id>/stats')
class CountryStats(Resource):
    @api.marshal_with(stats_model)
    def get(self, id):
        """Obtenir les statistiques de découpage d'un pays"""
        country = Country.query.get_or_404(id)
        regions = AdministrativeDivision.query.filter_by(country_id=id, level=1).count()
        depts = AdministrativeDivision.query.filter_by(country_id=id, level=2).count()
        communes = AdministrativeDivision.query.filter_by(country_id=id, level=3).count()
        return {
            "country": country.name,
            "regions_count": regions,
            "departments_count": depts,
            "communes_count": communes
        }

@api.route('/countries/<int:id>/full-tree')
class CountryFullTree(Resource):
    @api.marshal_with(full_tree_model)
    def get(self, id):
        """Récupère toute la hiérarchie d'un pays (Arbre complet avec coordonnées)"""
        return Country.query.get_or_404(id)

@api.route('/countries/<int:id>/regions')
class RegionList(Resource):
    @api.marshal_list_with(division_model)
    def get(self, id):
        """Liste les régions d'un pays spécifique"""
        return AdministrativeDivision.query.filter_by(country_id=id, level=1).all()

@api.route('/regions/<int:region_id>/departments')
class DepartmentList(Resource):
    @api.marshal_list_with(division_model)
    def get(self, region_id):
        """Liste les départements d'une région"""
        return AdministrativeDivision.query.filter_by(parent_id=region_id, level=2).all()

@api.route('/departments/<int:dept_id>/communes')
class CommuneList(Resource):
    @api.marshal_list_with(division_model)
    def get(self, dept_id):
        """Liste les communes d'un département"""
        return AdministrativeDivision.query.filter_by(parent_id=dept_id, level=3).all()

@api.route('/search/<string:name>')
class SearchLocation(Resource):
    @api.marshal_list_with(division_model)
    def get(self, name):
        """Rechercher une localité par son nom (Région, Dept ou Commune)"""
        return AdministrativeDivision.query.filter(AdministrativeDivision.name.ilike(f'%{name}%')).all()

@api.route('/nearby')
class NearbyLocations(Resource):
    @api.doc(params={
        'lat': 'Latitude du point central',
        'lon': 'Longitude du point central',
        'radius': 'Rayon de recherche en km (défaut: 50)'
    })
    @api.marshal_list_with(division_model)
    def get(self):
        """Trouver les localités à proximité d'un point GPS (Haversine)"""
        lat = request.args.get('lat', type=float)
        lon = request.args.get('lon', type=float)
        radius = request.args.get('radius', default=50, type=float)

        if lat is None or lon is None:
            api.abort(400, "Les paramètres 'lat' et 'lon' sont obligatoires.")

        all_locs = AdministrativeDivision.query.filter(AdministrativeDivision.latitude.isnot(None)).all()
        nearby = []

        # Formule de Haversine pour calculer la distance
        for loc in all_locs:
            R = 6371  # Rayon de la Terre en km
            dlat = math.radians(loc.latitude - lat)
            dlon = math.radians(loc.longitude - lon)
            a = math.sin(dlat/2)**2 + math.cos(math.radians(lat)) * \
                math.cos(math.radians(loc.latitude)) * math.sin(dlon/2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance = R * c

            if distance <= radius:
                nearby.append(loc)

        return nearby