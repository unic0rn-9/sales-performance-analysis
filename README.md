# Sales Performance Analysis Project

A complete end-to-end data analytics project involving **Python, SQL, and Power BI** to analyze **regional**, **product-wise**, and **salesperson-wise** sales performance.

---

## 🛠 Tools & Environment

- **Python** (Pandas, NumPy, Matplotlib)  
- **MySQL**  
- **Power BI**  
- **Jupyter Notebook**

---

## 🔄 Project Workflow

### **1️⃣ Raw Data Preparation**
- Collected messy sales dataset containing missing values, inconsistent names, and duplicates.

### **2️⃣ Python-Based Data Cleaning & Preprocessing**
- Handled missing values  
- Standardized region, product, and salesperson names  
- Calculated totals such as **Sales** and **Profit**  
- Exported cleaned dataset as `cleaned_sales_data_python.csv`

### **3️⃣ Cleaned Data Stored in MySQL**
- Imported final dataset into a MySQL table for structured storage.

### **4️⃣ Power BI Dashboard Development**
Created multiple dashboards to visualize insights:
- Sales by region  
- Profit trends  
- Product-wise performance  
- Salesperson performance  

---

## ⭐ Key Features

- **Sales analysis by region** – Identify best-performing regions using sales & profit data  
- **Product performance insights** – Compare performance across Smartwatch, Mobile, Laptop, Tablet, etc.  
- **Salesperson performance visualization** – Track top-performing agents  

---

## 📊 Dashboards Included

- **Sales Performance Dashboard (.pbix)**  
- Regional analysis page  
- Product performance page  

---

## 📁 Repository Structure

```
├── raw_sales_data.csv
├── cleaned_sales_data_python.csv
├── clean_data.py
├── sales_performance_dashboard.pbix
└── sales_performance_dashboard.sql
```

---

## ▶️ How to Run the Project

### **1) Run the Python cleaning script**
```bash
python clean_data.py
```

### **2) Import cleaned data into MySQL**
Upload the generated `cleaned_sales_data_python.csv` into a MySQL table.

### **3) Open the Power BI Report**
- Open → `sales_performance_dashboard.pbix`  
- Click **Refresh** if needed  

---

### 👍 This README is fully GitHub-formatted and will render perfectly.

