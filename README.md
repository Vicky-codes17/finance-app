# 💰 Finance App

## 📌 Overview
Finance App is a personal finance management tool built using Streamlit. It helps users track their income, expenses, and savings efficiently. The application includes UPI payment integration and provides real-time updates to charts and tables when adding transactions.

## 🚀 Features
- 🎨 **User-friendly UI**: Built with Streamlit for a clean and interactive experience.
- 📊 **Expense Tracking**: Log and categorize expenses easily.
- 💵 **Income Management**: Add and view income sources.
- 🏦 **Savings Monitoring**: Keep track of savings over time.
- 📂 **Data Persistence**: Transactions are stored in a CSV file.
- 🤖 **Machine Learning Model**: Predicts spending trends using a trained model.
- 💳 **UPI Payment Integration**: Supports real payment transaction.

## 📁 Project Structure
```
finance-app/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py
├── data/
│   └── transactions.csv
├── models/
│   └── spending_model.pkl
├── modules/
│   ├── finance_tracker_module.py
│   └── finance_tracker_module.cpython-312.pyc
├── scripts/
│   ├── db_connection.py
│   └── train_model.py
└── finance_tracker.cpython-312.pyc
```

## 🛠 Installation
### Prerequisites
Ensure you have Python 3.12 installed.

### Setup Instructions
```bash
# Clone the repository
git clone https://github.com/Vicky-codes17finance-app.git
cd finance-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📌 Usage
- ➕ **Adding Transactions**: Enter income and expenses via the UI.
- 📈 **Viewing Analytics**: Check charts and tables for financial insights.
- 🏗 **Training Model**:
  ```bash
  python scripts/train_model.py
  ```
- 🔗 **Database Connection Test**:
  ```bash
  python scripts/db_connection.py
  ```

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the application.

## 📧 Contact
For any questions, contact [vigneshrameshrm18@gmail.com](mailto:your-email@example.com).

🌐 Connect with me on [LinkedIn](https://www.linkedin.com/in/vigneshramesh-13j01/)
For any questions, contact [vigneshrameshrm18@gmail.com](mailto:your-email@example.com).

