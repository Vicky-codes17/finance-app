import pandas as pd
import streamlit as st

class FinanceTracker:
    def __init__(self):
        # Initialize the transation details
        if "transactions" not in st.session_state:
            st.session_state.transactions = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])
        self.data = st.session_state.transactions  # Connect with session state

    def add_transaction(self, date, category, amount, transaction_type):
        """
        Add a new transaction to the tracker.
        
        Args:
            date (str or datetime): The date of the transaction.
            category (str): The category of the transaction (e.g., "Salary", "Rent").
            amount (float): The amount of the transaction.
            transaction_type (str): The type of transaction ("Income" or "Expense").
        """
        # Ensureing the data in formatted
        date = pd.to_datetime(date)
        
        # Create a new transaction DataFrame
        new_transaction = pd.DataFrame({
            "Date": [date],
            "Category": [category],
            "Amount": [amount],
            "Type": [transaction_type]
        })
        
        # Adding new transaction to the existing data
        self.data = pd.concat([self.data, new_transaction], ignore_index=True)
        
        # Updating the state
        st.session_state.transactions = self.data

    def get_summary(self):
        """
        Returns the total income, expense, and savings.
        
        Returns:
            tuple: (total_income, total_expense, total_savings)
        """
        if self.data.empty:
            return 0.0, 0.0, 0.0
        
        # Calculate total income and expenses
        income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        expense = self.data[self.data["Type"] == "Expense"]["Amount"].sum()



        # Calculate savings as income - expenses
        savings = income - expense
        
        return income, expense, savings

    def get_transactions(self):
        """
        Returns the full transaction history sorted by date (newest first).
        
        Returns:
            pd.DataFrame: The transaction history.
        """
        if self.data.empty:
            return pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])
        
        return self.data.sort_values(by="Date", ascending=False)

    def get_monthly_summary(self):
        """
        Returns a grouped summary by month and type (Income, Expense).
        
        Returns:
            pd.DataFrame: Monthly summary with columns ["Month", "Type", "Amount"].
        """
        if self.data.empty:
            return pd.DataFrame(columns=["Month", "Type", "Amount"])
        
        # Date column is in datetime format
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        
        # Extracting  month from the date
        self.data["Month"] = self.data["Date"].dt.strftime('%Y-%m')
        
        # Group by month and type, then sum the amounts
        monthly_summary = self.data.groupby(["Month", "Type"])["Amount"].sum().reset_index()
        
        return monthly_summary