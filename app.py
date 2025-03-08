import streamlit as st
import pandas as pd
import plotly.express as px


from finance_tracker_module import FinanceTracker

# Streamlit Page layout
st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")


# Custom  CSS Styles
st.markdown(
    """
    <style>
        body {
            background: transparent !important;
        }
        .metric-box {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            transition: transform 0.3s ease, background-color 0.3s ease;
            background: rgba(255, 255, 255, 0.5);
            cursor: pointer;
        }
        .metric-box:hover {
            background-color: #4CAF50;
            color: white;
        }
        .metric-box.active {
            transform: scale(1.1);
            background-color: #4CAF50;
            color: white;
        }
        .savings-rate-box {
            padding: 20px;
            border-radius: 15px;
            border: 2px solid blue;
            background: rgba(255, 255, 255, 0.5); /* Transparent background */
            margin-top: 20px;
        }
        .savings-rate-excellent {
            color: green;
            font-weight: bold;
        }
        .savings-rate-good {
            color: blue;
            font-weight: bold;
        }
        .savings-rate-average {
            color: orange;
            font-weight: bold;
        }
        .savings-rate-below-average {
            color: #ffcc00; /* Yellow */
            font-weight: bold;
        }
        .savings-rate-need-improvement {
            color: red;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Adding the Finace Tracker (or) Linking the Finace Tracker Page
if "tracker" not in st.session_state:
    st.session_state.tracker = FinanceTracker()

# Sidebar Title Name 
st.sidebar.title("Personal Finance Tracker")

# Function for updating the Section
def set_active_section(section):
    st.session_state.active_section = section

# Dashboard Interface
st.title("💰 Personal Finance Dashboard")

# Displaying the Summary
income, expense, savings = st.session_state.tracker.get_summary()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Total Income", key="income", help="Click to add income"):
        set_active_section("Income")
    st.markdown(f'<div class="metric-box {"active" if st.session_state.active_section == "Income" else ""}">\n<b>₹{income:.2f}</b></div>', unsafe_allow_html=True)
with col2:
    if st.button("Total Expenses", key="expense", help="Click to add expense"):
        set_active_section("Expense")
    st.markdown(f'<div class="metric-box {"active" if st.session_state.active_section == "Expense" else ""}">\n<b>₹{expense:.2f}</b></div>', unsafe_allow_html=True)
with col3:
    if st.button("Savings", key="savings", help="Click to add savings"):
        set_active_section("Savings")
    st.markdown(f'<div class="metric-box {"active" if st.session_state.active_section == "Savings" else ""}">\n<b>₹{savings:.2f}</b></div>', unsafe_allow_html=True)

# Transaction Form
if st.session_state.active_section:
    st.sidebar.subheader(f"Add {st.session_state.active_section}")
    date = st.sidebar.date_input("Date")
    category = st.sidebar.text_input("Category")
    amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
    if st.sidebar.button(f"Add {st.session_state.active_section}"):
        st.session_state.tracker.add_transaction(date, category, amount, st.session_state.active_section)
        st.success(f"{st.session_state.active_section} added successfully!")
        st.session_state.active_section = None
        st.rerun()

# Sidebar Payment Section
st.sidebar.header("Payment Options")



# Dynamic Payment Button
if st.sidebar.button("Pay Now"):
    st.session_state.show_payment_options = True

# Paytm option When Clicked
if "show_payment_options" in st.session_state and st.session_state.show_payment_options:
    # Select Payment Method
    payment_method = st.sidebar.selectbox(
        "Select Payment Method",
        ["UPI", "Debit Card", "Credit Card", "Net Banking"]
    )

    # Enter Amount
    amount_to_pay = st.sidebar.number_input("Amount to Pay", min_value=0.0, format="%.2f")

    # Currency Symbol (₹ for India, $ for USA) At Present This
    country = st.sidebar.selectbox("Select Country", ["India", "USA"])
    currency_symbol = "₹" if country == "India" else "$"

    # Displaying Payment Details
    if payment_method == "UPI":
        st.sidebar.subheader("UPI Payment")
        upi_id = st.sidebar.text_input("Enter your UPI ID", placeholder="test@upi")
        if upi_id and amount_to_pay > 0:
            # Sample Payment Link
            payment_link = f"https://vicky-codes17.github.io/payment_page/" #={amount_to_pay}
            st.sidebar.markdown(
                f"""
                <a href="{payment_link}" target="_blank">
                    <button style="
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    ">Pay {currency_symbol}{amount_to_pay:.2f} via UPI</button>
                </a>
                """,
                unsafe_allow_html=True,
            )
            st.sidebar.write("**Note:** This is a test payment. No real money will be transferred.")
        else:
            st.sidebar.warning("Please enter a valid UPI ID and amount.")
    elif payment_method in ["Debit Card", "Credit Card", "Net Banking"]:
        st.sidebar.subheader(f"{payment_method} Payment")
        st.sidebar.write(f"Pay {currency_symbol}{amount_to_pay:.2f} using {payment_method}.")
        if st.sidebar.button("Confirm Payment"):
            st.sidebar.success("Payment Successful! (This is a test payment.)")

# Display Transactions Table
st.header("Transactions")
st.write(st.session_state.tracker.get_transactions())

# Monthly  Visualization Chart
st.header("Monthly Summary")
monthly_summary = st.session_state.tracker.get_monthly_summary()
if not monthly_summary.empty:
    fig = px.bar(monthly_summary, x="Month", y="Amount", color="Type", barmode="group")
    st.plotly_chart(fig)
else:
    st.write("No data available for monthly summary.")

# AI Recommendations Section (Heading and Styles)
st.markdown('<div class="savings-rate-box">', unsafe_allow_html=True)
st.header("AI Recommendations")

# Calculation of   Recommendations
if income > 0:
    savings_ratio = savings / income
    expense_ratio = expense / income

    if savings_ratio >= 0.3:
        st.markdown(
            '<p class="savings-rate-excellent">🎉 Excellent! You are managing your money very well. Keep saving and investing for the future,You are a Champ on Savings</p>',
            unsafe_allow_html=True,
        )
    elif 0.2 <= savings_ratio < 0.3:
        st.markdown(
            '<p class="savings-rate-good">👍 Good! You are on the right track. Consider saving a bit more to achieve your financial goals faster.Increase your Savings for future goals</p>',
            unsafe_allow_html=True,
        )
    elif 0.1 <= savings_ratio < 0.2:
        st.markdown(
            '<p class="savings-rate-average">🤔 Average. You are spending a significant portion of your income. Try to cut unnecessary expenses and save more.Donot Waste money on unessary things,Keep Going well</p>',
            unsafe_allow_html=True,
        )
    elif 0.05 <= savings_ratio < 0.1:
        st.markdown(
            '<p class="savings-rate-below-average">⚠️ Below Average. Your spending is high compared to your savings. Review your expenses and prioritize saving.</p>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<p class="savings-rate-need-improvement">🚨 Need Improvement. You are spending almost all of your income. Start by creating a budget and tracking your expenses.</p>',
            unsafe_allow_html=True,
        )

    # How To save or Manage the savings with tips
    if expense_ratio > 0.7:
        st.markdown(
            '<p class="savings-rate-need-improvement">💡 Tip: Your expenses are very high compared to your income. Consider reducing discretionary spending and focusing on needs over wants.</p>',
            unsafe_allow_html=True,
        )
    elif expense_ratio > 0.5:
        st.markdown(
            '<p class="savings-rate-average">💡 Tip: Your expenses are moderate. Look for areas where you can save, such as subscriptions or dining out.</p>',
            unsafe_allow_html=True,
        )
else:
    st.markdown(
        '<p class="savings-rate-need-improvement">⚠️ No income data available. Please add income transactions to get personalized recommendations.</p>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)
