from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Dummy-Daten für Elektrofahrzeuge
fleet_data = [
    {
        'id': 1,
        'name': 'Tesla Model 3',
        'mileage': '45,000 km',
        'battery_status': '80%',
        'last_service': '2024-01-10',
        'driving_behavior': 'Effizient',
        'avg_consumption': '14 kWh/100km',
        'image': 'https://via.placeholder.com/300x200.png?text=Tesla+Model+3'
    },
    {
        'id': 2,
        'name': 'Nissan Leaf',
        'mileage': '30,000 km',
        'battery_status': '75%',
        'last_service': '2023-11-20',
        'driving_behavior': 'Moderate',
        'avg_consumption': '16 kWh/100km',
        'image': 'https://via.placeholder.com/300x200.png?text=Nissan+Leaf'
    },
    {
        'id': 3,
        'name': 'Audi e-tron',
        'mileage': '25,000 km',
        'battery_status': '90%',
        'last_service': '2024-02-01',
        'driving_behavior': 'Sportlich',
        'avg_consumption': '20 kWh/100km',
        'image': 'https://via.placeholder.com/300x200.png?text=Audi+e-tron'
    }
]

# Verfügbare Fahrzeuge zur Miete
rental_cars = [
    {
        'id': 4,
        'name': 'BMW i3',
        'image': 'https://via.placeholder.com/300x200.png?text=BMW+i3',
        'rental_price': '400 CHF/Monat',
        'rental_period': [1, 3, 5]  # Mietoptionen in Jahren
    },
    {
        'id': 5,
        'name': 'Mercedes EQC',
        'image': 'https://via.placeholder.com/300x200.png?text=Mercedes+EQC',
        'rental_price': '550 CHF/Monat',
        'rental_period': [1, 3, 5]
    }
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/fleet')
def fleet():
    return render_template('fleet.html', vehicles=fleet_data)

@app.route('/vehicle/<int:vehicle_id>')
def vehicle(vehicle_id):
    vehicle = next((v for v in fleet_data if v['id'] == vehicle_id), None)
    if vehicle:
        return render_template('vehicle_detail.html', vehicle=vehicle)
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
    app.run(debug=True)
