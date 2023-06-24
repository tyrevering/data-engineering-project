
create or replace table `grocery_data_engineering.tbl_analytics` as (
select 
f.Order_ID,
i.Category,
i.Sub_Category,
cast(d.Order_Month as int) as Order_Month,
cast(d.Order_Year as int) as Order_Year,
f.Sales,
f.Profit,
l.City,
l.Region

from 

`grocery_data_engineering.fact_table` f
join `grocery_data_engineering.datetime_dim`d on f.datetime_id = d.datetime_id
join `grocery_data_engineering.customer_dim`c on f.Customer_ID = c.Customer_ID
join `grocery_data_engineering.location_dim`l on f.location_id = l.location_id
join `grocery_data_engineering.item_dim`i on f.Item_ID = i.Item_ID


);