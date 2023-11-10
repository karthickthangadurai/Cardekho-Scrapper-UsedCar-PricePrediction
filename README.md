# Cardekho-Scraper & UsedCar-PricePrediction
### **Developing a car price prediction model, combining data acquisition, preparation, analysis, modeling, and deployment**

Building a car price prediction model involves scraping data from reliable sources like CarDekho, cleaning and enhancing the dataset, exploring patterns, selecting a suitable machine learning algorithm, training and evaluating the model, tuning hyperparameters, deploying it into applications, and continuously monitoring and maintaining its performance for accuracy and reliability over time.

## About CarDekho

![cardekho](https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/62803edb-a79a-4afe-86c1-eb5063592e56)

CarDekho is a prominent online platform in the Indian automotive industry, offering a comprehensive range of services. Users can access detailed information, specifications, and reviews for various car models, aiding in informed decision-making. The platform features listings for both new and used cars, providing a marketplace for buying and selling vehicles. CarDekho also offers comparison tools, enabling users to assess different models based on specific criteria. Additionally, the website may provide automotive news and updates, covering new launches, reviews, and industry trends.

## Steps Involved To Predict

1. Collect the Car links
2. Data Collection from Car links
3. Data Transformation into Structured data
4. Data Cleansing
5. Exploratory Data Analysis
6. Feature Engineering
7. Model Building
8. Evaluation and Validation
9. Deployment

# How we are going to predict the car price ?

Collect data of Car Details, Car Overview, Car Features, Car Specifications for each and every car. As we know that Kilo meter driven can be the important independent variable to predict the price. In the same manner year of manufacturing, features and specifications makes changes in the car price. 

## 1. Collect the Car Links
## CarDekho Scraper

There are multiple filters available to search the used cars like Cities, Fuel Type, Brand. I am going to filter and collect data of the used cars by Cities. Click any of the cities.

<img width="789" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/20ca511a-2425-410c-a33c-a16f632009e4">

To intialize CarDekho Scraper below models has been utilized 

- selenium - For automating the pages
* BeautifulSoup - To get the html parser of the partcular page
+ pandas - To make the data into structured one


