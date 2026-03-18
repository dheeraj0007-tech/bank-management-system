import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Simple Bank Application")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create Account", "Deposit", "Withdraw", "View Balance", "Update Details", "Delete Account"]
)


# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4 digits)", type="password")

    if st.button("Create Account"):
        success, result = bank.create_account(
            name, age, email, int(pin)
        )
        if success:
            st.success("Account Created Successfully 🎉")
            st.write("Account Number:", result["accountNo"])
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit(acc, int(pin), amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw(acc, int(pin), amount)
        if success:
            st.success(f"New Balance: ₹{msg}")
        else:
            st.error(msg)

# ---------------- VIEW ----------------
elif menu == "View Balance":
    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        user = bank.authenticate(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid credentials")

# ---------------- UPDATE DETAILS ----------------
elif menu == "Update Details":
    st.header("Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN (4 digits)", type="password")

    if st.button("Update"):
        success, msg = bank.update_details(acc, int(pin), new_name, new_email, new_pin)
        if success:
            st.success(msg)
        else:
            st.error(msg)

# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        if success:
            st.success(msg)
        else:
            st.error(msg)