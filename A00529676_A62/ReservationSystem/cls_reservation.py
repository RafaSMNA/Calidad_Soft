"""
Clase Reservation
"""
import json


class Reservation:
    """
    Clase Reservatio
    """
    def __init__(self, reservations_file="reservations.json"):
        """
        Inicializacion de clase
        """
        self.reservations_file = reservations_file
        self.reservations = self.load_reservations()

    def load_reservations(self):
        """
        Metodo de Lectura de documento
        """
        try:
            with open(self.reservations_file, 'r', encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_reservations(self):
        """
        Metodo que guarda documento
        """
        with open(self.reservations_file, 'w', encoding="utf-8") as f:
            json.dump(self.reservations, f, indent=4)

    def create_reservation(self, customer_email, hotel_name, reservation_id):
        """
        Metodo que crea reservacion
        """
        reservation = {'customer_email': customer_email,
                       'hotel_name': hotel_name,
                       'reservation_id': reservation_id}
        self.reservations.append(reservation)
        self.save_reservations()
        print(f"Reservation created for customer '{customer_email}'")
        print(f"at hotel '{hotel_name}'.")

    def cancel_reservation(self, customer_email, hotel_name):
        """
        Metodo que cancela reservacion
        """
        matching_reservations = [r for r in self.reservations
                                 if r['customer_email'] == customer_email
                                 and r['hotel_name'] == hotel_name]
        if matching_reservations:
            self.reservations.remove(matching_reservations[0])
            self.save_reservations()
            print(f"Reservation canceled for customer '{customer_email}'")
            print(f"at hotel '{hotel_name}'.")
        else:
            print(f"No reservation found for customer '{customer_email}'")
            print(f"at hotel '{hotel_name}'.")
