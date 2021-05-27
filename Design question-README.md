
This architecture shows an end-to-end processing pipeline for bith streaming and Batch data. This is useful in use case provided in design question where an Pizza Store organization wants to ingest data from online application transactions and POS or custom applications as data sources and analyze the data in near real time. In the example below, the pipeline ingests data from two sources, correlates records in the streams and batch data, and performs a join on the related data streams and made available for consumption layer to enable data visualization and analysis of metrics by business users. The results are stored for further analysis that go beyond the capabilities of Stream Analytics and batch processing enables Data Science experiments to be performed on the data using Azure Databricks which stored on cosmos db. It is designed to simulate pizza store use case provided in design question.

Data Source
In this architecture, there is one data source that generate data streams in real time. The stream contains online sales and  customer information. This is generated in real time by an application within the pizza store.
seond data source is the POS data or from external relational databases which is processed via batch jobs for every 15 mins using schediling. In addition, there can be additional data stores that are used to collect data from.

Ingestion and Data Storage
data source sends a stream of data to an associated Azure Event Hub. Azure Event Hubs is a Big Data streaming platform and event ingestion service, capable of receiving and processing millions of events per second. It is then connected to Azure Databricks, which outputs its analysed data into an Azure Cosmos DB using the Cassandra API. The Cassandra API is used because it supports time series data modeling which can be used in the analysis of online application data.

Azure Blob Storage (Data Lake Storage Gen II could be used instead) is again used as an intermediate staging area for both the OLTP and external data. Azure Synapse Analytics is used as the final destination for the data storage.

Azure Data Factory is a managed service that orchestrates and automates data movement and data transformation. In this architecture, for batch processing, it coordinates the various stages of the ELT process using pipelines to cleanse and load the data. in this case, loading and transforming data into Azure Synapse Analytics. This architecture defines a master pipeline that runs a sequence of child pipelines. Each child pipeline loads data into one or more data warehouse tables incrementally.

To perform an incremental load, we need a way to identify which data has changed. The most common approach is to use a high water mark value, which means tracking the latest value of some column in the source table, either a datetime column or a unique integer column.

Analysis and Visualization
The analysis of the streaming data is performed with Azure Databricks, which is is an Apache Spark-based analytics platform optimized for the Microsoft Azure cloud services platform. Databricks is used to correlate online application data, and also to enrich the correlated data with processing layer.

In this architecture, Analysis Services reads data from the data warehouse to process the semantic model, and efficiently serves dashboard queries. It also supports elastic concurrency, by scaling out replicas for faster query processing. Power BI is a suite of business analytics tools to analyze data for business insights. In this architecture, it queries the semantic model stored in Analysis Services.
Custom data analysis and visualization tools can be used to present the data to the end users. 

Additional technologies
Application log data collected by Azure Monitor is stored in a Log Analytics workspace. Log Analytics queries can be used to analyze and visualize metrics and inspect log messages to identify issues within the application.



