# TranCIT/route_input/jeepney_data.py

LANDMARKS = {
    # 01C Specific - Sambag/Urgello Area
    "V. Rama Ave": (10.3098, 123.8864), 
    "USC South Campus": (10.3005, 123.8880), # "Girls High"
    "J. Alcantara": (10.3000, 123.8916),
    "E-Mall": (10.2983, 123.8937),
    "Leon Kilat": (10.2966, 123.8963),

    # 01C Specific - Downtown/Colon
    "Colon": (10.2967, 123.9020),
    "Metro Colon": (10.2967, 123.8982),
    "Colonnade": (10.2973, 123.8989),
    "Gaisano Main": (10.2976, 123.9022),
    "UV Main": (10.2987, 123.9013),
    "Colon Obelisk": (10.2982, 123.9036),
    "Mabini": (10.2982, 123.9038),
    "Zulueta": (10.2988, 123.9050),
    
    # 01C Specific - Pier Area
    "MJ Cuenco": (10.3002, 123.9064),
    "T. Padilla": (10.3022, 123.9072),
    "Benedicto": (10.3037, 123.9094),
    "Gen Maxilom Ext": (10.3037, 123.9127),
    "Pier 4": (10.3038, 123.9125),
    "Pier 3": (10.2987, 123.9084),
    
    # 01C Specific - Return Trip (Pier to Sambag)
    "V. Sotto St": (10.2950, 123.9070),
    "CTU Main": (10.2950, 123.9060), # Cebu Tech University
    "V. Gullas St": (10.2945, 123.9030),
    "D. Jakosalem St": (10.2960, 123.9040),
    "Sanciangko St": (10.2970, 123.8970),
    "UC Main": (10.2975, 123.8970), # University of Cebu

    # Sambag / Urgello / Private Area
    "Sambag 1": (10.3060, 123.8905),
    "Private": (10.3005, 123.8915), # Junction of V. Rama & J. Alcantara
    "ACT": (10.2985, 123.8940), # Asian College of Technology
    "Sacred Heart Hospital": (10.3035, 123.8895), # Already added, verifying
    "South Western University": (10.3020, 123.8886), # Already added
    "Urgello St": (10.3035, 123.8895),

    # Downtown / Heritage Area
    "Sandiego-Yap Ancestral House": (10.2986, 123.9038),
    "Parian": (10.2982, 123.9038), # Already added
    "GV Tower Hotel": (10.2975, 123.8975),
    "Sogo Hotel": (10.2972, 123.8978),
    "Legaspi St": (10.2950, 123.9020),
    "Pelaez St": (10.2980, 123.8980),
    "Junquera St": (10.2985, 123.8990),

    # Reclamation / North Area
    "NSO (PSA)": (10.3030, 123.9075), # MJ Cuenco
    "A. Soriano Ave": (10.3100, 123.9150),
    "Queen City Memorial Garden": (10.3090, 123.9135),
    "CICC": (10.3235, 123.9355), # Cebu International Convention Center
    "S&R Membership Shopping": (10.3220, 123.9330),
    "EO Perez St": (10.3220, 123.9280), # CD Seno / Ouano area
    "C. Arellano Blvd": (10.2920, 123.9080), # Pier area
    # Downtown Streets (02B Specific)
    "P. Burgos St": (10.2950, 123.9025), # Near Cathedral
    "F. Urdaneta St": (10.2935, 123.9030), # Near Plaza Independencia
    "Legaspi Ext": (10.2925, 123.9060),
    "Sergio Osmena Blvd": (10.2980, 123.9100), # Main road along piers
    
    # Reclamation / Pier Area (02B Specific)
    "Pier 5": (10.3065, 123.9145),
    "Robinsons Galleria Cebu": (10.3028, 123.9114), # "Robinson Mall"
    "Cebu City Health": (10.3052, 123.9105), # Gen Maxilom Ext
    "Bureau of Quarantine": (10.3055, 123.9100),
    
    # MJ Cuenco / Tejero Area
    "CPILS": (10.3048, 123.9088), # Benedicto/MJ Cuenco
    "A. Bonifacio St": (10.3010, 123.9050),
    "JC Zamora St": (10.2975, 123.9020),
    # Mabolo / Panagdait Area
    "Cityscape Hotel": (10.3235, 123.9215),
    "Panagdait": (10.3225, 123.9185), # Already added
    "Sykes": (10.3225, 123.9185), # Already added
    "Rainforest Park": (10.3220, 123.9200), # Already added
    "Sarrosa Hotel": (10.3245, 123.9160),
    "Castle Peak": (10.3242, 123.9131), # Already added
    "Carmelite Monastery": (10.3185, 123.9135),
    "Mabolo Church": (10.3146, 123.9140), # Already added
    "The Persimmon": (10.3125, 123.9100),
    "Carreta Cemetery": (10.3090, 123.9085),
    "Hipodromo": (10.3100, 123.9050),
    "Sindulan": (10.3180, 123.9150),
    "Cabantan St": (10.3185, 123.9085),
    "Juan Luna Ave": (10.3150, 123.9100),

    # Mango Ave / Uptown
    "USC North Campus": (10.3140, 123.8970),
    "Horizons 101": (10.3125, 123.8975),
    "Mango Square": (10.3115, 123.8965),
    "National Bookstore (Mango)": (10.3112, 123.8960),
    "Robinsons Place": (10.3110, 123.8935), # Fuente
    "Crown Regency": (10.3095, 123.8925),
    
    # Downtown / Carbon Specifics
    "Progreso St": (10.2925, 123.8995),
    "Senior Citizens Plaza": (10.2925, 123.9015),
    "Basilica Sto Nino": (10.2942, 123.9020),
    "La Nueva (City Hall)": (10.2930, 123.9018),
    "Prince Warehouse (City Hall)": (10.2932, 123.9015),
    "MCWD": (10.2945, 123.9045),
    "DFA": (10.2935, 123.9040),
    "USJR": (10.2930, 123.8990), # Carbon Campus
    "Lincoln St": (10.2935, 123.9005),

        # Lahug Area
    "JY Square": (10.3296, 123.8987),
    "USP": (10.3245, 123.9030), # University of Southern Philippines
    "Marco Polo": (10.3425, 123.8920), # For 04I
    "Busay": (10.3550, 123.8890), # For 04I
    "Plaza Housing": (10.3455, 123.8850), # For 04H
    "Camp Lapu-Lapu": (10.3350, 123.9020),

    # Gorordo / Mango / Ramos Loop
    "Gorordo": (10.3180, 123.9000),
    "CIC": (10.3165, 123.9015), # Colegio de la Inmaculada Concepcion
    "Ramos Market": (10.3095, 123.8950),
    "Velez Hospital": (10.3085, 123.8945),
    "Robinson's Fuente": (10.3110, 123.8935),
    "Capitol": (10.3160, 123.8915),
    
    # Mabolo Specific
    "Andok's Mabolo": (10.3150, 123.9135),
    "Juan Luna": (10.3120, 123.9100),
    # Lahug / Busay / Plaza Housing Area
    "Camp Lapu-Lapu": (10.3366, 123.9019), # Already added
    "Salinas Drive": (10.3270, 123.9050),
    "JY Square": (10.3296, 123.8987), # Already added
    "UP Cebu": (10.3228, 123.8985), # Already added
    "Harolds Hotel": (10.3180, 123.8965),
    "Mormons Church (Lahug)": (10.3320, 123.8985),
    "Lahug Brgy Hall": (10.3310, 123.8985),
    "Sudlon": (10.3350, 123.8990), # Corner Sudlon
    "Beverly Hills": (10.3380, 123.8950), # Junction
    "Dep-Ed (Ecotech)": (10.3230, 123.8990),
    "Marco Polo": (10.3425, 123.8920), # Already added
    "Plaza Housing": (10.3455, 123.8850), # Already added
    "Busay": (10.3550, 123.8890), # Already added
    "Cebu Transcentral Highway": (10.3600, 123.8800), # General point
    "Cebu Veterans Drive": (10.3500, 123.8900), # Road to Busay

    # Escario / Capitol / Fuente / Jones
    "Escario St": (10.3165, 123.8960), # Already added
    "Capitol": (10.3160, 123.8915), # Already added
    "Cebu Doctors Hospital": (10.3145, 123.8925), # Already added
    "Fuente Osmena": (10.3109, 123.8937), # Already added
    "Robinsons Fuente": (10.3110, 123.8935), # Already added
    "Crown Regency": (10.3095, 123.8925), # Already added
    "Jones (Osmena Blvd)": (10.3075, 123.8959), # Already added
    "Abellana Sports Complex": (10.3020, 123.8950), # Already added
    "Cebu Normal University": (10.3010, 123.8955), # Already added
    "SSS": (10.3045, 123.8995), # Already added
    "Golden Peak": (10.3175, 123.9005), # Already added
    "Philhealth": (10.3170, 123.9000), # Near Golden Peak
    "Asilo dela Milagrosa": (10.3160, 123.8980),
    "Camp Sotero (Police Station)": (10.3150, 123.8990), # Gorordo
    "Fooda Mango": (10.3120, 123.8975),
    "Mango Square": (10.3115, 123.8965), # Already added
    "National Bookstore (Mango)": (10.3112, 123.8960), # Already added
    "Summit Circle Hotel": (10.3105, 123.8940), # Near Fuente
    "Cebu Institute of Medicine": (10.3090, 123.8940),
    "Diplomat Hotel": (10.3080, 123.8950), # F. Ramos

    # Downtown / Carbon / Colon
    "Metro Colon": (10.2967, 123.8982), # Already added
    "USJR": (10.2930, 123.8990), # Already added
    "Carbon Market": (10.2923, 123.8985), # Already added
    "City Hall": (10.2935, 123.9015), # Already added
    "Basilica Sto Nino": (10.2942, 123.9020), # Already added
    "La Nueva (City Hall)": (10.2930, 123.9018), # Already added
    "MCWD": (10.2945, 123.9045), # Already added
    "Colonnade": (10.2973, 123.8989), # Already added
    "Pelaez St": (10.2980, 123.8980), # Already added
    "USC Main": (10.2993, 123.8983), # Already added
    "Sto Rosario Church": (10.2995, 123.8975),
    "Central Bank": (10.3000, 123.8965), # Jones
    "E-Mall": (10.2983, 123.8937), # Already added
    "Magallanes St": (10.2930, 123.9010), # Already added
    "Tabo-an Market": (10.2955, 123.8911), # Already added
    "Tupas St": (10.2920, 123.8890), # Pasil area
    "DFA": (10.2935, 123.9040), # Already added
    "Legaspi St": (10.2950, 123.9020), # Already added
    "Cebu Eastern College": (10.2960, 123.8995), # Dimasalang
    "Gaisano Main": (10.2976, 123.9022), # Already added
    "UV Main": (10.2987, 123.9013), # Already added
    "Ramos Market": (10.3095, 123.8950), # Already added
    "F. Ramos St": (10.3080, 123.8950),
    "Junquera St": (10.2985, 123.8990), # Already added
    "Sanciangko St": (10.2970, 123.8970), # Already added

    # Ayala / SM Area (for 04L/M)
    "Ayala Center Cebu": (10.3190, 123.9050), # Already added
    "Cebu Business Park": (10.3182, 123.9037), # Already added
    "Pag-IBIG Fund (Ayala)": (10.3170, 123.9060), # Already added
    "Cardinal Rosales Ave": (10.3175, 123.9070),
    "Pope John Paul II Ave": (10.3150, 123.9100),
    "Carmelite Monastery": (10.3185, 123.9135), # Already added
    "Mabolo Church": (10.3146, 123.9140), # Already added
    "SM City": (10.3118, 123.9180), # Already added
    "Radisson Blu": (10.3110, 123.9190),
    "Cebu Daily News": (10.3100, 123.9160), # Kaohsiung St
    "TESDA": (10.3272, 123.9050), # Already added
    "IT Park": (10.3295, 123.9056), # Already added
    "Waterfront Hotel": (10.3247, 123.9044), # Already added

    # Guadalupe / V. Rama Area
    "Crown Regency Residences": (10.3180, 123.8885), # V. Rama
    "Corner Banawa": (10.3140, 123.8900), # Intersection of V. Rama/Banawa
    "SEC": (10.3080, 123.8890), # Securities and Exchange Commission (V. Rama)
    "Calamba Cemetery": (10.3060, 123.8900),
    "Queensland Hotel": (10.3030, 123.8910), # Near V. Rama/N. Bacalso
    "Salazar Colleges": (10.2970, 123.8920), # N. Bacalso

    # San Nicolas / Pasil / Tabo-an Area
    "San Nicolas Elementary": (10.2960, 123.8895),
    "B. Aranas St": (10.2950, 123.8900),
    "Carlos Gothong HS": (10.2940, 123.8860),
    "R. Padilla St": (10.2920, 123.8800), # Duljo Fatima area
    
    # Downtown / Carbon Specifics
    "Plaridel St": (10.2940, 123.9000),
    "MC Briones": (10.2930, 123.9010), # Near City Hall
    "Bo's Coffee (Jones)": (10.3155, 123.8930), # Near Capitol/Jones

    # Banawa Specifics
    "R. Duterte St": (10.3130, 123.8860),
    "Rustans Banawa": (10.3135, 123.8825), # The Market by Rustan's
    "P. Lopez St": (10.2945, 123.8995), # Near USJR

    # Alumnos / Mambaling Specifics
    "Cacoy Doce Pares": (10.2935, 123.8835), # C. Padilla
    "San Roque (Mambaling)": (10.2900, 123.8750),

    # Basak / Quiot Area
    "Quiot (Basak Ibabao)": (10.2930, 123.8630),
    "Sabellano St": (10.2910, 123.8645),
    "Bayanihan Village": (10.2890, 123.8635),
    "Basak Night High School": (10.2930, 123.8670),
    "Don Vicente Rama Memorial NHS": (10.2925, 123.8665),
    "USJ-R Basak (High School)": (10.2935, 123.8675),
    
    # N. Bacalso Landmarks
    "SCSIT": (10.2970, 123.8920), # Salazar Colleges
    "Citilink Terminal": (10.2975, 123.8930),
    "Mambaling Flyover": (10.2900, 123.8720),
    "Fooda Mambaling": (10.2910, 123.8715),
    "Shopwise Mambaling": (10.2915, 123.8710), # Already added, verifying
    
    # Downtown / Historic
    "Shamrock (P. Burgos)": (10.2945, 123.9025),
    "USPF (Old Campus/Mabini)": (10.2982, 123.9040),
    "Magellan's Cross": (10.2935, 123.9020),
    "Lucky 7 Supermarket": (10.2945, 123.9025),
    "Duljo Fatima": (10.2915, 123.8780),
    
    # Bulacao / Pardo Specifics
    "St. Paul College (Bulacao)": (10.2640, 123.8515),
    "Citi Hardware (Bulacao)": (10.2675, 123.8530),
    "Prince Warehouse (Bulacao)": (10.2690, 123.8540),
    "Napolcom": (10.2975, 123.8910), # Near South Bus
    "Aerol Pensione House": (10.2995, 123.8940), # Near CCMC/N. Bacalso

    # Downtown / Colon Area
    "138 Mall": (10.2972, 123.8995), # Near Colonnade
    "Manalili St": (10.2938, 123.9025), # Already added, verifying
    "V. Gullas St": (10.2945, 123.9030), # Already added
    "Borromeo St": (10.2950, 123.8980), # Already added
    "Panganiban St": (10.2960, 123.8950), # Already added
    
    # Reclamation / White Gold Area
    "DSWD": (10.3050, 123.9085), # MJ Cuenco/Imus
    "Cebu City Civil Registrar": (10.3060, 123.9110), # Near White Gold
    "Queen City Memorial Garden": (10.3090, 123.9135), # Already added

    # Inayawan / Pardo Area
    "Inayawan Church": (10.2722, 123.8585), # San Agustin de Hippo
    "Rizal Ave Ext": (10.2750, 123.8550), # Road connecting Pardo/Inayawan
    "Cogon Pardo": (10.2820, 123.8600),
    
    # ... existing landmarks ...

    # Labangon / Tisa Specifics
    "Punta Princesa": (10.2943, 123.8701), # Already added
    "Punta Princesa Church": (10.2940, 123.8695), # Lourdes Parish
    "Brgy Tisa": (10.3000, 123.8780),
    "Gaisano Tisa": (10.2990, 123.8770),
    "F. Llamas St": (10.2980, 123.8750),
    "Salvador St": (10.3060, 123.8880), # Already added
    "Salvador Extension": (10.3080, 123.8860),
    
    # Reclamation / Pier Area (12G/12I)
    "APM Mall": (10.3110, 123.9165), # Near SM
    "Cebu Institute of Technology (Recla)": (10.3100, 123.9160), # CIA
    "Sugbutel": (10.3060, 123.9140),
    "PCSO": (10.3050, 123.9130),
    "Fort San Pedro": (10.2925, 123.9055),
    "Pacific Tourist Inn": (10.2955, 123.8990),
    "Manila Foodshoppe": (10.2940, 123.9020), # Manalili

    # Talamban / Pit-os Extension
    "H. Abella St": (10.3720, 123.9190), # Near Tintay
    "Bacayan": (10.3850, 123.9200),
    "Cebu North General Hospital": (10.3780, 123.9185),
    "The Family Park": (10.3620, 123.9140),
    "Paradise Village": (10.3350, 123.9110),
    "Cebu Country Club": (10.3300, 123.9100),
    "Samantabhadra Institute": (10.3280, 123.9080),
    "Oakridge Business Park": (10.3420, 123.9170),

    # Ayala Business Park Specifics
    "Samar Loop": (10.3175, 123.9060),
    "Luzon Ave": (10.3185, 123.9065),
    "Metro Ayala": (10.3190, 123.9055),
    "Marriot Hotel": (10.3180, 123.9050), # Now Seda
    "Hotel Elizabeth": (10.3185, 123.9025),
    "Tune Hotels": (10.3190, 123.9030), # Red Planet
    "Mactan St": (10.3160, 123.9080), # Access to Ayala
    "Leyte Loop": (10.3155, 123.9065),

    # Ramos / Echavez Area
    "Allson's Inn": (10.3120, 123.9020),
    "Zapatera Brgy Hall": (10.3090, 123.9010),
    "Junquera Ext": (10.3010, 123.8980),
    
    # Mandaue / AS Fortuna
    "Cebu Home & Builders": (10.3440, 123.9200),
    "Allure Hotel": (10.3390, 123.9260),
    "Benedicto College": (10.3350, 123.9330),
    "The Orchard": (10.3360, 123.9310),
    "Guizo": (10.3290, 123.9360),
    "Mantuyong": (10.3270, 123.9380),
    "Sosyoland": (10.3250, 123.9390),
    "Mandaue Sports Complex": (10.3230, 123.9400),
    "St. Joseph Parish (Mandaue)": (10.3250, 123.9440), # National Shrine
    "St. Joseph Academy": (10.3255, 123.9445),
    
    # 14D Specifics (Ramos / Osmena Blvd)
    "Saint Paul College Foundation (Ramos)": (10.3120, 123.8945),
    "Robinsons Cybergate": (10.3115, 123.8930), # Already added, verifying
    "Chong Hua Hospital": (10.3100, 123.8922), # Already added
    "Landbank (Osmena Blvd)": (10.3000, 123.8975), # Near P. del Rosario
    "Central Bank": (10.3000, 123.8965), # Near Abellana
    "Philhealth": (10.3170, 123.9000), # Already added
    
    # 15 Specifics (Oppra / Kalunasan)
    "Oppra (Kalunasan)": (10.3250, 123.8850), # Terminal area
    "Unitop (Colon)": (10.2965, 123.9000),
    "Kalunasan": (10.3300, 123.8800),

    # Apas / IT Park Internal Streets
    "Apas": (10.3374, 123.9044), # Barangay Hall area
    "Wilson St": (10.3350, 123.9040),
    "Omega St": (10.3340, 123.9045),
    "San Miguel Rd": (10.3330, 123.9050),
    "Skyrise 1": (10.3310, 123.9060),
    "Skyrise 2": (10.3312, 123.9065),
    "Skyrise 3": (10.3300, 123.9070),
    "Inez Villa St": (10.3305, 123.9060),
    "J. Maria del Mar St": (10.3290, 123.9055),
    "W. Geonzon St": (10.3280, 123.9050), # IT Park Entrance
    "Convergys (IT Park)": (10.3300, 123.9055), # Near i1 building
    
    # Gorordo / Lahug
    "USP-F (Lahug)": (10.3245, 123.9030), # University of Southern Philippines Foundation
    "Lahug High School": (10.3235, 123.8990),
    "Tonros Apartelle": (10.3190, 123.8970),
    "Handuraw Pizza (Lahug)": (10.3200, 123.8975),
    "Turtles Nest": (10.3185, 123.8980),
    
    # Ramos / Mango Area
    "Royal Concourse": (10.3170, 123.8985),
    "The Beat": (10.3120, 123.8970),
    "Raintree Mall": (10.3115, 123.8960),
    "Cogon Ramos": (10.3095, 123.8960),
    
    # Downtown Deviations
    "Taboan Dried Fish Market": (10.2950, 123.8910),
    "Cebu Grand Hotel": (10.3160, 123.8950), # Near Escario
    "Hotel de Mercedes": (10.2975, 123.8985), # Pelaez St

    # Mandaue - Reclamation / Centro Area
    "CICC": (10.3235, 123.9355), # Cebu International Convention Center
    "Uwell": (10.3260, 123.9370), # Near Guizo
    "Sosyoland": (10.3250, 123.9390), # Mantuyong area
    "Colonnade Mandaue": (10.3255, 123.9400), 
    "Mandaue Public Market (New)": (10.3240, 123.9445), # Behind City Hall/Sports Complex
    "BIR Mandaue": (10.3230, 123.9460),
    "Bureau of Immigration Mandaue": (10.3245, 123.9435), # J. Centre usually, but based on route description near City Hall
    "Mandaue City Hall": (10.3275, 123.9430), # Already added
    "St. Joseph Parish (Mandaue)": (10.3250, 123.9440), # Already added
    "Mandaue Coliseum": (10.3285, 123.9450),
    "Centro Mandaue": (10.3254, 123.9418),
    "Gaisano Grand Mandaue": (10.3260, 123.9425), # Centro

    # Mandaue - Highway / Maguikay / Pacific Mall
    "Estancia-Ibabao": (10.3350, 123.9480),
    "Super Metro Mandaue": (10.3380, 123.9500),
    "Pacific Mall": (10.3415, 123.9525), # Already added
    "DFA Mandaue": (10.3420, 123.9530), # Inside/Near Pacific Mall
    "Maguikay Flyover": (10.3430, 123.9400),
    "Coca Cola Plant": (10.3350, 123.9350), # Highway Seno
    "San Miguel Brewery": (10.3280, 123.9340),
    
    # Mandaue - Streets
    "SB Cabahug St": (10.3300, 123.9460),
    "UN Ave": (10.3350, 123.9550),
    "Plaridel St": (10.3300, 123.9500),
    "AC Cortes Ave": (10.3350, 123.9400),
    "A. Del Rosario St": (10.3280, 123.9380),
    "Wireless": (10.3220, 123.9320), # Subangdaku boundary
    "Subangdaku": (10.3194, 123.9258), # Already added
    "Tipolo": (10.3270, 123.9350),
    
    # Ayala Access
    "Dela Montana St": (10.3160, 123.9120), # Pope John Paul II Ave
    "Cardinal Rosales Ave": (10.3175, 123.9070), # Already added
    "Mindanao Ave": (10.3185, 123.9060), # Cebu Business Park

    # Subangdaku / Reclamation Access
    "Innodata": (10.3205, 123.9275),
    "CD Seno St": (10.3250, 123.9330), # Near Tipolo/Guizo
    "Albano St": (10.3200, 123.9280),
    "M. Logarta Ave": (10.3150, 123.9190), # North Bus/SM area
    "Aboitiz Football Field": (10.3160, 123.9210),
    
    # White Gold / Pier Area Specifics
    "G. Gaisano St": (10.3050, 123.9120),
    "SM Hypermarket": (10.3115, 123.9185),
    
    # Mandaue Specifics
    "Hi-Land": (10.3320, 123.9530), # UN Ave area
    "Prince Warehouse Mandaue": (10.3310, 123.9480), # AC Cortes
    "PJ Burgos St": (10.3260, 123.9420), # Near City Hall

    # Mandaue Streets / Specifics
    "Ouano (Mandaue Terminal)": (10.3230, 123.9440), # Near Market/City Hall
    "A. Mabini St": (10.3260, 123.9435),
    "B. Ceniza St": (10.3255, 123.9405),
    "Lopez Jaena St": (10.3220, 123.9280), # Subangdaku Highway
    "W.O. Seno St": (10.3240, 123.9340), # Near Parkmall
    "Albano St": (10.3200, 123.9280), # Subangdaku
    "Ginebra San Miguel": (10.3290, 123.9330),
    "CIC Mandaue": (10.3310, 123.9320), # Colegio de la Inmaculada Concepcion
    "Norkis Cyberpark": (10.3360, 123.9320), # AS Fortuna
    "Larsian Banilad": (10.3400, 123.9230), # Near Oakridge
    "JL Briones St": (10.3220, 123.9380), # Reclamation

    # Cebu City Specifics
    "Plaza Humabon": (10.2960, 123.9025), # Near Cathedral
    "F. Urdaneta St": (10.2935, 123.9030), # Already added, verifying
    "13th Ave": (10.3050, 123.9120), # Reclamation
    "Cebu Chinese Cemetery": (10.3110, 123.9050), # MJ Cuenco
    "F. Cabahug St": (10.3150, 123.9130), # Panagdait/Mabolo
    
    # Opon / Lapu-Lapu Town Proper
    "Opon PUJ Terminal": (10.3145, 123.9535),
    "ML Quezon Ave": (10.3180, 123.9600),
    "Old Mactan-Mandaue Bridge": (10.3220, 123.9560),
    "General Milling Corp": (10.3160, 123.9550),
    "Metro Mactan": (10.3150, 123.9540),
    "Mantawe Rd": (10.3160, 123.9520),
    "Ompad St": (10.3150, 123.9510),
    "GY dela Serna St": (10.3140, 123.9520),
    "La Nueva (Opon)": (10.3135, 123.9530),

    # Mandaue / AC Cortes / Reclamation
    "UCLM": (10.3295, 123.9515), # University of Cebu Lapu-Lapu Mandaue
    "Natures Spring Plant": (10.3300, 123.9490),
    "STI Mandaue": (10.3320, 123.9450),
    "Mandaue Catholic Cemetery": (10.3310, 123.9430),
    "P. Larazzabal Ave": (10.3220, 123.9350),
    "Chong Hua Hospital (Mandaue)": (10.3235, 123.9345),
    "MO2 Westown": (10.3230, 123.9340),
    "St. James Amusement Park": (10.3240, 123.9380),
    "Mandaue City College": (10.3250, 123.9400),
    "Hotel Nenita": (10.3315, 123.9500),
    "Metro Fresh & Easy": (10.3320, 123.9510),
    "Bridges Town Square": (10.3325, 123.9520),
    "Umapad": (10.3330, 123.9530),

    # Mactan North / Punta Engaño
    "New Mactan-Mandaue Bridge": (10.3270, 123.9630),
    "Pusok": (10.3280, 123.9700),
    "Marina Mall": (10.3290, 123.9770),
    "Savemore Mactan": (10.3295, 123.9765),
    "MEPZ 1 Gates": (10.3320, 123.9800),
    "Ibo": (10.3350, 123.9850),
    "Buaya": (10.3400, 123.9950),
    "Mactan Shrine": (10.3122, 124.0152), # Already added, verifying
    "Movenpick Resort": (10.3080, 124.0230),
    "Abaca Boutique Resort": (10.3090, 124.0250),
    "Be Resort": (10.3100, 124.0260),
    "Palm Beach Resort": (10.3110, 124.0270),
    "Amisa Residences": (10.3150, 124.0320),
    "Discovery Bay Hotel": (10.3160, 124.0330),
    
    # Consolacion / North Road
    "Corner Canduman": (10.3550, 123.9380),
    "Insular Square": (10.3580, 123.9450),
    "Paknaan": (10.3500, 123.9500),
    "Bagong Daan": (10.3800, 123.9800),

    # Ayala / Business Park Specifics
    "Quest Hotel": (10.3175, 123.9040), # Arch Reyes
    "Hongkong Plaza Hotel": (10.3185, 123.9020),
    "Sorsogon Rd": (10.3165, 123.9055),
    "Negros Rd": (10.3170, 123.9065),
    "Keppel Tower": (10.3165, 123.9055), # Already added, verifying
    "San Carlos Seminary": (10.3170, 123.9110), # Pope John Paul II Ave

    # Downtown / Historic
    "The Freeman": (10.2955, 123.9035), # Corner V. Gullas/D. Jakosalem
    "Bayantel": (10.3030, 123.9030), # Sikatuna St
    "Zapatera": (10.3090, 123.9010), # Brgy Hall

    # Lapu-Lapu City / Opon Poblacion
    "Opon Public Market": (10.3135, 123.9500),
    "Lapu-Lapu City Hall": (10.3155, 123.9555),
    "Gaisano Island Mall": (10.3165, 123.9560),
    "Metro Lapu-Lapu": (10.3140, 123.9510), # Super Metro
    "SSS Lapu-Lapu": (10.3220, 123.9600), # Near Pusok
    "LLC Central School": (10.3120, 123.9520),
    "P. Rodriguez St": (10.3110, 123.9515),
    "S. Osmena St (Opon)": (10.3125, 123.9495),
    "L. Jaena St (Opon)": (10.3115, 123.9505),

    # Maribago / Mactan Resorts (MI-02B)
    "Mactan Newtown": (10.3030, 124.0120), # "Mactan Ocean Town"
    "Maribago": (10.2900, 124.0000),
    "Maribago Bluewater": (10.2864, 124.0012),
    "Cebu White Sands": (10.2880, 124.0020),
    "Savemore Maribago": (10.2890, 123.9990),
    "Metro Express Maribago": (10.2910, 123.9980),
    "Highland (Mandaue)": (10.3320, 123.9530), # Near UN Ave

    # Cordova / Babag Area (MI-03A)
    "Babag 1": (10.2750, 123.9550),
    "Babag 2": (10.2650, 123.9500),
    "Deca Homes (Babag)": (10.2700, 123.9520),
    "Tiangue Rd": (10.2850, 123.9540),
    "Looc": (10.3000, 123.9530),
    "Yanadia": (10.3100, 123.9510), # Approximate

    # Basak / Tamiya Area (MI-04A)
    "Tamiya Terminal": (10.2940, 123.9610), # MEPZ 2
    "Robinsons Supermarket (Mactan)": (10.2920, 123.9605),
    "Crown Regency Suites (Mactan)": (10.3000, 123.9580),
    "MV Patalinghug Ave": (10.3050, 123.9570),

    # Opon / Ferry Terminal Area (MI-05A)
    "Hotel Cesario": (10.3235, 123.9680),
    "B.M. Dimataga St": (10.3130, 123.9500),
    "Muelle Osmena Port": (10.3110, 123.9480), # Ferry Terminal
    "Our Lady of Rule Parish": (10.3125, 123.9490), # Opon Church
    "R. Rodriguez St": (10.3135, 123.9520),
    
    # Gun-ob / Hoops Dome Area (MI-03B)
    "A. Tumulak St": (10.2900, 123.9450),
    "Gun-ob": (10.2930, 123.9450),
    "Hoops Dome": (10.2950, 123.9455),
    "Humay-humay Rd": (10.3000, 123.9480),
    "Cajulao": (10.2800, 123.9400),
    
    # Pusok / Hotels (MI-04B)
    "Dulcinea Hotel": (10.3200, 123.9630),
    "The Bellavista Hotel": (10.3225, 123.9680),
    "Goldberry Suites": (10.3220, 123.9670),
}

JEEPNEY_ROUTES = {
    "01C": {
        "description": "Private/Sambag 1 to Pier 3 via Colon/CTU/UC",
        "path": ["V. Rama Ave", "USC South Campus", "J. Alcantara", "E-Mall", "Leon Kilat", "Colon", "Metro Colon", "Colonnade", "Gaisano Main", "UV Main", "Colon Obelisk", "Mabini", "Zulueta", "MJ Cuenco", "T. Padilla", "Benedicto", "Gen Maxilom Ext", "Pier 4", "Pier 3", "V. Sotto St", "CTU Main", "V. Gullas St", "D. Jakosalem St", "Gaisano Main", "UV Main", "Sanciangko St", "UC Main", "Leon Kilat", "E-Mall", "J. Alcantara", "USC South Campus", "V. Rama Ave"]
    },
    "01B": {
        "description": "Sambag 1 to Pier 3 & 2 via Colon St.",
        "path": ["Sambag 1", "USC South Campus", "Private", "J. Alcantara", "ACT", "E-Mall", "Leon Kilat", "Gaisano Capital South", "Colon", "Metro Colon", "Colonnade", "UV Main", "Gaisano Main", "Colon Obelisk", "Mabini", "Sandiego-Yap Ancestral House", "Parian", "MJ Cuenco", "T. Padilla", "Pier 4", "Pier 3", "C. Arellano Blvd", "Pier 2", "C. Arellano Blvd", "Pier 3", "Pier 4", "T. Padilla", "Sikatuna St", "Parian", "Sanciangko St", "UV Main", "Sogo Hotel", "GV Tower Hotel", "UC Main", "Leon Kilat", "E-Mall", "ACT", "J. Alcantara", "Private", "USC South Campus", "Sambag 1"]
    },
    "01K": {
        "description": "Urgello St. to Parkmall via SM/North Bus",
        "path": ["Urgello St", "Sacred Heart Hospital", "South Western University", "E-Mall", "Leon Kilat", "Colon", "Metro Colon", "Colonnade", "UV Main", "Gaisano Main", "Parian", "Zulueta", "MJ Cuenco", "NSO (PSA)", "A. Soriano Ave", "SM City", "North Bus Terminal", "EO Perez St", "S&R Membership Shopping", "Cebu Doctors University", "CICC", "Parkmall", "CICC", "North Bus Terminal", "SM City", "White Gold", "Queen City Memorial Garden", "T. Padilla", "NSO (PSA)", "CTU Main", "Manalili St", "Legaspi St", "Colonnade", "Pelaez St", "Sanciangko St", "Sogo Hotel", "GV Tower Hotel", "E-Mall", "Urgello St", "South Western University", "Sacred Heart Hospital"]
    },
    "02B": {
        "description": "South Bus to Pier via Colon/Galleria",
        "path": ["Cebu City Medical Center", "N. Bacalso Ave", "South Bus Terminal", "E-Mall", "Leon Kilat", "Colon", "Metro Colon", "Colonnade", "Gaisano Main", "UV Main", "P. Burgos St", "Cathedral", "F. Urdaneta St", "Legaspi Ext", "Plaza Independencia", "C. Arellano Blvd", "Pier 1", "Pier 2", "Pier 3", "V. Sotto St", "Sergio Osmena Blvd", "Pier 4", "Pier 5", "Robinsons Galleria Cebu", "Gen Maxilom Ext", "White Gold", "Cebu City Health", "Bureau of Quarantine", "Imus Ave", "MJ Cuenco", "Museo Sugbo", "CPILS", "A. Bonifacio St", "Sikatuna St", "JC Zamora St", "Sanciangko St", "UV Main", "Sogo Hotel", "GV Tower Hotel", "UC Main", "E-Mall", "Panganiban St", "Cebu City Medical Center"]
    },
    "03A": {
        "description": "Mabolo (Panagdait) to Carbon via MJ Cuenco",
        "path": ["Cityscape Hotel", "Panagdait", "Sykes", "Rainforest Park", "Sarrosa Hotel", "Castle Peak", "Carmelite Monastery", "Mabolo Church", "The Persimmon", "Hipodromo", "Carreta Cemetery", "Imus Ave", "Museo Sugbo", "CPILS", "NSO (PSA)", "CTU Main", "V. Gullas St", "Gaisano Main", "Manalili St", "Colonnade", "Progreso St", "Carbon Market", "Senior Citizens Plaza", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "Prince Warehouse (City Hall)", "MCWD", "DFA", "MJ Cuenco", "CTU Main", "NSO (PSA)", "CPILS", "Museo Sugbo", "Carreta Cemetery", "The Persimmon", "Mabolo Church", "Carmelite Monastery", "Castle Peak", "Sarrosa Hotel", "Rainforest Park", "Sykes", "Panagdait", "Cityscape Hotel"]
    },
    "03B": {
        "description": "Mabolo to Colon via Jones/Mango Ave",
        "path": ["Sindulan", "Mabolo Church", "The Persimmon", "Hipodromo", "Carreta Cemetery", "Mango Ave", "USC North Campus", "Horizons 101", "Mango Square", "National Bookstore (Mango)", "Robinsons Place", "Fuente Osmena", "Crown Regency", "Jones (Osmena Blvd)", "Abellana National School", "Cebu Normal University", "SSS", "GV Tower Hotel", "Colon", "Metro Colon", "USJR", "Carbon Market", "Lincoln St", "City Hall", "La Nueva (City Hall)", "MCWD", "MJ Cuenco", "CTU Main", "NSO (PSA)", "CPILS", "Museo Sugbo", "Carreta Cemetery", "Mabolo Church", "Sindulan"]
    },
    "03L": {
        "description": "Mabolo (Cabantan) to Carbon via MJ Cuenco",
        "path": ["Cabantan St", "Juan Luna Ave", "Mabolo Church", "Carreta Cemetery", "Imus Ave", "MJ Cuenco", "NSO (PSA)", "CTU Main", "V. Gullas St", "Manalili St", "Progreso St", "Carbon Market", "City Hall", "Basilica Sto Nino", "Prince Warehouse (City Hall)", "La Nueva (City Hall)", "MCWD", "MJ Cuenco", "CTU Main", "NSO (PSA)", "CPILS", "Museo Sugbo", "Imus Ave", "Cabantan St"]
    },
    "03Q": {
        "description": "Mabolo to Colon via Ayala/Fuente",
        "path": ["Mabolo Church", "Andok's Mabolo", "Juan Luna", "Ayala", "Gorordo", "Mango Ave", "Fuente Osmena", "Jones (Osmena Blvd)", "Colon", "Mabolo Church"]
    },
    "04B": {
        "description": "Lahug to Carbon via Jones/Osmena Blvd",
        "path": ["Camp Lapu-Lapu", "Salinas Drive", "JY Square", "UP Cebu", "Harolds Hotel", "Escario St", "Capitol", "Cebu Doctors Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Jones (Osmena Blvd)", "SSS", "Metro Colon", "Magallanes St", "USJR", "Carbon Market", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MCWD", "Colonnade", "Pelaez St", "USC Main", "Sto Rosario Church", "Central Bank", "Cebu Normal University", "Abellana Sports Complex", "Fuente Osmena", "Cebu Doctors Hospital", "Capitol", "Escario St", "Golden Peak", "Philhealth", "Gorordo", "Harolds Hotel", "UP Cebu", "JY Square", "Salinas Drive", "Camp Lapu-Lapu"]
    },
    "04C": {
        "description": "Lahug to Carbon via Ramos",
        "path": ["Camp Lapu-Lapu", "JY Square", "Sudlon", "Mormons Church (Lahug)", "Lahug Brgy Hall", "UP Cebu", "Harolds Hotel", "Philhealth", "Golden Peak", "Gorordo", "Asilo dela Milagrosa", "Camp Sotero (Police Station)", "Mango Ave", "USC North Campus", "Fooda Mango", "Mango Square", "National Bookstore (Mango)", "Robinsons Fuente", "Summit Circle Hotel", "F. Ramos St", "Cebu Institute of Medicine", "Diplomat Hotel", "Junquera St", "USC Main", "Sanciangko St", "UC Main", "E-Mall", "Magallanes St", "Carbon Market", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MCWD", "DFA", "Legaspi St", "Cebu Eastern College", "Gaisano Main", "UV Main", "Ramos Market", "F. Ramos St", "Summit Circle Hotel", "Robinsons Fuente", "Mango Ave", "Mango Square", "USC North Campus", "Gorordo", "Golden Peak", "Philhealth", "Harolds Hotel", "UP Cebu", "JY Square", "Camp Lapu-Lapu"]
    },
    "04D": {
        "description": "Plaza Housing to Carbon via Tabo-an",
        "path": ["Plaza Housing", "Cebu Transcentral Highway", "Marco Polo", "JY Square", "Gorordo", "UP Cebu", "Harolds Hotel", "Escario St", "Capitol", "Cebu Doctors Hospital", "Fuente Osmena", "Robinsons Fuente", "Jones (Osmena Blvd)", "Abellana Sports Complex", "Cebu Normal University", "SSS", "Sanciangko St", "UC Main", "E-Mall", "Tabo-an Market", "Tupas St", "Magallanes St", "Carbon Market", "Basilica Sto Nino", "City Hall", "MJ Cuenco", "Jones (Osmena Blvd)", "Legaspi St", "Cathedral", "Colonnade", "Pelaez St", "USC Main", "Sto Rosario Church", "Central Bank", "Cebu Normal University", "Crown Regency", "Fuente Osmena", "Capitol", "Escario St", "Gorordo", "UP Cebu", "JY Square", "Marco Polo", "Plaza Housing"]
    },
    "04H": {
        "description": "Plaza Housing to Carbon via Jones Ave",
        "path": ["Plaza Housing", "Cebu Transcentral Highway", "Marco Polo", "JY Square", "Gorordo", "Dep-Ed (Ecotech)", "Beverly Hills", "Mormons Church (Lahug)", "UP Cebu", "Harolds Hotel", "Escario St", "Capitol", "Jones (Osmena Blvd)", "Cebu Doctors Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Vicente Sotto Hospital", "Abellana Sports Complex", "Cebu Normal University", "GV Tower Hotel", "Sanciangko St", "E-Mall", "USJR", "Carbon Market", "City Hall", "La Nueva (City Hall)", "Basilica Sto Nino", "MCWD", "DFA", "Legaspi St", "Cathedral", "Cebu Eastern College", "Colonnade", "Pelaez St", "USC Main", "Jones (Osmena Blvd)", "Abellana Sports Complex", "Crown Regency", "Fuente Osmena", "Capitol", "Escario St", "Golden Peak", "Philhealth", "Gorordo", "Harolds Hotel", "UP Cebu", "JY Square", "Marco Polo", "Plaza Housing"]
    },
    "04I": {
        "description": "Busay/Plaza Housing to Carbon via Ramos/Jones",
        "path": ["Busay", "Plaza Housing", "Cebu Transcentral Highway", "Marco Polo", "JY Square", "Gorordo", "UP Cebu", "Harolds Hotel", "Golden Peak", "Philhealth", "Asilo dela Milagrosa", "Mango Ave", "Fooda Mango", "Horizons 101", "Robinsons Fuente", "F. Ramos St", "Junquera St", "Sanciangko St", "E-Mall", "Magallanes St", "USJR", "Carbon Market", "City Hall", "La Nueva (City Hall)", "Basilica Sto Nino", "Legaspi St", "Cathedral", "Gaisano Main", "UV Main", "F. Ramos St", "Robinsons Fuente", "Mango Ave", "Horizons 101", "Gorordo", "Golden Peak", "Philhealth", "Harolds Hotel", "UP Cebu", "JY Square", "Marco Polo", "Plaza Housing", "Busay"]
    },
    "04L": {
        "description": "Lahug to SM City via Ayala/Mabolo",
        "path": ["JY Square", "Gorordo", "Sudlon", "Beverly Hills", "Dep-Ed (Ecotech)", "Mormons Church (Lahug)", "Lahug Brgy Hall", "UP Cebu", "Harolds Hotel", "Golden Peak", "Philhealth", "Cebu Business Park", "Pag-IBIG Fund (Ayala)", "Ayala Center Cebu", "Cardinal Rosales Ave", "Pope John Paul II Ave", "Carmelite Monastery", "Mabolo Church", "SM City", "Radisson Blu", "Cebu Daily News", "A. Soriano Ave", "Juan Luna Ave", "Mabolo Church", "Carmelite Monastery", "TESDA", "Salinas Drive", "IT Park", "Waterfront Hotel", "JY Square"]
    },
    "04M": {
        "description": "Ayala to Lahug (JY) Loop",
        "path": ["Ayala Center Cebu", "Gorordo", "Philhealth", "Golden Peak", "UP Cebu", "Lahug Brgy Hall", "Mormons Church (Lahug)", "Sudlon", "JY Square", "Salinas Drive", "IT Park", "Waterfront Hotel", "Ayala Center Cebu"]
    },
    "06B": {
        "description": "Guadalupe to Carbon via M. Velez/Capitol",
        "path": ["Guadalupe Church", "Fooda Guadalupe", "PRC", "M. Velez St", "Capitol", "Jones (Osmena Blvd)", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Abellana Sports Complex", "Metro Colon", "USJR", "Carbon Market", "City Hall", "Basilica Sto Nino", "Metro Colon", "Abellana Sports Complex", "Cebu Normal University", "Crown Regency", "Robinsons Fuente", "Fuente Osmena", "Cebu Doctors Hospital", "Capitol", "M. Velez St", "PRC", "Fooda Guadalupe", "Guadalupe Church"]
    },
    "06C": {
        "description": "Guadalupe to Colon via V. Rama/B. Rodriguez",
        "path": ["Guadalupe Church", "Fooda Guadalupe", "PRC", "V. Rama Ave", "B. Rodriguez St", "Vicente Sotto Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Abellana Sports Complex", "Cebu Normal University", "SSS", "Metro Colon", "Plaridel St", "MC Briones", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MCWD", "Metro Colon", "Jones (Osmena Blvd)", "Abellana Sports Complex", "Cebu Normal University", "Crown Regency", "Fuente Osmena", "Robinsons Fuente", "B. Rodriguez St", "Vicente Sotto Hospital", "V. Rama Ave", "PRC", "Fooda Guadalupe", "Guadalupe Church"]
    },
    "06H": {
        "description": "Guadalupe to SM City via Capitol/Ayala",
        "path": ["Guadalupe Church", "V. Rama Ave", "Crown Regency Residences", "Fooda Guadalupe", "Corner Banawa", "Capitol", "Bo's Coffee (Jones)", "Cebu Doctors Hospital", "Escario St", "Philhealth", "Ayala Center Cebu", "Cabantan St", "Juan Luna Ave", "Mabolo Church", "SM City", "Mabolo Church", "Ayala Center Cebu", "Asilo dela Milagrosa", "Fooda Mango", "Mango Ave", "Robinsons Fuente", "Fuente Osmena", "Vicente Sotto Hospital", "B. Rodriguez St", "V. Rama Ave", "Corner Banawa", "PRC", "Fooda Guadalupe", "Guadalupe Church"]
    },
    "06G": {
        "description": "Guadalupe to C. Padilla via V. Rama/Tabo-an",
        "path": ["Guadalupe Church", "V. Rama Ave", "Fooda Guadalupe", "PRC", "SEC", "Calamba Cemetery", "USC South Campus", "Katipunan St", "Tres de Abril", "Carlock St", "San Nicolas Elementary", "B. Aranas St", "Tabo-an Market", "Pasil Fish Market", "San Nicolas Church", "Carlos Gothong HS", "C. Padilla St", "R. Padilla St", "N. Bacalso Ave", "Salazar Colleges", "V. Rama Ave", "USC South Campus", "Queensland Hotel", "Calamba Cemetery", "SEC", "PRC", "Fooda Guadalupe", "Guadalupe Church"]
    },
    "07B": {
        "description": "Banawa to Carbon via B. Rodriguez/Capitol Loop",
        "path": ["Banawa Public Market", "R. Duterte St", "V. Rama Ave", "B. Rodriguez St", "Vicente Sotto Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Jones (Osmena Blvd)", "Metro Colon", "P. Lopez St", "USJR", "Magallanes St", "Manalili St", "Carbon Market", "Progreso St", "MC Briones", "MJ Cuenco", "Jones (Osmena Blvd)", "Metro Colon", "Abellana Sports Complex", "Cebu Normal University", "Crown Regency", "Robinsons Fuente", "Fuente Osmena", "Capitol", "M. Velez St", "R. Duterte St", "Rustans Banawa", "Banawa Public Market"]
    },
    "08G": {
        "description": "Alumnos to Colon via Pasil/C. Padilla",
        "path": ["Alumnos", "Tagunol", "C. Padilla St", "Jai-Alai", "Carlock St", "Spolarium St", "Pasil", "San Nicolas Church", "Colon", "Metro Colon", "Colonnade", "Gaisano Main", "UV Main", "Zulueta", "MJ Cuenco", "CTU Main", "Legaspi St", "Cathedral", "V. Gullas St", "Manalili St", "Magallanes St", "USJR", "Carbon Market", "C. Padilla St", "Cacoy Doce Pares", "Jai-Alai", "San Roque (Mambaling)", "Mambaling", "Alumnos"]
    },
    "09C": {
        "description": "Basak to Cathedral via N. Bacalso",
        "path": ["Quiot (Basak Ibabao)", "Sabellano St", "Bayanihan Village", "Basak Pardo", "Mambaling", "Shopwise Mambaling", "Fooda Mambaling", "Mambaling Flyover", "CIT-U", "SCSIT", "Citilink Terminal", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "P. del Rosario", "USC Main", "Sikatuna St", "Colon Obelisk", "P. Burgos St", "Shamrock (P. Burgos)", "USPF (Old Campus/Mabini)", "Cathedral", "Basilica Sto Nino", "Magellan's Cross", "City Hall", "D. Jakosalem St", "Magallanes St", "Carbon Market", "USJR", "Tres de Abril", "C. Padilla St", "R. Padilla St", "CIT-U", "N. Bacalso Ave", "Mambaling Flyover", "Mambaling", "Fooda Mambaling", "Shopwise Mambaling", "Basak Pardo", "Bayanihan Village", "Sabellano St", "Quiot (Basak Ibabao)"]
    },
    "09F": {
        "description": "Basak-Ibabao (Quiot) to Colon via N. Bacalso",
        "path": ["Quiot (Basak Ibabao)", "Sabellano St", "South Western University", "Don Vicente Rama Memorial NHS", "Basak Pardo", "Mambaling", "Shopwise Mambaling", "Mambaling Flyover", "CIT-U", "SCSIT", "N. Bacalso Ave", "E-Mall", "ACT", "P. del Rosario", "USC Main", "Junquera St", "Colon", "Gaisano Main", "UV Main", "Zulueta", "MJ Cuenco", "Legaspi St", "Cathedral", "Basilica Sto Nino", "Legaspi St", "Manalili St", "Magallanes St", "USJR", "Carbon Market", "C. Padilla St", "Duljo Fatima", "CIT-U", "N. Bacalso Ave", "Mambaling Flyover", "Mambaling", "Shopwise Mambaling", "Basak Pardo", "Basak Night High School", "USJ-R Basak (High School)", "Bayanihan Village", "Sabellano St", "Quiot (Basak Ibabao)"]
    },
    "09G": {
        "description": "Basak (Ibabao) to Colon via C. Padilla/Pasil",
        "path": ["Quiot (Basak Ibabao)", "N. Bacalso Ave", "Shopwise Mambaling", "Fooda Mambaling", "Mambaling Flyover", "C. Padilla St", "Carlock St", "Spolarium St", "Pasil", "San Nicolas Church", "Colon", "Leon Kilat", "USJR", "Carbon Market", "Magallanes St", "Basilica Sto Nino", "City Hall", "MCWD", "Lucky 7 Supermarket", "Legaspi St", "Colonnade", "Colon", "Metro Colon", "C. Padilla St", "Jai-Alai", "Mambaling Flyover", "N. Bacalso Ave", "Mambaling", "Fooda Mambaling", "Shopwise Mambaling", "Basak Pardo", "Bayanihan Village", "Sabellano St", "Quiot (Basak Ibabao)"]
    },
    "10G": {
        "description": "Pardo to Magallanes via C. Padilla/Pasil",
        "path": ["Pardo Church", "Basak Pardo", "Shopwise Mambaling", "Fooda Mambaling", "Mambaling", "C. Padilla St", "Jai-Alai", "Pasil", "San Nicolas Church", "Colon", "Leon Kilat", "USJR", "Carbon Market", "Magallanes St", "Basilica Sto Nino", "City Hall", "Prince Warehouse (City Hall)", "La Nueva (City Hall)", "MCWD", "Legaspi St", "D. Jakosalem St", "Colon", "Gaisano Main", "UV Main", "Colonnade", "Metro Colon", "C. Padilla St", "Mambaling", "Fooda Mambaling", "Shopwise Mambaling", "Basak Pardo", "Pardo Church"]
    },
    "10M": {
        "description": "Bulacao to SM City via Colon/MJ Cuenco",
        "path": ["St. Paul College (Bulacao)", "Citi Hardware (Bulacao)", "Prince Warehouse (Bulacao)", "Pardo Church", "Basak Pardo", "USJ-R Basak (High School)", "Mambaling", "Shopwise Mambaling", "Fooda Mambaling", "Mambaling Flyover", "CIT-U", "SCSIT", "Napolcom", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "Leon Kilat", "Colon", "Metro Colon", "Colonnade", "138 Mall", "Gaisano Main", "UV Main", "Colon Obelisk", "Zulueta", "MJ Cuenco", "NSO (PSA)", "T. Padilla", "Benedicto", "White Gold", "A. Soriano Ave", "Queen City Memorial Garden", "SM City", "A. Soriano Ave", "White Gold", "Queen City Memorial Garden", "Queensland Hotel", "Benedicto", "T. Padilla", "MJ Cuenco", "NSO (PSA)", "CTU Main", "Plaza Independencia", "Legaspi St", "V. Gullas St", "Manalili St", "Borromeo St", "Sanciangko St", "Panganiban St", "Cebu City Medical Center", "CIT-U", "Mambaling", "Fooda Mambaling", "Shopwise Mambaling", "Basak Pardo", "Pardo Church", "Prince Warehouse (Bulacao)", "St. Paul College (Bulacao)"]
    },
    "10H": {
        "description": "Bulacao to SM City via Sikatuna/T. Padilla",
        "path": ["St. Paul College (Bulacao)", "Pardo Church", "Basak Pardo", "Mambaling", "CIT-U", "SCSIT", "Citilink Terminal", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "ACT", "P. del Rosario", "Sikatuna St", "T. Padilla", "White Gold", "SM City", "White Gold", "Cebu City Civil Registrar", "DSWD", "Imus Ave", "MJ Cuenco", "NSO (PSA)", "Legaspi St", "Cathedral", "Manalili St", "Borromeo St", "Sanciangko St", "Aerol Pensione House", "Cebu City Medical Center", "Citilink Terminal", "SCSIT", "Napolcom", "CIT-U", "Mambaling", "Shopwise Mambaling", "Basak Pardo", "Pardo Church", "St. Paul College (Bulacao)"]
    },
    "10F": {
        "description": "Bulacao to Junquera via N. Bacalso",
        "path": ["St. Paul College (Bulacao)", "Pardo Church", "Basak Pardo", "Mambaling", "CIT-U", "SCSIT", "Citilink Terminal", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "P. del Rosario", "USC Main", "Junquera St", "Colon", "Metro Colon", "Borromeo St", "Sanciangko St", "Panganiban St", "Cebu City Medical Center", "CIT-U", "Mambaling", "Fooda Mambaling", "Shopwise Mambaling", "Basak Pardo", "Pardo Church", "St. Paul College (Bulacao)"]
    },
    "11A": {
        "description": "Inayawan to Colon via C. Padilla/Pasil",
        "path": ["Inayawan Church", "Rizal Ave Ext", "Tagunol", "Mambaling Flyover", "C. Padilla St", "Carlock St", "Spolarium St", "Pasil", "San Nicolas Church", "Magallanes St", "Basilica Sto Nino", "D. Jakosalem St", "Gaisano Main", "UV Main", "Colon", "138 Mall", "Colonnade", "Metro Colon", "C. Padilla St", "Carlos Gothong HS", "Jai-Alai", "Mambaling Flyover", "Tagunol", "Rizal Ave Ext", "Cogon Pardo", "Inayawan Church"]
    },
    "12G": {
        "description": "Labangon to SM City via Pasil/Tabo-an",
        "path": ["Punta Princesa", "Tres de Abril", "Labangon Public Market", "Carlock St", "B. Aranas St", "Tabo-an Market", "Lakandula St", "San Nicolas Church", "Pasil", "Spolarium St", "Magallanes St", "USJR", "Carbon Market", "Magellan's Cross", "Basilica Sto Nino", "D. Jakosalem St", "MC Briones", "City Hall", "Senior Citizens Plaza", "La Nueva (City Hall)", "Plaza Independencia", "MJ Cuenco", "Legaspi Ext", "Sergio Osmena Blvd", "Pier 3", "Pier 4", "Sugbutel", "Pier 5", "Pier 6", "Radisson Blu", "Juan Luna Ave", "SM City", "North Bus Terminal", "Juan Luna Ave", "F. Cabahug St", "APM Mall", "Sergio Osmena Blvd", "Cebu Daily News", "Pier 6", "Sugbutel", "Pier 5", "PCSO", "Pier 4", "T. Padilla", "MJ Cuenco", "A. Bonifacio St", "Sikatuna St", "Parian", "JC Zamora St", "Sanciangko St", "UC Main", "Sogo Hotel", "GV Tower Hotel", "E-Mall", "Panganiban St", "Cebu City Medical Center", "N. Bacalso Ave", "Citilink Terminal", "Katipunan St", "Labangon Public Market", "F. Llamas St", "Brgy Tisa", "Punta Princesa", "Tres de Abril"]
    },
    "12I": {
        "description": "Labangon to SM City via Pier/Colon",
        "path": ["Punta Princesa", "F. Llamas St", "Brgy Tisa", "Gaisano Tisa", "Katipunan St", "Labangon Public Market", "Tres de Abril", "N. Bacalso Ave", "Citilink Terminal", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "ACT", "P. del Rosario", "USC Main", "Junquera St", "Colon", "Gaisano Main", "UV Main", "Colon Obelisk", "P. Burgos St", "USPF (Old Campus/Mabini)", "Cathedral", "F. Urdaneta St", "MJ Cuenco", "Legaspi Ext", "Plaza Independencia", "Fort San Pedro", "Sergio Osmena Blvd", "Pier 3", "Pier 4", "Pier 5", "Robinsons Galleria Cebu", "PCSO", "Sugbutel", "SM City", "North Bus Terminal", "Juan Luna Ave", "F. Cabahug St", "APM Mall", "Sergio Osmena Blvd", "Radisson Blu", "Sugbutel", "PCSO", "Robinsons Galleria Cebu", "Legaspi Ext", "Plaza Independencia", "Fort San Pedro", "Cathedral", "Basilica Sto Nino", "V. Gullas St", "Manalili St", "Manila Foodshoppe", "Pacific Tourist Inn", "Borromeo St", "Sanciangko St", "Aerol Pensione House", "Panganiban St", "Cebu City Medical Center", "N. Bacalso Ave", "Katipunan St", "Tres de Abril", "Punta Princesa"]
    },
    "12L": {
        "description": "Labangon to Ayala via Banawa/Capitol",
        "path": ["Punta Princesa Church", "Tres de Abril", "Salvador St", "Katipunan St", "N. Bacalso Ave", "V. Rama Ave", "B. Rodriguez St", "Fuente Osmena", "Robinsons Fuente", "Mango Ave", "Gen Maxilom Ext", "Gorordo", "Camp Sotero (Police Station)", "Ayala Center Cebu", "Harolds Hotel", "Escario St", "Capitol", "M. Velez St", "R. Duterte St", "Rustans Banawa", "Salvador Extension", "Katipunan St", "F. Llamas St", "Gaisano Tisa", "Brgy Tisa", "Punta Princesa", "Punta Princesa Church"]
    },
    "12D": {
        "description": "Labangon to Colon via Katipunan",
        "path": ["Punta Princesa", "F. Llamas St", "Brgy Tisa", "Labangon Public Market", "Katipunan St", "Tres de Abril", "N. Bacalso Ave", "Citilink Terminal", "Cebu City Medical Center", "South Bus Terminal", "E-Mall", "ACT", "P. del Rosario", "USC Main", "Junquera St", "Colon", "Gaisano Main", "UV Main", "P. Burgos St", "USPF (Old Campus/Mabini)", "Cathedral", "Legaspi St", "Colonnade", "Pelaez St", "Sanciangko St", "Sogo Hotel", "GV Tower Hotel", "UC Main", "Leon Kilat", "E-Mall", "N. Bacalso Ave", "South Bus Terminal", "Cebu City Medical Center", "Citilink Terminal", "Katipunan St", "Tres de Abril", "Punta Princesa"]
    },
    "13B": {
        "description": "Talamban to Carbon via Ramos",
        "path": ["Tintay", "H. Abella St", "Talamban Gym", "Gaisano Grand Talamban", "The Family Park", "USC Talamban", "Gaisano Country Mall", "UC Banilad", "Cebu Business Park", "Ayala Center Cebu", "Samar Loop", "Luzon Ave", "Metro Ayala", "Gorordo", "Asilo dela Milagrosa", "Echavez St", "Allson's Inn", "Sikatuna St", "D. Jakosalem St", "Ramos Market", "Junquera Ext", "Junquera St", "USC Main", "Colon", "Gaisano Main", "UV Main", "Colon Obelisk", "Mabini", "V. Gullas St", "Manalili St", "Carbon Market", "Progreso St", "MC Briones", "D. Jakosalem St", "City Hall", "Magellan's Cross", "Basilica Sto Nino", "Gaisano Main", "UV Main", "Ramos Market", "Zapatera Brgy Hall", "Sikatuna St", "Echavez St", "Gorordo", "Cebu Business Park", "Luzon Ave", "Ayala Center Cebu", "Metro Ayala", "Cardinal Rosales Ave", "Marriot Hotel", "Pag-IBIG Fund (Ayala)", "Banilad", "UC Banilad", "Gaisano Country Mall", "USC Talamban", "The Family Park", "Gaisano Grand Talamban", "Tintay"]
    },
    "13C": {
        "description": "Talamban to Colon via Ayala",
        "path": ["Talamban Gym", "Gaisano Grand Talamban", "USC Talamban", "Banilad", "Banilad Town Centre (BTC)", "Gaisano Country Mall", "UC Banilad", "Paradise Village", "Cebu Country Club", "Samantabhadra Institute", "BIR", "Cebu Business Park", "Pag-IBIG Fund (Ayala)", "Ayala Center Cebu", "Samar Loop", "Luzon Ave", "Tune Hotels", "Hotel Elizabeth", "Gorordo", "Asilo dela Milagrosa", "Camp Sotero (Police Station)", "Echavez St", "Sikatuna St", "Parian", "Colon", "Gaisano Main", "UV Main", "Colonnade", "Pelaez St", "USC Main", "P. del Rosario", "Imus Ave", "MJ Cuenco", "Hipodromo", "Mactan St", "Cebu Business Park", "Leyte Loop", "Samar Loop", "Ayala Center Cebu", "BIR", "Samantabhadra Institute", "Banilad", "UC Banilad", "Gaisano Country Mall", "Banilad Town Centre (BTC)", "Foodland", "USC Talamban", "Gaisano Grand Talamban", "Talamban Gym"]
    },
    "13H": {
        "description": "Pit-os to Mandaue Public Market via A.S. Fortuna",
        "path": ["Pit-os", "Bacayan", "Cebu North General Hospital", "Talamban Gym", "Gaisano Grand Talamban", "The Family Park", "USC Talamban", "Banilad", "UC Banilad", "Foodland", "A.S. Fortuna St", "Cebu Home & Builders", "Oftana Suites", "Allure Hotel", "Benedicto College", "J Centre Mall", "The Orchard", "Guizo", "Mantuyong", "Sosyoland", "Colonnade", "A. Soriano Ave", "Mandaue Sports Complex", "Mandaue Public Market", "St. Joseph Parish (Mandaue)", "St. Joseph Academy", "Pacific Mall", "Mantuyong", "Guizo", "San Miguel Brewery", "A.S. Fortuna St", "J Centre Mall", "Benedicto College", "Oftana Suites", "Oakridge Business Park", "Cebu Home & Builders", "Banilad", "Foodland", "UC Banilad", "USC Talamban", "The Family Park", "Gaisano Grand Talamban", "Talamban Gym", "Cebu North General Hospital", "Bacayan", "Pit-os"]
    },
    "14D": {
        "description": "Ayala to Colon via Ramos/Osmena Blvd Loop",
        "path": ["Ayala Center Cebu", "Harolds Hotel", "Escario St", "Capitol", "Jones (Osmena Blvd)", "Fuente Osmena", "Robinsons Cybergate", "Chong Hua Hospital", "Robinsons Fuente", "F. Ramos St", "Saint Paul College Foundation (Ramos)", "USC Main", "Junquera St", "Colon", "Gaisano Main", "UV Main", "V. Gullas St", "Manalili St", "Metro Colon", "Landbank (Osmena Blvd)", "Central Bank", "Abellana Sports Complex", "Crown Regency", "Fuente Osmena", "Jones (Osmena Blvd)", "Escario St", "Philhealth", "Ayala Center Cebu"]
    },
    "15": {
        "description": "Oppra (Kalunasan) to Carbon",
        "path": ["Oppra (Kalunasan)", "Kalunasan", "Capitol", "Jones (Osmena Blvd)", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Abellana Sports Complex", "Cebu Normal University", "Metro Colon", "Unitop (Colon)", "Carbon Market", "City Hall", "Basilica Sto Nino", "Magallanes St", "Borromeo St", "Colon", "Jones (Osmena Blvd)", "Fuente Osmena", "Capitol", "Kalunasan", "Oppra (Kalunasan)"]
    },
    "17D": {
        "description": "Apas to Carbon via Tabo-an/Escario",
        "path": ["Apas", "Wilson St", "Omega St", "San Miguel Rd", "IT Park", "Skyrise 1", "Skyrise 2", "Inez Villa St", "J. Maria del Mar St", "Skyrise 3", "W. Geonzon St", "Salinas Drive", "USP-F (Lahug)", "JY Square", "Lahug", "Gorordo", "Mormons Church (Lahug)", "UP Cebu", "Harolds Hotel", "Escario St", "Capitol", "Cebu Doctors Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Abellana Sports Complex", "Cebu Normal University", "SSS", "Sanciangko St", "GV Tower Hotel", "UC Main", "E-Mall", "Tabo-an Market", "Taboan Dried Fish Market", "Lakandula St", "San Nicolas Church", "Pasil Fish Market", "Spolarium St", "Magallanes St", "USJR", "Carbon Market", "Progreso St", "MC Briones", "Senior Citizens Plaza", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MCWD", "DFA", "Legaspi St", "Colonnade", "Hotel de Mercedes", "Pelaez St", "USC Main", "P. del Rosario", "Cebu Normal University", "Abellana Sports Complex", "Crown Regency", "Robinsons Fuente", "Fuente Osmena", "Cebu Doctors Hospital", "Capitol", "Escario St", "Cebu Grand Hotel", "Philhealth", "Golden Peak", "Gorordo", "Turtles Nest", "Handuraw Pizza (Lahug)", "UP Cebu", "Lahug", "Mormons Church (Lahug)", "JY Square", "Salinas Drive", "USP-F (Lahug)", "W. Geonzon St", "IT Park", "Convergys (IT Park)", "J. Maria del Mar St", "Skyrise 3", "Inez Villa St", "Skyrise 1", "Skyrise 2", "San Miguel Rd", "Omega St", "Wilson St", "Apas"]
    },
    "17B": {
        "description": "Apas to Carbon via Jones/IT Park",
        "path": ["Apas", "IT Park", "W. Geonzon St", "Salinas Drive", "JY Square", "Gorordo", "UP Cebu", "Harolds Hotel", "Escario St", "Capitol", "Cebu Doctors Hospital", "Fuente Osmena", "Robinsons Fuente", "Crown Regency", "Abellana Sports Complex", "Jones (Osmena Blvd)", "SSS", "Metro Colon", "P. Lopez St", "Magallanes St", "Manalili St", "Carbon Market", "Progreso St", "MC Briones", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MJ Cuenco", "Jones (Osmena Blvd)", "Lapulapu St", "Legaspi St", "Colonnade", "Pelaez St", "USC Main", "Cebu Normal University", "Crown Regency", "Robinsons Fuente", "Fuente Osmena", "Cebu Doctors Hospital", "Capitol", "Escario St", "Gorordo", "UP Cebu", "JY Square", "Salinas Drive", "W. Geonzon St", "IT Park", "Apas"]
    },
    "17C": {
        "description": "Apas to Carbon via Ramos/Gen. Maxilom",
        "path": ["Apas", "IT Park", "Salinas Drive", "USP-F (Lahug)", "JY Square", "Gorordo", "Lahug High School", "UP Cebu", "Golden Peak", "Philhealth", "Royal Concourse", "Asilo dela Milagrosa", "Gen Maxilom Ext", "Mango Ave", "Fooda Mango", "Horizons 101", "Mango Square", "The Beat", "Robinsons Fuente", "F. Ramos St", "Junquera St", "USC Main", "Sanciangko St", "UC Main", "GV Tower Hotel", "E-Mall", "Panganiban St", "Magallanes St", "USJR", "Carbon Market", "Progreso St", "MC Briones", "City Hall", "Basilica Sto Nino", "La Nueva (City Hall)", "MCWD", "Legaspi St", "Cathedral", "D. Jakosalem St", "Gaisano Main", "UV Main", "Cogon Ramos", "Ramos Market", "F. Ramos St", "Robinsons Fuente", "Mango Ave", "Raintree Mall", "Mango Square", "Horizons 101", "Fooda Mango", "Gen Maxilom Ext", "Gorordo", "Royal Concourse", "Philhealth", "Golden Peak", "Tonros Apartelle", "Harolds Hotel", "UP Cebu", "Lahug", "JY Square", "Salinas Drive", "W. Geonzon St", "IT Park", "Apas"]
    },
    "20A": {
        "description": "Ayala to Mandaue (Pacific Mall) via Parkmall/Centro",
        "path": ["Ayala Center Cebu", "Mabolo Church", "Subangdaku", "Wireless", "Tipolo", "San Miguel Brewery", "Parkmall", "CICC", "Guizo", "Uwell", "Mantuyong", "Sosyoland", "Colonnade Mandaue", "Mandaue Public Market (New)", "BIR Mandaue", "Bureau of Immigration Mandaue", "Mandaue City Hall", "St. Joseph Parish (Mandaue)", "SB Cabahug St", "Mandaue Coliseum", "Estancia-Ibabao", "Super Metro Mandaue", "Pacific Mall", "DFA Mandaue", "Super Metro Mandaue", "UN Ave", "Plaridel St", "AC Cortes Ave", "Maguikay Flyover", "Coca Cola Plant", "San Miguel Brewery", "Tipolo", "Wireless", "Subangdaku", "Mabolo Church", "Dela Montana St", "Cardinal Rosales Ave", "Mindanao Ave", "Ayala Center Cebu"]
    },
    "20B": {
        "description": "Ayala to Ibabao-Estancia via Highway",
        "path": ["Ayala Center Cebu", "Mabolo Church", "Subangdaku", "Wireless", "Tipolo", "San Miguel Brewery", "Coca Cola Plant", "Maguikay Flyover", "Estancia-Ibabao", "Mandaue Coliseum", "SB Cabahug St", "Centro Mandaue", "Gaisano Grand Mandaue", "A. Del Rosario St", "Guizo", "San Miguel Brewery", "Tipolo", "Wireless", "Subangdaku", "Mabolo Church", "Cebu Business Park", "Ayala Center Cebu"]
    },
    "21A": {
        "description": "Cathedral to Pacific Mall via Mandaue Centro/Subangdaku",
        "path": ["Cathedral", "MJ Cuenco", "CTU Main", "NSO (PSA)", "Museo Sugbo", "CPILS", "Imus Ave", "MJ Cuenco", "Carreta Cemetery", "Hipodromo", "The Persimmon", "Mabolo Church", "Subangdaku", "Innodata", "Wireless", "Tipolo", "CD Seno St", "A.S. Fortuna St", "Guizo", "Mantuyong", "Centro Mandaue", "Sosyoland", "Colonnade Mandaue", "Mandaue Public Market (New)", "BIR Mandaue", "Bureau of Immigration Mandaue", "Mandaue City Hall", "St. Joseph Parish (Mandaue)", "SB Cabahug St", "Mandaue Coliseum", "Estancia-Ibabao", "Pacific Mall", "Super Metro Mandaue", "DFA Mandaue", "Pacific Mall", "UN Ave", "Plaridel St", "AC Cortes Ave", "Prince Warehouse Mandaue", "Mandaue Coliseum", "Maguikay Flyover", "Coca Cola Plant", "San Miguel Brewery", "Tipolo", "Wireless", "Albano St", "M. Logarta Ave", "North Bus Terminal", "SM Hypermarket", "SM City", "A. Soriano Ave", "White Gold", "G. Gaisano St", "T. Padilla", "Pier 4", "Sergio Osmena Blvd", "V. Sotto St", "CTU Main", "V. Gullas St", "P. Burgos St", "Cathedral"]
    },
    "21D": {
        "description": "Cathedral to Pacific Mall via Reclamation/Parkmall",
        "path": ["Benedicto", "White Gold", "A. Soriano Ave", "White Gold", "Queen City Memorial Garden", "SM City", "SM Hypermarket", "Aboitiz Football Field", "North Bus Terminal", "M. Logarta Ave", "Wireless", "Tipolo", "San Miguel Brewery", "Parkmall", "CICC", "Guizo", "Uwell", "Centro Mandaue", "Sosyoland", "Colonnade Mandaue", "Mandaue Public Market (New)", "Bureau of Immigration Mandaue", "PJ Burgos St", "Mandaue City Hall", "St. Joseph Parish (Mandaue)", "SB Cabahug St", "Mandaue Coliseum", "Estancia-Ibabao", "Pacific Mall", "Super Metro Mandaue", "UN Ave", "Hi-Land", "Plaridel St", "AC Cortes Ave", "Prince Warehouse Mandaue", "Mandaue Coliseum", "Maguikay Flyover", "Coca Cola Plant", "San Miguel Brewery", "Tipolo", "Wireless", "Subangdaku", "Andok's Mabolo", "Mabolo Church", "Hipodromo", "MJ Cuenco", "Imus Ave", "MJ Cuenco", "CPILS", "T. Padilla", "NSO (PSA)", "CTU Main", "Cathedral"]
    },
    "22A": {
        "description": "Cathedral to Ouano (Mandaue) via MJ Cuenco/Highway",
        "path": ["Cathedral", "F. Urdaneta St", "MJ Cuenco", "CTU Main", "NSO (PSA)", "CPILS", "Museo Sugbo", "DSWD", "Carreta Cemetery", "Hipodromo", "The Persimmon", "Mabolo Church", "Lopez Jaena St", "Subangdaku", "Wireless", "Tipolo", "A. Del Rosario St", "San Miguel Brewery", "CD Seno St", "W.O. Seno St", "Parkmall", "CICC", "Mantuyong", "Centro Mandaue", "Sosyoland", "Colonnade Mandaue", "Ouano Ave", "A. Soriano Ave", "Mandaue Public Market (New)", "BIR Mandaue", "JL Briones St", "A. Mabini St", "Ouano (Mandaue Terminal)", "Mandaue City Hall", "Gaisano Grand Mandaue", "A. Del Rosario St", "Mantuyong", "Guizo", "San Miguel Brewery", "Tipolo", "Wireless", "Subangdaku", "Albano St", "North Bus Terminal", "Aboitiz Football Field", "SM Hypermarket", "APM Mall", "SM City", "A. Soriano Ave", "Queen City Memorial Garden", "White Gold", "G. Gaisano St", "Benedicto", "T. Padilla", "Sergio Osmena Blvd", "Pier 4", "Pier 3", "V. Sotto St", "MJ Cuenco", "CTU Main", "V. Gullas St", "P. Burgos St", "Plaza Humabon", "Cathedral"]
    },
    "22D": {
        "description": "Cathedral to Mandaue (Ouano) via Pier/Recla",
        "path": ["Cathedral", "F. Urdaneta St", "Plaza Independencia", "Legaspi Ext", "Sergio Osmena Blvd", "Pier 3", "Pier 4", "13th Ave", "Benedicto", "Gen Maxilom Ext", "A. Soriano Ave", "White Gold", "Queen City Memorial Garden", "SM City", "F. Cabahug St", "M. Logarta Ave", "SM Hypermarket", "Aboitiz Football Field", "North Bus Terminal", "Lopez Jaena St", "Tipolo", "San Miguel Brewery", "A. Del Rosario St", "CD Seno St", "Parkmall", "CICC", "W.O. Seno St", "Uwell", "Mantuyong", "Sosyoland", "Colonnade Mandaue", "A. Soriano Ave", "Mandaue Public Market (New)", "A. Mabini St", "Ouano (Mandaue Terminal)", "P. Burgos St", "Mandaue City Hall", "Gaisano Grand Mandaue", "A. Del Rosario St", "Mantuyong", "Guizo", "San Miguel Brewery", "MC Briones", "Lopez Jaena St", "Tipolo", "Wireless", "Ginebra San Miguel", "Innodata", "Subangdaku", "MJ Cuenco", "Mabolo Church", "The Persimmon", "Hipodromo", "Cebu Chinese Cemetery", "Carreta Cemetery", "Imus Ave", "MJ Cuenco", "Museo Sugbo", "CPILS", "NSO (PSA)", "CTU Main", "V. Gullas St", "Plaza Humabon", "Cathedral"]
    },
    "22G": {
        "description": "Cathedral to Mandaue (Ouano) via SM/Highway",
        "path": ["Cathedral", "F. Urdaneta St", "MJ Cuenco", "CTU Main", "NSO (PSA)", "T. Padilla", "Benedicto", "Gen Maxilom Ext", "A. Soriano Ave", "White Gold", "SM City", "F. Cabahug St", "APM Mall", "M. Logarta Ave", "SM Hypermarket", "Aboitiz Football Field", "North Bus Terminal", "Lopez Jaena St", "Wireless", "Tipolo", "A. Del Rosario St", "CD Seno St", "CICC", "W.O. Seno St", "Guizo", "Mantuyong", "Uwell", "B. Ceniza St", "Sosyoland", "Colonnade Mandaue", "A. Soriano Ave", "Mandaue Public Market (New)", "BIR Mandaue", "JL Briones St", "Norkis Cyberpark", "A. Mabini St", "Ouano (Mandaue Terminal)", "P. Burgos St", "St. Joseph Parish (Mandaue)", "Mandaue City Hall", "Gaisano Grand Mandaue", "A. Del Rosario St", "Mantuyong", "Guizo", "San Miguel Brewery", "MC Briones", "Lopez Jaena St", "Tipolo", "Wireless", "Subangdaku", "Mabolo Church", "Pope John Paul II Ave", "SM City", "A. Soriano Ave", "Queen City Memorial Garden", "White Gold", "Queensland Hotel", "Gen Maxilom Ext", "G. Gaisano St", "T. Padilla", "Sergio Osmena Blvd", "Pier 4", "Pier 3", "V. Sotto St", "CTU Main", "MJ Cuenco", "V. Gullas St", "P. Burgos St", "Cathedral"]
    },
    "22I": {
        "description": "Country Mall to Mandaue Public Market",
        "path": ["Country Mall", "Banilad Town Centre (BTC)", "A.S. Fortuna St", "J Centre Mall", "A. Del Rosario St", "Uwell", "B. Ceniza St", "Sosyoland", "Colonnade Mandaue", "A. Soriano Ave", "Mandaue Public Market (New)", "Bureau of Immigration Mandaue", "Mandaue City Hall", "St. Joseph Parish (Mandaue)", "St. Joseph Academy", "A. Del Rosario St", "Gaisano Grand Mandaue", "Mantuyong", "Guizo", "CIC Mandaue", "San Miguel Brewery", "MC Briones", "A.S. Fortuna St", "Norkis Cyberpark", "J Centre Mall", "Benedicto College", "Larsian Banilad", "Cebu Home & Builders", "Foodland", "Banilad", "Banilad Town Centre (BTC)", "Country Mall"]
    },
    "23D": {
        "description": "Opon to Mandaue (Parkmall) via AC Cortes",
        "path": ["Opon PUJ Terminal", "ML Quezon Ave", "Old Mactan-Mandaue Bridge", "AC Cortes Ave", "UCLM", "Natures Spring Plant", "Mandaue Coliseum", "STI Mandaue", "SB Cabahug St", "Mandaue Catholic Cemetery", "A. Del Rosario St", "Guizo", "CD Seno St", "CICC", "Parkmall", "W.O. Seno St", "EO Perez St", "S&R Membership Shopping", "P. Larazzabal Ave", "Cebu Doctors University", "Ouano Ave", "CICC", "Mandaue Public Market (New)", "JL Briones St", "Norkis Cyberpark", "University of the Visayas", "AC Cortes Ave", "Natures Spring Plant", "UCLM", "Old Mactan-Mandaue Bridge", "ML Quezon Ave", "General Milling Corp", "Metro Mactan", "Mantawe Rd", "Ompad St", "GY dela Serna St", "La Nueva (Opon)", "Opon PUJ Terminal"]
    },

    "23": {
        "description": "Parkmall to Punta Engaño via MEPZ 1",
        "path": ["Parkmall", "W.O. Seno St", "Chong Hua Hospital (Mandaue)", "MO2 Westown", "EO Perez St", "S&R Membership Shopping", "P. Larazzabal Ave", "Cebu Doctors University", "Ouano Ave", "St. James Amusement Park", "A. Soriano Ave", "Mandaue City College", "BIR Mandaue", "Mandaue Public Market (New)", "JL Briones St", "Norkis Cyberpark", "University of the Visayas", "Hotel Nenita", "Plaridel St", "Metro Fresh & Easy", "Umapad", "Bridges Town Square", "UN Ave", "New Mactan-Mandaue Bridge", "Pusok", "Marina Mall", "Savemore Mactan", "MEPZ 1 Gates", "Ibo", "Buaya", "Mactan Shrine", "Punta Engaño", "Shangri-La Mactan", "Movenpick Resort", "Abaca Boutique Resort", "Be Resort", "Palm Beach Resort", "Amisa Residences", "Discovery Bay Hotel", "Amisa Residences", "Palm Beach Resort", "Be Resort", "Abaca Boutique Resort", "Movenpick Resort", "Shangri-La Mactan", "Mactan Shrine", "Buaya", "Ibo", "MEPZ 1 Gates", "Savemore Mactan", "Marina Mall", "Pusok", "New Mactan-Mandaue Bridge", "UN Ave", "Umapad", "Plaridel St", "Bridges Town Square", "Hotel Nenita", "AC Cortes Ave", "Prince Warehouse Mandaue", "STI Mandaue", "SB Cabahug St", "A. Del Rosario St", "Tipolo", "CD Seno St", "CICC", "W.O. Seno St", "Parkmall"]
    },

    "24": {
        "description": "Consolacion to White Gold/SM",
        "path": ["Consolacion Church", "SM City Consolacion", "Fooda Consolacion", "Corner Canduman", "Basak", "Insular Square", "Pacific Mall", "Super Metro Mandaue", "Maguikay Flyover", "Tipolo", "Wireless", "Subangdaku", "Innodata", "Mabolo Church", "SM City", "White Gold", "North Bus Terminal", "Wireless", "Subangdaku", "Tipolo", "Maguikay Flyover", "Pacific Mall", "Super Metro Mandaue", "Paknaan", "Basak", "Corner Canduman", "Consolacion Church", "Fooda Consolacion", "SM City Consolacion", "Bagong Daan"]
    },
    "62B": {
        "description": "Pit-os to Carbon via Ayala/Echavez (Loop)",
        "path": ["Pit-os", "Bacayan", "Talamban Gym", "Gaisano Grand Talamban", "The Family Park", "USC Talamban", "Gaisano Country Mall", "UC Banilad", "Banilad", "Pope John Paul II Ave", "Cebu Business Park", "Ayala Center Cebu", "Marriot Hotel", "Samar Loop", "Luzon Ave", "Arch. Reyes Ave", "Gorordo", "Asilo dela Milagrosa", "Gen. Echavez St", "Sikatuna St", "Zapatera", "Colon Obelisk", "V. Gullas St", "Manalili St", "Carbon Market", "Progreso St", "MC Briones", "D. Jakosalem St", "City Hall", "Basilica Sto Nino", "The Freeman", "Gaisano Main", "UV Main", "Imus Ave", "Mango Ave", "Sorsogon Rd", "Negros Rd", "Cardinal Rosales Ave", "Luzon Ave", "Metro Ayala", "Ayala Center Cebu", "Arch. Reyes Ave", "Quest Hotel", "Hongkong Plaza Hotel", "Banilad", "Gaisano Country Mall", "Banilad Town Centre (BTC)", "Foodland", "USC Talamban", "The Family Park", "Talamban Gym", "Gaisano Grand Talamban", "Bacayan", "Pit-os"]
    },
    "62C": {
        "description": "Pit-os to Carbon via Ayala/Ramos/Junquera",
        "path": ["Pit-os", "Talamban Gym", "Gaisano Grand Talamban", "USC Talamban", "Banilad", "Gaisano Country Mall", "Juan Luna Ave", "San Carlos Seminary", "Cardinal Rosales Ave", "Ayala Center Cebu", "Keppel Tower", "Samar Loop", "Luzon Ave", "Arch. Reyes Ave", "Hotel Elizabeth", "Asilo dela Milagrosa", "Gorordo", "Gen. Echavez St", "Sikatuna St", "D. Jakosalem St", "Ramos Market", "Junquera Ext", "Junquera St", "USC Main", "Colon", "Gaisano Main", "UV Main", "P. Burgos St", "V. Gullas St", "Manalili St", "Carbon Market", "Progreso St", "MC Briones", "City Hall", "D. Jakosalem St", "Basilica Sto Nino", "Gaisano Main", "UV Main", "Ramos Market", "Bayantel", "Sikatuna St", "Gen. Echavez St", "Gorordo", "Arch. Reyes Ave", "Ayala Center Cebu", "BIR", "Paradise Village", "Gaisano Country Mall", "UC Banilad", "Banilad", "Banilad Town Centre (BTC)", "Foodland", "USC Talamban", "Talamban Gym", "Bacayan", "Pit-os"]
    },
    "MI-01A": {
        "description": "Punta Engaño to Opon Market Loop",
        "path": ["Punta Engaño", "Mactan Shrine", "MEPZ 1 Gates", "Marina Mall", "Pusok", "SSS Lapu-Lapu", "Lapu-Lapu City Hall", "Gaisano Island Mall", "Metro Lapu-Lapu", "Opon Public Market", "Metro Lapu-Lapu", "Gaisano Island Mall", "Lapu-Lapu City Hall", "SSS Lapu-Lapu", "Pusok", "Marina Mall", "MEPZ 1 Gates", "Ibo", "Mactan Shrine", "Shangri-La Mactan", "Punta Engaño"]
    },
    "MI-02B": {
        "description": "Mandaue (Parkmall) to Maribago Loop",
        "path": ["Parkmall", "W.O. Seno St", "EO Perez St", "S&R Membership Shopping", "P. Larazzabal Ave", "Cebu Doctors University", "Ouano Ave", "St. James Amusement Park", "CICC", "A. Soriano Ave", "Mandaue Public Market (New)", "Mandaue City Hospital", "JL Briones St", "University of the Visayas", "Plaridel St", "Bridges Town Square", "Highland (Mandaue)", "UN Ave", "Umapad", "New Mactan-Mandaue Bridge", "Pusok", "ML Quezon Ave", "Marina Mall", "MEPZ 1 Gates", "Ibo", "Mactan Shrine", "Punta Engaño", "Mactan Newtown", "Maribago", "Maribago Bluewater", "Cebu White Sands", "Savemore Maribago", "Metro Express Maribago", "Cebu White Sands", "Maribago Bluewater", "Mactan Newtown", "Ibo", "MEPZ 1 Gates", "Marina Mall", "Pusok", "New Mactan-Mandaue Bridge", "UN Ave", "Highland (Mandaue)", "Plaridel St", "Bridges Town Square", "AC Cortes Ave", "Prince Warehouse Mandaue", "Mandaue Coliseum", "STI Mandaue", "SB Cabahug St", "Mandaue Catholic Cemetery", "Guizo", "A. Del Rosario St", "Tipolo", "CD Seno St", "W.O. Seno St", "Parkmall"]
    },
    "MI-03A": {
        "description": "Cordova to Opon Market Loop",
        "path": ["Cordova", "Babag 2", "Deca Homes (Babag)", "Babag 1", "Tiangue Rd", "Looc", "LLC Central School", "GY dela Serna St", "Yanadia", "S. Osmena St (Opon)", "Opon Public Market", "L. Jaena St (Opon)", "P. Rodriguez St", "LLC Central School", "Tiangue Rd", "Looc", "Babag 1", "Deca Homes (Babag)", "Babag 2", "Cordova"]
    },
    "MI-04A": {
        "description": "Tamiya (MEPZ 2) to Mandaue Loop",
        "path": ["Tamiya Terminal", "Robinsons Supermarket (Mactan)", "Marigondon", "Crown Regency Suites (Mactan)", "Old Mactan-Mandaue Bridge", "UCLM", "AC Cortes Ave", "Prince Warehouse Mandaue", "SB Cabahug St", "A. Del Rosario St", "CD Seno St", "Parkmall", "W.O. Seno St", "EO Perez St", "P. Larazzabal Ave", "Cebu Doctors University", "Ouano Ave", "St. James Amusement Park", "A. Soriano Ave", "Mandaue City Hospital", "JL Briones St", "AC Cortes Ave", "UCLM", "Old Mactan-Mandaue Bridge", "MV Patalinghug Ave", "Crown Regency Suites (Mactan)", "Robinsons Supermarket (Mactan)", "Tamiya Terminal"]
    },
    "MI-05A": {
        "description": "Mactan Airport to Opon Church via Pusok",
        "path": ["Mactan-Cebu International Airport", "Marina Mall", "Pusok", "Hotel Cesario", "SSS Lapu-Lapu", "Lapu-Lapu City Hall", "Gaisano Island Mall", "General Milling Corp", "Metro Lapu-Lapu", "Mantawe Rd", "B.M. Dimataga St", "Muelle Osmena Port", "Our Lady of Rule Parish", "R. Rodriguez St", "GY dela Serna St", "Opon Public Market", "La Nueva (Opon)", "ML Quezon Ave", "Metro Lapu-Lapu", "Gaisano Island Mall", "Lapu-Lapu City Hall", "Pusok", "Marina Mall", "Mactan-Cebu International Airport"]
    },
    "MI-23A": {
        "description": "Opon to Mandaue (Parkmall) via AC Cortes",
        "path": ["Opon PUJ Terminal", "ML Quezon Ave", "Old Mactan-Mandaue Bridge", "AC Cortes Ave", "UCLM", "Natures Spring Plant", "Mandaue Coliseum", "STI Mandaue", "SB Cabahug St", "Mandaue Catholic Cemetery", "A. Del Rosario St", "Guizo", "CD Seno St", "CICC", "Parkmall", "W.O. Seno St", "EO Perez St", "S&R Membership Shopping", "P. Larazzabal Ave", "Cebu Doctors University", "Ouano Ave", "CICC", "Mandaue Public Market (New)", "JL Briones St", "Norkis Cyberpark", "University of the Visayas", "AC Cortes Ave", "Natures Spring Plant", "UCLM", "Old Mactan-Mandaue Bridge", "ML Quezon Ave", "General Milling Corp", "Metro Mactan", "Mantawe Rd", "Ompad St", "GY dela Serna St", "La Nueva (Opon)", "Opon PUJ Terminal"]
    },
    "MI-03B": {
        "description": "Cordova to MEPZ 1 via Hoops Dome",
        "path": ["Cordova", "Babag 2", "Tiangue Rd", "Babag 1", "A. Tumulak St", "Gun-ob", "S. Osmena St (Opon)", "Hoops Dome", "MV Patalinghug Ave", "Gaisano Island Mall", "Lapu-Lapu City Hall", "Pusok", "Marina Mall", "Savemore Mactan", "MEPZ 1 Gates", "Pusok", "Lapu-Lapu City Hall", "Gaisano Island Mall", "MV Patalinghug Ave", "Humay-humay Rd", "Hoops Dome", "S. Osmena St (Opon)", "Gun-ob", "A. Tumulak St", "Cajulao", "Tiangue Rd", "Babag 1", "Deca Homes (Babag)", "Babag 2", "Cordova"]
    },
    "MI-04B": {
        "description": "Tamiya (MEPZ 2) to MEPZ 1 via City Hall",
        "path": ["Tamiya Terminal", "Robinsons Supermarket (Mactan)", "MV Patalinghug Ave", "Crown Regency Suites (Mactan)", "Gaisano Island Mall", "Lapu-Lapu City Hall", "Dulcinea Hotel", "SSS Lapu-Lapu", "The Bellavista Hotel", "Goldberry Suites", "Pusok", "Marina Mall", "Savemore Mactan", "MEPZ 1 Gates", "Marina Mall", "Savemore Mactan", "Pusok", "The Bellavista Hotel", "Goldberry Suites", "SSS Lapu-Lapu", "Lapu-Lapu City Hall", "Gaisano Island Mall", "MV Patalinghug Ave", "Crown Regency Suites (Mactan)", "Pueblo Verde", "Robinsons Supermarket (Mactan)", "Tamiya Terminal"]
    },
}
