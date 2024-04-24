import streamlit as st
import pandas as pd
import plotly.express as px

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()
        self.available_categories = ["Food", "Clothes", "Accommodation", "Miscellaneous"]

    def load_expenses(self):
        try:
            expenses = pd.read_csv("expenses.csv")
        except FileNotFoundError:
            expenses = pd.DataFrame(columns=["Category", "Expense", "Amount"])
        return expenses

    def save_expenses(self):
        self.expenses.to_csv("expenses.csv", index=False)

    def add_expense(self, category, expense, amount):
        if category not in self.available_categories:
            self.available_categories.append(category)

        new_expense = pd.DataFrame({"Category": [category], "Expense": [expense], "Amount": [amount]})
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        self.expenses.index = self.expenses.index + 1  # Start index from 1
        self.save_expenses()

    def delete_expense(self, selected_index):
        self.expenses = self.expenses.drop(selected_index, axis=0)
        self.expenses.reset_index(drop=True, inplace=True)  # Reset index starting from 0
        self.save_expenses()

    def display_expenses(self):
        st.header("Expenses")

        st.table(self.expenses.style.set_caption("Expenses").set_table_styles([{'selector': 'caption', 'props': [('text-align', 'center')]}]))

        selected_index = st.selectbox("Select expense index to delete:", self.expenses.index + 1, format_func=lambda x: f"{x} - {self.expenses.loc[x-1, 'Expense']}")

        if st.button("Delete Expense"):
            if selected_index:
                self.delete_expense(selected_index - 1)
                st.success("Expense deleted successfully!")

        # Display total expenses
        total_expenses = self.expenses["Amount"].sum()
        st.info(f"Total Expenses: Rs.{total_expenses:.2f}")

        # Bar chart for total expenses by category
        st.header("Total Expenses by Category")
        bar_chart = px.bar(self.expenses, x="Category", y="Amount", title="Total Expenses by Category")
        st.plotly_chart(bar_chart, use_container_width=True)

        # Pie chart for distribution of expenses across categories
        st.header("Expense Distribution")
        pie_chart = px.pie(self.expenses, names="Category", values="Amount", title="Expense Distribution")
        st.plotly_chart(pie_chart, use_container_width=True)

def main():
    st.set_page_config(layout="wide") 
    st.title("Expense Tracker")

    tracker = ExpenseTracker()

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox("Category:", tracker.available_categories, key="category")
    with col2:
        expense = st.text_input("Expense:")
    with col3:
        amount = st.number_input("Amount:", min_value=0.01, format="%.2f")

    add_button = st.button("Add Expense")

    if add_button:
        tracker.add_expense(category, expense, amount)
        st.success("Expense added successfully!")

    # Display the list of expenses and charts
    tracker.display_expenses()

if __name__ == "__main__":
    main()
