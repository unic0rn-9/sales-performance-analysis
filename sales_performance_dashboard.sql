CREATE DATABASE sales_db;
USE sales_db;
SELECT * FROM cleaned_sales_data;

SELECT COUNT(*) AS Total_Records 
FROM cleaned_sales_data;

SELECT Region, SUM(Sales) AS Total_Sales
FROM cleaned_sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT Region, SUM(Profit) AS Total_Profit
FROM cleaned_sales_data
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT Salesperson, 
       SUM(Sales) AS Total_Sales, 
       SUM(Profit) AS Total_Profit
FROM cleaned_sales_data
GROUP BY Salesperson
ORDER BY Total_Sales DESC;

SELECT Product, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM cleaned_sales_data
GROUP BY Product
ORDER BY Avg_Sales DESC;

SELECT Product, SUM(Sales) AS Total_Sales
FROM cleaned_sales_data
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;

SELECT Region, SUM(Quantity) AS Total_Quantity
FROM cleaned_sales_data
GROUP BY Region
ORDER BY Total_Quantity DESC;

SELECT MONTHNAME(Order_Date) AS Month, SUM(Sales) AS Total_Sales
FROM cleaned_sales_data
GROUP BY MONTH(Order_Date)
ORDER BY Total_Sales DESC
LIMIT 1;

SELECT Region, 
       ROUND(AVG(Profit / Sales * 100), 2) AS Avg_Profit_Percentage
FROM cleaned_sales_data
GROUP BY Region
ORDER BY Avg_Profit_Percentage DESC;

SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, 
       SUM(Sales) AS Total_Sales
FROM cleaned_sales_data
GROUP BY Month
ORDER BY Month;

