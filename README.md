# Project Goal
------------
We want to launch a new marketing campaign in the near future. The holidays are a time for celebration. For many, they also mean the return of the dreaded shopping season. With Black Friday and Cyber Monday right around the corner, it is important to start preparing now. The 4th quarter of the year is shoulder season for our online store, we would like to create a marketing plan for 2018. 


The threes Ps of marketing are the key factors that are involved in the marketing of a good or service. They are the product, profit, and promotion of a good or service. With our data analysis, our goal is draw a near accurate marketing strategy.



Initial Questions
-----------------
* How much did the store make and sell between 2014 and 2017?

* Which was the most profitable sub-category? 

* What item / discount is responsible for the dip in profit for 2017?

* Overall Q4 Sales for the past three years? 

* What's the discount distribution? 


# Project Planning
Plan -> Acquire -> Prepare -> Explore -> Deliver
Planning:

***Create a README file***
* Ensure my dataprep modules are well documents and functional

***Acquisition***

* Obtain superstore data from Codeup mySQL database via dataprep.py

***Preparation***

* Clean superstore data from Codeup mySQL database via wrangle.py


***Exploration ***

* Ask and answer questions about the superstore data.
* Visually represent findings with charts. 

***Deliver***

* Deliver a 5 minute presentation via a powerpoint. 
* Answer questions about my code, process, and findings.

***

# Data Dictionary
--------------

Feature -----> Discription

order_id    ----->       The order number. 

ship_date     ----->     The date an order was shipped. 

shipping_method  ----->  Standard delivery method for stock items sent to this customer.  

customer_id  ----->      Customer ID Number (system assigned)

segment     ----->       Customer type, home office, consumer and corporate. 

country     ----->       Delivery country for the customer.

city     ----->          Delivery city code for the customer.

state     ----->         Delivery state for the customer. 

zip_code    ----->       Delivery postal code for the customer 

product id   ----->      Product ID number. 

sales     ----->         The sale amount of an order. 

quantity   ----->        The quantity amount. 

discount   ----->        The discount percentage. 

profit     ----->        The profit amount of an order. 

category_id  ----->      A unique identifier for a category.

region_id    ----->      A unique identifier for a region. 

product name   ----->    The name of a product. 

category     ----->      The name of the category in the product catalog.

sub_category   ----->    The name of the category in the product catalog.

region_name    ----->    The name of the region. 

year          ----->     The name of the year for an order. 

month         ----->     The name of the month for an order. 

# Steps to Reproduce
You will need your own env file with database credentials along with all the necessary files listed below to run the "Final Report" notebook.

Read this README.md

Download at the aquire.py and Final Report.ipynb file into your working directory

Create a .gitignore for your .env file

Add your own env file to your directory with username, password, and host address.

Run the final_report.ipynb notebook

***

# Key Findings
* Majority of profit comes from Office Supplies, Technology 
* Office Supply sell 4-to-1 compared to Technology, with Tech being 3x as profitable    on avg.
* Office Supplies had a steady growth over the past 4 years while our Tech has barely grown
* Technology sales need to be better regulated, as large discounts applied to Machine Sales have dramatically impacted our overall profit more than once.


# Recommendation
* If our Technology Sales increased at even 50% the rate of our Office Supply Sales our profits would undoubtedly increase
* A Marketing Push on Superstore Technology should help increase revenue
Limit the discounts available for Technology to no more than 20%


# Next Steps 
* Continue observations of Technology and push the growth of Tech Sales
* There is potential to continue exploring the data to find what Technologies are more marketable to larger corporate offices
* Explore the reason behind high discount machines, maybe encountered a strong competitor, and needs to be analyzed in combination with the actual business and appropriately improve the business strategy.

