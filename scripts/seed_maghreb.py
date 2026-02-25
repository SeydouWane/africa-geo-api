import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_maghreb():
    with app.app_context():

        # ================================================================
        # MAROC (ID: 504)
        # ================================================================
        print("\n--- Initialisation du Maroc (ID: 504) ---")
        ma_id = 504
        ma = Country.query.get(ma_id)
        if not ma:
            ma = Country(id=ma_id, name="Maroc", iso_code="MA")
            db.session.add(ma)
            db.session.commit()
            print("Pays Maroc créé.")

        ma_data = {
            "Tanger-Tétouan-Al Hoceïma": {
                "coords": {"lat": 35.7595, "lon": -5.8340},
                "provinces": ["Tanger-Assilah", "Fahs-Anjra", "Tétouan", "Mdiq-Fnideq", "Chefchaouen", "Larache", "Al Hoceïma", "Ouezzane", "Taounate"]
            },
            "Oriental": {
                "coords": {"lat": 34.6814, "lon": -1.9086},
                "provinces": ["Oujda-Angad", "Berkane", "Taourirt", "Nador", "Driouch", "Guercif", "Figuig", "Jerada"]
            },
            "Fès-Meknès": {
                "coords": {"lat": 33.9716, "lon": -5.0078},
                "provinces": ["Fès", "Meknès", "Ifrane", "El Hajeb", "Sefrou", "Moulay Yacoub", "Boulemane", "Taza", "Taounate"]
            },
            "Rabat-Salé-Kénitra": {
                "coords": {"lat": 34.0209, "lon": -6.8416},
                "provinces": ["Rabat", "Salé", "Skhirate-Témara", "Kénitra", "Sidi Kacem", "Sidi Slimane", "Khémisset"]
            },
            "Béni Mellal-Khénifra": {
                "coords": {"lat": 32.3372, "lon": -6.3498},
                "provinces": ["Béni Mellal", "Khénifra", "Azilal", "Fquih Ben Salah", "Khouribga"]
            },
            "Casablanca-Settat": {
                "coords": {"lat": 33.5731, "lon": -7.5898},
                "provinces": ["Casablanca", "Mohammadia", "El Jadida", "Nouaceur", "Médiouna", "Benslimane", "Berrechid", "Settat", "Sidi Bennour"]
            },
            "Marrakech-Safi": {
                "coords": {"lat": 31.6295, "lon": -7.9811},
                "provinces": ["Marrakech", "Al Haouz", "Chichaoua", "El Kelâa des Sraghna", "Essaouira", "Safi", "Youssoufia", "Rehamna"]
            },
            "Drâa-Tafilalet": {
                "coords": {"lat": 31.1728, "lon": -4.4272},
                "provinces": ["Errachidia", "Ouarzazate", "Zagora", "Midelt", "Tinghir"]
            },
            "Souss-Massa": {
                "coords": {"lat": 30.4202, "lon": -9.5981},
                "provinces": ["Agadir-Ida Ou Tanane", "Inezgane-Aït Melloul", "Chtouka-Aït Baha", "Taroudannt", "Tiznit", "Tata"]
            },
            "Guelmim-Oued Noun": {
                "coords": {"lat": 28.9870, "lon": -10.0574},
                "provinces": ["Guelmim", "Assa-Zag", "Tan-Tan", "Sidi Ifni"]
            },
            "Laâyoune-Sakia El Hamra": {
                "coords": {"lat": 27.1536, "lon": -13.2033},
                "provinces": ["Laâyoune", "Boujdour", "Tarfaya", "Es-Semara"]
            },
            "Dakhla-Oued Ed-Dahab": {
                "coords": {"lat": 23.6847, "lon": -15.9572},
                "provinces": ["Oued Ed-Dahab", "Aousserd"]
            }
        }

        for region_name, info in ma_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=ma_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=ma_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for prov_name in info["provinces"]:
                prov = AdministrativeDivision.query.filter_by(
                    name=prov_name, level=2, parent_id=region.id
                ).first()
                if not prov:
                    prov = AdministrativeDivision(
                        name=prov_name, level=2, country_id=ma_id, parent_id=region.id
                    )
                    db.session.add(prov)

        db.session.commit()
        print("Maroc : OK")

        # ================================================================
        # ALGÉRIE (ID: 12)
        # ================================================================
        print("\n--- Initialisation de l'Algérie (ID: 12) ---")
        dz_id = 12
        dz = Country.query.get(dz_id)
        if not dz:
            dz = Country(id=dz_id, name="Algérie", iso_code="DZ")
            db.session.add(dz)
            db.session.commit()
            print("Pays Algérie créé.")

        dz_data = {
            "Adrar": {"coords": {"lat": 27.8741, "lon": -0.2921}, "communes": ["Adrar", "Reggane", "Timimoun", "Aoulef", "Bordj Badji Mokhtar"]},
            "Chlef": {"coords": {"lat": 36.1647, "lon": 1.3317}, "communes": ["Chlef", "Ténès", "Sobha", "Oued Fodda"]},
            "Laghouat": {"coords": {"lat": 33.8000, "lon": 2.8833}, "communes": ["Laghouat", "Aflou", "Ksar El Hirane", "Gueltat Sidi Saad"]},
            "Oum El Bouaghi": {"coords": {"lat": 35.8833, "lon": 7.1167}, "communes": ["Oum El Bouaghi", "Aïn Beïda", "Khenchela", "Aïn M'lila"]},
            "Batna": {"coords": {"lat": 35.5560, "lon": 6.1742}, "communes": ["Batna", "Aïn Touta", "Barika", "Merouana", "Timgad"]},
            "Béjaïa": {"coords": {"lat": 36.7509, "lon": 5.0567}, "communes": ["Béjaïa", "Akbou", "Amizour", "Kherrata", "Sidi Aïch"]},
            "Biskra": {"coords": {"lat": 34.8500, "lon": 5.7333}, "communes": ["Biskra", "Tolga", "Ouled Djellal", "Sidi Okba", "El Oued"]},
            "Béchar": {"coords": {"lat": 31.6167, "lon": -2.2167}, "communes": ["Béchar", "Abadla", "Beni Ounif", "Taghit"]},
            "Blida": {"coords": {"lat": 36.4700, "lon": 2.8300}, "communes": ["Blida", "Boufarik", "Larbaa", "Meftah", "Bougara"]},
            "Bouira": {"coords": {"lat": 36.3739, "lon": 3.9003}, "communes": ["Bouira", "Lakhdaria", "Sour El Ghozlane", "Aïn Bessem"]},
            "Tamanrasset": {"coords": {"lat": 22.7850, "lon": 5.5228}, "communes": ["Tamanrasset", "In Salah", "In Guezzam", "Abalessa"]},
            "Tébessa": {"coords": {"lat": 35.4000, "lon": 8.1167}, "communes": ["Tébessa", "Bir El Ater", "Cheria", "El Aouinet"]},
            "Tlemcen": {"coords": {"lat": 34.8828, "lon": -1.3167}, "communes": ["Tlemcen", "Maghnia", "Ghazaouet", "Remchi", "Nedroma"]},
            "Tiaret": {"coords": {"lat": 35.3706, "lon": 1.3217}, "communes": ["Tiaret", "Frenda", "Mahdia", "Rahouia", "Sougueur"]},
            "Tizi Ouzou": {"coords": {"lat": 36.7169, "lon": 4.0497}, "communes": ["Tizi Ouzou", "Azazga", "Draa Ben Khedda", "Larbaa Nath Irathen", "Tigzirt"]},
            "Alger": {"coords": {"lat": 36.7372, "lon": 3.0869}, "communes": ["Alger Centre", "Bab El Oued", "Kouba", "Hussein Dey", "Bir Mourad Raïs", "Bir Touta", "Bab Ezzouar", "Rouiba"]},
            "Djelfa": {"coords": {"lat": 34.6733, "lon": 3.2631}, "communes": ["Djelfa", "Aïn Oussera", "Messaad", "Moudjbara"]},
            "Jijel": {"coords": {"lat": 36.8200, "lon": 5.7658}, "communes": ["Jijel", "Taher", "El Milia", "Ziama Mansouriah"]},
            "Sétif": {"coords": {"lat": 36.1898, "lon": 5.4108}, "communes": ["Sétif", "El Eulma", "Aïn Oulmene", "Aïn Azel", "Bougaa"]},
            "Saïda": {"coords": {"lat": 34.8317, "lon": 0.1500}, "communes": ["Saïda", "Aïn El Hadjar", "Sidi Boubekeur", "Youb"]},
            "Skikda": {"coords": {"lat": 36.8761, "lon": 6.9064}, "communes": ["Skikda", "Azzaba", "Collo", "El Harrouch", "Tamalous"]},
            "Sidi Bel Abbès": {"coords": {"lat": 35.1897, "lon": -0.6306}, "communes": ["Sidi Bel Abbès", "Telagh", "Tessala", "Aïn Tindamine"]},
            "Annaba": {"coords": {"lat": 36.9000, "lon": 7.7667}, "communes": ["Annaba", "El Bouni", "El Hadjar", "Aïn Berda", "Berrahal"]},
            "Guelma": {"coords": {"lat": 36.4628, "lon": 7.4264}, "communes": ["Guelma", "Bouchegouf", "Oued Zenati", "Heliopolis"]},
            "Constantine": {"coords": {"lat": 36.3650, "lon": 6.6147}, "communes": ["Constantine", "El Khroub", "Aïn Smara", "Hamma Bouziane", "Ibn Ziad"]},
            "Médéa": {"coords": {"lat": 36.2636, "lon": 2.7539}, "communes": ["Médéa", "Ksar El Boukhari", "Berrouaghia", "El Azizia"]},
            "Mostaganem": {"coords": {"lat": 35.9317, "lon": 0.0872}, "communes": ["Mostaganem", "Aïn Tédelès", "Sidi Ali", "Achaacha"]},
            "M'Sila": {"coords": {"lat": 35.7058, "lon": 4.5408}, "communes": ["M'Sila", "Bou Saâda", "Sidi Aïssa", "Aïn El Melh"]},
            "Mascara": {"coords": {"lat": 35.3956, "lon": 0.1400}, "communes": ["Mascara", "Sig", "Mohammadia", "Bouhanifia"]},
            "Ouargla": {"coords": {"lat": 31.9494, "lon": 5.3244}, "communes": ["Ouargla", "Hassi Messaoud", "Touggourt", "El Hadjira", "Temacine"]},
            "Oran": {"coords": {"lat": 35.6969, "lon": -0.6331}, "communes": ["Oran", "Es Sénia", "Bir El Djir", "Aïn El Turck", "Arzew", "Bethioua"]},
            "El Bayadh": {"coords": {"lat": 33.6833, "lon": 1.0167}, "communes": ["El Bayadh", "Brezina", "El Abiodh Sidi Cheikh", "Chellala"]},
            "Illizi": {"coords": {"lat": 26.5000, "lon": 8.4667}, "communes": ["Illizi", "Djanet", "Bordj Omar Driss", "In Amenas"]},
            "Bordj Bou Arréridj": {"coords": {"lat": 36.0731, "lon": 4.7608}, "communes": ["Bordj Bou Arréridj", "Ras El Oued", "El Anseur", "Mansourah"]},
            "Boumerdès": {"coords": {"lat": 36.7692, "lon": 3.4772}, "communes": ["Boumerdès", "Khemis El Khechna", "Boudouaou", "Thenia", "Naciria"]},
            "El Tarf": {"coords": {"lat": 36.7672, "lon": 8.3128}, "communes": ["El Tarf", "El Kala", "Ben M'hidi", "Bouteldja"]},
            "Tindouf": {"coords": {"lat": 27.6736, "lon": -8.1472}, "communes": ["Tindouf", "Oum El Assel"]},
            "Tissemsilt": {"coords": {"lat": 35.6072, "lon": 1.8117}, "communes": ["Tissemsilt", "Khemisti", "Bordj Bou Naama", "Lazharia"]},
            "El Oued": {"coords": {"lat": 33.3683, "lon": 6.8631}, "communes": ["El Oued", "Guemar", "Robbah", "Bayadha", "Nakhla"]},
            "Khenchela": {"coords": {"lat": 35.4333, "lon": 7.1333}, "communes": ["Khenchela", "Aïn Touila", "Babar", "Kais"]},
            "Souk Ahras": {"coords": {"lat": 36.2867, "lon": 7.9517}, "communes": ["Souk Ahras", "Sedrata", "Merahna", "Aïn Soltane"]},
            "Tipaza": {"coords": {"lat": 36.5894, "lon": 2.4472}, "communes": ["Tipaza", "Hadjout", "Koléa", "Cherchell", "Aïn Tagourait"]},
            "Mila": {"coords": {"lat": 36.4500, "lon": 6.2667}, "communes": ["Mila", "Chelghoum Laïd", "Ferdjioua", "Grarem Gouga"]},
            "Aïn Defla": {"coords": {"lat": 36.2639, "lon": 1.9658}, "communes": ["Aïn Defla", "Khemis Miliana", "Miliana", "El Abadia"]},
            "Naâma": {"coords": {"lat": 33.2667, "lon": -0.3167}, "communes": ["Naâma", "Méchéria", "Aïn Sefra", "Sfissifa"]},
            "Aïn Témouchent": {"coords": {"lat": 35.2983, "lon": -1.1400}, "communes": ["Aïn Témouchent", "Hammam Bouhadjar", "Beni Saf", "El Amria"]},
            "Ghardaïa": {"coords": {"lat": 32.4833, "lon": 3.6667}, "communes": ["Ghardaïa", "Guerrara", "El Meniaa", "Berriane", "Metlili"]},
            "Relizane": {"coords": {"lat": 35.7333, "lon": 0.5667}, "communes": ["Relizane", "Aïn Tarik", "Zemmoura", "Mazouna"]},
            "Timimoun": {"coords": {"lat": 29.2639, "lon": 0.2308}, "communes": ["Timimoun", "Aougrout", "Charouine"]},
            "Bordj Badji Mokhtar": {"coords": {"lat": 21.3294, "lon": 0.9469}, "communes": ["Bordj Badji Mokhtar", "Timiaouine"]},
            "Ouled Djellal": {"coords": {"lat": 34.4167, "lon": 5.0667}, "communes": ["Ouled Djellal", "Sidi Khaled", "Ras El Miad"]},
            "Béni Abbès": {"coords": {"lat": 30.1281, "lon": -2.1650}, "communes": ["Béni Abbès", "Kerzaz", "Ksabi"]},
            "In Salah": {"coords": {"lat": 27.1958, "lon": 2.4731}, "communes": ["In Salah", "In Ghar", "Foggaret Ezzaouia"]},
            "In Guezzam": {"coords": {"lat": 19.5667, "lon": 5.7667}, "communes": ["In Guezzam", "Tin Zaouatine"]},
            "Touggourt": {"coords": {"lat": 33.1000, "lon": 6.0667}, "communes": ["Touggourt", "Temacine", "Megarine", "El Hadjira"]},
            "Djanet": {"coords": {"lat": 24.5530, "lon": 9.4840}, "communes": ["Djanet", "Bordj El Houasse"]},
            "El M'Ghair": {"coords": {"lat": 33.9500, "lon": 5.9167}, "communes": ["El M'Ghair", "Djamaa", "Sidi Amrane"]},
            "El Meniaa": {"coords": {"lat": 30.5833, "lon": 2.8833}, "communes": ["El Meniaa", "Hassi Gara"]}
        }

        for wilaya_name, info in dz_data.items():
            wilaya = AdministrativeDivision.query.filter_by(
                name=wilaya_name, level=1, country_id=dz_id
            ).first()
            if not wilaya:
                wilaya = AdministrativeDivision(
                    name=wilaya_name, level=1, country_id=dz_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(wilaya)
                db.session.flush()
                print(f"  -> Wilaya : {wilaya_name}")

            for commune_name in info["communes"]:
                commune = AdministrativeDivision.query.filter_by(
                    name=commune_name, level=2, parent_id=wilaya.id
                ).first()
                if not commune:
                    commune = AdministrativeDivision(
                        name=commune_name, level=2, country_id=dz_id, parent_id=wilaya.id
                    )
                    db.session.add(commune)

        db.session.commit()
        print("Algérie : OK")

        # ================================================================
        # TUNISIE (ID: 788)
        # ================================================================
        print("\n--- Initialisation de la Tunisie (ID: 788) ---")
        tn_id = 788
        tn = Country.query.get(tn_id)
        if not tn:
            tn = Country(id=tn_id, name="Tunisie", iso_code="TN")
            db.session.add(tn)
            db.session.commit()
            print("Pays Tunisie créé.")

        tn_data = {
            "Tunis": {"coords": {"lat": 36.8190, "lon": 10.1658}, "delegations": ["Tunis", "Le Bardo", "La Marsa", "Carthage", "Sidi Bou Saïd", "Le Kram", "La Goulette"]},
            "Ariana": {"coords": {"lat": 36.8664, "lon": 10.1647}, "delegations": ["Ariana Ville", "Raoued", "Kalâat el-Andalous", "Sidi Thabet", "La Soukra", "Mnihla"]},
            "Ben Arous": {"coords": {"lat": 36.7536, "lon": 10.2167}, "delegations": ["Ben Arous", "Hammam Lif", "Hammam Chott", "Bou Mhel el-Bassatine", "Ezzahra", "Radès", "Mégrine", "Mourouj", "Nouvelle Médina", "Fouchana", "Mornag"]},
            "Manouba": {"coords": {"lat": 36.8089, "lon": 10.0986}, "delegations": ["Manouba", "Den Den", "Douar Hicher", "Oued Ellil", "El Mornaguia", "Borj El Amri", "Tebourba", "Djedeïda"]},
            "Nabeul": {"coords": {"lat": 36.4561, "lon": 10.7376}, "delegations": ["Nabeul", "Hammamet", "Kelibia", "Grombalia", "Soliman", "Korba", "Menzel Temime", "Béni Khalled"]},
            "Zaghouan": {"coords": {"lat": 36.4028, "lon": 10.1428}, "delegations": ["Zaghouan", "Zriba", "Ennadhour", "Bir Mcherga", "El Fahs", "Saouaf"]},
            "Bizerte": {"coords": {"lat": 37.2744, "lon": 9.8739}, "delegations": ["Bizerte Nord", "Bizerte Sud", "Menzel Bourguiba", "Mateur", "Sejnane", "Ras Jebel", "Menzel Jemil", "Tinja", "Utique"]},
            "Béja": {"coords": {"lat": 36.7256, "lon": 9.1817}, "delegations": ["Béja Nord", "Béja Sud", "Amdoun", "Nefza", "Téboursouk", "Testour", "Goubellat", "Medjez el-Bab"]},
            "Jendouba": {"coords": {"lat": 36.5011, "lon": 8.7803}, "delegations": ["Jendouba", "Jendouba Nord", "Bousalem", "Ain Draham", "Tabarka", "Fernana", "Ghardimaou", "Oued Meliz", "Balta-Bou Aouane"]},
            "Le Kef": {"coords": {"lat": 36.1826, "lon": 8.7147}, "delegations": ["Le Kef Ouest", "Le Kef Est", "Nebeur", "Sakiet Sidi Youssef", "Tajerouine", "Kalâat Sinane", "Kalâat Khasba", "Dahmani", "El Ksour", "Jerissa", "Sers"]},
            "Siliana": {"coords": {"lat": 36.0847, "lon": 9.3711}, "delegations": ["Siliana Nord", "Siliana Sud", "Bou Arada", "Gaâfour", "El Krib", "Bargou", "Maktar", "Rouhia", "Kesra", "Makthar"]},
            "Sousse": {"coords": {"lat": 35.8245, "lon": 10.6346}, "delegations": ["Sousse Médina", "Sousse Riadh", "Sousse Jaouhara", "Sousse Sidi Abdelhamid", "Hammam Sousse", "Akouda", "Kalâa Kebira", "Kalâa Seghira", "Bouficha", "Kondar", "Enfidha", "M'Saken", "Sidi Bou Ali", "Hergla"]},
            "Monastir": {"coords": {"lat": 35.7770, "lon": 10.8262}, "delegations": ["Monastir", "Jemmal", "Bembla", "Zeramdine", "Menzel Hayet", "Ksar Hellal", "Moknine", "Téboulba", "Bekalta", "Sahline", "Ouerdanine", "Beni Hassen"]},
            "Mahdia": {"coords": {"lat": 35.5047, "lon": 11.0622}, "delegations": ["Mahdia", "Ksour Essef", "Chorbane", "El Bradaa", "Hbira", "Ouled Chamekh", "Louta", "Hebira", "Essouassi", "El Jem", "Sidi Alouane"]},
            "Sfax": {"coords": {"lat": 34.7406, "lon": 10.7603}, "delegations": ["Sfax Médina", "Sfax Ouest", "Sfax Sud", "Sakiet Ezzit", "Sakiet Eddaïer", "Gremda", "El Aïn", "Thyna", "Agareb", "Jebeniana", "Bir Ali Ben Khalifa", "Skhira", "Mahres", "Hencha"]},
            "Kairouan": {"coords": {"lat": 35.6781, "lon": 10.0963}, "delegations": ["Kairouan Nord", "Kairouan Sud", "El Alaa", "Haffouz", "El Oueslatia", "Nasrallah", "Chebika", "Sbikha", "Bouhajla", "Cherarda", "Hajeb El Ayoun", "Menzel Mhiri"]},
            "Kasserine": {"coords": {"lat": 35.1722, "lon": 8.8306}, "delegations": ["Kasserine Nord", "Kasserine Sud", "Ezzouhour", "Hassi El Frid", "Sbeitla", "Sbiba", "Jedeliane", "El Ayoun", "Thala", "Hidra", "Foussana", "Feriana", "Majel Bel Abbès"]},
            "Sidi Bouzid": {"coords": {"lat": 35.0381, "lon": 9.4858}, "delegations": ["Sidi Bouzid Ouest", "Sidi Bouzid Est", "Jilma", "Bir El Hafey", "Sidi Ali Ben Aoun", "Menzel Bouzaïene", "Meknassy", "Souk Jedid", "Mezzouna", "Regueb", "Ouled Haffouz"]},
            "Gabès": {"coords": {"lat": 33.8814, "lon": 10.0983}, "delegations": ["Gabès Médina", "Gabès Ouest", "Gabès Sud", "Ghannouch", "El Hamma", "Mareth", "Agareb", "Métouia", "Nouvelle Matmata", "Matmata", "Menzel El Habib"]},
            "Médenine": {"coords": {"lat": 33.3547, "lon": 10.4953}, "delegations": ["Médenine Nord", "Médenine Sud", "Ben Gardane", "Zarzis", "Houmet Souk", "Ajim", "Erriadh", "Beni Khedache", "Sidi Makhlouf", "Midoun"]},
            "Tataouine": {"coords": {"lat": 32.9211, "lon": 10.4511}, "delegations": ["Tataouine Nord", "Tataouine Sud", "Bir Lahmar", "Ghomrassen", "Smar", "Dhehiba", "Remada"]},
            "Gafsa": {"coords": {"lat": 34.4250, "lon": 8.7842}, "delegations": ["Gafsa Nord", "Gafsa Sud", "Sidi Aïch", "El Ksar", "Guetar", "El Guettar", "Lalla", "Métlaoui", "El Mdhilla", "Redeyef", "Moulares", "Belkhir"]},
            "Tozeur": {"coords": {"lat": 33.9197, "lon": 8.1335}, "delegations": ["Tozeur", "Degache", "Tameghza", "Hezoua", "Nefta"]},
            "Kébili": {"coords": {"lat": 33.7042, "lon": 8.9719}, "delegations": ["Kébili Nord", "Kébili Sud", "Souk Lahad", "Douz Nord", "Douz Sud", "Faouar"]}
        }

        for gouv_name, info in tn_data.items():
            gouv = AdministrativeDivision.query.filter_by(
                name=gouv_name, level=1, country_id=tn_id
            ).first()
            if not gouv:
                gouv = AdministrativeDivision(
                    name=gouv_name, level=1, country_id=tn_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(gouv)
                db.session.flush()
                print(f"  -> Gouvernorat : {gouv_name}")

            for deleg_name in info["delegations"]:
                deleg = AdministrativeDivision.query.filter_by(
                    name=deleg_name, level=2, parent_id=gouv.id
                ).first()
                if not deleg:
                    deleg = AdministrativeDivision(
                        name=deleg_name, level=2, country_id=tn_id, parent_id=gouv.id
                    )
                    db.session.add(deleg)

        db.session.commit()
        print("Tunisie : OK")

        # ================================================================
        # LIBYE (ID: 434)
        # ================================================================
        print("\n--- Initialisation de la Libye (ID: 434) ---")
        ly_id = 434
        ly = Country.query.get(ly_id)
        if not ly:
            ly = Country(id=ly_id, name="Libye", iso_code="LY")
            db.session.add(ly)
            db.session.commit()
            print("Pays Libye créé.")

        ly_data = {
            "Tripoli": {"coords": {"lat": 32.9011, "lon": 13.1800}, "baladiyats": ["Tripoli", "Aïn Zara", "Souq Al Jumaa", "Tajoura", "Sidi Al Masri"]},
            "Benghazi": {"coords": {"lat": 32.1167, "lon": 20.0667}, "baladiyats": ["Benghazi", "Qwarsha", "Al Abraq", "Al Julyana"]},
            "Misrata": {"coords": {"lat": 32.3754, "lon": 15.0925}, "baladiyats": ["Misrata", "Bani Walid", "Tarhuna", "Zliten"]},
            "Marj": {"coords": {"lat": 32.4900, "lon": 20.8333}, "baladiyats": ["Marj", "Al Bayda", "Shahat", "Derna"]},
            "Jabal Al Akhdar": {"coords": {"lat": 32.7667, "lon": 21.7500}, "baladiyats": ["Al Bayda", "Shahat", "Susa"]},
            "Jabal Al Gharbi": {"coords": {"lat": 29.9000, "lon": 13.8833}, "baladiyats": ["Gharyan", "Yafran", "Zintan", "Nalut"]},
            "Al Jafarah": {"coords": {"lat": 32.8500, "lon": 12.9167}, "baladiyats": ["Al Ajaylat", "Az Zawiyah", "Sabratah", "Surman"]},
            "Az Zawiyah": {"coords": {"lat": 32.7522, "lon": 12.7278}, "baladiyats": ["Az Zawiyah", "Sabratah", "Surman", "Al Ajaylat"]},
            "Al Murqub": {"coords": {"lat": 32.4833, "lon": 14.0667}, "baladiyats": ["Khoms", "Qasr Bin Ghashir", "Tarhuna", "Msallata"]},
            "Wadi Al Hayaa": {"coords": {"lat": 26.5000, "lon": 12.9167}, "baladiyats": ["Ubari", "Murzuq", "Sabha"]},
            "Sabha": {"coords": {"lat": 27.0367, "lon": 14.4286}, "baladiyats": ["Sabha", "Brak", "Umm al-Abid"]},
            "Murzuq": {"coords": {"lat": 25.9167, "lon": 13.9167}, "baladiyats": ["Murzuq", "Traghen", "Umm al-Aranib"]},
            "Ghat": {"coords": {"lat": 24.9644, "lon": 10.1733}, "baladiyats": ["Ghat", "Barakat"]},
            "Al Kufrah": {"coords": {"lat": 24.1864, "lon": 23.3075}, "baladiyats": ["Al Jawf", "Rabyanah", "Al Kufrah"]},
            "Surt": {"coords": {"lat": 31.2089, "lon": 16.5887}, "baladiyats": ["Surt", "Bin Jawwad", "Waddan"]},
            "Al Jufrah": {"coords": {"lat": 29.1167, "lon": 16.0167}, "baladiyats": ["Hun", "Waddan", "Sokna", "Zillah"]},
            "Derna": {"coords": {"lat": 32.7550, "lon": 22.6367}, "baladiyats": ["Derna", "Al Qubbah", "Martubah", "Tmassah"]},
            "Al Wahat": {"coords": {"lat": 29.0667, "lon": 21.9833}, "baladiyats": ["Ajdabiya", "Jalu", "Al Kufrah"]},
            "Nuqat Al Khams": {"coords": {"lat": 32.9500, "lon": 12.0833}, "baladiyats": ["Zuwara", "Al Jumayl", "Regdalin"]},
            "Al Butnan": {"coords": {"lat": 31.0833, "lon": 25.1167}, "baladiyats": ["Tobruk", "Al Jaghbub", "Bardiyah"]}
        }

        for district_name, info in ly_data.items():
            district = AdministrativeDivision.query.filter_by(
                name=district_name, level=1, country_id=ly_id
            ).first()
            if not district:
                district = AdministrativeDivision(
                    name=district_name, level=1, country_id=ly_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(district)
                db.session.flush()
                print(f"  -> District : {district_name}")

            for bald_name in info["baladiyats"]:
                bald = AdministrativeDivision.query.filter_by(
                    name=bald_name, level=2, parent_id=district.id
                ).first()
                if not bald:
                    bald = AdministrativeDivision(
                        name=bald_name, level=2, country_id=ly_id, parent_id=district.id
                    )
                    db.session.add(bald)

        db.session.commit()
        print("Libye : OK")

        # ================================================================
        # MAURITANIE (ID: 478)
        # ================================================================
        print("\n--- Initialisation de la Mauritanie (ID: 478) ---")
        mr_id = 478
        mr = Country.query.get(mr_id)
        if not mr:
            mr = Country(id=mr_id, name="Mauritanie", iso_code="MR")
            db.session.add(mr)
            db.session.commit()
            print("Pays Mauritanie créé.")

        mr_data = {
            "Hodh Ech Chargui": {"coords": {"lat": 18.0000, "lon": -7.5000}, "departments": ["Nema", "Bassikounou", "Djiguenni", "Amourj", "Oualata", "Timbedra", "Koubenni", "Adel Bagrou"]},
            "Hodh El Gharbi": {"coords": {"lat": 16.5000, "lon": -9.5000}, "departments": ["Aïoun El Atrouss", "Tamchakett", "Kobenni", "Boumdeid", "Tintane"]},
            "Assaba": {"coords": {"lat": 16.5000, "lon": -11.5000}, "departments": ["Kiffa", "Guerou", "Barkéwol", "Kankossa", "Boumdeid"]},
            "Gorgol": {"coords": {"lat": 15.9167, "lon": -12.6667}, "departments": ["Kaédi", "Mbout", "Maghama", "Monguel", "M'Bout"]},
            "Brakna": {"coords": {"lat": 17.0000, "lon": -13.5000}, "departments": ["Aleg", "Bababé", "Boghé", "Maghama", "Mbagne", "M'Bagne"]},
            "Trarza": {"coords": {"lat": 18.0000, "lon": -15.5000}, "departments": ["Rosso", "Boutilimit", "Keur Macène", "Mederdra", "Ouad Naga", "R'Kiz"]},
            "Adrar": {"coords": {"lat": 20.5000, "lon": -13.0000}, "departments": ["Atar", "Aoujeft", "Chinguetti", "Ouadane"]},
            "Dakhlet Nouadhibou": {"coords": {"lat": 20.9333, "lon": -17.0333}, "departments": ["Nouadhibou", "Chami"]},
            "Tagant": {"coords": {"lat": 18.5000, "lon": -11.5000}, "departments": ["Tidjikja", "Moudjéria", "Tichit"]},
            "Guidimaka": {"coords": {"lat": 15.2000, "lon": -12.2000}, "departments": ["Sélibaby", "Ould Yengé", "Baydiam"]},
            "Tiris Zemmour": {"coords": {"lat": 23.0000, "lon": -11.5000}, "departments": ["Zouerate", "Bir Moghrein", "F'Dérik"]},
            "Inchiri": {"coords": {"lat": 20.0000, "lon": -15.5000}, "departments": ["Akjoujt", "Bénichab"]},
            "Nouakchott Nord": {"coords": {"lat": 18.1100, "lon": -15.9750}, "departments": ["Dar Naim", "Teyarett", "Toujounine"]},
            "Nouakchott Ouest": {"coords": {"lat": 18.0800, "lon": -15.9850}, "departments": ["Tevragh-Zeïna", "Ksar", "Sebkha"]},
            "Nouakchott Sud": {"coords": {"lat": 18.0500, "lon": -15.9700}, "departments": ["Arafat", "Riyadh", "El Mina"]}
        }

        for wilaya_name, info in mr_data.items():
            wilaya = AdministrativeDivision.query.filter_by(
                name=wilaya_name, level=1, country_id=mr_id
            ).first()
            if not wilaya:
                wilaya = AdministrativeDivision(
                    name=wilaya_name, level=1, country_id=mr_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(wilaya)
                db.session.flush()
                print(f"  -> Wilaya : {wilaya_name}")

            for dept_name in info["departments"]:
                dept = AdministrativeDivision.query.filter_by(
                    name=dept_name, level=2, parent_id=wilaya.id
                ).first()
                if not dept:
                    dept = AdministrativeDivision(
                        name=dept_name, level=2, country_id=mr_id, parent_id=wilaya.id
                    )
                    db.session.add(dept)

        db.session.commit()
        print("Mauritanie : OK")

        # ================================================================
        # RÉSUMÉ FINAL
        # ================================================================
        print("\n" + "="*50)
        print("Succès : Toutes les données du Maghreb sont à jour !")
        print("  - Maroc        (ID: 504) : 12 régions")
        print("  - Algérie      (ID: 12)  : 58 wilayas")
        print("  - Tunisie      (ID: 788) : 24 gouvernorats")
        print("  - Libye        (ID: 434) : 20 districts")
        print("  - Mauritanie   (ID: 478) : 15 wilayas")
        print("="*50)

if __name__ == "__main__":
    seed_maghreb()