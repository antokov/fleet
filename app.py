from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Dummy data for fleet vehicles
fleet_data = [
    {
        'id': 1,
        'name': 'Tesla Model 3',
        'mileage': '45,000 km',
        'battery_status': '80%',
        'last_service': '2024-01-10',
        'next_service': '2024-07-10',
        'driving_behavior': 'Effizient',
        'avg_consumption': '14 kWh/100km',
        'image': 'https://via.placeholder.com/300x200.png?text=Tesla+Model+3',
        'charging_cycles': None,
        'tire_pressure_status': 'OK',
        'availability': 'Verfügbar',
        'utilization': 85
    },
    {
        'id': 2,
        'name': 'Nissan Leaf',
        'mileage': '30,000 km',
        'battery_status': '75%',
        'last_service': '2023-11-20',
        'next_service': '2024-05-20',
        'driving_behavior': 'Moderate',
        'avg_consumption': '16 kWh/100km',
        'image': 'https://via.placeholder.com/300x200.png?text=Nissan+Leaf',
        'charging_cycles': None,
        'tire_pressure_status': 'OK',
        'availability': 'Verfügbar',
        'utilization': 70
    }
]

# Dummy data for rental cars
rental_cars = [
    {
        'id': 3,
        'name': 'BMW i3',
        'image': 'https://via.placeholder.com/300x200.png?text=BMW+i3',
        'rental_price': '400 CHF/Monat',
        'rental_period': [1, 3, 5]  # Mietoptionen in Jahren
    },
    {
        'id': 4,
        'name': 'Mercedes EQC',
        'image': 'https://via.placeholder.com/300x200.png?text=Mercedes+EQC',
        'rental_price': '550 CHF/Monat',
        'rental_period': [1, 3, 5]
    }
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', vehicles=fleet_data)

@app.route('/fleet')
def fleet():
    return render_template('fleet.html', vehicles=fleet_data)

@app.route('/vehicle/<int:vehicle_id>')
def vehicle(vehicle_id):
    vehicle = next((v for v in fleet_data if v['id'] == vehicle_id), None)
    if vehicle:
        # Calculate days until next service
        next_service_date = datetime.strptime(vehicle['next_service'], '%Y-%m-%d')
        today = datetime.now()
        days_until_service = (next_service_date - today).days

        return render_template('vehicle_detail.html', vehicle=vehicle, days_until_service=days_until_service)
    return "Vehicle not found", 404

@app.route('/rent')
def rent():
    return render_template('rent.html', rental_cars=rental_cars)

@app.route('/rent/<int:car_id>')
def rent_details(car_id):
    car = next((c for c in rental_cars if c['id'] == car_id), None)
    if car:
        return render_template('rent_detail.html', car=car)
    return "Car not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
