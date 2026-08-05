"""
vehicle_database.py

Shared vehicle database for the Vehicle Dynamics Calculator project.
Each vehicle stores:
- power: Horsepower (hp)
- weight: Kerb weight (kg)
- cd: Drag coefficient
- area: Frontal area (m²)
- drive: Drivetrain
- fuel: Fuel type
"""

cars = {

    # HATCHBACKS
    "Maruti Suzuki Alto K10": {"power":67,"weight":790,"cd":0.34,"area":1.95,"drive":"FWD","fuel":"Petrol"},
    "Maruti Suzuki Swift": {"power":89,"weight":920,"cd":0.32,"area":2.05,"drive":"FWD","fuel":"Petrol"},
    "Maruti Suzuki Baleno": {"power":89,"weight":955,"cd":0.31,"area":2.08,"drive":"FWD","fuel":"Petrol"},
    "Hyundai i20": {"power":88,"weight":1055,"cd":0.31,"area":2.08,"drive":"FWD","fuel":"Petrol"},
    "Volkswagen Polo": {"power":108,"weight":1163,"cd":0.32,"area":2.03,"drive":"FWD","fuel":"Petrol"},
    "Tata Altroz": {"power":88,"weight":1036,"cd":0.32,"area":2.10,"drive":"FWD","fuel":"Petrol"},

    # SEDANS
    "Honda City": {"power":121,"weight":1150,"cd":0.29,"area":2.20,"drive":"FWD","fuel":"Petrol"},
    "Hyundai Verna": {"power":113,"weight":1178,"cd":0.28,"area":2.20,"drive":"FWD","fuel":"Petrol"},
    "Honda Civic": {"power":174,"weight":1320,"cd":0.27,"area":2.18,"drive":"FWD","fuel":"Petrol"},
    "Volkswagen Virtus": {"power":148,"weight":1275,"cd":0.30,"area":2.23,"drive":"FWD","fuel":"Petrol"},
    "Skoda Slavia": {"power":148,"weight":1260,"cd":0.29,"area":2.23,"drive":"FWD","fuel":"Petrol"},
    "Maruti Suzuki Ciaz": {"power":103,"weight":1010,"cd":0.29,"area":2.21,"drive":"FWD","fuel":"Petrol"},
    "Audi A4": {"power":201,"weight":1555,"cd":0.26,"area":2.22,"drive":"AWD","fuel":"Petrol"},
    "BMW 3 Series": {"power":255,"weight":1625,"cd":0.23,"area":2.20,"drive":"RWD","fuel":"Petrol"},
    "Mercedes-Benz C-Class": {"power":255,"weight":1670,"cd":0.24,"area":2.23,"drive":"RWD","fuel":"Petrol"},
    "Mercedes-Benz S-Class": {"power":362,"weight":1950,"cd":0.22,"area":2.40,"drive":"RWD","fuel":"Petrol"},
    "Toyota Camry Hybrid": {"power":227,"weight":1645,"cd":0.27,"area":2.28,"drive":"FWD","fuel":"Hybrid"},

    # SUVs
    "Hyundai Venue": {"power":118,"weight":1165,"cd":0.35,"area":2.30,"drive":"FWD","fuel":"Petrol"},
    "Kia Sonet": {"power":118,"weight":1220,"cd":0.35,"area":2.32,"drive":"FWD","fuel":"Petrol"},
    "Honda Elevate": {"power":121,"weight":1213,"cd":0.35,"area":2.40,"drive":"FWD","fuel":"Petrol"},
    "Maruti Suzuki Brezza": {"power":102,"weight":1130,"cd":0.35,"area":2.35,"drive":"FWD","fuel":"Petrol"},
    "Toyota Hyryder": {"power":102,"weight":1195,"cd":0.34,"area":2.38,"drive":"FWD","fuel":"Petrol"},
    "Maruti Suzuki Grand Vitara": {"power":102,"weight":1185,"cd":0.34,"area":2.38,"drive":"FWD","fuel":"Petrol"},
    "Hyundai Creta": {"power":113,"weight":1260,"cd":0.36,"area":2.45,"drive":"FWD","fuel":"Petrol"},
    "Hyundai Alcazar": {"power":158,"weight":1500,"cd":0.35,"area":2.55,"drive":"FWD","fuel":"Petrol"},
    "Kia Seltos": {"power":158,"weight":1350,"cd":0.35,"area":2.43,"drive":"FWD","fuel":"Petrol"},
    "MG Astor": {"power":108,"weight":1320,"cd":0.35,"area":2.40,"drive":"FWD","fuel":"Petrol"},
    "MG Hector": {"power":168,"weight":1710,"cd":0.37,"area":2.60,"drive":"FWD","fuel":"Petrol"},
    "Mahindra XUV700": {"power":197,"weight":1775,"cd":0.35,"area":2.60,"drive":"FWD","fuel":"Petrol"},
    "Mahindra Scorpio-N": {"power":200,"weight":1880,"cd":0.40,"area":2.70,"drive":"RWD","fuel":"Diesel"},
    "Mahindra Bolero Neo": {"power":100,"weight":1600,"cd":0.43,"area":2.55,"drive":"RWD","fuel":"Diesel"},
    "Mahindra Thar": {"power":150,"weight":1750,"cd":0.52,"area":2.65,"drive":"4WD","fuel":"Diesel"},
    "Mahindra Thar Roxx": {"power":174,"weight":1950,"cd":0.49,"area":2.75,"drive":"4WD","fuel":"Diesel"},
    "Toyota Fortuner": {"power":201,"weight":2095,"cd":0.38,"area":2.75,"drive":"4WD","fuel":"Diesel"},
    "Toyota Land Cruiser 300": {"power":304,"weight":2490,"cd":0.35,"area":2.90,"drive":"4WD","fuel":"Diesel"},
    "Toyota Hilux": {"power":201,"weight":2205,"cd":0.41,"area":2.85,"drive":"4WD","fuel":"Diesel"},
    "Tata Nexon": {"power":118,"weight":1230,"cd":0.36,"area":2.38,"drive":"FWD","fuel":"Petrol"},
    "Tata Harrier": {"power":168,"weight":1650,"cd":0.36,"area":2.55,"drive":"FWD","fuel":"Diesel"},
    "Tata Safari": {"power":168,"weight":1825,"cd":0.37,"area":2.60,"drive":"FWD","fuel":"Diesel"},
    "Jeep Compass": {"power":168,"weight":1580,"cd":0.36,"area":2.48,"drive":"FWD","fuel":"Diesel"},
    "Jeep Meridian": {"power":168,"weight":1798,"cd":0.37,"area":2.60,"drive":"FWD","fuel":"Diesel"},
    "Volkswagen Tiguan": {"power":201,"weight":1703,"cd":0.33,"area":2.55,"drive":"AWD","fuel":"Petrol"},
    "Volkswagen Tayron": {"power":201,"weight":1780,"cd":0.32,"area":2.58,"drive":"AWD","fuel":"Petrol"},
    "Skoda Kodiaq": {"power":201,"weight":1820,"cd":0.33,"area":2.60,"drive":"AWD","fuel":"Petrol"},
    "Land Rover Defender 110": {"power":296,"weight":2361,"cd":0.38,"area":2.85,"drive":"AWD","fuel":"Diesel"},
    "Range Rover Sport": {"power":395,"weight":2350,"cd":0.34,"area":2.80,"drive":"AWD","fuel":"Petrol"},

    # MPVs
    "Toyota Innova Hycross": {"power":183,"weight":1785,"cd":0.34,"area":2.65,"drive":"FWD","fuel":"Hybrid"},
    "Kia Carens": {"power":158,"weight":1420,"cd":0.34,"area":2.55,"drive":"FWD","fuel":"Petrol"},

    # SPORTS CARS
    "Toyota Supra MK5": {"power":382,"weight":1540,"cd":0.31,"area":2.00,"drive":"RWD","fuel":"Petrol"},
    "Porsche 911 Carrera": {"power":379,"weight":1505,"cd":0.29,"area":2.05,"drive":"RWD","fuel":"Petrol"},
    "BMW M3": {"power":473,"weight":1730,"cd":0.34,"area":2.25,"drive":"RWD","fuel":"Petrol"},
    "BMW M4 Competition": {"power":503,"weight":1725,"cd":0.34,"area":2.18,"drive":"RWD","fuel":"Petrol"},
    "Audi S5": {"power":349,"weight":1695,"cd":0.29,"area":2.20,"drive":"AWD","fuel":"Petrol"},
    "Ford Mustang GT": {"power":486,"weight":1765,"cd":0.36,"area":2.25,"drive":"RWD","fuel":"Petrol"},
    "Nissan GT-R R35": {"power":565,"weight":1740,"cd":0.26,"area":2.10,"drive":"AWD","fuel":"Petrol"},
    "Bugatti Chiron": {"power":1479,"weight":1995,"cd":0.36,"area":2.07,"drive":"AWD","fuel":"Petrol"},
    "Koenigsegg Jesko": {"power":1600,"weight":1420,"cd":0.28,"area":1.95,"drive":"RWD","fuel":"Petrol"},

    # ELECTRIC VEHICLES
    "Tata Punch EV": {"power":120,"weight":1360,"cd":0.36,"area":2.30,"drive":"FWD","fuel":"Electric"},
    "Tata Nexon EV": {"power":143,"weight":1400,"cd":0.35,"area":2.38,"drive":"FWD","fuel":"Electric"},
    "Tata Curvv EV": {"power":167,"weight":1700,"cd":0.30,"area":2.42,"drive":"FWD","fuel":"Electric"},
    "MG Windsor EV": {"power":134,"weight":1550,"cd":0.29,"area":2.45,"drive":"FWD","fuel":"Electric"},
    "MG ZS EV": {"power":174,"weight":1610,"cd":0.33,"area":2.43,"drive":"FWD","fuel":"Electric"},
    "Hyundai Creta Electric": {"power":169,"weight":1650,"cd":0.34,"area":2.42,"drive":"FWD","fuel":"Electric"},
    "Mahindra BE 6": {"power":282,"weight":1950,"cd":0.27,"area":2.38,"drive":"RWD","fuel":"Electric"},
    "Mahindra XEV 9e": {"power":282,"weight":2100,"cd":0.26,"area":2.50,"drive":"RWD","fuel":"Electric"},
    "Tesla Model 3": {"power":283,"weight":1765,"cd":0.23,"area":2.22,"drive":"RWD","fuel":"Electric"},
    "Tesla Model S": {"power":670,"weight":2069,"cd":0.208,"area":2.34,"drive":"AWD","fuel":"Electric"},
}