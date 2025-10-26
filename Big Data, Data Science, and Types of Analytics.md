# Big Data

Big data refers to datasets or combination of datasets that are extremely large in volume, complex in nature, and sometimes growing. Big data are those datasets that are too large or too complex for conventional data management tools. Because of the volume and and/or complexity of these datasets, it becomes difficult to store, process, or perform any analytics on said datasets.

Big data are often too large to store in local devices. For example the Common Crawl dataset, which is a database of web crawl data from 25 billion web pages from the internet is as large as 250 TB [^1]. Or the 1000 genome dataset, a dataset of 1000 complete human genome data which is 260 TB in total [^2]. It would be too much to download these datasets to your own devices, so it is usually processed in the cloud. 

[^1]: https://registry.opendata.aws/commoncrawl/
[^2]: https://www.internationalgenome.org/data/

Not only are these too large for storage, conventional data management software simply cannot handle their volume. Google Sheets for example has a hard limit of 10 million cells, while MS Excel has a hard limit of around 1 million rows. Big Data simply cannot fit in these tools.

Big data is often complex. This means that the datasets may come from different sources. It may come in different formats like images, text, map data, etc. The CelebFaces dataset for example is a dataset composed of 200,000 celebrity images along with tables of labels [^3]. The Yahoo News dataset  on the other hand is a dateset composed of text data from Yahoo News Articles with accompanying labels [^4]. These datasets are not structured in tabular form, which means if you want to process it using tabular analytics you will end up with large tables with thousands of columns.

[^3]: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset
[^4]: https://github.com/TobeyYang/Yahoo-News-Dataset

>  Extra Reading:
>
> - [What is Big Data?](https://cloud.google.com/learn/what-is-big-data#how-are-data-driven-businesses-performing) from Google Cloud 

# Data Science and Data Analytics

There is usually some confusion between these two domains. Mainly because both Data Science and Data Analytics use similar skillsets, techniques, and tools to solve similar problems. But you can think about it this way: Data Science is a more advanced and broad form of Data Analytics.

While both handle datasets, Data Science may involve complex, unstructured data, and big data. These datasets require more tools and skills to convert them into tabular data. On the other hand Data Analytics handle structured tabular data that is ready for use.

Data Science also involve the use of more advanced tools to for more advanced data processing. These tools would include programming languages like Python, R, SQL. Advanced data processing software frameworks like hadoop or spark. A Data Scientist would be expected to know how to use these tools. Data Analytics may sometimes use the same tools, but it is usually not required.

Data Science doesn't only includes data analytics, its scope includes, data engineering, machine learning and more. Data analytics is a simpler and smaller subset that involves, data cleaning, data visualization, and exploratory data analysis.

The goal of Data Science is more complex and encompassing. It involves revealing hidden patterns in the data by creating models for prediction, classification and clustering, creating models for recommendation, natural language processing and more. While Data analytics is often limited to uncovering descriptive, diagnostic, prescriptive and predictive insights based on the data.

Here is a breakdown of their differences:

|          | Data Science                                                 | Data Analytics                                               |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Datasets | Unstructured Data, Complex Data, Big Data                    | Tabular Data                                                 |
| Tools    | Programming Languages, Advanced Data management Frameworks   | Spreadsheet software, Visualization Software                 |
| Scope    | Data Engineering, Data Mining, Data Analytics, Machine Learning | Data Cleaning, Data Visualization, Exploratory Data Analysis |
| Goals    | Find hidden pattern by building models                       | Reveal insights from data                                    |

# Types of Analytics

Data analytics can be divided into 4 types, based on the goals or the types of insights you are looking for. Each type of analytics are built on top of each other. For example, descriptive insights will help form diagnostic, predictive, and prescriptive insights. Diagnostic insights will help form predictive and prescriptive insights. Predictive insights will help form prescriptive insights.

## Descriptive Analytics

Descriptive analytics answers the question *What is happening?*. From the given dataset you might be interested in **describing** important insights. For example, in the coffee sales dataset, you might be interested in describing which month experienced the highest daily sales averages.

![Daily Sales Throughout The year](https://docs.google.com/spreadsheets/d/e/2PACX-1vTraMVohtFzftmHl1Oc369U1HCqUCPvCkVe-bLkG4wyE-eqFsLCLl2Q_hLd0zsjhomtCteX_b2eV1_B/pubchart?oid=1530500193&format=image)

## Diagnostic Analytics

Diagnostic Analytics answers the question, *Why did this happen?*. From a given dataset you might be interested in **diagnosing** why such insight is found. With more context, you can infer the underlying reasons for descriptive insights. For example, in the coffee sales dataset, you might be interested in understanding *why coffee sales are high during the month of February*.

Diagnostic analytics involves studying causation. Without extensive experimentation and testing, you can only rely on domain knowledge to infer causes. In the coffee sales example, let's say you want to verify that the cause of the February spikes in sales is due to holidays. To support this insight you need to have data that can compare holiday transactions and non-holiday transactions. With this comparative data you can perform statistical tests or correlation analysis.

## Predictive Analytics

Diagnostic Analytics answers the question, *What might happen in the future?* From a given dataset you might be interested in **predicting** the future based on historical data. From historical data you can reveal patterns that help form insights about the future. In the coffee sales example you have data on the current sales of the year. You can look into sales data from previous years to check if sales are consistently highest around February. This establishes a pattern that can predict that February of the next year will experience high sales.

## Prescriptive Analytics

Prescriptive Analytics answers the question, *What should we do next?* Building from the descriptive, diagnostic, and predictive insights, you can form prescriptive insights. This leads you to recommendations on what to do next to achieve a specific outcome. In the coffee sales problem, if the objective is to maximize sales, you can form insights that recommend increasing the staffing and marketing during peak months. 

By breaking down analytics into these four types, you can formulate a plan to reach a data driven decision. Starting from descriptive analytics which starts as your baseline, you can build on top of your descriptive insights with the support of extra data and tools. From descriptive insights to diagnostic, predictive, and prescriptive insights.

|                         | Descriptive Analytics                 | Diagnostic Analytics                      | Predictive Analytics     | Prescriptive Analytics                                       |
| ----------------------- | ------------------------------------- | ----------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| Insights                | What is happening?                    | Why did this happen?                      | What is going to happen? | What should we do?                                           |
| Data Needed             | Data of interest                      | Comparative Data                          | Historical Data          | Diverse data from multiple sources, including comparative and historical data |
| Tools and Skills Needed | Descriptive statistics, Visualization | Correlation Analysis, Statistical Testing | Regression Analysis      | Simulation Tools, Optimization Tools                         |