import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Country, AdministrativeDivision

app = create_app()

def seed_data():
    with app.app_context():

        # ================================================================
        # AFRIQUE DU SUD (ID: 710)
        # ================================================================
        print("\n--- Initialisation de l'Afrique du Sud (ID: 710) ---")
        za_id = 710
        za = Country.query.get(za_id)
        if not za:
            za = Country(id=za_id, name="Afrique du Sud", iso_code="ZA")
            db.session.add(za)
            db.session.commit()
            print("Pays Afrique du Sud créé.")

        za_data = {
            "Gauteng": {
                "coords": {"lat": -26.2708, "lon": 28.1123},
                "districts": ["City of Johannesburg", "City of Tshwane", "Ekurhuleni",
                              "Sedibeng", "West Rand"]
            },
            "Western Cape": {
                "coords": {"lat": -33.2278, "lon": 21.8569},
                "districts": ["City of Cape Town", "Cape Winelands", "Central Karoo",
                              "Garden Route", "Overberg", "West Coast"]
            },
            "Eastern Cape": {
                "coords": {"lat": -32.2968, "lon": 26.4194},
                "districts": ["Alfred Nzo", "Amathole", "Buffalo City", "Chris Hani",
                              "Joe Gqabi", "Nelson Mandela Bay", "OR Tambo", "Sarah Baartman"]
            },
            "KwaZulu-Natal": {
                "coords": {"lat": -28.5306, "lon": 30.8958},
                "districts": ["Amajuba", "eThekwini", "Harry Gwala", "iLembe",
                              "King Cetshwayo", "Msunduzi", "Ugu", "uMgungundlovu",
                              "uMkhanyakude", "uMzinyathi", "uThukela", "Zululand"]
            },
            "Limpopo": {
                "coords": {"lat": -23.4013, "lon": 29.4179},
                "districts": ["Capricorn", "Mopani", "Sekhukhune", "Vhembe", "Waterberg"]
            },
            "Mpumalanga": {
                "coords": {"lat": -25.5653, "lon": 30.5279},
                "districts": ["Ehlanzeni", "Gert Sibande", "Nkangala"]
            },
            "North West": {
                "coords": {"lat": -26.6638, "lon": 25.4285},
                "districts": ["Bojanala Platinum", "Dr Kenneth Kaunda",
                              "Dr Ruth Segomotsi Mompati", "Ngaka Modiri Molema"]
            },
            "Free State": {
                "coords": {"lat": -28.4541, "lon": 26.7968},
                "districts": ["Fezile Dabi", "Lejweleputswa", "Mangaung",
                              "Thabo Mofutsanyana", "Xhariep"]
            },
            "Northern Cape": {
                "coords": {"lat": -29.0467, "lon": 21.8569},
                "districts": ["Frances Baard", "John Taolo Gaetsewe",
                              "Namakwa", "Pixley ka Seme", "ZF Mgcawu"]
            }
        }

        for province_name, info in za_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=za_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=za_id,
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
                        name=district_name, level=2, country_id=za_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Afrique du Sud : OK")

        # ================================================================
        # NAMIBIE (ID: 516)
        # ================================================================
        print("\n--- Initialisation de la Namibie (ID: 516) ---")
        na_id = 516
        na = Country.query.get(na_id)
        if not na:
            na = Country(id=na_id, name="Namibie", iso_code="NA")
            db.session.add(na)
            db.session.commit()
            print("Pays Namibie créé.")

        na_data = {
            "Erongo": {
                "coords": {"lat": -22.2558, "lon": 14.5251},
                "constituencies": ["Arandis", "Daures", "Karibib", "Khomas", "Omaruru",
                                   "Sandwich Harbour", "Swakopmund", "Walvis Bay Rural",
                                   "Walvis Bay Urban"]
            },
            "Hardap": {
                "coords": {"lat": -24.2400, "lon": 18.0000},
                "constituencies": ["Daweb", "Gibeon", "Groot Aub", "Maltahöhe",
                                   "Mariental Rural", "Mariental Urban", "Rehoboth Rural",
                                   "Rehoboth Urban", "Stampriet"]
            },
            "//Karas": {
                "coords": {"lat": -27.0000, "lon": 18.5000},
                "constituencies": ["Berseba", "Karasburg", "Keetmanshoop Rural",
                                   "Keetmanshoop Urban", "Lüderitz", "Namaland",
                                   "Oranjemund", "Tses", "Warmbad"]
            },
            "Kavango Est": {
                "coords": {"lat": -18.0833, "lon": 20.5833},
                "constituencies": ["Andara", "Gciriku-Diriku", "Kahenge", "Kapako",
                                   "Mankumpi", "Mashare", "Mukwe", "Ndiyona",
                                   "Rundu Rural", "Rundu Urban"]
            },
            "Kavango Ouest": {
                "coords": {"lat": -18.2500, "lon": 19.5833},
                "constituencies": ["Kahenge", "Kapako", "Mankumpi", "Nkurenkuru",
                                   "Mpungu", "Musese"]
            },
            "Khomas": {
                "coords": {"lat": -22.5609, "lon": 17.0658},
                "constituencies": ["Katutura Central", "Katutura East", "Khomasdal",
                                   "Moses Garoëb", "Samora Machel", "Tobias Hainyeko",
                                   "Windhoek East", "Windhoek Rural", "Windhoek West"]
            },
            "Kunene": {
                "coords": {"lat": -19.5000, "lon": 13.5000},
                "constituencies": ["Epupa", "Kamanjab", "Opuwo Rural", "Opuwo Urban",
                                   "Outjo", "Sesfontein"]
            },
            "Ohangwena": {
                "coords": {"lat": -17.8000, "lon": 16.5000},
                "constituencies": ["Eengodi", "Endola", "Engela", "Epembe",
                                   "Okongo", "Ombulantu", "Ompundja", "Ondobe",
                                   "Ongenga", "Oshikango"]
            },
            "Omaheke": {
                "coords": {"lat": -22.0000, "lon": 21.0000},
                "constituencies": ["Aminuis", "Buitepos", "Epukiro", "Gobabis",
                                   "Kalahari", "Otjinene", "Otjiwarongo South", "Steinhausen"]
            },
            "Omusati": {
                "coords": {"lat": -18.5000, "lon": 14.5000},
                "constituencies": ["Anamulenge", "Elim", "Etayi", "Ogongo",
                                   "Okahao", "Okalongo", "Ombadja", "Omulonga",
                                   "Onesi", "Oshikuku", "Otamanzi", "Outapi",
                                   "Ruacana", "Tsandi"]
            },
            "Oshana": {
                "coords": {"lat": -18.0000, "lon": 15.7500},
                "constituencies": ["Egbeda", "Okatana", "Okathitu", "Ompundja",
                                   "Ondangwa Rural", "Ondangwa Urban", "Ongwediva",
                                   "Oshakati East", "Oshakati West", "Uuvudhiya"]
            },
            "Oshikoto": {
                "coords": {"lat": -18.0000, "lon": 17.0000},
                "constituencies": ["Eengodi", "Guinas", "Nehale lya Mpingana",
                                   "Okankolo", "Olukonda", "Omuthiyagwiipundi",
                                   "Onayena", "Oniipa", "Onyaanya", "Tsumeb"]
            },
            "Otjozondjupa": {
                "coords": {"lat": -20.5000, "lon": 17.5000},
                "constituencies": ["Grootfontein", "Okahandja", "Okakarara",
                                   "Otavi", "Otjiwarongo", "Tsumkwe"]
            },
            "Zambezi": {
                "coords": {"lat": -17.8500, "lon": 23.5000},
                "constituencies": ["Judea Lyaboloma", "Kabbe North", "Kabbe South",
                                   "Katima Mulilo Rural", "Katima Mulilo Urban",
                                   "Kongola", "Linyanti", "Sibbinda"]
            }
        }

        for region_name, info in na_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=na_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=na_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for constituency_name in info["constituencies"]:
                constituency = AdministrativeDivision.query.filter_by(
                    name=constituency_name, level=2, parent_id=region.id
                ).first()
                if not constituency:
                    constituency = AdministrativeDivision(
                        name=constituency_name, level=2, country_id=na_id, parent_id=region.id
                    )
                    db.session.add(constituency)

        db.session.commit()
        print("Namibie : OK")

        # ================================================================
        # BOTSWANA (ID: 72)
        # ================================================================
        print("\n--- Initialisation du Botswana (ID: 72) ---")
        bw_id = 72
        bw = Country.query.get(bw_id)
        if not bw:
            bw = Country(id=bw_id, name="Botswana", iso_code="BW")
            db.session.add(bw)
            db.session.commit()
            print("Pays Botswana créé.")

        bw_data = {
            "Central": {
                "coords": {"lat": -22.0000, "lon": 26.5000},
                "sub_districts": ["Bobonong", "Boteti", "Mahalapye", "Orapa",
                                  "Serowe-Palapye", "Sowa Town", "Tutume"]
            },
            "Ghanzi": {
                "coords": {"lat": -21.7000, "lon": 21.6500},
                "sub_districts": ["Ghanzi", "Kgalagadi North", "Kgalagadi South"]
            },
            "Kgalagadi": {
                "coords": {"lat": -24.7500, "lon": 21.8333},
                "sub_districts": ["Kgalagadi North", "Kgalagadi South"]
            },
            "Kgatleng": {
                "coords": {"lat": -24.1667, "lon": 26.2500},
                "sub_districts": ["Kgatleng"]
            },
            "Kweneng": {
                "coords": {"lat": -23.8333, "lon": 25.0000},
                "sub_districts": ["Kweneng East", "Kweneng West"]
            },
            "Ngamiland": {
                "coords": {"lat": -19.5000, "lon": 22.5000},
                "sub_districts": ["Maun", "Ngami", "Okavango", "Chobe"]
            },
            "North East": {
                "coords": {"lat": -21.0000, "lon": 27.5000},
                "sub_districts": ["North East", "Tati"]
            },
            "North West": {
                "coords": {"lat": -20.0000, "lon": 24.0000},
                "sub_districts": ["Chobe", "Ngamiland West"]
            },
            "South East": {
                "coords": {"lat": -24.7500, "lon": 25.9167},
                "sub_districts": ["Gaborone", "South East"]
            },
            "Southern": {
                "coords": {"lat": -25.0000, "lon": 25.5000},
                "sub_districts": ["Barolong", "Batlokwa", "Good Hope",
                                  "Ngwaketse Central", "Ngwaketse South",
                                  "Ngwaketse West"]
            }
        }

        for district_name, info in bw_data.items():
            district = AdministrativeDivision.query.filter_by(
                name=district_name, level=1, country_id=bw_id
            ).first()
            if not district:
                district = AdministrativeDivision(
                    name=district_name, level=1, country_id=bw_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(district)
                db.session.flush()
                print(f"  -> District : {district_name}")

            for sub_name in info["sub_districts"]:
                sub = AdministrativeDivision.query.filter_by(
                    name=sub_name, level=2, parent_id=district.id
                ).first()
                if not sub:
                    sub = AdministrativeDivision(
                        name=sub_name, level=2, country_id=bw_id, parent_id=district.id
                    )
                    db.session.add(sub)

        db.session.commit()
        print("Botswana : OK")

        # ================================================================
        # ZIMBABWE (ID: 716)
        # ================================================================
        print("\n--- Initialisation du Zimbabwe (ID: 716) ---")
        zw_id = 716
        zw = Country.query.get(zw_id)
        if not zw:
            zw = Country(id=zw_id, name="Zimbabwe", iso_code="ZW")
            db.session.add(zw)
            db.session.commit()
            print("Pays Zimbabwe créé.")

        zw_data = {
            "Bulawayo": {
                "coords": {"lat": -20.1500, "lon": 28.5833},
                "districts": ["Bulawayo"]
            },
            "Harare": {
                "coords": {"lat": -17.8252, "lon": 31.0335},
                "districts": ["Harare", "Chitungwiza", "Epworth"]
            },
            "Manicaland": {
                "coords": {"lat": -19.1667, "lon": 32.5000},
                "districts": ["Buhera", "Chimanimani", "Chipinge", "Makoni",
                              "Mutare", "Mutasa", "Nyanga"]
            },
            "Mashonaland Central": {
                "coords": {"lat": -16.7833, "lon": 31.0667},
                "districts": ["Bindura", "Centenary", "Guruve", "Mazowe",
                              "Mount Darwin", "Muzarabani", "Rushinga", "Shamva"]
            },
            "Mashonaland East": {
                "coords": {"lat": -18.5833, "lon": 31.9167},
                "districts": ["Chikomba", "Goromonzi", "Hwedza", "Marondera",
                              "Mudzi", "Murehwa", "Mutoko", "Seke", "UMP"]
            },
            "Mashonaland West": {
                "coords": {"lat": -17.4833, "lon": 29.7667},
                "districts": ["Chegutu", "Hurungwe", "Kariba", "Makonde",
                              "Mhondoro-Ngezi", "Sanyati", "Zvimba"]
            },
            "Masvingo": {
                "coords": {"lat": -20.0667, "lon": 30.8333},
                "districts": ["Bikita", "Chiredzi", "Chivi", "Gutu",
                              "Masvingo", "Mwenezi", "Zaka"]
            },
            "Matabeleland North": {
                "coords": {"lat": -18.5000, "lon": 27.5000},
                "districts": ["Binga", "Bubi", "Hwange", "Lupane",
                              "Nkayi", "Tsholotsho", "Umguza"]
            },
            "Matabeleland South": {
                "coords": {"lat": -21.0000, "lon": 29.0000},
                "districts": ["Beitbridge", "Bulilima", "Gwanda",
                              "Insiza", "Mangwe", "Matobo", "Umzingwane"]
            },
            "Midlands": {
                "coords": {"lat": -19.5000, "lon": 29.7500},
                "districts": ["Chirumhanzu", "Gokwe North", "Gokwe South",
                              "Gweru", "Kwekwe", "Mberengwa", "Shurugwi", "Zvishavane"]
            }
        }

        for province_name, info in zw_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=zw_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=zw_id,
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
                        name=district_name, level=2, country_id=zw_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Zimbabwe : OK")

        # ================================================================
        # MOZAMBIQUE (ID: 508)
        # ================================================================
        print("\n--- Initialisation du Mozambique (ID: 508) ---")
        mz_id = 508
        mz = Country.query.get(mz_id)
        if not mz:
            mz = Country(id=mz_id, name="Mozambique", iso_code="MZ")
            db.session.add(mz)
            db.session.commit()
            print("Pays Mozambique créé.")

        mz_data = {
            "Maputo Cidade": {
                "coords": {"lat": -25.9692, "lon": 32.5732},
                "districts": ["Kamavota", "Kampfumo", "Kanyaka", "KaMaxaquene",
                              "KaMpfumo", "KaMubukwana", "KaNhlamankulu", "KaTembe",
                              "Nlhamankulu"]
            },
            "Maputo": {
                "coords": {"lat": -25.2500, "lon": 32.5833},
                "districts": ["Boane", "Magude", "Manhiça", "Marracuene",
                              "Matola", "Matutuíne", "Moamba", "Namaacha"]
            },
            "Gaza": {
                "coords": {"lat": -23.5000, "lon": 33.5000},
                "districts": ["Bilene", "Chibuto", "Chicualacuala", "Chigubo",
                              "Chokwé", "Guijá", "Limpopo", "Mabalane",
                              "Manjacaze", "Massangena", "Massingir", "Xai-Xai"]
            },
            "Inhambane": {
                "coords": {"lat": -22.0000, "lon": 34.5000},
                "districts": ["Funhalouro", "Govuro", "Homoíne", "Inhambane",
                              "Inharrime", "Inhassoro", "Jangamo", "Mabote",
                              "Massinga", "Morrumbene", "Panda", "Vilanculos",
                              "Zavala"]
            },
            "Sofala": {
                "coords": {"lat": -19.5000, "lon": 34.5000},
                "districts": ["Bárue", "Beira", "Buzi", "Caia", "Chemba",
                              "Cheringoma", "Chibabava", "Dondo", "Gorongosa",
                              "Machanga", "Maringue", "Marromeu", "Muanza",
                              "Nhamatanda"]
            },
            "Manica": {
                "coords": {"lat": -19.5000, "lon": 33.0000},
                "districts": ["Bárue", "Chimoio", "Gondola", "Guro", "Macate",
                              "Machaze", "Macossa", "Mossurize", "Sussundenga",
                              "Tambara"]
            },
            "Tete": {
                "coords": {"lat": -15.5000, "lon": 33.0000},
                "districts": ["Angónia", "Cahora-Bassa", "Changara", "Chifunde",
                              "Chiuta", "Dôa", "Macanga", "Marávia", "Moatize",
                              "Mutarara", "Tete", "Tsangano", "Zumbo"]
            },
            "Zambézia": {
                "coords": {"lat": -16.5000, "lon": 36.0000},
                "districts": ["Alto Molócuè", "Chinde", "Derre", "Gilé",
                              "Guruè", "Ile", "Inhassunge", "Lugela", "Maganja da Costa",
                              "Milange", "Mocuba", "Mopeia", "Morrumbala",
                              "Namacurra", "Namarroi", "Nicoadala", "Pebane",
                              "Quelimane"]
            },
            "Nampula": {
                "coords": {"lat": -15.0000, "lon": 39.0000},
                "districts": ["Angoche", "Eráti", "Ilha de Moçambique", "Lalaua",
                              "Larde", "Liúpo", "Malema", "Meconta", "Mecubúri",
                              "Memba", "Mogincual", "Mogovolas", "Moma",
                              "Monapo", "Mossuril", "Muecate", "Murrupula",
                              "Nacala-a-Velha", "Nacala Porto", "Nacarôa",
                              "Nampula", "Rapale", "Ribaué"]
            },
            "Cabo Delgado": {
                "coords": {"lat": -12.0000, "lon": 40.0000},
                "districts": ["Ancuabe", "Balama", "Chiúre", "Ibo", "Macomia",
                              "Mecúfi", "Meluco", "Metuge", "Mocímboa da Praia",
                              "Montepuez", "Mueda", "Muidumbe", "Namuno",
                              "Nangade", "Palma", "Pemba", "Quissanga"]
            },
            "Niassa": {
                "coords": {"lat": -13.0000, "lon": 36.0000},
                "districts": ["Chimbonila", "Cuamba", "Lago", "Lichinga",
                              "Majune", "Mandimba", "Marrupa", "Maúa",
                              "Mavago", "Mecanhelas", "Mecula", "Metarica",
                              "Muembe", "N'gauma", "Nipepe", "Sanga"]
            }
        }

        for province_name, info in mz_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=mz_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=mz_id,
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
                        name=district_name, level=2, country_id=mz_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Mozambique : OK")

        # ================================================================
        # ZAMBIE (ID: 894)
        # ================================================================
        print("\n--- Initialisation de la Zambie (ID: 894) ---")
        zm_id = 894
        zm = Country.query.get(zm_id)
        if not zm:
            zm = Country(id=zm_id, name="Zambie", iso_code="ZM")
            db.session.add(zm)
            db.session.commit()
            print("Pays Zambie créé.")

        zm_data = {
            "Central": {
                "coords": {"lat": -14.5000, "lon": 28.5000},
                "districts": ["Chibombo", "Kabwe", "Kapiri Mposhi", "Mkushi",
                              "Mumbwa", "Ngabwe", "Serenje", "Shibuyunji"]
            },
            "Copperbelt": {
                "coords": {"lat": -13.0000, "lon": 27.8667},
                "districts": ["Chililabombwe", "Chingola", "Kalulushi",
                              "Kitwe", "Luanshya", "Lufwanyama", "Masaiti",
                              "Mpongwe", "Mufulira", "Ndola"]
            },
            "Eastern": {
                "coords": {"lat": -13.5000, "lon": 32.5000},
                "districts": ["Chadiza", "Chama", "Chipata", "Katete",
                              "Lumezi", "Lundazi", "Mambwe", "Nyimba",
                              "Petauke", "Sinda", "Vubwi"]
            },
            "Luapula": {
                "coords": {"lat": -11.0000, "lon": 29.0000},
                "districts": ["Chembe", "Chienge", "Chiengi", "Kawambwa",
                              "Mansa", "Milenge", "Mwense", "Nchelenge",
                              "Samfya"]
            },
            "Lusaka": {
                "coords": {"lat": -15.4167, "lon": 28.2833},
                "districts": ["Chirundu", "Chongwe", "Kafue", "Luangwa",
                              "Lusaka", "Rufunsa"]
            },
            "Muchinga": {
                "coords": {"lat": -11.0000, "lon": 32.0000},
                "districts": ["Chinsali", "Isoka", "Kanchibiya", "Lavushimanda",
                              "Mafinga", "Mpika", "Nakonde", "Shiwang'andu"]
            },
            "Northern": {
                "coords": {"lat": -10.0000, "lon": 31.0000},
                "districts": ["Chilubi", "Chitambo", "Kasama", "Luwingu",
                              "Mbala", "Mporokoso", "Mpulungu", "Mungwi",
                              "Nsama"]
            },
            "North-Western": {
                "coords": {"lat": -13.0000, "lon": 24.0000},
                "districts": ["Chavuma", "Ikelenge", "Kabompo", "Kasempa",
                              "Manyinga", "Mufumbwe", "Mushindamo", "Mwinilunga",
                              "Solwezi", "Zambezi"]
            },
            "Southern": {
                "coords": {"lat": -16.5000, "lon": 27.0000},
                "districts": ["Choma", "Gwembe", "Itezhi-Tezhi", "Kalomo",
                              "Kazungula", "Livingstone", "Mazabuka",
                              "Monze", "Namwala", "Pemba", "Siavonga",
                              "Sinazongwe", "Zimba"]
            },
            "Western": {
                "coords": {"lat": -15.5000, "lon": 23.0000},
                "districts": ["Kalabo", "Kaoma", "Limulunga", "Lukulu",
                              "Mitete", "Mongu", "Mulobezi", "Mwandi",
                              "Nalolo", "Nkeyema", "Senanga", "Sesheke",
                              "Shangombo"]
            }
        }

        for province_name, info in zm_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=zm_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=zm_id,
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
                        name=district_name, level=2, country_id=zm_id, parent_id=province.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Zambie : OK")

        # ================================================================
        # MALAWI (ID: 454)
        # ================================================================
        print("\n--- Initialisation du Malawi (ID: 454) ---")
        mw_id = 454
        mw = Country.query.get(mw_id)
        if not mw:
            mw = Country(id=mw_id, name="Malawi", iso_code="MW")
            db.session.add(mw)
            db.session.commit()
            print("Pays Malawi créé.")

        mw_data = {
            "Northern": {
                "coords": {"lat": -11.0000, "lon": 34.0000},
                "districts": ["Chitipa", "Karonga", "Likoma", "Mzimba",
                              "Nkhata Bay", "Rumphi"]
            },
            "Central": {
                "coords": {"lat": -13.2500, "lon": 33.7500},
                "districts": ["Dedza", "Dowa", "Kasungu", "Lilongwe",
                              "Mchinji", "Nkhotakota", "Ntcheu",
                              "Ntchisi", "Salima"]
            },
            "Southern": {
                "coords": {"lat": -15.5000, "lon": 35.0000},
                "districts": ["Balaka", "Blantyre", "Chikwawa", "Chiradzulu",
                              "Machinga", "Mangochi", "Mulanje", "Mwanza",
                              "Neno", "Nsanje", "Phalombe", "Thyolo",
                              "Zomba"]
            }
        }

        for region_name, info in mw_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=mw_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=mw_id,
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
                        name=district_name, level=2, country_id=mw_id, parent_id=region.id
                    )
                    db.session.add(district)

        db.session.commit()
        print("Malawi : OK")

        # ================================================================
        # ANGOLA (ID: 24)
        # ================================================================
        print("\n--- Initialisation de l'Angola (ID: 24) ---")
        ao_id = 24
        ao = Country.query.get(ao_id)
        if not ao:
            ao = Country(id=ao_id, name="Angola", iso_code="AO")
            db.session.add(ao)
            db.session.commit()
            print("Pays Angola créé.")

        ao_data = {
            "Bengo": {
                "coords": {"lat": -9.1000, "lon": 13.7333},
                "municipalities": ["Ambriz", "Bula Atumba", "Dande", "Dembos",
                                   "Kissama", "Nambuangongo", "Pango Aluquém"]
            },
            "Benguela": {
                "coords": {"lat": -12.5763, "lon": 13.4055},
                "municipalities": ["Balombo", "Baía Farta", "Benguela", "Bocoio",
                                   "Caimbambo", "Chongoroi", "Cubal", "Ganda",
                                   "Lobito"]
            },
            "Bié": {
                "coords": {"lat": -12.5000, "lon": 17.0000},
                "municipalities": ["Andulo", "Camacupa", "Catabola", "Chinguar",
                                   "Chitembo", "Cuemba", "Cunhinga", "Kuito",
                                   "Nharea"]
            },
            "Cabinda": {
                "coords": {"lat": -5.5500, "lon": 12.2000},
                "municipalities": ["Belize", "Buco-Zau", "Cabinda", "Cacongo"]
            },
            "Cuando Cubango": {
                "coords": {"lat": -16.5000, "lon": 19.5000},
                "municipalities": ["Calai", "Cuangar", "Cuchi", "Cuito Cuanavale",
                                   "Dirico", "Longa", "Mavinga", "Menongue",
                                   "Nancova", "Rivungo"]
            },
            "Cuanza Norte": {
                "coords": {"lat": -9.0000, "lon": 15.0000},
                "municipalities": ["Ambaca", "Bolongongo", "Banga", "Cazengo",
                                   "Golungo Alto", "Gonguembo", "Lucala",
                                   "Quiculungo", "Samba Cajú"]
            },
            "Cuanza Sul": {
                "coords": {"lat": -11.0000, "lon": 14.5000},
                "municipalities": ["Amboim", "Cassongue", "Cela", "Conda",
                                   "Ebo", "Libolo", "Mussende", "Porto Amboim",
                                   "Quibala", "Quilenda", "Seles", "Sumbe"]
            },
            "Cunene": {
                "coords": {"lat": -16.5000, "lon": 15.5000},
                "municipalities": ["Cahama", "Cuanhama", "Curoca",
                                   "Namacunde", "Ombadja"]
            },
            "Huambo": {
                "coords": {"lat": -12.7761, "lon": 15.7395},
                "municipalities": ["Bailundo", "Caála", "Catchiungo",
                                   "Chicala Cholohanga", "Chilembo", "Chinjenje",
                                   "Ecunha", "Huambo", "Londuimbali", "Longonjo",
                                   "Mungo", "Tchicala-Tcholoanga", "Ucuma"]
            },
            "Huíla": {
                "coords": {"lat": -14.9289, "lon": 13.5000},
                "municipalities": ["Caconda", "Cacula", "Caluquembe", "Cuvango",
                                   "Chibia", "Chicomba", "Chipindo", "Gambos",
                                   "Humpata", "Jamba", "Lubango", "Matala",
                                   "Quilengues", "Quipungo"]
            },
            "Luanda": {
                "coords": {"lat": -8.8368, "lon": 13.2343},
                "municipalities": ["Belas", "Cacuaco", "Cazenga", "Icolo e Bengo",
                                   "Kilamba Kiaxi", "Luanda", "Quiçama",
                                   "Talatona", "Viana"]
            },
            "Lunda Norte": {
                "coords": {"lat": -8.5000, "lon": 20.5000},
                "municipalities": ["Alto Cuilo", "Cambulo", "Capenda-Camulemba",
                                   "Caungula", "Chitato", "Cuango", "Cuilo",
                                   "Lubalo", "Lucapa", "Xá-Muteba"]
            },
            "Lunda Sul": {
                "coords": {"lat": -10.5000, "lon": 21.0000},
                "municipalities": ["Cacolo", "Dala", "Muconda", "Saurimo"]
            },
            "Malanje": {
                "coords": {"lat": -9.5400, "lon": 16.3500},
                "municipalities": ["Cacuso", "Caombo", "Cunda-Dia-Baze",
                                   "Duque de Bragança", "Kiwaba Nzoji",
                                   "Luquembo", "Malanje", "Massango", "Marimba",
                                   "Mucari", "Quela", "Quirima"]
            },
            "Moxico": {
                "coords": {"lat": -12.5000, "lon": 21.5000},
                "municipalities": ["Alto Zambeze", "Bundas", "Camanongue",
                                   "Léua", "Luchazes", "Luau", "Luena",
                                   "Moxico", "Nhamatanda"]
            },
            "Namibe": {
                "coords": {"lat": -15.1961, "lon": 12.1522},
                "municipalities": ["Bibala", "Camucuio", "Namibe",
                                   "Tombua", "Virei"]
            },
            "Uíge": {
                "coords": {"lat": -7.6089, "lon": 15.0614},
                "municipalities": ["Alto Cauale", "Ambuila", "Bembe",
                                   "Buengas", "Bungo", "Cangola", "Damba",
                                   "Maquela do Zombo", "Milunga", "Mucaba",
                                   "Negage", "Puri", "Quimbele", "Quitexe",
                                   "Sanza Pombo", "Songo", "Uíge", "Zombo"]
            },
            "Zaire": {
                "coords": {"lat": -6.0000, "lon": 13.5000},
                "municipalities": ["Cuimba", "M'banza-Kongo", "Noqui",
                                   "Nzeto", "Soyo", "Tomboco"]
            }
        }

        for province_name, info in ao_data.items():
            province = AdministrativeDivision.query.filter_by(
                name=province_name, level=1, country_id=ao_id
            ).first()
            if not province:
                province = AdministrativeDivision(
                    name=province_name, level=1, country_id=ao_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(province)
                db.session.flush()
                print(f"  -> Province : {province_name}")

            for mun_name in info["municipalities"]:
                mun = AdministrativeDivision.query.filter_by(
                    name=mun_name, level=2, parent_id=province.id
                ).first()
                if not mun:
                    mun = AdministrativeDivision(
                        name=mun_name, level=2, country_id=ao_id, parent_id=province.id
                    )
                    db.session.add(mun)

        db.session.commit()
        print("Angola : OK")

        # ================================================================
        # ESWATINI (ID: 748)
        # ================================================================
        print("\n--- Initialisation de l'Eswatini (ID: 748) ---")
        sz_id = 748
        sz = Country.query.get(sz_id)
        if not sz:
            sz = Country(id=sz_id, name="Eswatini", iso_code="SZ")
            db.session.add(sz)
            db.session.commit()
            print("Pays Eswatini créé.")

        sz_data = {
            "Hhohho": {
                "coords": {"lat": -26.0000, "lon": 31.1667},
                "tinkhundla": ["Lobamba", "Mbabane", "Ngwane Park", "Nhlangano",
                               "Piggs Peak", "Bulembu", "Ethandakukhanya",
                               "Mahlangatsha", "Ngwempisi", "Hhukwini"]
            },
            "Lubombo": {
                "coords": {"lat": -26.5000, "lon": 31.8333},
                "tinkhundla": ["Big Bend", "Lomahasha", "Nhlangano", "Nsoko",
                               "Siteki", "Siphofaneni", "Mhlume", "Hlatikhulu",
                               "Mpuluzi", "Tikhuba"]
            },
            "Manzini": {
                "coords": {"lat": -26.4833, "lon": 31.3667},
                "tinkhundla": ["Luyengo", "Manzini", "Matsapha", "Malkerns",
                               "Mankayane", "Mbelebeleni", "Kwaluseni",
                               "Mphalaleni", "Ngolweni", "Siphocosini"]
            },
            "Shiselweni": {
                "coords": {"lat": -27.0667, "lon": 31.4167},
                "tinkhundla": ["Hlatikhulu", "Lavumisa", "Nhlangano",
                               "Nkomazi", "Zombodze", "Hhelehhele",
                               "Hosea", "Mtsambama", "Sandleni", "Zilweleni"]
            }
        }

        for region_name, info in sz_data.items():
            region = AdministrativeDivision.query.filter_by(
                name=region_name, level=1, country_id=sz_id
            ).first()
            if not region:
                region = AdministrativeDivision(
                    name=region_name, level=1, country_id=sz_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(region)
                db.session.flush()
                print(f"  -> Région : {region_name}")

            for inkhundla_name in info["tinkhundla"]:
                inkhundla = AdministrativeDivision.query.filter_by(
                    name=inkhundla_name, level=2, parent_id=region.id
                ).first()
                if not inkhundla:
                    inkhundla = AdministrativeDivision(
                        name=inkhundla_name, level=2, country_id=sz_id, parent_id=region.id
                    )
                    db.session.add(inkhundla)

        db.session.commit()
        print("Eswatini : OK")

        # ================================================================
        # LESOTHO (ID: 426)
        # ================================================================
        print("\n--- Initialisation du Lesotho (ID: 426) ---")
        ls_id = 426
        ls = Country.query.get(ls_id)
        if not ls:
            ls = Country(id=ls_id, name="Lesotho", iso_code="LS")
            db.session.add(ls)
            db.session.commit()
            print("Pays Lesotho créé.")

        ls_data = {
            "Berea": {
                "coords": {"lat": -29.2333, "lon": 27.7167},
                "constituencies": ["Berea East", "Berea West", "Koeneng",
                                   "Mafeteng", "Mapoteng", "Peka",
                                   "Senqu", "Thabana-Morena"]
            },
            "Butha-Buthe": {
                "coords": {"lat": -28.7667, "lon": 28.2500},
                "constituencies": ["Butha-Buthe", "Hololo", "Koro-Koro",
                                   "Motete", "Muela", "Ngoajane"]
            },
            "Leribe": {
                "coords": {"lat": -28.8667, "lon": 28.0333},
                "constituencies": ["Fobane", "Ha Lejone", "Khabo",
                                   "Leribe", "Liqhobong", "Mafube",
                                   "Maisa", "Malimong", "Mechachane",
                                   "Motete", "Tsikoane"]
            },
            "Mafeteng": {
                "coords": {"lat": -29.8167, "lon": 27.2333},
                "constituencies": ["Mafeteng East", "Mafeteng West",
                                   "Matelile", "Mekaling", "Mpharane",
                                   "Tajane", "Tsoaring"]
            },
            "Maseru": {
                "coords": {"lat": -29.3167, "lon": 27.4833},
                "constituencies": ["Kolonyama", "Likotsi", "Lithabaneng",
                                   "Mafube", "Maseru Central", "Maseru East",
                                   "Maseru West", "Motimposo", "Thaba-Bosiu",
                                   "Thamae", "Tsosane"]
            },
            "Mohale's Hoek": {
                "coords": {"lat": -30.1500, "lon": 27.4667},
                "constituencies": ["Bereng", "Khoelenya", "Mohale's Hoek",
                                   "Mpiti", "Qalabane", "Semena",
                                   "Tele Bridge"]
            },
            "Mokhotlong": {
                "coords": {"lat": -29.2833, "lon": 29.0667},
                "constituencies": ["Mapholaneng", "Mokhotlong", "Moremoholo",
                                   "Motete", "Sani", "Senqu"]
            },
            "Qacha's Nek": {
                "coords": {"lat": -30.1167, "lon": 28.6833},
                "constituencies": ["Qacha's Nek", "Sehlabathebe", "Semena",
                                   "Tele", "Tsoelike"]
            },
            "Quthing": {
                "coords": {"lat": -30.3833, "lon": 27.7000},
                "constituencies": ["Mphaki", "Quthing East", "Quthing West",
                                   "Sinxele", "Tosing"]
            },
            "Thaba-Tseka": {
                "coords": {"lat": -29.5167, "lon": 28.6000},
                "constituencies": ["Katse", "Lesobeng", "Linakeng",
                                   "Mpiti", "Thaba-Tseka", "Thaba-Moea"]
            }
        }

        for district_name, info in ls_data.items():
            district = AdministrativeDivision.query.filter_by(
                name=district_name, level=1, country_id=ls_id
            ).first()
            if not district:
                district = AdministrativeDivision(
                    name=district_name, level=1, country_id=ls_id,
                    latitude=info["coords"]["lat"], longitude=info["coords"]["lon"]
                )
                db.session.add(district)
                db.session.flush()
                print(f"  -> District : {district_name}")

            for constituency_name in info["constituencies"]:
                constituency = AdministrativeDivision.query.filter_by(
                    name=constituency_name, level=2, parent_id=district.id
                ).first()
                if not constituency:
                    constituency = AdministrativeDivision(
                        name=constituency_name, level=2, country_id=ls_id, parent_id=district.id
                    )
                    db.session.add(constituency)

        db.session.commit()
        print("Lesotho : OK")

        # ================================================================
        # RÉSUMÉ FINAL
        # ================================================================
        print("\n" + "="*58)
        print("Succès : Toutes les données d'Afrique Australe sont à jour !")
        print("  - Afrique du Sud  (ID: 710) :  9 provinces")
        print("  - Namibie         (ID: 516) : 14 régions")
        print("  - Botswana        (ID:  72) : 10 districts")
        print("  - Zimbabwe        (ID: 716) : 10 provinces")
        print("  - Mozambique      (ID: 508) : 11 provinces")
        print("  - Zambie          (ID: 894) : 10 provinces")
        print("  - Malawi          (ID: 454) :  3 régions")
        print("  - Angola          (ID:  24) : 18 provinces")
        print("  - Eswatini        (ID: 748) :  4 régions")
        print("  - Lesotho         (ID: 426) : 10 districts")
        print("="*58)

if __name__ == "__main__":
    seed_data()