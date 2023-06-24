-- average profit by location id
select AVG(Profit), location_id from `grocery_data_engineering.fact_table`  
group by location_id;

--sales by customer
select c.Customer_Name,ft.Sales from `grocery_data_engineering.fact_table` ft 
join `grocery_data_engineering.customer_dim`c
on c.Customer_ID = ft.Customer_ID;

--profit by subcategory
select ft.Profit, cat.Sub_Category from `grocery_data_engineering.fact_table` ft 
join `grocery_data_engineering.item_dim`cat 
on cat.Item_ID=ft.Item_ID;