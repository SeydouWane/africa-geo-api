import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():

        # ================================================================
        # CAMEROUN (ID: 120)
        # ================================================================
        print("\n--- Initialisation du Cameroun (ID: 120) ---")
        cm_id = 120
        cm = Country.query.get(cm_id)
        if not cm:
            cm = Country(id=cm_id, name="Cameroun", iso_code="CM")
            db.session.add(cm)
            db.session.commit()
            print("Pays Cameroun créé.")

        cm_data = {
            "Adamaoua": {
                "coords": {"lat": 7.3167, "lon": 13.5833},
                "departments": ["Djérem", "Faro-et-Déo", "Mayo-Banyo", "Mbéré", "Vina"]
            },
            "Centre": {
                "coords": {"lat": 3.8667, "lon": 11.5167},
                "departments": ["Haute-Sanaga", "Lékié", "Mbam-et-Inoubou", "Mbam-et-Kim", "Méfou-et-Afamba", "Méfou-et-Akono", "Mfoundi", "Nyong-et-Kellé", "Nyong-et-Mfoumou", "Nyong-et-So'o"]
            },
            "Est": {
                "coords": {"lat": 4.0000, "lon": 14.0000},
                "departments": ["Boumba-et-Ngoko", "Haut-Nyong", "Kadey", "Lom-et-Djérem"]
            },
            "Extrême-Nord": {
                "coords": {"lat": 11.0000, "lon": 14.5000},
                "departments": ["Diamaré", "Logone-et-Chari", "Mayo-Danay", "Mayo-Kani", "Mayo-Sava", "Mayo-Tsanaga"]
            },
            "Littoral": {
                "coords": {"lat": 4.0500, "lon": 9.7000},
                "departments": ["Moungo", "Nkam", "Sanaga-Maritime", "Wouri"]
            },
            "Nord": {
                "coords": {"lat": 8.5000, "lon": 14.0000},
                "departments": ["Bénoué", "Faro", "Mayo-Louti", "Mayo-Rey"]
            },
            "Nord-Ouest": {
                "coords": {"lat": 6.2000, "lon": 10.3000},
                "departments": ["Boyo", "Bui", "Donga-Mantung", "Menchum", "Mezam", "Momo", "Ngo-Ketunjia"]
            },
            "Ouest": {
                "coords": {"lat": 5.5333, "lon": 10.4000},
                "departments": ["Bamboutos", "Haut-Nkam", "Hauts-Plateaux", "Koupé-Manengouba", "Menoua", "Mifi", "Ndé", "Noun"]
            },
            "Sud": {
                "coords": {"lat": 2.9000, "lon": 11.5000},
                "departments": ["Dja-et-Lobo", "Mvila", "Océan", "Vallée-du-Ntem"]
            },
            "Sud-Ouest": {
                "coords": {"lat": 4.5667, "lon": 9.4000},
                "departments": ["Fako", "Koupé-Manengouba", "Lebialem", "Manyu", "Meme", "Ndian"]
            }
        }

        for region_name, info in cm_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=cm_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=cm_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for dept_name in info["departments"]:
                dept = AdministrativeDivision.query.filter_by(
                    name=dept_name, level=2, parent_id=region.id
                ).first()
                if not dept:
                    dept = AdministrativeDivision(
                        name=dept_name, level=2, country_id=cm_id, parent_id=region.id
                    )
                    db.session.add(dept)

        db.session.commit()
        print("Cameroun : OK")

        # ================================================================
        # RÉPUBLIQUE CENTRAFRICAINE (ID: 140)
        # ================================================================
        print("\n--- Initialisation de la RCA (ID: 140) ---")
        cf_id = 140
        cf = Country.query.get(cf_id)
        if not cf:
            cf = Country(id=cf_id, name="République Centrafricaine", iso_code="CF")
            db.session.add(cf)
            db.session.commit()
            print("Pays RCA créé.")

        cf_data = {
            "Bangui": {
                "coords": {"lat": 4.3612, "lon": 18.5550},
                "prefectures": ["Bangui 1er", "Bangui 2ème", "Bangui 3ème", "Bangui 4ème", "Bangui 5ème", "Bangui 6ème", "Bangui 7ème", "Bangui 8ème"]
            },
            "Bamingui-Bangoran": {
                "coords": {"lat": 8.5000, "lon": 20.5000},
                "prefectures": ["Bamingui", "Bangoran", "Ndélé"]
            },
            "Bangassou": {
                "coords": {"lat": 4.7333, "lon": 22.8167},
                "prefectures": ["Bangassou", "Rafaï", "Zemio"]
            },
            "Basse-Kotto": {
                "coords": {"lat": 4.6167, "lon": 21.6500},
                "prefectures": ["Alindao", "Kemo-Gribingui", "Mingala", "Mobaye"]
            },
            "Haute-Kotto": {
                "coords": {"lat": 7.0000, "lon": 23.5000},
                "prefectures": ["Bria", "Ouadda", "Yalinga"]
            },
            "Haut-Mbomou": {
                "coords": {"lat": 5.5000, "lon": 25.5000},
                "prefectures": ["Obo", "Zémio"]
            },
            "Kémo": {
                "coords": {"lat": 5.8833, "lon": 19.2000},
                "prefectures": ["Dékoa", "Sibut"]
            },
            "Lobaye": {
                "coords": {"lat": 3.7667, "lon": 17.4333},
                "prefectures": ["Boda", "M'Baïki", "Mbaïki", "Mongoumba"]
            },
            "Mambéré-Kadéï": {
                "coords": {"lat": 4.3667, "lon": 15.5833},
                "prefectures": ["Berberati", "Carnot", "Gamboula"]
            },
            "Mbomou": {
                "coords": {"lat": 5.1500, "lon": 24.0000},
                "prefectures": ["Bangassou", "Gambo", "Mobaye"]
            },
            "Nana-Grébizi": {
                "coords": {"lat": 6.9833, "lon": 18.8167},
                "prefectures": ["Kaga-Bandoro", "Mbrès"]
            },
            "Nana-Mambéré": {
                "coords": {"lat": 5.7000, "lon": 15.8333},
                "prefectures": ["Baboua", "Baoro", "Bouar"]
            },
            "Ombella-M'Poko": {
                "coords": {"lat": 4.9167, "lon": 18.0000},
                "prefectures": ["Bimbo", "Boali", "Damara", "Yaloké"]
            },
            "Ouaka": {
                "coords": {"lat": 5.9000, "lon": 20.4167},
                "prefectures": ["Bambari", "Grimari", "Ippy", "Kouango"]
            },
            "Ouham": {
                "coords": {"lat": 7.0000, "lon": 17.5000},
                "prefectures": ["Batangafo", "Bossangoa", "Bouca", "Kabo"]
            },
            "Ouham-Pendé": {
                "coords": {"lat": 6.3667, "lon": 16.0000},
                "prefectures": ["Bozoum", "Bocaranga", "Paoua"]
            },
            "Sangha-Mbaéré": {
                "coords": {"lat": 2.9500, "lon": 16.2500},
                "prefectures": ["Bayanga", "Nola"]
            },
            "Vakaga": {
                "coords": {"lat": 10.0000, "lon": 22.5000},
                "prefectures": ["Birao", "Gordil", "Ouanda-Djallé"]
            }
        }

        for prefecture_name, info in cf_data.items():
            prefecture = AdministrativeDivision.query.filter_by(
                name=prefecture_name, level=1, country_id=cf_id
            ).first()
            if not prefecture:
                prefecture = AdministrativeDivision(
                    name=prefecture_name, level=1, country_id=cf_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(prefecture)
                db.session.flush()
                print(f"  -> Préfecture : {prefecture_name}")

            for sous_pref_name in info["prefectures"]:
                sous_pref = AdministrativeDivision.query.filter_by(
                    name=sous_pref_name, level=2, parent_id=prefecture.id
                ).first()
                if not sous_pref:
                    sous_pref = AdministrativeDivision(
                        name=sous_pref_name, level=2, country_id=cf_id, parent_id=prefecture.id
                    )
                    db.session.add(sous_pref)

        db.session.commit()
        print("République Centrafricaine : OK")

        # ================================================================
        # TCHAD (ID: 148)
        # ================================================================
        print("\n--- Initialisation du Tchad (ID: 148) ---")
        td_id = 148
        td = Country.query.get(td_id)
        if not td:
            td = Country(id=td_id, name="Tchad", iso_code="TD")
            db.session.add(td)
            db.session.commit()
            print("Pays Tchad créé.")

        td_data = {
            "N'Djamena": {
                "coords": {"lat": 12.1048, "lon": 15.0445},
                "departments": ["N'Djamena 1er", "N'Djamena 2ème", "N'Djamena 3ème", "N'Djamena 4ème", "N'Djamena 5ème", "N'Djamena 6ème", "N'Djamena 7ème", "N'Djamena 8ème", "N'Djamena 9ème", "N'Djamena 10ème"]
            },
            "Batha": {
                "coords": {"lat": 13.8500, "lon": 18.3500},
                "departments": ["Batha Est", "Batha Ouest", "Fitri"]
            },
            "Borkou": {
                "coords": {"lat": 17.8500, "lon": 18.5167},
                "departments": ["Borkou", "Borkou-Ennedi-Tibesti"]
            },
            "Chari-Baguirmi": {
                "coords": {"lat": 11.7500, "lon": 15.7500},
                "departments": ["Baguirmi", "Chari", "Loug Chari"]
            },
            "Ennedi Est": {
                "coords": {"lat": 16.0000, "lon": 23.0000},
                "departments": ["Ennedi", "Mortcha"]
            },
            "Ennedi Ouest": {
                "coords": {"lat": 17.0000, "lon": 21.0000},
                "departments": ["Ennedi Ouest"]
            },
            "Guéra": {
                "coords": {"lat": 11.5000, "lon": 18.5000},
                "departments": ["Abtouyour", "Barh Signaka", "Guéra", "NDam"]
            },
            "Hadjer-Lamis": {
                "coords": {"lat": 13.0000, "lon": 15.0000},
                "departments": ["Dababa", "Haraze Al Biar", "Kabia"]
            },
            "Kanem": {
                "coords": {"lat": 14.5000, "lon": 15.5000},
                "departments": ["Kanem", "Mao", "Wayi"]
            },
            "Lac": {
                "coords": {"lat": 13.5000, "lon": 14.0000},
                "departments": ["Fouli", "Kaya", "Mamdi"]
            },
            "Logone Occidental": {
                "coords": {"lat": 8.5833, "lon": 16.0500},
                "departments": ["La Nya", "La Nya Pende", "Lac Wey", "Ngourkosso"]
            },
            "Logone Oriental": {
                "coords": {"lat": 8.0000, "lon": 16.5000},
                "departments": ["La Pendé", "Monts de Lam", "Nye", "Nye Pende"]
            },
            "Mandoul": {
                "coords": {"lat": 8.6000, "lon": 17.5000},
                "departments": ["Barh Sara", "Mandoul Est", "Mandoul Occidental"]
            },
            "Mayo-Kebbi Est": {
                "coords": {"lat": 9.8333, "lon": 14.8333},
                "departments": ["Kabia", "Lac Léré", "Mont Illi"]
            },
            "Mayo-Kebbi Ouest": {
                "coords": {"lat": 10.3333, "lon": 15.7500},
                "departments": ["Lac Léré", "Mayo Binder", "Mayo Dallah"]
            },
            "Moyen-Chari": {
                "coords": {"lat": 9.1667, "lon": 18.5000},
                "departments": ["Barh Köh", "Grande Sido", "Lac Iro"]
            },
            "Ouaddaï": {
                "coords": {"lat": 13.5000, "lon": 21.5000},
                "departments": ["Abdi", "Assoungha", "Ouara"]
            },
            "Salamat": {
                "coords": {"lat": 10.5000, "lon": 20.5000},
                "departments": ["Abou Deïa", "Barh Azoum", "Haraze Mangueigne"]
            },
            "Sila": {
                "coords": {"lat": 12.5000, "lon": 21.5000},
                "departments": ["Adila", "Kimiti", "Sila"]
            },
            "Tandjilé": {
                "coords": {"lat": 9.0000, "lon": 16.5000},
                "departments": ["Tandjilé Est", "Tandjilé Ouest"]
            },
            "Tibesti": {
                "coords": {"lat": 21.0000, "lon": 17.5000},
                "departments": ["Tibesti Est", "Tibesti Ouest"]
            },
            "Wadi Fira": {
                "coords": {"lat": 15.0000, "lon": 22.0000},
                "departments": ["Biltine", "Dar Tama", "Kobé"]
            }
        }

        for province_name, info in td_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=td_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=td_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for dept_name in info["departments"]:
                dept = AdministrativeDivision.query.filter_by(
                    name=dept_name, level=2, parent_id=province.id
                ).first()
                if not dept:
                    dept = AdministrativeDivision(
                        name=dept_name, level=2, country_id=td_id, parent_id=province.id
                    )
                    db.session.add(dept)

        db.session.commit()
        print("Tchad : OK")

        # ================================================================
        # RÉPUBLIQUE DU CONGO (ID: 178)
        # ================================================================
        print("\n--- Initialisation du Congo-Brazzaville (ID: 178) ---")
        cg_id = 178
        cg = Country.query.get(cg_id)
        if not cg:
            cg = Country(id=cg_id, name="République du Congo", iso_code="CG")
            db.session.add(cg)
            db.session.commit()
            print("Pays Congo-Brazzaville créé.")

        cg_data = {
            "Brazzaville": {
                "coords": {"lat": -4.2694, "lon": 15.2711},
                "districts": ["Bacongo", "Djiri", "Kintelé", "Lumumba", "Madibou", "Makélékélé", "Mfilou", "Moungali", "Ngaliema", "Poto-Poto", "Talangaï"]
            },
            "Pointe-Noire": {
                "coords": {"lat": -4.7761, "lon": 11.8635},
                "districts": ["Loandjili", "Lumumba", "Mongo-Mpoukou", "Mpita", "Ngoyo", "Tié-Tié"]
            },
            "Bouenza": {
                "coords": {"lat": -4.1167, "lon": 13.7333},
                "districts": ["Boko-Songho", "Kayes", "Kimongo", "Loudima", "Madingou", "Mfouati", "Mouyondzi", "Nkayi", "Tsiaki", "Yamba"]
            },
            "Cuvette": {
                "coords": {"lat": 0.0000, "lon": 16.0000},
                "districts": ["Boundji", "Ewo", "Kellé", "Loukolela", "Makoua", "Mossaka", "Oyo"]
            },
            "Cuvette-Ouest": {
                "coords": {"lat": 0.0000, "lon": 14.5000},
                "districts": ["Etoumbi", "Kelle", "Mbama", "Okoyo"]
            },
            "Kouilou": {
                "coords": {"lat": -4.0000, "lon": 11.8333},
                "districts": ["Hinda", "Kakamoeka", "Loango", "Madingo-Kayes", "Mvouti", "Nzambi", "Tchiamba-Nzassi"]
            },
            "Lékoumou": {
                "coords": {"lat": -3.0000, "lon": 13.5000},
                "districts": ["Bambama", "Komono", "Sibiti", "Zanaga"]
            },
            "Likouala": {
                "coords": {"lat": 2.0000, "lon": 17.5000},
                "districts": ["Bétou", "Dongou", "Epéna", "Impfondo", "Liranga", "Enyellé"]
            },
            "Niari": {
                "coords": {"lat": -3.2333, "lon": 12.3667},
                "districts": ["Divénié", "Kibangou", "Kimongo", "Londela-Kayes", "Loudima", "Makabana", "Moutamba", "Nyanga"]
            },
            "Plateaux": {
                "coords": {"lat": -1.5000, "lon": 15.5000},
                "districts": ["Abala", "Allembé", "Gamboma", "Lékana", "Makotipoko", "Mpama", "Ngo", "Ongogni"]
            },
            "Pool": {
                "coords": {"lat": -4.0000, "lon": 15.5000},
                "districts": ["Boko", "Goma Tsé-Tsé", "Ignié", "Kinkala", "Louingui", "Loumo", "Mayama", "Ngabe", "Vindza"]
            },
            "Sangha": {
                "coords": {"lat": 2.0000, "lon": 16.0000},
                "districts": ["Mokéko", "Ouesso", "Pikounda", "Sembé", "Souanké"]
            }
        }

        for dept_name, info in cg_data.items():
            dept = AdministrativeDivision.query.filter_by(
                name=dept_name, level=1, country_id=cg_id
            ).first()
            if not dept:
                dept = AdministrativeDivision(
                    name=dept_name, level=1, country_id=cg_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(dept)
                db.session.flush()
                print(f"  -> Département : {dept_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=dept.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=cg_id, parent_id=dept.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("République du Congo : OK")

        # ================================================================
        # RD CONGO (ID: 180)
        # ================================================================
        print("\n--- Initialisation de la RD Congo (ID: 180) ---")
        cd_id = 180
        cd = Country.query.get(cd_id)
        if not cd:
            cd = Country(id=cd_id, name="République Démocratique du Congo", iso_code="CD")
            db.session.add(cd)
            db.session.commit()
            print("Pays RD Congo créé.")

        cd_data = {
            "Kinshasa": {
                "coords": {"lat": -4.3276, "lon": 15.3136},
                "territories": ["Gombe", "Lingwala", "Barumbu", "Kinshasa", "Kintambo", "Bandalungwa", "Kalamu", "Lemba", "Makala", "Ngiri-Ngiri", "Selembao", "Bumbu", "Kisenso", "Maluku", "Masina", "Matete", "Mont-Ngafula", "Ndjili", "Ngaba", "Nsele", "Ngaliema", "Kasa-Vubu", "Limete", "Moulaert", "N'Sele"]
            },
            "Bas-Uélé": {
                "coords": {"lat": 3.5000, "lon": 24.5000},
                "territories": ["Aketi", "Ango", "Bambesa", "Bondo", "Buta", "Dingila", "Dongo", "Poko"]
            },
            "Équateur": {
                "coords": {"lat": 0.0000, "lon": 19.0000},
                "territories": ["Basankusu", "Befale", "Bikoro", "Bomongo", "Budjala", "Ingende", "Mbandaka", "Makanza", "Ntends"]
            },
            "Haut-Katanga": {
                "coords": {"lat": -10.5000, "lon": 27.5000},
                "territories": ["Kambove", "Kasenga", "Kipushi", "Likasi", "Lubumbashi", "Pweto"]
            },
            "Haut-Lomami": {
                "coords": {"lat": -7.5000, "lon": 26.5000},
                "territories": ["Bukama", "Kabalo", "Kamina", "Kaniama", "Malemba-Nkulu", "Mweneditu"]
            },
            "Haut-Uélé": {
                "coords": {"lat": 3.0000, "lon": 27.5000},
                "territories": ["Dungu", "Faradje", "Isiro", "Niangara", "Rungu", "Watsa", "Wamba"]
            },
            "Ituri": {
                "coords": {"lat": 1.5000, "lon": 29.5000},
                "territories": ["Aru", "Djugu", "Irumu", "Mambasa", "Mahagi"]
            },
            "Kasaï": {
                "coords": {"lat": -5.5000, "lon": 21.5000},
                "territories": ["Dekese", "Ilebo", "Luebo", "Mweka", "Tshikapa"]
            },
            "Kasaï Central": {
                "coords": {"lat": -5.9000, "lon": 22.4000},
                "territories": ["Dimbelenge", "Demba", "Kananga", "Luiza", "Kazumba"]
            },
            "Kasaï Oriental": {
                "coords": {"lat": -6.1333, "lon": 23.9833},
                "territories": ["Kabinda", "Kabeya-Kamwanga", "Katanda", "Lupatapata", "Miabi", "Mbuji-Mayi", "Tshilenge"]
            },
            "Kinshasa (Ville-Province)": {
                "coords": {"lat": -4.3000, "lon": 15.3000},
                "territories": ["Kinshasa Centre", "Kinshasa Est", "Kinshasa Ouest", "Kinshasa Sud"]
            },
            "Kongo Central": {
                "coords": {"lat": -5.5000, "lon": 14.5000},
                "territories": ["Banana", "Boma", "Kimvula", "Luozi", "Madimba", "Matadi", "Mbanza-Ngungu", "Moanda", "Muanda", "Seke-Banza", "Songololo", "Tshela"]
            },
            "Kwango": {
                "coords": {"lat": -6.5000, "lon": 17.5000},
                "territories": ["Feshi", "Kahemba", "Kasongo-Lunda", "Kenge", "Popokabaka"]
            },
            "Kwilu": {
                "coords": {"lat": -5.0000, "lon": 18.5000},
                "territories": ["Bagata", "Bulungu", "Gungu", "Idiofa", "Kikwit", "Masimanimba"]
            },
            "Lomami": {
                "coords": {"lat": -6.0000, "lon": 24.5000},
                "territories": ["Kabinda", "Kamiji", "Lubao", "Ngandajika", "Sankuru"]
            },
            "Lualaba": {
                "coords": {"lat": -9.0000, "lon": 25.5000},
                "territories": ["Dilolo", "Kapanga", "Kolwezi", "Lubudi", "Mutshatsha", "Sandoa"]
            },
            "Mai-Ndombe": {
                "coords": {"lat": -2.5000, "lon": 18.5000},
                "territories": ["Bolobo", "Inongo", "Kiri", "Kutu", "Oshwe", "Yumbi"]
            },
            "Maniema": {
                "coords": {"lat": -3.5000, "lon": 27.0000},
                "territories": ["Kabambare", "Kailo", "Kasongo", "Kibombo", "Kindu", "Lubutu", "Pangi", "Punia"]
            },
            "Mongala": {
                "coords": {"lat": 1.5000, "lon": 21.5000},
                "territories": ["Bongandanga", "Bumba", "Lisala", "Mobayi-Mbongo"]
            },
            "Nord-Kivu": {
                "coords": {"lat": -0.5000, "lon": 29.0000},
                "territories": ["Beni", "Goma", "Lubero", "Masisi", "Nyiragongo", "Rutshuru", "Walikale"]
            },
            "Nord-Ubangi": {
                "coords": {"lat": 3.5000, "lon": 21.5000},
                "territories": ["Bosobolo", "Businga", "Gbadolite", "Gemena", "Kungu", "Libenge", "Mobayi-Mbongo"]
            },
            "Sankuru": {
                "coords": {"lat": -3.5000, "lon": 24.0000},
                "territories": ["Katako-Kombe", "Kole", "Lomela", "Lubefu", "Lodja"]
            },
            "Sud-Kivu": {
                "coords": {"lat": -3.0000, "lon": 28.0000},
                "territories": ["Bukavu", "Fizi", "Idjwi", "Kabare", "Kalehe", "Mwenga", "Shabunda", "Uvira", "Walungu"]
            },
            "Sud-Ubangi": {
                "coords": {"lat": 2.0000, "lon": 19.5000},
                "territories": ["Budjala", "Kungu", "Libenge", "Zongo"]
            },
            "Tanganyika": {
                "coords": {"lat": -6.5000, "lon": 28.5000},
                "territories": ["Kabalo", "Kalemie", "Kongolo", "Manono", "Moba", "Nyunzu"]
            },
            "Tshopo": {
                "coords": {"lat": 1.0000, "lon": 25.0000},
                "territories": ["Bafwasende", "Banalia", "Isangi", "Kisangani", "Opala", "Ubundu", "Yahuma"]
            },
            "Tshuapa": {
                "coords": {"lat": -0.5000, "lon": 22.0000},
                "territories": ["Befale", "Boende", "Bokungu", "Djolu", "Ikela", "Monkoto"]
            }
        }

        for province_name, info in cd_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=cd_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=cd_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for territory_name in info["territories"]:
                territory = AdministrativeDivision.query.filter_by(
                    name=territory_name, level=2, parent_id=province.id
                ).first()
                if not territory:
                    territory = AdministrativeDivision(
                        name=territory_name, level=2, country_id=cd_id, parent_id=province.id
                    )
                    db.session.add(territory)

        db.session.commit()
        print("RD Congo : OK")

        # ================================================================
        # GUINÉE ÉQUATORIALE (ID: 226)
        # ================================================================
        print("\n--- Initialisation de la Guinée Équatoriale (ID: 226) ---")
        gq_id = 226
        gq = Country.query.get(gq_id)
        if not gq:
            gq = Country(id=gq_id, name="Guinée Équatoriale", iso_code="GQ")
            db.session.add(gq)
            db.session.commit()
            print("Pays Guinée Équatoriale créé.")

        gq_data = {
            "Annobón": {
                "coords": {"lat": -1.4272, "lon": 5.6347},
                "districts": ["San Antonio de Palé"]
            },
            "Bioko Norte": {
                "coords": {"lat": 3.7500, "lon": 8.7833},
                "districts": ["Malabo", "Baney", "Rebola"]
            },
            "Bioko Sur": {
                "coords": {"lat": 3.4167, "lon": 8.6833},
                "districts": ["Luba", "Moka", "Riaba"]
            },
            "Centro Sur": {
                "coords": {"lat": 1.2000, "lon": 10.5833},
                "districts": ["Evinayong", "Akonibe", "Nsork"]
            },
            "Djibloho": {
                "coords": {"lat": 1.5833, "lon": 10.6667},
                "districts": ["Djibloho"]
            },
            "Kié-Ntem": {
                "coords": {"lat": 2.0833, "lon": 10.7833},
                "districts": ["Ebebiyín", "Mongomo", "Nsangayong", "Mikomeseng"]
            },
            "Litoral": {
                "coords": {"lat": 1.4000, "lon": 9.6500},
                "districts": ["Bata", "Mbini", "Cogo"]
            },
            "Wele-Nzas": {
                "coords": {"lat": 1.3833, "lon": 11.0000},
                "districts": ["Mongomo", "Añisok", "Ncue", "Acurenam"]
            }
        }

        for province_name, info in gq_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=gq_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=gq_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=province.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=gq_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Guinée Équatoriale : OK")

        # ================================================================
        # GABON (ID: 266)
        # ================================================================
        print("\n--- Initialisation du Gabon (ID: 266) ---")
        ga_id = 266
        ga = Country.query.get(ga_id)
        if not ga:
            ga = Country(id=ga_id, name="Gabon", iso_code="GA")
            db.session.add(ga)
            db.session.commit()
            print("Pays Gabon créé.")

        ga_data = {
            "Estuaire": {
                "coords": {"lat": 0.4167, "lon": 9.4667},
                "departments": ["Komo", "Komo-Mondah", "Komo-Océan", "Libreville", "Noya"]
            },
            "Haut-Ogooué": {
                "coords": {"lat": -1.5000, "lon": 13.9167},
                "departments": ["Bakoumba", "Boungou", "Djouori-Agnili", "Lékabi-Léwolo", "Lékana", "Lékoni-Lékori", "Mpassa", "Ogooué-Létili", "Plateaux"]
            },
            "Moyen-Ogooué": {
                "coords": {"lat": -0.7000, "lon": 10.9167},
                "departments": ["Abanga-Bigné", "Etimboué", "Ogooué et des Lacs"]
            },
            "Ngounié": {
                "coords": {"lat": -2.1000, "lon": 11.5500},
                "departments": ["Boumi-Louétsi", "Dola", "Douya-Onoye", "Lombo-Bouenguidi", "Louétsi-Bibaka", "Louétsi-Wano", "Ogoulou", "Tsamba-Magotsi"]
            },
            "Nyanga": {
                "coords": {"lat": -3.0000, "lon": 11.0000},
                "departments": ["Basse-Banio", "Douigny", "Haute-Banio", "Mougalaba", "Moulengui-Binza", "Ndolou"]
            },
            "Ogooué-Ivindo": {
                "coords": {"lat": 0.8833, "lon": 13.1667},
                "departments": ["Ivindo", "Lopé", "Minkébé", "Zadié"]
            },
            "Ogooué-Lolo": {
                "coords": {"lat": -0.8333, "lon": 12.4667},
                "departments": ["Lombo-Bouenguidi", "Lolo-Bouenguidi", "Mulundu", "Offoué-Onoye"]
            },
            "Ogooué-Maritime": {
                "coords": {"lat": -1.6167, "lon": 9.4333},
                "departments": ["Bendje", "Boudji-Batengue", "Etimboué", "Mongo", "Ndougou"]
            },
            "Woleu-Ntem": {
                "coords": {"lat": 2.0000, "lon": 11.7500},
                "departments": ["Haut-Komo", "Haut-Ntem", "Haut-Okano", "Ntem", "Okano", "Woleu"]
            }
        }

        for province_name, info in ga_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=ga_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=ga_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for dept_name in info["departments"]:
                dept = AdministrativeDivision.query.filter_by(
                    name=dept_name, level=2, parent_id=province.id
                ).first()
                if not dept:
                    dept = AdministrativeDivision(
                        name=dept_name, level=2, country_id=ga_id, parent_id=province.id
                    )
                    db.session.add(dept)

        db.session.commit()
        print("Gabon : OK")

        # ================================================================
        # SÃO TOMÉ-ET-PRÍNCIPE (ID: 678)
        # ================================================================
        print("\n--- Initialisation de São Tomé-et-Príncipe (ID: 678) ---")
        st_id = 678
        st = Country.query.get(st_id)
        if not st:
            st = Country(id=st_id, name="São Tomé-et-Príncipe", iso_code="ST")
            db.session.add(st)
            db.session.commit()
            print("Pays São Tomé-et-Príncipe créé.")

        st_data = {
            "São Tomé": {
                "coords": {"lat": 0.3365, "lon": 6.7273},
                "districts": ["Água Grande", "Cantagalo", "Caué", "Lembá", "Lobata", "Mé-Zóchi"]
            },
            "Príncipe": {
                "coords": {"lat": 1.6139, "lon": 7.4050},
                "districts": ["Pagué"]
            }
        }

        for province_name, info in st_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=st_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=st_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=province.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=st_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("São Tomé-et-Príncipe : OK")

        # ================================================================
        # BURUNDI (ID: 108)
        # ================================================================
        print("\n--- Initialisation du Burundi (ID: 108) ---")
        bi_id = 108
        bi = Country.query.get(bi_id)
        if not bi:
            bi = Country(id=bi_id, name="Burundi", iso_code="BI")
            db.session.add(bi)
            db.session.commit()
            print("Pays Burundi créé.")

        bi_data = {
            "Bubanza": {
                "coords": {"lat": -3.0833, "lon": 29.3833},
                "communes": ["Bubanza", "Gihanga", "Mpanda", "Musigati", "Rugazi"]
            },
            "Bujumbura Mairie": {
                "coords": {"lat": -3.3822, "lon": 29.3644},
                "communes": ["Kinama", "Kanyosha", "Muha", "Mukaza", "Ntahangwa"]
            },
            "Bujumbura Rural": {
                "coords": {"lat": -3.5000, "lon": 29.3000},
                "communes": ["Isale", "Kabezi", "Kanyosha", "Mugamba", "Muhuta", "Mutimbuzi", "Nyabiraba", "Nyambuye", "Rohero"]
            },
            "Bururi": {
                "coords": {"lat": -3.9500, "lon": 29.6167},
                "communes": ["Burambi", "Bururi", "Buyengero", "Matana", "Mugamba", "Rumonge", "Rutovu", "Songa"]
            },
            "Cankuzo": {
                "coords": {"lat": -3.2167, "lon": 30.5500},
                "communes": ["Cankuzo", "Gisagara", "Kigamba", "Mishiha", "Murungazi"]
            },
            "Cibitoke": {
                "coords": {"lat": -2.8833, "lon": 29.1167},
                "communes": ["Buganda", "Bukinanyana", "Cibitoke", "Mabayi", "Mugina", "Murwi", "Rugombo"]
            },
            "Gitega": {
                "coords": {"lat": -3.4264, "lon": 29.9244},
                "communes": ["Bugendana", "Buraza", "Giheta", "Gitega", "Itaba", "Makebuko", "Mutaho", "Nyanкoronko", "Ryansoro"]
            },
            "Karuzi": {
                "coords": {"lat": -3.1000, "lon": 30.1667},
                "communes": ["Buhiga", "Gitaramuka", "Mutumba", "Nyabikere", "Shombo"]
            },
            "Kayanza": {
                "coords": {"lat": -2.9167, "lon": 29.6333},
                "communes": ["Butaganzwa", "Gatara", "Guharo", "Kayanza", "Kabarore", "Muruta", "Rango", "Shombo"]
            },
            "Kirundo": {
                "coords": {"lat": -2.5833, "lon": 30.1000},
                "communes": ["Bugabira", "Bwambarangwe", "Busoni", "Gitobe", "Kirundo", "Ntega", "Vumbi"]
            },
            "Makamba": {
                "coords": {"lat": -4.1333, "lon": 29.8000},
                "communes": ["Kayogoro", "Kibago", "Makamba", "Mabanda", "Nyanza-Lac", "Vugizo"]
            },
            "Muramvya": {
                "coords": {"lat": -3.2667, "lon": 29.6000},
                "communes": ["Bukeye", "Kiganda", "Muramvya", "Rutegama"]
            },
            "Muyinga": {
                "coords": {"lat": -2.8500, "lon": 30.3333},
                "communes": ["Buhinyuza", "Butihinda", "Gasorwe", "Giteranyi", "Muyinga", "Mwakiro", "Ruhororo"]
            },
            "Mwaro": {
                "coords": {"lat": -3.5000, "lon": 29.6833},
                "communes": ["Bisoro", "Gisozi", "Kayokwe", "Mihigo", "Ndava", "Nyabihanga"]
            },
            "Ngozi": {
                "coords": {"lat": -2.9078, "lon": 29.8306},
                "communes": ["Busiga", "Gashikanwa", "Kiremba", "Marangara", "Mwumba", "Ngozi", "Nyamurenza", "Ruhororo", "Tangara"]
            },
            "Rumonge": {
                "coords": {"lat": -3.9742, "lon": 29.4386},
                "communes": ["Buyengero", "Kigwena", "Rumonge", "Vyanda"]
            },
            "Rutana": {
                "coords": {"lat": -3.9167, "lon": 30.0000},
                "communes": ["Giharo", "Gitanga", "Mpinga-Kayove", "Musongati", "Rutana"]
            },
            "Ruyigi": {
                "coords": {"lat": -3.4833, "lon": 30.2500},
                "communes": ["Butaganzwa", "Butezi", "Bweru", "Gisuru", "Kinyinya", "Nyabitsinda", "Ruyigi"]
            }
        }

        for province_name, info in bi_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=bi_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=bi_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for commune_name in info["communes"]:
                commune = AdministrativeDivision.query.filter_by(
                    name=commune_name, level=2, parent_id=province.id
                ).first()
                if not commune:
                    commune = AdministrativeDivision(
                        name=commune_name, level=2, country_id=bi_id, parent_id=province.id
                    )
                    db.session.add(commune)

        db.session.commit()
        print("Burundi : OK")

        # ================================================================
        # RWANDA (ID: 646)
        # ================================================================
        print("\n--- Initialisation du Rwanda (ID: 646) ---")
        rw_id = 646
        rw = Country.query.get(rw_id)
        if not rw:
            rw = Country(id=rw_id, name="Rwanda", iso_code="RW")
            db.session.add(rw)
            db.session.commit()
            print("Pays Rwanda créé.")

        rw_data = {
            "Kigali": {
                "coords": {"lat": -1.9441, "lon": 30.0619},
                "districts": ["Gasabo", "Kicukiro", "Nyarugenge"]
            },
            "Province du Nord": {
                "coords": {"lat": -1.5000, "lon": 30.0000},
                "districts": ["Burera", "Gakenke", "Gicumbi", "Musanze", "Rulindo"]
            },
            "Province du Sud": {
                "coords": {"lat": -2.3000, "lon": 29.7500},
                "districts": ["Gisagara", "Huye", "Kamonyi", "Muhanga", "Nyamagabe", "Nyanza", "Nyaruguru", "Ruhango"]
            },
            "Province de l'Est": {
                "coords": {"lat": -1.7500, "lon": 30.6667},
                "districts": ["Bugesera", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Nyagatare", "Rwamagana"]
            },
            "Province de l'Ouest": {
                "coords": {"lat": -2.0000, "lon": 29.2500},
                "districts": ["Karongi", "Ngororero", "Nyabihu", "Nyamasheke", "Rubavu", "Rutsiro", "Rusizi"]
            }
        }

        for province_name, info in rw_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=rw_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=rw_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for district_name in info["districts"]:
                district = AdministrativeDivision.query.filter_by(
                    name=district_name, level=2, parent_id=province.id
                ).first()
                if not district:
                    district = AdministrativeDivision(
                        name=district_name, level=2, country_id=rw_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Rwanda : OK")

        # ================================================================
        # RÉSUMÉ FINAL
        # ================================================================
        print("\n" + "="*55)
        print("Succès : Toutes les données d'Afrique Centrale sont à jour !")
        print("  - Cameroun                   (ID: 120) : 10 régions")
        print("  - Rép. Centrafricaine        (ID: 140) : 18 préfectures")
        print("  - Tchad                      (ID: 148) : 22 provinces")
        print("  - Rép. du Congo              (ID: 178) : 12 départements")
        print("  - RD Congo                   (ID: 180) : 26 provinces")
        print("  - Guinée Équatoriale         (ID: 226) : 8 provinces")
        print("  - Gabon                      (ID: 266) : 9 provinces")
        print("  - São Tomé-et-Príncipe       (ID: 678) : 2 provinces")
        print("  - Burundi                    (ID: 108) : 18 provinces")
        print("  - Rwanda                     (ID: 646) : 5 provinces")
        print("="*55)

if __name__ == "__main__":
    seed_data()