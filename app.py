from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)

# Fleet data including only Mercedes-Benz eSprinter and eVito with individual descriptions
fleet_data = [
    {
        'id': 1,
        'name': 'Mercedes-Benz eSprinter',
        'mileage': '20,000 km',
        'battery_status': '85%',
        'last_service': '2024-03-15',
        'next_service': '2024-09-15',
        'driving_behavior': 'Effizient',
        'avg_consumption': '20 kWh/100km',
        'image': 'img/mercedes_esprinter.jpg',
        'rental_price': '600 CHF/Monat',
        'rental_period': [1, 3, 5],
        'description': 'Der Mercedes-Benz eSprinter ist ein vollelektrischer Transporter mit hoher Ladekapazität und moderner Technologie.'
    },
    {
        'id': 2,
        'name': 'Mercedes-Benz eVito',
        'mileage': '25,000 km',
        'battery_status': '80%',
        'last_service': '2024-02-10',
        'next_service': '2024-08-10',
        'driving_behavior': 'Moderate',
        'avg_consumption': '22 kWh/100km',
        'image': 'img/mercedes_evito.jpg',
        'rental_price': '550 CHF/Monat',
        'rental_period': [1, 2, 4],
        'description': 'Der Mercedes-Benz eVito bietet elektrische Mobilität für vielseitige Einsätze.'
    }
]

# Fleet Overview Data
fleet_overview_data = [
    {
        'id': 1,
        'name': 'Mercedes-Benz eSprinter',
        'vin': 'WDB9066571P123456',
        'license_plate': 'ZH-123456',
        'year': 2022,
        'mileage': '20,000 km',
        'battery_status': '85%',
        'last_service': '2024-03-15',
        'next_service': '2024-09-15',
        'days_until_service': 45,
        'driving_behavior': 'Efficient',
        'avg_consumption': '20 kWh/100km',
        'charging_cycles': 150,
        'tire_pressure': {
            'front_left': 2.5,
            'front_right': 2.5,
            'rear_left': 2.8,
            'rear_right': 2.8
        },
        'efficiency': 90,  # Efficiency percentage
        'availability': 'Available',
        'current_location': 'Zurich Depot',
        'assigned_driver': 'John Smith',
        'cost_per_km': '0.20 CHF/km',
        'maintenance_costs': '1,500 CHF',
        'fuel_energy_costs': '800 CHF',
        'depreciation_value': '45,000 CHF',
        'image': 'img/mercedes_esprinter.jpg',
        'accident_history': [
            {'date': '2023-11-15', 'description': 'Rear-end collision at low speed. Minor bumper damage.'},
            {'date': '2022-08-02', 'description': 'Scratches on the left door due to a parking incident.'},
        ]
    },
    {
        'id': 2,
        'name': 'Mercedes-Benz eVito',
        'vin': 'WDB4477031N654321',
        'license_plate': 'BE-654321',
        'year': 2021,
        'mileage': '25,000 km',
        'battery_status': '80%',
        'last_service': '2024-02-10',
        'next_service': '2024-08-10',
        'days_until_service': 102,
        'driving_behavior': 'Moderate',
        'avg_consumption': '22 kWh/100km',
        'charging_cycles': 200,
        'tire_pressure': {
            'front_left': 2.4,
            'front_right': 2.4,
            'rear_left': 2.7,
            'rear_right': 2.7
        },
        'efficiency': 75,  # Efficiency percentage
        'availability': 'In Use',
        'current_location': 'Bern Depot',
        'assigned_driver': 'Jane Doe',
        'cost_per_km': '0.25 CHF/km',
        'maintenance_costs': '1,800 CHF',
        'fuel_energy_costs': '1,000 CHF',
        'depreciation_value': '40,000 CHF',
        'image': 'img/mercedes_evito.jpg',
        'accident_history': [
            {'date': '2023-06-20', 'description': 'Minor dent on the rear door due to reversing.'},
        ]
    },
    {
        'id': 3,
        'name': 'Mercedes-Benz eVito',
        'vin': 'WDF4156031P789012',
        'license_plate': 'GE-789012',
        'year': 2023,
        'mileage': '15,000 km',
        'battery_status': '90%',
        'last_service': '2024-04-01',
        'next_service': '2024-10-01',
        'days_until_service': 5,
        'driving_behavior': 'Eco-friendly',
        'avg_consumption': '18 kWh/100km',
        'charging_cycles': 100,
        'tire_pressure': {
            'front_left': 2.6,
            'front_right': 2.6,
            'rear_left': 2.9,
            'rear_right': 2.9
        },
        'efficiency': 95,  # Efficiency percentage
        'availability': 'In Use',
        'current_location': 'Geneva Depot',
        'assigned_driver': 'Michael Brown',
        'cost_per_km': '0.18 CHF/km',
        'maintenance_costs': '1,200 CHF',
        'fuel_energy_costs': '700 CHF',
        'depreciation_value': '48,000 CHF',
        'image': 'img/mercedes_evito.jpg',
        'accident_history': [
            {'date': '2023-06-20', 'description': 'Minor dent on the rear door due to reversing.'},
        ]
    }
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', vehicles=fleet_overview_data)

@app.route('/fleet')
def fleet():
    return render_template('fleet.html', vehicles=fleet_overview_data)

@app.route('/vehicle/<int:vehicle_id>')
def vehicle(vehicle_id):
    vehicle = next((v for v in fleet_overview_data if v['id'] == vehicle_id), None)
    if vehicle:
        next_service_date = datetime.strptime(vehicle['next_service'], '%Y-%m-%d')
        today = datetime.now()
        days_until_service = (next_service_date - today).days

        return render_template('vehicle_detail.html', vehicle=vehicle, days_until_service=days_until_service)
    return "Vehicle not found", 404

@app.route('/rent')
def rent():
    return render_template('rent.html', rental_cars=fleet_data)

@app.route('/rent/<int:car_id>', methods=['GET', 'POST'])
def rent_details(car_id):
    car = next((c for c in fleet_data if c['id'] == car_id), None)
    if not car:
        return "Car not found", 404

    # Rack options defined here
    rack_options = [
        {'value': 'none', 'name': 'None', 'description': 'Kein Regalsystem ausgewählt.', 'image': 'img/none.jpg'},
        {'value': 'safety', 'name': 'Safety Rack', 'description': 'Für sicheren Transport von Werkzeugen und Materialien.', 'image': 'img/safety-1-300x280.jpg'},
        {'value': 'professional', 'name': 'Professional Rack', 'description': 'Optimiert für professionelle Anwendungen mit hoher Kapazität.', 'image': 'img/professional-1-300x280.jpg'},
        {'value': 'mobile', 'name': 'Mobile Rack', 'description': 'Flexibel und mobil für vielseitige Einsätze.', 'image': 'img/mobile-1-300x280.jpg'},
        {'value': 'light_shelf', 'name': 'Light Shelf', 'description': 'Leichtes Regalsystem für kleinere Lasten.', 'image': 'img/lightshelf-1-300x280.jpg'}
    ]

    return render_template(
        'rent_detail.html',
        car=car,
        rack_options=rack_options
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
