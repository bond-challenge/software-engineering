# Bond Challenge

## Coding Question

Write an interface for a data structure that can provide the moving average of the last N elements added, add elements to the structure and get access to the elements. Provide an efficient implementation of the interface for the data structure.

For your submission, please submit a PR to the `main` branch of this repository. 

### Minimum Requirements

1. Provide a separate interface (i.e. `interface`/`trait`) with documentation for the data structure
2. Provide an implementation for the interface
3. Provide any additional explanation about the interface and implementation in a README file.

###
### Solution is in the index.js file ###
###
An interface is a programming structure/syntax that allows the computer to enforce certain properties on an object (class).
ref. https://www.cs.utah.edu/~germain/PPS/Topics/interfaces.html

Clone the file in Visual Studio Code with node installed. 
Run npm install and then run the command:
> node index.js

## You will see following output:
This is based on random no. generated between 0-10. It shows the moving average of last 3 elements 
i.e. (2+4+2)/3 = 2.66
[
  3, 1, 1, 7, 9,
  9, 5, 2, 4, 2
]
2.6666666666666665


## Design Question

A Pizza Restaurant chain “Pizza House” has more than 2000 stores across the country. Each store manages its own inventory of raw materials. Each store prepares pizzas, side dishes, etc. and sells them along with ready to eat products such as cookies, drinks, etc. The sale can happen by Point of Sale (POS) or Online. The online transactions would be flowing in real time whereas the transactions made by POS can be synced every 15 minutes in batches. They offer pick-up and deliveries by 3rd party providers. 

At the head office of the restaurant chain, management is concerned with the logistics of ordering, stocking and selling products while maximizing profits as well as understanding their marketing & communications. Several promotional schemes such as temporary price reductions, ads in newspapers, displays etc., also keep rising. Considering the huge data volumes (hundreds of GB per month) and the variety of the data they have; management wants the architecture to be robust enough to handle the varying data loads. 

Design a cloud data platform to process and deliver insights based on the above. Please provide a high level solution design for the architecture. Feel free to choose any cloud provider you want.

### Requirements

1. Handle large write volume: Billions of write events per day.
2. Handle large read/query volume: Millions of merchants wish to gain insight into their business. Read/Query patterns are time-series related metrics.
3. Provide metrics to customers with at most one hour delay.
4. Run with minimum downtime.
5. Have the ability to reprocess historical data in case of bugs in the processing logic.

###
### The cloud architecture design of the “Pizza House” web application:
###
Refer to Pizza House cloud architecture image in the repository.

The web application can have different role-based access control users in the system. The main focus areas of the system are ordering, stocking and selling products, marketing and communication. Each focus areas can be under a specific role in the system and can has permissions and access policies to access data and drive insights. 

At the very high level, the web app can consider building a dynamic application using NodeJS as backend framework that can have all the endpoints of data, AngularJS as frontend framework that can display a friendly responsive user interface for good user experience. The app can use different libraries such as high charts or D3.js to create visualizations and metrics or it can embed a dashboards or tiles from PowerBI using PowerBI APIs. The application can be hosted on an Azure web app service. 

The data from the application can be stored on a NoSQL (Azure Cosmos Database) which can help to drive Artificial Intelligence solutions using MLFlow and Databricks.  

When considering high volume of data, the ETL/LTE can be done using Azure Data Factory. Creating various pipelines, triggers in a timely manner to sync data. For loading transformed data or unstructured data we could also use a SQL database or Delta Lake, respectfully. 

The code versions can be managed using Azure DevOps so differentiate the developers code on the main production branch, staging and development branch. 

Thank you for your time and consideration.

Regards,
Alvira Narshidani
email: alviranarshidani7@gmail.com
