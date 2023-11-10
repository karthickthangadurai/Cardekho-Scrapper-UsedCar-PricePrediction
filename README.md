# :oncoming_automobile::oncoming_police_car: Cardekho-Scraper & UsedCar-PricePrediction :oncoming_taxi::weight_lifting_man:
### **Developing a car price prediction model, combining data acquisition, preparation, analysis, modeling, and deployment**

Building a car price prediction model involves scraping data from reliable sources like CarDekho, cleaning and enhancing the dataset, exploring patterns, selecting a suitable machine learning algorithm, training and evaluating the model, tuning hyperparameters, deploying it into applications, and continuously monitoring and maintaining its performance for accuracy and reliability over time.

### About CarDekho

![cardekho](https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/62803edb-a79a-4afe-86c1-eb5063592e56)

CarDekho is a prominent online platform in the Indian automotive industry, offering a comprehensive range of services. Users can access detailed information, specifications, and reviews for various car models, aiding in informed decision-making. The platform features listings for both new and used cars, providing a marketplace for buying and selling vehicles. CarDekho also offers comparison tools, enabling users to assess different models based on specific criteria. Additionally, the website may provide automotive news and updates, covering new launches, reviews, and industry trends.

### Steps Involved To Predict

1. Collect the Car links
2. Data Collection from Car links
3. Data Transformation into Structured data
4. Data Cleansing
5. Exploratory Data Analysis
6. Feature Engineering
7. Model Building
8. Evaluation and Validation
9. Deployment

### How we are going to predict the car price ?

Collect data of Car Details, Car Overview, Car Features, Car Specifications for each and every car. As we know that Kilo meter driven can be the important independent variable to predict the price. In the same manner year of manufacturing, features and specifications makes changes in the car price. 

## 1. Collect the Car Links

### CarDekho Scraper

There are multiple filters available to see used cars based on Cities, Fuel Type, Brand. I am going to filter and collect data of the used cars by Cities. Click any of the cities.

<img width="789" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/20ca511a-2425-410c-a33c-a16f632009e4">

To intialize CarDekho Scraper below models has been utilized 

- selenium - For automating the pages
* BeautifulSoup - To get the html parser of the partcular page
+ pandas - To make the data into structured one

### Links Page

We will able to collect max 1500 links per cities. Since only 1580 links will be present in one page. Code was written in such a way that it scroll down the entire page and collects atleast 1500 links if more than 1500 present in the particular page

<img width="849" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/4a9f696c-c8b8-44e1-aaf4-c508a5bc76e3">



I wrote a script to collect the links. You can find it in CarDekhoScrapperFile.ipynb file.

<img width="776" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/591ea3b3-5335-4906-8aec-4ffedd5dae96">

## 2. Data Collection From Car Links

After the links are scraped now the time is to navigate all the cars page and collect the data. If we use selenium there are multiple clicks has to be done to for features, specifications. It consumes a lot of time so here I have used combination of Selenium and BeautifulSoup to collect the data. 

Once we get into the car page we can send html.parser and collect the whole page html doc. From this we can get all the data. It takes almost 2hrs of time to complete 1200 links.

### 2.1 Car Details Data

<img width="881" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/abb9dfbf-0fd4-4ba0-8e10-816de2a986f5">

Collected Data

<img width="791" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/0c518bbf-0287-4ece-973a-36f1b7911e3a">

### 2.2 Car Overview Data

<img width="545" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/d59c86d1-e816-4920-aeab-0f4941d24eb4">

Collected Data 

<img width="791" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/29f1b893-c4f1-4fe1-a79f-057f856747cb">

### 2.3 Car Features Data

<img width="455" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/e206ea74-0d33-426d-bdf1-af8ea1913c03">

Collected Data

<img width="793" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/7ae9d5e8-4d9d-49c5-8089-2e3e2b87b104">


### 2.4 Car Specs Data

<img width="512" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/6f03ce36-38a6-4c47-9a44-84902b2ca734">

Collected Data

<img width="792" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/ef0b36e3-2b15-462d-a43e-8330b5716407">



