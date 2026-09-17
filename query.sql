SELECT 
    e.name AS employee_name,
    e.department,
    SUM(s.amount) AS total_sales,
    COUNT(s.id) AS total_orders
FROM sales s
INNER JOIN employees e ON s.employee_id = e.id
GROUP BY e.id, e.name, e.department
ORDER BY total_sales DESC;
