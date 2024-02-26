"""
Clase Customer
"""
import json


class Customer:
    """
    Clase Customer
    """
    def __init__(self, customers_file="customers.json"):
        """
        Inicializacion de clase
        """
        self.customers_file = customers_file
        self.customers = self.load_customers()

    def load_customers(self):
        """
        Metodo de Lectura de documento
        """
        try:
            with open(self.customers_file, 'r', encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_customers(self):
        """
        Metodo que Guarda documento
        """
        with open(self.customers_file, 'w', encoding="utf-8") as f:
            json.dump(self.customers, f, indent=4)

    def create_customer(self, name, email):
        """
        Metodo que Crea Customer
        """
        if email not in self.customers:
            self.customers[email] = {'name': name}
            self.save_customers()
            print(f"Customer '{name}' with email '{email}' created.")
        else:
            print(f"Customer with email '{email}' already exists.")

    def delete_customer(self, email):
        """
        Metodo que Borra Customer
        """
        if email in self.customers:
            del self.customers[email]
            self.save_customers()
            print(f"Customer with email '{email}' deleted.")
        else:
            print(f"Customer with email '{email}' not found.")

    def display_customer_info(self, email):
        """
        Metodo que muestra informacion de Customer
        """
        if email in self.customers:
            print(f"Customer information for email '{email}':")
            print(json.dumps(self.customers[email], indent=4))
        return self.customers[email]['name']

    def modify_customer_info(self, email, **kwargs):
        """
        Metodo que Modifica Customer
        """
        if email in self.customers:
            self.customers[email].update(kwargs)
            self.save_customers()
            print(f"Customer information for email '{email}' modified.")
        else:
            print(f"Customer with email '{email}' not found.")
