# myntra scrapper project

A complete end-to-end project that scrapes product reviews from Myntra, stores them in MongoDB, and visualizes the data with a Streamlit dashboard inside VS Code.

---

## 📁 Project Structure

myntra_scraper/
│
├── src/
│ ├── scrapper/ # Web scraping logic
│ ├── cloud_io/ # MongoDB interaction
│ ├── data_report/ # Streamlit dashboard logic
│ └── constants/ # Config values (Mongo URI, DB name, etc.)
│
├── pages/ # Streamlit sub-pages
├── app.py # Streamlit entry point
├── requirements.txt
├── README.md
└── .env/ # Virtual environment folder

2. Create Virtual Environment

In the terminal (inside project folder):

python -m venv .env
Activate it:

PowerShell (in VS Code Terminal):

.\.env\Scripts\Activate.ps1
CMD:

.env\Scripts\activate.bat

3. Install Dependencies

pip install -r requirements.txt

4. Set the Python Interpreter in VS Code
Press Ctrl + Shift + P

Choose: Python: Select Interpreter

Select .env\Scripts\python.exe

5. Configure MongoDB Connection
Edit the file:

src/constants/constants.py

MONGO_URI = "mongodb+srv://Neetesh:12345@cluster0.oibqarz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "myntra_reviews"
Make sure MongoDB is running on your machine.

6. Run the App

In the VS Code terminal:
streamlit run app.py
It will open the dashboard in your browser.

🔍 Features
✅ Scrape reviews from Myntra with Selenium

✅ Store and fetch data from MongoDB

✅ Display product analysis using:

Pie and bar charts (Plotly)

Positive and negative comments

Price and rating distribution

📦 Requirements
Install all dependencies via:

pip install -r requirements.txt
🧾 Sample requirements.txt

streamlit
pandas
plotly
selenium
pymongo
dnspython
beautifulsoup4

📬 Contact
Created by Neetesh Kumar.
Feel free to connect on LinkedIn for queries or collaborations!



