## Design Question

Given the scenario we’ll implement the following architecture in Azure cloud infrastructure:

## Architecture diagram:

![alt text](https://github.com/vvsivaprasadreddy/software-engineering/blob/siva-vundela/DesignChallange/images/architecture.jpg?raw=true)

## <u>Data Loading</u>

The above architecture proviceds real-time data warehousing of large volumns of data using proprietary Azure technologies for CDC (change data capture), data replication, ETL (extract-transform-load) and the RDBMS (relational database management software) components.

### Streaming Data:

To generate a streams of data we will use a utility to generate json data using client API's. We’ll need to use Kafka to consume the stream and route it based on the contents of the file to Azure Event hub. The raw streaming data will be stored in Azure blob storage

### SQL Datatabase:

The POS transactions are stored in Client Databases and can be synced to Azure SQL DB using Azure data facory

## <u>Data Transformation</u>

We can use Databricks to transform the raw data.One of the advantages of Databricks is that you can read from many different data sources and data formats with relative ease, perform joins and transformations, and then write the output to a multitude of targets

## <u>Analytics</u>

The transformared data that is stored in Azure Data Ware house can be utlized to buid analytics dashboards using Power BI or Tableau

## <u>Handling Failure Cases</u>
If any stage is failed in the above pipeline, we can rerun the stage using Azure Data Factory, It allows us to rerun activities inside the pipelines. We can rerun the entire pipeline or choose to rerun downstream from a particular activity inside the data factory pipelines.