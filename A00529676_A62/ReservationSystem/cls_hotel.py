import json
from datetime import datetime

class Hotel:
    def __init__(self, hotels_file="hotels.json"):
        self.hotels_file = hotels_file
        self.hotels = self.load_hotels()

    def load_hotels(self):
        try:
            with open(self.hotels_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}    

    def save_hotels(self):
        with open(self.hotels_file, 'w') as f:
            json.dump(self.hotels, f, indent=4)

    def create_hotel(self, name, capacity):
        if name not in self.hotels:
            self.hotels[name] = {'capacity': capacity, 'reservations': {}}
            self.save_hotels()
            print(f"Hotel '{name}' created with capacity {capacity}.")
        else:
            print(f"Hotel '{name}' already exists.")    

    def delete_hotel(self, name):
        if name in self.hotels:
            del self.hotels[name]
            self.save_hotels()
            print(f"Hotel '{name}' deleted.")
        else:
            print(f"Hotel '{name}' not found.")

    def display_hotel_info(self, name):
        if name in self.hotels:
            print(f"Hotel '{name}' information:")
            print(json.dumps(self.hotels[name], indent=4))
        else:
            print(f"Hotel '{name}' not found.")

    def modify_hotel_info(self, name, **kwargs):
        if name in self.hotels:
            self.hotels[name].update(kwargs)
            self.save_hotels()
            print(f"Hotel '{name}' information modified.")
        else:
            print(f"Hotel '{name}' not found.")

    def reserve_room(self, hotel_name, customer_name, check_in_date, check_out_date):
        if hotel_name in self.hotels:
            reservations = self.hotels[hotel_name]['reservations']
            reservation_id = len(reservations) + 1
            reservations[reservation_id] = {
                'customer': customer_name,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date
            }
            self.save_hotels()
            print(f"Room reserved for {customer_name} at hotel '{hotel_name}' from {check_in_date} to {check_out_date}.")
        else:
            print(f"Hotel '{hotel_name}' not found.")

    def cancel_reservation(self, hotel_name, reservation_id):
        if hotel_name in self.hotels:
            reservations = self.hotels[hotel_name]['reservations']
            if reservation_id in reservations:
                del reservations[reservation_id]
                self.save_hotels()
                print(f"Reservation {reservation_id} canceled for hotel '{hotel_name}'.")
            else:
                print(f"Reservation {reservation_id} not found for hotel '{hotel_name}'.")
        else:
            print(f"Hotel '{hotel_name}' not found.")

