import json
import random
import string
from pathlib import Path


class Bank:
    def __init__(self, database="data.json"):
        self.database = database
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            with open(self.database, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account_no(self):
        while True:
            acc = "".join(random.choices(
                string.ascii_uppercase + string.digits, k=8
            ))
            if not any(i["accountNo"] == acc for i in self.data):
                return acc

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account_no(),
            "balance": 0
        }

        self.data.append(account)
        self.save_data()
        return True, account

    def authenticate(self, acc_no, pin):
        for user in self.data:
            if user["accountNo"] == acc_no and user["pin"] == pin:
                return user
        return None

    def deposit(self, acc_no, pin, amount):
        user = self.authenticate(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0 or amount > 10000:
            return False, "Amount must be between 1 and 10000"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, acc_no, pin, amount):
        user = self.authenticate(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]
    
    def update_details(self, acc_no, pin, new_name, new_email, new_pin):
        user = self.authenticate(acc_no, pin)

        if not user:
            return False, "Invalid credentials"
        if new_name:
            user["name"] = new_name
        if new_email:
            user["email"] = new_email
        if new_pin:
            user["pin"] = int(new_pin)

        self.save_data()
        return True, "Details updated successfully"

    def delete_account(self, acc_no, pin):
        user = self.authenticate(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        self.data.remove(user)
        self.save_data()
        return True, "Account deleted"