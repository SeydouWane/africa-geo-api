import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():

        # ================================================================
        # ÉTHIOPIE (ID: 231)
        # ================================================================
        print("\n--- Initialisation de l'Éthiopie (ID: 231) ---")
        et_id = 231
        et = Country.query.get(et_id)
        if not et:
            et = Country(id=et_id, name="Éthiopie", iso_code="ET")
            db.session.add(et)
            db.session.commit()
            print("Pays Éthiopie créé.")

        et_data = {
            "Addis-Abeba": {
                "coords": {"lat": 9.0320, "lon": 38.7469},
                "zones": ["Addis Abeba Zone 1", "Addis Abeba Zone 2", "Addis Abeba Zone 3",
                          "Addis Abeba Zone 4", "Addis Abeba Zone 5", "Addis Abeba Zone 6",
                          "Addis Abeba Zone 7", "Addis Abeba Zone 8", "Addis Abeba Zone 9",
                          "Addis Abeba Zone 10"]
            },
            "Afar": {
                "coords": {"lat": 11.7557, "lon": 40.9689},
                "zones": ["Awsi Rasu", "Kilbet Rasu", "Gabi Rasu", "Fantena Rasu", "Hari Rasu"]
            },
            "Amhara": {
                "coords": {"lat": 11.3396, "lon": 37.9519},
                "zones": ["Agew Awi", "Bete Amhara", "East Gojjam", "North Gondar",
                          "North Shewa", "North Wollo", "Oromia", "South Gondar",
                          "South Wollo", "Wag Hemra", "West Gojjam"]
            },
            "Benishangul-Gumuz": {
                "coords": {"lat": 10.7800, "lon": 35.5700},
                "zones": ["Assosa", "Kamashi", "Metekel"]
            },
            "Dire Dawa": {
                "coords": {"lat": 9.5930, "lon": 41.8661},
                "zones": ["Dire Dawa Urban", "Dire Dawa Rural"]
            },
            "Gambéla": {
                "coords": {"lat": 8.2490, "lon": 34.5889},
                "zones": ["Agnewak", "Mejenger", "Nuer"]
            },
            "Harari": {
                "coords": {"lat": 9.3121, "lon": 42.1198},
                "zones": ["Harar Town", "Harar Rural"]
            },
            "Oromia": {
                "coords": {"lat": 7.5460, "lon": 40.6588},
                "zones": ["Arsi", "Bale", "Borena", "East Hararghe", "East Shewa",
                          "East Wollega", "Guji", "Horo Guduru Wollega", "Illu Aba Bora",
                          "Jimma", "Kelem Wollega", "North Shewa", "South West Shewa",
                          "West Arsi", "West Hararghe", "West Shewa", "West Wollega"]
            },
            "Sidama": {
                "coords": {"lat": 6.7650, "lon": 38.4192},
                "zones": ["Sidama Zone"]
            },
            "Somali": {
                "coords": {"lat": 6.8700, "lon": 44.1500},
                "zones": ["Afder", "Degehabur", "Fafan", "Jarar", "Korahe",
                          "Liben", "Nogob", "Sitti", "Shabelle", "Dollo"]
            },
            "Sud-Ouest": {
                "coords": {"lat": 6.0000, "lon": 36.5000},
                "zones": ["Bench Sheko", "Dawro", "Kaffa", "Konta", "Sheka", "West Omo"]
            },
            "SNNPR": {
                "coords": {"lat": 6.5000, "lon": 37.5000},
                "zones": ["Alaba", "Amaro", "Basketo", "Burji", "Gamo", "Gedeo",
                          "Gurage", "Hadiya", "Halaba", "Kembata Tembaro",
                          "Konso", "Silte", "Wolaita", "Yem"]
            },
            "Tigré": {
                "coords": {"lat": 14.0323, "lon": 38.3168},
                "zones": ["Central Tigray", "Eastern Tigray", "North Western Tigray",
                          "South Eastern Tigray", "Southern Tigray", "Western Tigray"]
            }
        }

        for region_name, info in et_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=et_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=et_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for zone_name in info["zones"]:
                zone = AdministrativeDivision.query.filter_by(
                    name=zone_name, level=2, parent_id=region.id
                ).first()
                if not zone:
                    zone = AdministrativeDivision(
                        name=zone_name, level=2, country_id=et_id, parent_id=region.id
                    )
                    db.session.add(zone)

        db.session.commit()
        print("Éthiopie : OK")

        # ================================================================
        # ÉRYTHRÉE (ID: 232)
        # ================================================================
        print("\n--- Initialisation de l'Érythrée (ID: 232) ---")
        er_id = 232
        er = Country.query.get(er_id)
        if not er:
            er = Country(id=er_id, name="Érythrée", iso_code="ER")
            db.session.add(er)
            db.session.commit()
            print("Pays Érythrée créé.")

        er_data = {
            "Anseba": {
                "coords": {"lat": 16.1000, "lon": 37.6833},
                "districts": ["Adi Tekelezan", "Asmat", "Elabered", "Hagaz", "Hamelmalo",
                              "Keren", "Habero", "Ker Ker", "Logo Anseba"]
            },
            "Debub": {
                "coords": {"lat": 15.0000, "lon": 38.8333},
                "districts": ["Adi Keih", "Adi Quala", "Areza", "Dekemhare", "Debarwa",
                              "Emni Haili", "Kudo Felasi", "Mai Mine", "Maakel", "Mendefera",
                              "Segeneiti", "Senafe", "Tserona"]
            },
            "Debubawi Keyih Bahri": {
                "coords": {"lat": 13.5000, "lon": 42.5000},
                "districts": ["Beylul", "Danakalia", "Deheba"]
            },
            "Gash-Barka": {
                "coords": {"lat": 15.4500, "lon": 37.2167},
                "districts": ["Agordat", "Barentu", "Dghe", "Forto", "Gogne",
                              "Haicota", "Logo Anseba", "Laelay Gash", "Mensura",
                              "Molki", "Om Hajer", "Shambuko", "Tesseney"]
            },
            "Maakel": {
                "coords": {"lat": 15.3387, "lon": 38.9312},
                "districts": ["Asmara Central", "Asmara North", "Asmara South",
                              "Asmara West", "Berikh", "Mai-Tsebri", "Serejeka"]
            },
            "Semienawi Keyih Bahri": {
                "coords": {"lat": 16.0000, "lon": 39.5000},
                "districts": ["Afabet", "Dahlak", "Foro", "Ghinda", "Karura", "Massawa", "She'eb"]
            }
        }

        for region_name, info in er_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=er_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=er_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=er_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Érythrée : OK")

        # ================================================================
        # DJIBOUTI (ID: 262)
        # ================================================================
        print("\n--- Initialisation de Djibouti (ID: 262) ---")
        dj_id = 262
        dj = Country.query.get(dj_id)
        if not dj:
            dj = Country(id=dj_id, name="Djibouti", iso_code="DJ")
            db.session.add(dj)
            db.session.commit()
            print("Pays Djibouti créé.")

        dj_data = {
            "Djibouti": {
                "coords": {"lat": 11.5886, "lon": 43.1451},
                "districts": ["Balbala", "Boulaos", "Arhiba", "Plateau du Serpent", "Quartier 7"]
            },
            "Ali Sabieh": {
                "coords": {"lat": 11.1553, "lon": 42.7126},
                "districts": ["Ali Sabieh", "Holhol", "Assamo", "Ali Adde"]
            },
            "Arta": {
                "coords": {"lat": 11.5231, "lon": 42.8497},
                "districts": ["Arta", "Damerjog", "Loyada"]
            },
            "Dikhil": {
                "coords": {"lat": 11.1053, "lon": 42.3708},
                "districts": ["Dikhil", "As Eyla", "Galafi", "Yoboki"]
            },
            "Obock": {
                "coords": {"lat": 11.9801, "lon": 43.2975},
                "districts": ["Obock", "Khor Angar", "Loyada"]
            },
            "Tadjourah": {
                "coords": {"lat": 11.7840, "lon": 42.8851},
                "districts": ["Tadjourah", "Randa", "Sagallou", "Dorra", "Balho"]
            }
        }

        for region_name, info in dj_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=dj_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=dj_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=dj_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Djibouti : OK")

        # ================================================================
        # SOMALIE (ID: 706)
        # ================================================================
        print("\n--- Initialisation de la Somalie (ID: 706) ---")
        so_id = 706
        so = Country.query.get(so_id)
        if not so:
            so = Country(id=so_id, name="Somalie", iso_code="SO")
            db.session.add(so)
            db.session.commit()
            print("Pays Somalie créé.")

        so_data = {
            "Awdal": {
                "coords": {"lat": 10.6167, "lon": 43.4833},
                "districts": ["Borama", "Baki", "Lughaya", "Zeila"]
            },
            "Bakool": {
                "coords": {"lat": 4.2667, "lon": 43.6333},
                "districts": ["Hudur", "El Barde", "Rabdhure", "Tiyeglow", "Waajid"]
            },
            "Banaadir": {
                "coords": {"lat": 2.0469, "lon": 45.3182},
                "districts": ["Mogadiscio", "Abdiaziz", "Bondhere", "Daynile",
                              "Dharkenley", "Hamar-Jajab", "Hamar-Weyne", "Heliwa",
                              "Hodan", "Howlwadag", "Karan", "Shangani", "Shibis",
                              "Waberi", "Wadajir", "Wardhigley", "Yaqshid"]
            },
            "Bari": {
                "coords": {"lat": 10.4167, "lon": 49.8333},
                "districts": ["Bosaso", "Bandarbeyla", "Iskushuban", "Qandala", "Qardho"]
            },
            "Bay": {
                "coords": {"lat": 2.7667, "lon": 43.4833},
                "districts": ["Baidoa", "Buur Hakaba", "Diinsoor", "Qansax Dheere"]
            },
            "Galguduud": {
                "coords": {"lat": 5.1667, "lon": 46.7667},
                "districts": ["Dhuusamarreeb", "Abudwak", "Balcad", "Cabudwaaq", "Ceel Buur"]
            },
            "Gedo": {
                "coords": {"lat": 3.5000, "lon": 41.8667},
                "districts": ["Garbaharey", "Baardheere", "Belet Xaawo", "Ceel Waaq", "Doolow", "Luuq"]
            },
            "Hiiraan": {
                "coords": {"lat": 4.3333, "lon": 45.3333},
                "districts": ["Beledweyne", "Bulo Burto", "Jalalaqsi"]
            },
            "Jubbada Dhexe": {
                "coords": {"lat": 1.5000, "lon": 42.5000},
                "districts": ["Bu'aale", "Jilib", "Saakow"]
            },
            "Jubbada Hoose": {
                "coords": {"lat": -0.3667, "lon": 42.5500},
                "districts": ["Afmadow", "Badhaadhe", "Jamaame", "Kismayo"]
            },
            "Mudug": {
                "coords": {"lat": 6.5000, "lon": 47.7500},
                "districts": ["Gaalkacyo", "Galdogob", "Hobyo", "Jariban"]
            },
            "Nugaal": {
                "coords": {"lat": 8.5000, "lon": 49.1667},
                "districts": ["Garoowe", "Burtinle", "Eyl"]
            },
            "Sanaag": {
                "coords": {"lat": 10.5833, "lon": 47.3667},
                "districts": ["Ceerigaavo", "Badhan", "Dhahar", "Laasqoray"]
            },
            "Shabeellaha Dhexe": {
                "coords": {"lat": 2.6667, "lon": 45.5000},
                "districts": ["Jowhar", "Adan Yabaal", "Balcad"]
            },
            "Shabeellaha Hoose": {
                "coords": {"lat": 1.6667, "lon": 44.5000},
                "districts": ["Marka", "Baraawe", "Bu'aale", "Jawhar", "Qoryooley", "Wanlaweyn"]
            },
            "Sool": {
                "coords": {"lat": 8.6500, "lon": 46.8333},
                "districts": ["Laas Caanood", "Caynabo", "Taleh", "Xudun"]
            },
            "Togdheer": {
                "coords": {"lat": 9.5500, "lon": 45.4833},
                "districts": ["Burco", "Buuhoodle", "Odweyne", "Sheikh"]
            },
            "Woqooyi Galbeed": {
                "coords": {"lat": 9.5597, "lon": 44.0650},
                "districts": ["Hargeysa", "Berbera", "Gebiley"]
            }
        }

        for region_name, info in so_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=so_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=so_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=so_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Somalie : OK")

        # ================================================================
        # KENYA (ID: 404)
        # ================================================================
        print("\n--- Initialisation du Kenya (ID: 404) ---")
        ke_id = 404
        ke = Country.query.get(ke_id)
        if not ke:
            ke = Country(id=ke_id, name="Kenya", iso_code="KE")
            db.session.add(ke)
            db.session.commit()
            print("Pays Kenya créé.")

        ke_data = {
            "Baringo": {"coords": {"lat": 0.8330, "lon": 35.9720}, "sub_counties": ["Baringo Central", "Baringo North", "Baringo South", "Eldama Ravine", "Mogotio", "Tiaty"]},
            "Bomet": {"coords": {"lat": -0.7829, "lon": 35.3416}, "sub_counties": ["Bomet Central", "Bomet East", "Chepalungu", "Konoin", "Sotik"]},
            "Bungoma": {"coords": {"lat": 0.5635, "lon": 34.5606}, "sub_counties": ["Bumula", "Kabuchai", "Kanduyi", "Kimilili", "Mt Elgon", "Sirisia", "Tongaren", "Webuye East", "Webuye West"]},
            "Busia": {"coords": {"lat": 0.4608, "lon": 34.1116}, "sub_counties": ["Budalangi", "Butula", "Funyula", "Matayos", "Nambale", "Teso North", "Teso South"]},
            "Elgeyo-Marakwet": {"coords": {"lat": 0.9833, "lon": 35.5167}, "sub_counties": ["Keiyo North", "Keiyo South", "Marakwet East", "Marakwet West"]},
            "Embu": {"coords": {"lat": -0.5390, "lon": 37.4581}, "sub_counties": ["Manyatta", "Mbeere North", "Mbeere South", "Runyenjes"]},
            "Garissa": {"coords": {"lat": -0.4532, "lon": 39.6460}, "sub_counties": ["Daadab", "Fafi", "Garissa Township", "Ijara", "Lagdera", "Balambala"]},
            "Homa Bay": {"coords": {"lat": -0.5270, "lon": 34.4571}, "sub_counties": ["Homa Bay Town", "Kabondo Kasipul", "Karachuonyo", "Kasipul", "Mbita", "Ndhiwa", "Rangwe", "Suba North", "Suba South"]},
            "Isiolo": {"coords": {"lat": 0.3543, "lon": 37.5822}, "sub_counties": ["Garbatulla", "Isiolo", "Merti"]},
            "Kajiado": {"coords": {"lat": -2.0985, "lon": 36.7819}, "sub_counties": ["Kajiado Central", "Kajiado East", "Kajiado North", "Kajiado South", "Kajiado West", "Loitokitok"]},
            "Kakamega": {"coords": {"lat": 0.2827, "lon": 34.7519}, "sub_counties": ["Butere", "Ikolomani", "Khwisero", "Lugari", "Lurambi", "Malava", "Matungu", "Mumias East", "Mumias West", "Navakholo", "Shinyalu"]},
            "Kericho": {"coords": {"lat": -0.3689, "lon": 35.2863}, "sub_counties": ["Ainamoi", "Belgut", "Bureti", "Kipkelion East", "Kipkelion West", "Soin Sigowet"]},
            "Kiambu": {"coords": {"lat": -1.0314, "lon": 36.8311}, "sub_counties": ["Gatundu North", "Gatundu South", "Githunguri", "Kabete", "Kiambaa", "Kiambu", "Kikuyu", "Lari", "Limuru", "Ruiru", "Thika Town", "Thika Rural"]},
            "Kilifi": {"coords": {"lat": -3.5100, "lon": 39.8500}, "sub_counties": ["Ganze", "Kaloleni", "Kilifi North", "Kilifi South", "Malindi", "Magarini", "Rabai"]},
            "Kirinyaga": {"coords": {"lat": -0.5587, "lon": 37.2630}, "sub_counties": ["Gichugu", "Kirinyaga Central", "Mwea East", "Mwea West", "Ndia"]},
            "Kisii": {"coords": {"lat": -0.6817, "lon": 34.7660}, "sub_counties": ["Bobasi", "Bonchari", "Bomachoge Borabu", "Bomachoge Chache", "Kitutu Chache North", "Kitutu Chache South", "Nyaribari Chache", "Nyaribari Masaba", "South Mugirango"]},
            "Kisumu": {"coords": {"lat": -0.0917, "lon": 34.7680}, "sub_counties": ["Kisumu Central", "Kisumu East", "Kisumu West", "Muhoroni", "Nyakach", "Nyando", "Seme"]},
            "Kitui": {"coords": {"lat": -1.3669, "lon": 38.0104}, "sub_counties": ["Kitui Central", "Kitui East", "Kitui Rural", "Kitui South", "Kitui West", "Mwingi Central", "Mwingi North", "Mwingi West"]},
            "Kwale": {"coords": {"lat": -4.1744, "lon": 39.4522}, "sub_counties": ["Kinango", "Lungalunga", "Matuga", "Msambweni"]},
            "Laikipia": {"coords": {"lat": 0.3604, "lon": 36.7820}, "sub_counties": ["Laikipia Central", "Laikipia East", "Laikipia North", "Laikipia West", "Nyahururu"]},
            "Lamu": {"coords": {"lat": -2.2686, "lon": 40.9020}, "sub_counties": ["Lamu East", "Lamu West"]},
            "Machakos": {"coords": {"lat": -1.5177, "lon": 37.2634}, "sub_counties": ["Kathiani", "Machakos Town", "Masinga", "Matungulu", "Mavoko", "Mwala", "Yatta"]},
            "Makueni": {"coords": {"lat": -2.2558, "lon": 37.8944}, "sub_counties": ["Kaiti", "Kibwezi East", "Kibwezi West", "Kilome", "Makueni", "Mbooni"]},
            "Mandera": {"coords": {"lat": 3.9366, "lon": 41.8670}, "sub_counties": ["Banissa", "Lafey", "Mandera East", "Mandera North", "Mandera South", "Mandera West"]},
            "Marsabit": {"coords": {"lat": 2.3284, "lon": 37.9899}, "sub_counties": ["Laisamis", "Marsabit Central", "Moyale", "North Horr", "Saku"]},
            "Meru": {"coords": {"lat": 0.0467, "lon": 37.6495}, "sub_counties": ["Buuri", "Igembe Central", "Igembe North", "Igembe South", "Imenti Central", "Imenti North", "Imenti South", "Tigania East", "Tigania West"]},
            "Migori": {"coords": {"lat": -1.0634, "lon": 34.4731}, "sub_counties": ["Awendo", "Kuria East", "Kuria West", "Mabera", "Ntimaru", "Nyatike", "Rongo", "Suna East", "Suna West", "Uriri"]},
            "Mombasa": {"coords": {"lat": -4.0435, "lon": 39.6682}, "sub_counties": ["Changamwe", "Jomvu", "Kisauni", "Likoni", "Mvita", "Nyali"]},
            "Murang'a": {"coords": {"lat": -0.7197, "lon": 37.0311}, "sub_counties": ["Gatanga", "Kahuro", "Kandara", "Kangema", "Kigumo", "Kiharu", "Mathioya", "Murang'a South"]},
            "Nairobi": {"coords": {"lat": -1.2921, "lon": 36.8219}, "sub_counties": ["Dagoretti North", "Dagoretti South", "Embakasi Central", "Embakasi East", "Embakasi North", "Embakasi South", "Embakasi West", "Kasarani", "Kibra", "Langata", "Makadara", "Mathare", "Roysambu", "Ruaraka", "Starehe", "Westlands"]},
            "Nakuru": {"coords": {"lat": -0.3031, "lon": 36.0800}, "sub_counties": ["Bahati", "Gilgil", "Kuresoi North", "Kuresoi South", "Molo", "Naivasha", "Nakuru Town East", "Nakuru Town West", "Njoro", "Rongai", "Subukia"]},
            "Nandi": {"coords": {"lat": 0.1833, "lon": 35.1167}, "sub_counties": ["Chesumei", "Emgwen", "Mosop", "Nandi Hills", "Tinderet"]},
            "Narok": {"coords": {"lat": -1.0828, "lon": 35.8708}, "sub_counties": ["Narok East", "Narok North", "Narok South", "Narok West", "Trans-Mara East", "Trans-Mara West"]},
            "Nyamira": {"coords": {"lat": -0.5665, "lon": 34.9350}, "sub_counties": ["Borabu", "Manga", "Masaba North", "Nyamira North", "Nyamira South"]},
            "Nyandarua": {"coords": {"lat": -0.1827, "lon": 36.5226}, "sub_counties": ["Kinangop", "Kipipiri", "Ndaragwa", "North Kinangop", "Ol Kalou"]},
            "Nyeri": {"coords": {"lat": -0.4167, "lon": 36.9500}, "sub_counties": ["Kieni", "Mathira", "Mukurweini", "Nyeri Town", "Othaya", "Tetu"]},
            "Samburu": {"coords": {"lat": 1.2167, "lon": 36.7667}, "sub_counties": ["Samburu East", "Samburu North", "Samburu West"]},
            "Siaya": {"coords": {"lat": 0.0607, "lon": 34.2879}, "sub_counties": ["Alego Usonga", "Bondo", "Gem", "Rarieda", "Ugenya", "Ugunja"]},
            "Taita-Taveta": {"coords": {"lat": -3.3160, "lon": 38.3580}, "sub_counties": ["Mwatate", "Taveta", "Voi", "Wundanyi"]},
            "Tana River": {"coords": {"lat": -1.5833, "lon": 39.6000}, "sub_counties": ["Bura", "Garsen", "Galole"]},
            "Tharaka-Nithi": {"coords": {"lat": -0.3000, "lon": 37.7167}, "sub_counties": ["Chuka/Igambang'ombe", "Maara", "Tharaka North", "Tharaka South"]},
            "Trans Nzoia": {"coords": {"lat": 1.0167, "lon": 34.9500}, "sub_counties": ["Cherangany", "Endebess", "Kiminini", "Kwanza", "Saboti"]},
            "Turkana": {"coords": {"lat": 3.1167, "lon": 35.5667}, "sub_counties": ["Loima", "Turkana Central", "Turkana East", "Turkana North", "Turkana South", "Turkana West"]},
            "Uasin Gishu": {"coords": {"lat": 0.5167, "lon": 35.2667}, "sub_counties": ["Ainabkoi", "Kapseret", "Kesses", "Moiben", "Soy", "Turbo"]},
            "Vihiga": {"coords": {"lat": 0.0831, "lon": 34.7235}, "sub_counties": ["Emuhaya", "Hamisi", "Luanda", "Sabatia", "Vihiga"]},
            "Wajir": {"coords": {"lat": 1.7471, "lon": 40.0573}, "sub_counties": ["Eldas", "Tarbaj", "Wajir East", "Wajir North", "Wajir South", "Wajir West"]},
            "West Pokot": {"coords": {"lat": 1.7500, "lon": 35.1167}, "sub_counties": ["Kacheliba", "Kapenguria", "Pokot Central", "Pokot North", "Pokot South", "Sigor"]}
        }

        for county_name, info in ke_data.items():
            county = AdministrativeDivision.query.filter_by(
                name=county_name, level=1, country_id=ke_id
            ).first()
            if not county:
                county = AdministrativeDivision(
                    name=county_name, level=1, country_id=ke_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(county)
                db.session.flush()
                print(f"  -> Comté : {county_name}")

            for sub_name in info["sub_counties"]:
                sub = AdministrativeDivision.query.filter_by(
                    name=sub_name, level=2, parent_id=county.id
                ).first()
                if not sub:
                    sub = AdministrativeDivision(
                        name=sub_name, level=2, country_id=ke_id, parent_id=county.id
                    )
                    db.session.add(sub)

        db.session.commit()
        print("Kenya : OK")

        # ================================================================
        # TANZANIE (ID: 834)
        # ================================================================
        print("\n--- Initialisation de la Tanzanie (ID: 834) ---")
        tz_id = 834
        tz = Country.query.get(tz_id)
        if not tz:
            tz = Country(id=tz_id, name="Tanzanie", iso_code="TZ")
            db.session.add(tz)
            db.session.commit()
            print("Pays Tanzanie créé.")

        tz_data = {
            "Arusha": {"coords": {"lat": -3.3869, "lon": 36.6830}, "districts": ["Arusha City", "Arusha", "Karatu", "Longido", "Meru", "Monduli", "Ngorongoro"]},
            "Dar es Salaam": {"coords": {"lat": -6.7924, "lon": 39.2083}, "districts": ["Ilala", "Kinondoni", "Kigamboni", "Temeke", "Ubungo"]},
            "Dodoma": {"coords": {"lat": -6.1731, "lon": 35.7395}, "districts": ["Bahi", "Chamwino", "Chemba", "Dodoma City", "Kondoa", "Kongwa", "Mpwapwa"]},
            "Geita": {"coords": {"lat": -2.8671, "lon": 32.1653}, "districts": ["Bukombe", "Chato", "Geita", "Mbogwe", "Nyang'hwale"]},
            "Iringa": {"coords": {"lat": -7.7667, "lon": 35.7000}, "districts": ["Iringa", "Iringa Rural", "Kilolo", "Mufindi"]},
            "Kagera": {"coords": {"lat": -1.3000, "lon": 31.3500}, "districts": ["Biharamulo", "Bukoba", "Bukoba Rural", "Karagwe", "Kyerwa", "Missenyi", "Muleba", "Ngara"]},
            "Katavi": {"coords": {"lat": -6.3667, "lon": 31.1333}, "districts": ["Mlele", "Mpanda", "Nsimbo"]},
            "Kigoma": {"coords": {"lat": -4.8833, "lon": 29.6333}, "districts": ["Buhigwe", "Kakonko", "Kasulu", "Kibondo", "Kigoma", "Kigoma Rural", "Uvinza"]},
            "Kilimanjaro": {"coords": {"lat": -3.3500, "lon": 37.3500}, "districts": ["Hai", "Moshi", "Moshi Rural", "Mwanga", "Rombo", "Same", "Siha"]},
            "Lindi": {"coords": {"lat": -9.9934, "lon": 39.7151}, "districts": ["Kilwa", "Lindi", "Lindi Rural", "Liwale", "Nachingwea", "Ruangwa"]},
            "Manyara": {"coords": {"lat": -4.3167, "lon": 36.9500}, "districts": ["Babati", "Babati Rural", "Hanang", "Kiteto", "Mbulu", "Simanjiro"]},
            "Mara": {"coords": {"lat": -1.7500, "lon": 34.1667}, "districts": ["Bunda", "Butiama", "Musoma", "Musoma Rural", "Rorya", "Serengeti", "Tarime"]},
            "Mbeya": {"coords": {"lat": -8.9000, "lon": 33.4500}, "districts": ["Busokelo", "Chunya", "Kyela", "Mbarali", "Mbeya City", "Mbeya Rural", "Rungwe"]},
            "Morogoro": {"coords": {"lat": -6.8167, "lon": 37.6667}, "districts": ["Gairo", "Ifakara", "Kilombero", "Kilosa", "Malinyi", "Morogoro", "Morogoro Rural", "Mvomero", "Ulanga"]},
            "Mtwara": {"coords": {"lat": -10.2667, "lon": 40.1833}, "districts": ["Masasi", "Mtwara", "Mtwara Rural", "Nanyumbu", "Newala", "Tandahimba"]},
            "Mwanza": {"coords": {"lat": -2.5167, "lon": 32.9000}, "districts": ["Ilemela", "Kwimba", "Magu", "Misungwi", "Nyamagana", "Sengerema", "Ukerewe"]},
            "Njombe": {"coords": {"lat": -9.3333, "lon": 34.7667}, "districts": ["Ludewa", "Makete", "Njombe", "Njombe Rural", "Wanging'ombe"]},
            "Pwani": {"coords": {"lat": -7.0000, "lon": 38.8333}, "districts": ["Bagamoyo", "Kibiti", "Kilwa", "Kisarawe", "Mafia", "Mkuranga", "Rufiji"]},
            "Rukwa": {"coords": {"lat": -7.9333, "lon": 31.4500}, "districts": ["Kalambo", "Nkasi", "Sumbawanga", "Sumbawanga Rural"]},
            "Ruvuma": {"coords": {"lat": -10.6833, "lon": 36.0000}, "districts": ["Madaba", "Mbinga", "Namtumbo", "Nyasa", "Songea", "Songea Rural", "Tunduru"]},
            "Shinyanga": {"coords": {"lat": -3.6667, "lon": 33.4167}, "districts": ["Kahama", "Kishapu", "Shinyanga", "Shinyanga Rural"]},
            "Simiyu": {"coords": {"lat": -2.8500, "lon": 34.5000}, "districts": ["Bariadi", "Busega", "Itilima", "Maswa", "Meatu"]},
            "Singida": {"coords": {"lat": -5.7500, "lon": 34.7500}, "districts": ["Ikungi", "Iramba", "Manyoni", "Mkalama", "Singida", "Singida Rural"]},
            "Songwe": {"coords": {"lat": -9.0000, "lon": 32.5000}, "districts": ["Ileje", "Mbozi", "Momba", "Songwe"]},
            "Tabora": {"coords": {"lat": -5.0167, "lon": 32.8000}, "districts": ["Igunga", "Kaliua", "Nzega", "Sikonge", "Tabora", "Urambo", "Uyui"]},
            "Tanga": {"coords": {"lat": -5.0667, "lon": 39.1000}, "districts": ["Handeni", "Kilindi", "Korogwe", "Lushoto", "Mkinga", "Muheza", "Pangani", "Tanga City"]},
            "Zanzibar Nord": {"coords": {"lat": -5.7667, "lon": 39.3833}, "districts": ["Kaskazini A", "Kaskazini B"]},
            "Zanzibar Sud et Centre": {"coords": {"lat": -6.1667, "lon": 39.2000}, "districts": ["Kati", "Kusini"]},
            "Zanzibar Ouest": {"coords": {"lat": -6.1500, "lon": 39.1833}, "districts": ["Magharibi A", "Magharibi B", "Mjini"]},
            "Pemba Nord": {"coords": {"lat": -5.0333, "lon": 39.7500}, "districts": ["Micheweni", "Wete"]},
            "Pemba Sud": {"coords": {"lat": -5.3500, "lon": 39.7500}, "districts": ["Chake-Chake", "Mkoani"]}
        }

        for region_name, info in tz_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=tz_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=tz_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=tz_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Tanzanie : OK")

        # ================================================================
        # OUGANDA (ID: 800)
        # ================================================================
        print("\n--- Initialisation de l'Ouganda (ID: 800) ---")
        ug_id = 800
        ug = Country.query.get(ug_id)
        if not ug:
            ug = Country(id=ug_id, name="Ouganda", iso_code="UG")
            db.session.add(ug)
            db.session.commit()
            print("Pays Ouganda créé.")

        ug_data = {
            "Kampala": {"coords": {"lat": 0.3476, "lon": 32.5825}, "districts": ["Kampala Central", "Kawempe", "Makindye", "Nakawa", "Rubaga"]},
            "Centrale": {"coords": {"lat": 0.2500, "lon": 32.0000}, "districts": ["Buikwe", "Bukomansimbi", "Butebo", "Buvuma", "Gomba", "Kalangala", "Kalungu", "Kayunga", "Kiboga", "Kyankwanzi", "Luweero", "Lwengo", "Lyantonde", "Masaka", "Mityana", "Mpigi", "Mubende", "Mukono", "Nakaseke", "Nakasongola", "Rakai", "Sembabule", "Wakiso"]},
            "Est": {"coords": {"lat": 1.2000, "lon": 34.0000}, "districts": ["Amuria", "Bukedea", "Bukwa", "Bulambuli", "Busia", "Butaleja", "Iganga", "Jinja", "Kaberamaido", "Kaliro", "Kamuli", "Kapchorwa", "Katakwi", "Kibuku", "Kumi", "Kween", "Luuka", "Manafwa", "Mayuge", "Mbale", "Namayingo", "Namisindwa", "Namutumba", "Ngora", "Pallisa", "Serere", "Sironko", "Soroti", "Tororo"]},
            "Nord": {"coords": {"lat": 2.5000, "lon": 32.5000}, "districts": ["Abim", "Adjumani", "Agago", "Alebtong", "Amolatar", "Amudat", "Amuru", "Apac", "Arua", "Dokolo", "Gulu", "Kitgum", "Koboko", "Kole", "Kotido", "Lamwo", "Lira", "Maracha", "Moroto", "Moyo", "Nakapiripirit", "Napak", "Nebbi", "Nwoya", "Otuke", "Oyam", "Pader", "Pakwach", "Yumbe", "Zombo"]},
            "Ouest": {"coords": {"lat": 0.5000, "lon": 30.0000}, "districts": ["Buliisa", "Bundibugyo", "Bwamba", "Hoima", "Ibanda", "Isingiro", "Kabale", "Kabarole", "Kagadi", "Kakumiro", "Kamwenge", "Kanungu", "Kasese", "Kibaale", "Kiruhura", "Kiryandongo", "Kisoro", "Kyegegwa", "Kyenjojo", "Masindi", "Mbarara", "Mitooma", "Ntoroko", "Ntungamo", "Rubanda", "Rubirizi", "Rukiga", "Rukungiri", "Sheema"]}
        }

        for region_name, info in ug_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=ug_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=ug_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=ug_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Ouganda : OK")

        # ================================================================
        # SOUDAN DU SUD (ID: 728)
        # ================================================================
        print("\n--- Initialisation du Soudan du Sud (ID: 728) ---")
        ss_id = 728
        ss = Country.query.get(ss_id)
        if not ss:
            ss = Country(id=ss_id, name="Soudan du Sud", iso_code="SS")
            db.session.add(ss)
            db.session.commit()
            print("Pays Soudan du Sud créé.")

        ss_data = {
            "Jonglei": {"coords": {"lat": 7.0000, "lon": 32.0000}, "counties": ["Akobo", "Ayod", "Bor South", "Duk", "Fangak", "Nyirol", "Pibor", "Pochalla", "Twic East", "Uror"]},
            "Lakes": {"coords": {"lat": 6.5000, "lon": 30.0000}, "counties": ["Awerial", "Cueibet", "Gok", "Rumbek Centre", "Rumbek East", "Rumbek North", "Wulu", "Yirol East", "Yirol West"]},
            "Northern Bahr el Ghazal": {"coords": {"lat": 8.7833, "lon": 26.9667}, "counties": ["Aweil Centre", "Aweil East", "Aweil North", "Aweil South", "Aweil West"]},
            "Unity": {"coords": {"lat": 8.5000, "lon": 29.5000}, "counties": ["Abiemnhom", "Guit", "Koch", "Leer", "Mayendit", "Mayom", "Pariang", "Panyijar", "Rubkona"]},
            "Upper Nile": {"coords": {"lat": 9.5000, "lon": 32.5000}, "counties": ["Akoka", "Baliet", "Fashoda", "Longochuk", "Luakpiny", "Maban", "Malakal", "Manyo", "Maiwut", "Melut", "Nasir", "Panyikang", "Renk", "Ulang"]},
            "Warrap": {"coords": {"lat": 8.0000, "lon": 28.5000}, "counties": ["Gogrial East", "Gogrial West", "Kwajok", "Tonj East", "Tonj North", "Tonj South", "Twic"]},
            "Western Bahr el Ghazal": {"coords": {"lat": 8.0000, "lon": 25.5000}, "counties": ["Jur River", "Wau"]},
            "Western Equatoria": {"coords": {"lat": 5.0000, "lon": 28.5000}, "counties": ["Ezo", "Ibba", "Maridi", "Mundri East", "Mundri West", "Mvolo", "Nagero", "Nzara", "Tambura", "Yambio"]},
            "Central Equatoria": {"coords": {"lat": 4.5000, "lon": 31.5000}, "counties": ["Juba", "Kajo-Keji", "Lainya", "Morobo", "Rajaf", "Terekeka", "Yei"]},
            "Eastern Equatoria": {"coords": {"lat": 4.5000, "lon": 33.5000}, "counties": ["Budi", "Ikotos", "Kapoeta East", "Kapoeta North", "Kapoeta South", "Lafon", "Magwi", "Torit"]}
        }

        for state_name, info in ss_data.items():
            state = AdministrativeDivision.query.filter_by(
                name=state_name, level=1, country_id=ss_id
            ).first()
            if not state:
                state = AdministrativeDivision(
                    name=state_name, level=1, country_id=ss_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(state)
                db.session.flush()
                print(f"  -> État : {state_name}")

            for county_name in info["counties"]:
                county = AdministrativeDivision.query.filter_by(
                    name=county_name, level=2, parent_id=state.id
                ).first()
                if not county:
                    county = AdministrativeDivision(
                        name=county_name, level=2, country_id=ss_id, parent_id=state.id
                    )
                    db.session.add(county)

        db.session.commit()
        print("Soudan du Sud : OK")

        # ================================================================
        # SOUDAN (ID: 729)
        # ================================================================
        print("\n--- Initialisation du Soudan (ID: 729) ---")
        sd_id = 729
        sd = Country.query.get(sd_id)
        if not sd:
            sd = Country(id=sd_id, name="Soudan", iso_code="SD")
            db.session.add(sd)
            db.session.commit()
            print("Pays Soudan créé.")

        sd_data = {
            "Khartoum": {"coords": {"lat": 15.5007, "lon": 32.5599}, "localities": ["Khartoum", "Omdurman", "Khartoum North", "Karari", "Jebel Aulia", "Bahri"]},
            "Gezira": {"coords": {"lat": 14.9082, "lon": 33.0893}, "localities": ["Wad Madani", "Al Managil", "Hasaheisa", "Al Kamlin", "Al Qurshi"]},
            "Kassala": {"coords": {"lat": 15.4517, "lon": 36.4003}, "localities": ["Kassala", "Wad Al Hileau", "Telkov", "Hamashkoreib"]},
            "Al Qadarif": {"coords": {"lat": 14.0404, "lon": 35.3618}, "localities": ["Al Qadarif", "Al Fashir", "Hawata", "Al Rahad"]},
            "Al Jazirah": {"coords": {"lat": 14.3667, "lon": 33.5000}, "localities": ["Rufa'a", "Al Hasahisa", "Al Managil", "Um Al Qura"]},
            "Sennar": {"coords": {"lat": 13.5530, "lon": 33.6188}, "localities": ["Sennar", "Sinja", "Al Damazin", "Al Suki"]},
            "Al Nil Al Azraq": {"coords": {"lat": 13.1489, "lon": 34.3976}, "localities": ["Al Damazin", "Kurmuk", "Bau", "Roseires"]},
            "Al Nil Al Abyad": {"coords": {"lat": 13.1667, "lon": 32.5000}, "localities": ["Kosti", "Rabak", "Al Duweim", "Tendelti"]},
            "Ash Shamaliyah": {"coords": {"lat": 18.0000, "lon": 30.0000}, "localities": ["Dongola", "Al Dabbah", "Kareima", "Wadi Halfa", "Abu Hamed"]},
            "Nahr Al Nil": {"coords": {"lat": 17.5000, "lon": 33.9167}, "localities": ["Atbara", "Shendi", "Berber", "Al Matamma"]},
            "Al Bahr Al Ahmar": {"coords": {"lat": 21.0000, "lon": 37.0000}, "localities": ["Port Sudan", "Suakin", "Halaib", "Tokar"]},
            "Al Jabal Al Awsat": {"coords": {"lat": 11.5000, "lon": 29.5000}, "localities": ["Kadugli", "Al Buram", "El Tadamon", "Al Azrak"]},
            "South Kordofan": {"coords": {"lat": 11.0000, "lon": 29.5000}, "localities": ["Kadugli", "Dilling", "Al Rashad", "Um Ruwaba"]},
            "North Kordofan": {"coords": {"lat": 13.5000, "lon": 29.0000}, "localities": ["El Obeid", "Al Nahud", "Bara", "Umm Rawaba"]},
            "West Kordofan": {"coords": {"lat": 12.0000, "lon": 27.5000}, "localities": ["Al Fula", "Abu Zabad", "Al Nahud"]},
            "North Darfur": {"coords": {"lat": 16.0000, "lon": 25.0000}, "localities": ["El Fasher", "Kutum", "Kebkabiyah", "Mellit", "Tine"]},
            "South Darfur": {"coords": {"lat": 11.5000, "lon": 25.0000}, "localities": ["Nyala", "Ed Daein", "Buram", "Tulus", "Adila"]},
            "West Darfur": {"coords": {"lat": 13.0000, "lon": 22.5000}, "localities": ["Al Geneina", "Kulbus", "Serif Omra", "Silea"]},
            "Central Darfur": {"coords": {"lat": 13.5000, "lon": 23.5000}, "localities": ["Zalingei", "Bindisi", "Rokero", "Nertiti"]},
            "East Darfur": {"coords": {"lat": 12.0000, "lon": 26.5000}, "localities": ["Ed Daein", "Abu Karinka", "Adila", "Al Sunta"]}
        }

        for state_name, info in sd_data.items():
            state = AdministrativeDivision.query.filter_by(
                name=state_name, level=1, country_id=sd_id
            ).first()
            if not state:
                state = AdministrativeDivision(
                    name=state_name, level=1, country_id=sd_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(state)
                db.session.flush()
                print(f"  -> État : {state_name}")

            for locality_name in info["localities"]:
                locality = AdministrativeDivision.query.filter_by(
                    name=locality_name, level=2, parent_id=state.id
                ).first()
                if not locality:
                    locality = AdministrativeDivision(
                        name=locality_name, level=2, country_id=sd_id, parent_id=state.id
                    )
                    db.session.add(locality)

        db.session.commit()
        print("Soudan : OK")

        # ================================================================
        # COMORES (ID: 174)
        # ================================================================
        print("\n--- Initialisation des Comores (ID: 174) ---")
        km_id = 174
        km = Country.query.get(km_id)
        if not km:
            km = Country(id=km_id, name="Comores", iso_code="KM")
            db.session.add(km)
            db.session.commit()
            print("Pays Comores créé.")

        km_data = {
            "Grande Comore (Ngazidja)": {
                "coords": {"lat": -11.7004, "lon": 43.3550},
                "prefectures": ["Moroni", "Badjini Est", "Badjini Ouest", "Bambao", "Dimani",
                                "Hamahame", "Hamahamet", "Itsandra", "Mbude", "Mbadjini Ouest",
                                "Oichili", "Outer", "Hamahamet"]
            },
            "Anjouan (Ndzuwani)": {
                "coords": {"lat": -12.2167, "lon": 44.4333},
                "prefectures": ["Mutsamudu", "Domoni", "Ouani", "Sima", "Mrémani",
                                "Tsembehou", "Bandrani-Bimbini"]
            },
            "Mohéli (Mwali)": {
                "coords": {"lat": -12.3333, "lon": 43.7333},
                "prefectures": ["Fomboni", "Djando", "Nioumachoua", "Ouallah"]
            }
        }

        for island_name, info in km_data.items():
            island = AdministrativeDivision.query.filter_by(
                name=island_name, level=1, country_id=km_id
            ).first()
            if not island:
                island = AdministrativeDivision(
                    name=island_name, level=1, country_id=km_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(island)
                db.session.flush()
                print(f"  -> Île : {island_name}")

            for pref_name in info["prefectures"]:
                pref = AdministrativeDivision.query.filter_by(
                    name=pref_name, level=2, parent_id=island.id
                ).first()
                if not pref:
                    pref = AdministrativeDivision(
                        name=pref_name, level=2, country_id=km_id, parent_id=island.id
                    )
                    db.session.add(pref)

        db.session.commit()
        print("Comores : OK")

        # ================================================================
        # MADAGASCAR (ID: 450)
        # ================================================================
        print("\n--- Initialisation de Madagascar (ID: 450) ---")
        mg_id = 450
        mg = Country.query.get(mg_id)
        if not mg:
            mg = Country(id=mg_id, name="Madagascar", iso_code="MG")
            db.session.add(mg)
            db.session.commit()
            print("Pays Madagascar créé.")

        mg_data = {
            "Analamanga": {"coords": {"lat": -18.9137, "lon": 47.5361}, "districts": ["Ambohidratrimo", "Andramasina", "Anjozorobe", "Ankazobe", "Antananarivo-Avaradrano", "Antananarivo-Atsimondrano", "Antananarivo-Renivohitra", "Manjakandriana"]},
            "Vakinankaratra": {"coords": {"lat": -19.8667, "lon": 46.8333}, "districts": ["Ambatolampy", "Antanifotsy", "Antsirabe I", "Antsirabe II", "Betafo", "Faratsiho", "Mandoto"]},
            "Itasy": {"coords": {"lat": -19.0833, "lon": 46.6167}, "districts": ["Arivonimamo", "Miarinarivo", "Soavinandriana"]},
            "Bongolava": {"coords": {"lat": -18.3333, "lon": 45.5000}, "districts": ["Fenoarivobe", "Tsiroanomandidy"]},
            "Haute Matsiatra": {"coords": {"lat": -21.4500, "lon": 47.0833}, "districts": ["Ambalavao", "Ambohimahasoa", "Fianarantsoa I", "Fianarantsoa II", "Ikalamavony", "Isandra", "Lalangina", "Vohibato"]},
            "Amoron'i Mania": {"coords": {"lat": -20.5000, "lon": 46.5000}, "districts": ["Ambatofinandrahana", "Ambositra", "Fandriana", "Manandriana"]},
            "Vatovavy": {"coords": {"lat": -21.5000, "lon": 48.1667}, "districts": ["Ifanadiana", "Ikongo", "Mananjary", "Nosy Varika"]},
            "Fitovinany": {"coords": {"lat": -22.5000, "lon": 47.7500}, "districts": ["Ivohibe", "Midongy Atsimo", "Vangaindrano", "Vondrozo"]},
            "Atsimo-Atsinanana": {"coords": {"lat": -23.3500, "lon": 47.6000}, "districts": ["Befotaka", "Farafangana", "Midongy du Sud", "Vangaindrano"]},
            "Atsinanana": {"coords": {"lat": -18.1667, "lon": 49.3833}, "districts": ["Brickaville", "Fénerive Est", "Mahanoro", "Marolambo", "Toamasina I", "Toamasina II", "Vatomandry"]},
            "Analanjirofo": {"coords": {"lat": -16.5833, "lon": 49.5000}, "districts": ["Fenoarivo Atsinanana", "Mananara Avaratra", "Maroantsetra", "Nosy Boraha", "Soanierana Ivongo", "Vavatenina"]},
            "Alaotra-Mangoro": {"coords": {"lat": -17.5500, "lon": 48.5000}, "districts": ["Ambatondrazaka", "Amparafaravola", "Andilamena", "Anosibe An'Ala", "Moramanga"]},
            "Boeny": {"coords": {"lat": -16.1167, "lon": 46.7000}, "districts": ["Ambato-Boeny", "Keliloha", "Mahajanga I", "Mahajanga II", "Marovoay", "Mitsinjo"]},
            "Sofia": {"coords": {"lat": -14.7667, "lon": 47.5000}, "districts": ["Analalava", "Befandriana Avaratra", "Befandriana-Avaratra", "Kandreho", "Mampikony", "Mandritsara", "Port-Bergé", "Tsaratanana"]},
            "Betsiboka": {"coords": {"lat": -17.0000, "lon": 46.5000}, "districts": ["Kandreho", "Maevatanana", "Tsaratanana"]},
            "Melaky": {"coords": {"lat": -17.0000, "lon": 44.5000}, "districts": ["Antsalova", "Besalampy", "Maintirano", "Mitsinjo", "Morafenobe"]},
            "Atsimo-Andrefana": {"coords": {"lat": -23.3500, "lon": 43.6667}, "districts": ["Ampanihy", "Ankazoabo", "Benenitra", "Beroroha", "Betioky Atsimo", "Morombe", "Sakaraha", "Toliara I", "Toliara II"]},
            "Androy": {"coords": {"lat": -25.0333, "lon": 45.5000}, "districts": ["Ambovombe-Androy", "Bekily", "Beloha", "Tsihombe"]},
            "Anosy": {"coords": {"lat": -24.5000, "lon": 46.8833}, "districts": ["Amboasary-Atsimo", "Betroka", "Taolagnaro"]},
            "Ihorombe": {"coords": {"lat": -22.8333, "lon": 45.8333}, "districts": ["Iakora", "Ihosy", "Ivohibe"]},
            "SAVA": {"coords": {"lat": -14.3000, "lon": 49.9500}, "districts": ["Andapa", "Antalaha", "Sambava", "Vohimarina"]},
            "Diana": {"coords": {"lat": -12.3500, "lon": 49.2833}, "districts": ["Ambanja", "Ambilobe", "Antsiranana I", "Antsiranana II", "Nosy Be"]}
        }

        for region_name, info in mg_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=mg_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=mg_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=region.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=mg_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Madagascar : OK")

        # ================================================================
        # MAURICE (ID: 480)
        # ================================================================
        print("\n--- Initialisation de Maurice (ID: 480) ---")
        mu_id = 480
        mu = Country.query.get(mu_id)
        if not mu:
            mu = Country(id=mu_id, name="Maurice", iso_code="MU")
            db.session.add(mu)
            db.session.commit()
            print("Pays Maurice créé.")

        mu_data = {
            "Black River": {"coords": {"lat": -20.3500, "lon": 57.3833}, "villages": ["Bambous", "Cascavelle", "Flic en Flac", "Grande Rivière Noire", "La Gaulette", "Le Morne", "Rivière Noire", "Tamarin"]},
            "Flacq": {"coords": {"lat": -20.2167, "lon": 57.7167}, "villages": ["Bel Air", "Central Flacq", "Clémencia", "Ecroignard", "La Réunion", "Lalmatie", "Poste Lafayette", "Quatre Cocos", "Queen Victoria", "Saint Julien", "Sebastopol"]},
            "Grand Port": {"coords": {"lat": -20.3833, "lon": 57.6833}, "villages": ["Bambous Virieux", "Beau Vallon", "Calebasses", "Camp Diable", "Mahébourg", "New Grove", "Rivière des Anguilles", "Rivière du Poste"]},
            "Moka": {"coords": {"lat": -20.2333, "lon": 57.5833}, "villages": ["Moka", "Quartier Militaire", "Roches Brunes", "Saint Pierre", "Sébastopol", "Verdun"]},
            "Pamplemousses": {"coords": {"lat": -20.1000, "lon": 57.5667}, "villages": ["Mapou", "Pamplemousses", "Piton", "Triolet", "Terre Rouge"]},
            "Plaines Wilhems": {"coords": {"lat": -20.2667, "lon": 57.5000}, "villages": ["Beau Bassin", "Curepipe", "Quatre Bornes", "Rose Hill", "Vacoas-Phoenix"]},
            "Port Louis": {"coords": {"lat": -20.1644, "lon": 57.4990}, "villages": ["Port Louis Centre", "Bois Marchands", "Cassis", "Montagne Longue", "Roche Bois", "Vallée des Prêtres"]},
            "Rivière du Rempart": {"coords": {"lat": -20.0833, "lon": 57.6667}, "villages": ["Amaury", "Cap Malheureux", "Goodlands", "Grand Baie", "Péreybère", "Rivière du Rempart"]},
            "Savanne": {"coords": {"lat": -20.4667, "lon": 57.5000}, "villages": ["Chemin Grenier", "Rivière des Anguilles", "Souillac", "Surinam"]},
            "Rodrigues": {"coords": {"lat": -19.7167, "lon": 63.4167}, "villages": ["Port Mathurin", "La Ferme", "Rodrigues Rural"]},
            "Agalega": {"coords": {"lat": -10.4167, "lon": 56.6167}, "villages": ["North Agalega", "South Agalega"]}
        }

        for district_name, info in mu_data.items():
            district = AdministrativeDivision.query.filter_by(
                name=district_name, level=1, country_id=mu_id
            ).first()
            if not district:
                district = AdministrativeDivision(
                    name=district_name, level=1, country_id=mu_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(district)
                db.session.flush()
                print(f"  -> District : {district_name}")

            for village_name in info["villages"]:
                village = AdministrativeDivision.query.filter_by(
                    name=village_name, level=2, parent_id=district.id
                ).first()
                if not village:
                    village = AdministrativeDivision(
                        name=village_name, level=2, country_id=mu_id, parent_id=district.id
                    )
                    db.session.add(village)

        db.session.commit()
        print("Maurice : OK")

        # ================================================================
        # SEYCHELLES (ID: 690)
        # ================================================================
        print("\n--- Initialisation des Seychelles (ID: 690) ---")
        sc_id = 690
        sc = Country.query.get(sc_id)
        if not sc:
            sc = Country(id=sc_id, name="Seychelles", iso_code="SC")
            db.session.add(sc)
            db.session.commit()
            print("Pays Seychelles créé.")

        sc_data = {
            "Mahé": {
                "coords": {"lat": -4.6796, "lon": 55.4920},
                "districts": ["Beau Vallon", "Bel Air", "Bel Ombre", "Cascade", "English River",
                              "Glacis", "Grand Anse Mahé", "Les Mamelles", "Mont Buxton",
                              "Mont Fleuri", "Plaisance", "Pointe Larue", "Port Glaud",
                              "Roche Caiman", "Saint Louis", "Takamaka", "Au Cap", "Baie Lazare",
                              "Baie Sainte Anne", "Beau Vallon", "Bel Ombre"]
            },
            "Praslin": {
                "coords": {"lat": -4.3167, "lon": 55.7333},
                "districts": ["Baie Sainte Anne", "Grand Anse Praslin"]
            },
            "La Digue": {
                "coords": {"lat": -4.3667, "lon": 55.8333},
                "districts": ["La Digue"]
            },
            "Îles Éloignées": {
                "coords": {"lat": -9.5000, "lon": 46.5000},
                "districts": ["Aldabra", "Alphonse", "Bijoutier", "Cosmoledo", "Desroches",
                              "Farquhar", "Platte", "Poivre", "Providence"]
            }
        }

        for island_name, info in sc_data.items():
            island = AdministrativeDivision.query.filter_by(
                name=island_name, level=1, country_id=sc_id
            ).first()
            if not island:
                island = AdministrativeDivision(
                    name=island_name, level=1, country_id=sc_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(island)
                db.session.flush()
                print(f"  -> Île : {island_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=island.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=sc_id, parent_id=island.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Seychelles : OK")

        # ================================================================
        # RÉSUMÉ FINAL
        # ================================================================
        print("\n" + "="*58)
        print("Succès : Toutes les données d'Afrique de l'Est sont à jour !")
        print("  - Éthiopie          (ID: 231) : 13 régions")
        print("  - Érythrée          (ID: 232) :  6 régions")
        print("  - Djibouti          (ID: 262) :  6 régions")
        print("  - Somalie           (ID: 706) : 18 régions")
        print("  - Kenya             (ID: 404) : 47 comtés")
        print("  - Tanzanie          (ID: 834) : 31 régions")
        print("  - Ouganda           (ID: 800) :  5 régions")
        print("  - Soudan du Sud     (ID: 728) : 10 états")
        print("  - Soudan            (ID: 729) : 20 états")
        print("  - Comores           (ID: 174) :  3 îles")
        print("  - Madagascar        (ID: 450) : 22 régions")
        print("  - Maurice           (ID: 480) : 11 districts")
        print("  - Seychelles        (ID: 690) :  4 groupes d'îles")
        print("="*58)

if __name__ == "__main__":
    seed_data()