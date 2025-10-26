# Data Analytics Life Cycle

Data analytics as whole is a process that goes through multiple stages. Different sources and textbooks will give you different answers but they all generally break down the Data analytics life cycle into the following stages.

1. **Data Collection/Acquisition** - the stage where you acquire the data. You can either collect the data yourself or acquire it from an external source
2. **Data Processing** - during this stage you will process the data to fit your analytical needs. This involves cleaning the data to improve its quality, transforming the data to create new features, or summarizing the data into the appropriate level of granularity.
3. **Exploratory Data Analysis** - during this stage you will perform some descriptive processing to reveal some descriptive insights, create descriptive visualization and more. When performing descriptive analytics you usually stop at this stage.
4. **Model Building** - during this stage you will build a model to fit your analytical needs. You can build models for prediction, clustering, classification and more
5. **Model Evaluation** - in this stage you will evaluate if the model you created from your data is usable, you can use multiple scoring techniques

# Data Collection/Acquisition

This is generally the first step of data analytics. Before you can start working on data, you need to have access to the data first. You can either collect the data yourself or acquire it from a source. Collecting the data yourself is ideal, it will lead into higher quality data. If you collect the data yourself, you become the primary source. As the primary the source you are able to control how the data is collected, what data collection techniques are observed, what sampling methods are used and so on. But unfortunately, data collection is time consuming and labor intensive. The more data you need, the more planning, preparation, and actual collection is needed. For this introductory course, data collection is a little bit out of scope and not ideal so we will not be able to do it. We will instead focus on data acquisition instead.

If you can't collect the data yourself, you will need to acquire it from some source. If your working in an organization as an analyst, the data collection will be done by some other expert and you can simply acquire the data from them as primary sources. You can also acquire the data through some publicly or privately available data repositories. In the case of this course we will settle for the former method. Here is a list of publicly available repositories you can use for free:

- [kaggle](https://www.kaggle.com/datasets) - data science community. It contains datasets shared by users across various domains
- [UCI machine learning repository](https://archive.ics.uci.edu/datasets) - a repository of datasets, mostly used for creating prediction and classification models.
- [open data philippines](https://data.gov.ph/index/public/dataset) - a curated collection of publicly available data from the Philippine government. 
- [data.gov](https://catalog.data.gov/dataset/) - collection of public datasets maintained by the US government
- [NCEI](https://www.ncei.noaa.gov/resources/weather-climate-links#ghcn) - a collection of US weather data maintained by the US government 
- [fivethirtyeight](https://data.fivethirtyeight.com/) - data used by ABC News' 538 website. Contains survey data in the domain of US Politics and more

# Quality Data

Not all datasets are created equally. While you  can collect or acquire as much as data as you can, its usability doesn't only depend on the amount of samples or the amount of features. You can collect 1 million samples of of data but you're bound to encounter issues if only 100 of those samples are good quality. 

Whether you collect the data yourself or if your acquire the data from another source, it is important to consider the quality of data. You can apply these considerations while collecting your data so that you end up with clean, accurate, and relevant data. You can also apply these considerations when assessing the quality of data acquired from another source. In those cases you cannot control how the data was collected, but you can still apply these principles to make sure that the dataset is usable for the purposes of analytics.

### Accuracy

Accurate data is good quality data. When we say the data is accurate it means that the data is **error-free**. The values of the features in the dataset must be an accurate representation of real world observations. Errors can come from multiple sources. Most commonly, errors can come from data collection issues. These data collection issues can come from human errors, human bias, sensor errors, data entry errors, and many more. 

A dataset collected through surveys like the Student Performance Factors dataset, can encounter human errors during data collection. These human errors can come in the form of erroneous survey responses or imperfect collection methods. Even if the data was not manually collected by humans, it can still encounter errors. For example, if you have a dataset that represents daily air quality samples collected from sensor data, some of those sensors can malfunction and report erroneous measurements.

Errors can also come from data management issues. This can come in the form of data corruption, data loss and many more. While these kinds of errors are much rarer it is still a consideration, especially if you as an analyst do not have control over how the data is  collected and managed.

In an ideal scenario you would want to have 100% accurate data. But unfortunately in a real world scenario, it is unavoidable that a dataset is error free. You just have to assume a part of the data is inaccurate. When assessing data quality in terms of accuracy, an analyst must consider if and how these errors can be overcome. For example, is the dataset large enough to overcome these inaccuracies? Is there a way to detect and process these errors?

### Completeness

The quality of data also depends on its completeness. Similar to errors, your data collection and management can cause issues that will lead to **missing data**. During data collection, some of your survey respondents may miss answering some questions. Some sensors can stop working and not report data at all. All of these issues can contribute to incomplete data.

Incomplete data can come in the form of missing values from a feature. Sometimes missing values can be marked with a specific value. For example a specific sample (row 3) in the Student Performance Factors Dataset is missing the a value in the *Parental Education*, column. But if you look closely, row 1 is missing values in the *Distance from School* feature and in the *Gender* feature.

| Learning Disability | Parental Education | Distance from School | Gender | Exam Score |
| ------------------- | ------------------ | -------------------- | ------ | ---------- |
| No                  | Postgraduate       | UNKNOWN              | ?      | 68         |
| No                  | College            | Moderate             | Male   | 70         |
| No                  |                    | Near                 | Female | 69         |
| No                  | High School        | Near                 | Female | 67         |
| No                  | College            | Moderate             | Male   | 62         |

Missing data can also come in the form of missing entire rows or columns. Or in more dire cases data can be incomplete because it is missing a specific representation. In the Coffee Sales dataset, you might be interested in the difference between card payment transactions and cash payment transactions. But unfortunately cash payment transactions are missing from the dataset. Either it was missing due to data management issues, or the data was not collected at all. This incompleteness makes it impossible to compare the two payment methods.

You can avoid missing data by adopting good practices in data collection and management. But as said earlier, a Data Analyst might have no control over these stages. At that point, what you will need to consider as an analyst is how to manage the missing data to overcome the incompleteness.

### Consistency

You want your dataset to be consistent. For example your features must have consistent formatting and consistent types. Below is an example of very inconsistent data.

| Money    | Is Member | Month | Weekday | Date         | Time       |
| -------- | --------- | ----- | ------- | ------------ | ---------- |
| $38.7    | True      | Mar   | Friday  | 2024-03-01   | 10:15:51   |
| 38.7     | No        | 3     | 5       | 1 March 2024 | 12:19:23   |
| 38.7 USD | False     | Mar   | 5       | 2024-03-01   | 12:20 noon |
| 28.90    | Yes       | Mar   | Friday  | 2024-03-01   | 13:46:33   |
| 38.7     | Yes       | March | 5       | March 1      | 13:48:15   |
| 33.8     | True      | Mar   | 5       | 3/1/2024     | 15:39:48   |
| $33.80   | Yes       | 3     | Fri     | 2024-03-01   | 16:19:03   |

While the data above can be considered accurate, complete, and timely, it's horribly inconsistent. Its date and time formatting is inconsistent within the same features. Some values come with units while some don't. It uses different ways to express positive and negative categorical values. Consistent data will stick with a uniform formatting, uniform unit expression, etc. 

In many cases you will end up working with inconsistent data. Data inconsistency can come from poor data collection practices or from combining multiple sources of data. While inconsistent data can still be used, you must fix the inconsistencies before your can properly apply your calculations or models, which creates way more work during the data processing stage.

### Uniqueness

As much as possible, you need to keep your datasets unique. Unique dataset refers to datasets that do not contain duplicate samples. While duplicate samples are easy to detect, you will need to properly eliminate these duplicates. Not only do they contribute to redundancy and space. They can also cause overrepresentation, which can throw off statistical measurements.

When considering uniqueness, you also need to take into account that there also cases where two samples can have the same values across all features. Depending on the context, it is possible for two samples to have the exact same measurements and observations based on chance. These cases are not considered duplicates. If you end up mistakenly treating these as duplicates and removing them, then you will risk underrepresentation. 

It is very easy to remove duplicates, what is important is how an analyst is able to properly avoid and identify them. To avoid and identify duplicates, proper data collection and indexing is important. Indexing allows you to uniquely identify samples. Indexing gives each sample an identifier that is not based on feature values. 

### Data Granularity

Data granularity refers to how specific and detailed the dataset. Consider the following datasets:

| Date       | SUM of money | number of transactions |
| ---------- | ------------ | ---------------------- |
| 2024-03-01 | 396.3        | 11                     |
| 2024-03-02 | 188.1        | 6                      |
| 2024-03-03 | 309.1        | 9                      |
| 2024-03-04 | 135.2        | 4                      |

| sales_index | hour_of_day | cash_type | money | coffee_name         | Date       |
| ----------- | ----------- | --------- | ----- | ------------------- | ---------- |
| 1           | 10          | card      | 38.7  | Latte               | 2024-03-01 |
| 2           | 12          | card      | 38.7  | Hot Chocolate       | 2024-03-01 |
| 3           | 12          | card      | 38.7  | Hot Chocolate       | 2024-03-01 |
| 4           | 13          | card      | 28.9  | Americano           | 2024-03-01 |
| 5           | 13          | card      | 38.7  | Latte               | 2024-03-01 |
| 6           | 15          | card      | 33.8  | Americano with Milk | 2024-03-01 |
| ...         | ...         | ...       | ...   | ...                 | ...        |

While datasets represents the same coffee sales, they have different levels of granularity. The first dataset represents the total daily sales of the coffee shop while the second represents each separate transaction. The first dataset is less granular, it is able to summarize the the data into a bigger picture but is loses the details of each transaction, such as coffee name and time of transaction. The second dataset is more granular, it keeps the details of each transaction but the characteristics of the bigger picture are less obvious. While you can process the second dataset into the first (using groupby, converting pivot table), it requires extra work.

When taking granularity into consideration, you must assess which level of granularity is appropriate for the context. You need to take into account what kind of insights you are looking for. But if you're not sure you can always opt for datasets with high granularity since you can always perform data processing to summarize the dataset properly.

### Timeliness and currency

Timeliness and currency is another consideration for assessing the quality of data. Historical data is important for descriptive and predictive insights. But, if your historical data is so outdated that it doesn't properly represent the real world, then it can instead become a source of outdated and inaccurate insights. Historical data will not be as effective if you are missing current and recent data that represents more relevant observations. For example, if your are trying to uncover the profile of your businesses' customers, you need to have  timely and current data. If your data sources are too outdated, then the descriptive insights might also be too outdated. Customer data from a decade ago might not be an accurate representation of your customers today.

Whether or not your dataset is timely and current depends on the context. If you are studying a quickly evolving domain then your analytics might require data as recent as possible. But if you are studying a domain where there are not a lot of changes or developments, then you might be able to get away with decades old data.

# Data Processing/Cleaning

In practice, it is very rare that the data you collect and acquire is in the best quality. It is even rarer for your data to be perfectly relevant for your needs. With the considerations of good quality data in mind, you need to dedicate an extra stage in analytics to convert not-so-good quality data into good quality data that is perfect for your analytics needs. This aforementioned stage is the data processing stage.

The data processing stage mainly depends on the current level of data quality and the context of your problem. But below are steps you can follow as a general framework for data processing. You can skip some of these steps or reorder them appropriately for your own data. 

These steps are ordered according to how easy it is to detect the data quality issue:

1. Handling incomplete data
2. Handling inconsistent data
3. Handling duplicates
4. Selecting the appropriate level of granularity

### Incomplete Data

The most obvious data quality issue you can detect is missing data. The first thing you need to do is to check if your dataset has missing data. And if it has missing data you need to check how much missing data is there. You also need to which parts of the data are missing.

- For each feature in your dataset, you can check what proportion of the samples are missing values for those features.
- For each row in the dataset, you can also check how many of it's values are missing

By doing these steps you can identify which columns or rows are largely incomplete. Once you find the distribution of missing values in your dataset, you can make a decision on how to handle missing data.

#### Removing vs Imputing

You have two choices when you encounter missing data. You can either remove entire rows or columns with missing values or you can replace those values with a representative value (imputing).

Removing data is the simplest solution. You can either remove entire rows or remove entire columns. You need to choose which removal has the least impact in your dataset. If you remove rows with missing data, you will lose some specific observations which may result in **underrepresentation**. For example if a huge proportion of your missing data is biased towards a specific categorical value, you will end up having less representative samples for said categorical value. In the table below, "Hot Chocolate" sales are missing their date values. If you do end up removing these rows then you will lose representatives of "Hot Chocolate" sales. Because of the  underrepresentation your dataset may not be an accurate representation of real world sales, leading you to erroneous insights.

| sales_index | hour_of_day | cash_type | money | coffee_name         | Date       |
| ----------- | ----------- | --------- | ----- | ------------------- | ---------- |
| 1           | 10          | card      | 38.7  | Latte               | 2024-03-01 |
| 2           | 12          | card      | 38.7  | Hot Chocolate       | ?          |
| 3           | 12          | card      | 38.7  | Hot Chocolate       | ?          |
| 4           | 13          | card      | 28.9  | Americano           | 2024-03-01 |
| 5           | 13          | card      | 38.7  | Latte               | 2024-03-01 |
| 6           | 15          | card      | 33.8  | Americano with Milk | 2024-03-01 |
| ...         | ...         | ...       | ...   | ...                 | ...        |

If your missing data is randomly distributed across different values (some missing values are latte sales, some missing values are americano sales, etc). Then it is safer to remove samples with missing values.

You can also remove entire columns of data. This is especially useful if a specific feature is missing data across a huge proportion of samples. For example, in the dataset below, the *Parental Education* feature is missing a lot values. If you choose to remove each row that has missing values in this column then you will lose a huge proportion of your data. What you can do instead is to remove the entire column itself. This way, you are able to keep all of your rows. But use this approach with caution since you will completely lose the insights provided by *Parental Education*. You should only delete columns if (a) a huge proportion of values within it are missing to the point that it affects the column itself is useless, (b) a huge proportion of rows will be unusable because of the missing information.

| Learning Disability | Parental Education | Distance from School | Gender | Exam Score |
| ------------------- | ------------------ | -------------------- | ------ | ---------- |
| No                  |                    | Near                 | Female | 68         |
| No                  | College            | Moderate             | Male   | 70         |
| No                  |                    | Near                 | Female | 69         |
| No                  | High School        | Near                 | Female | 67         |
| No                  |                    | Moderate             | Male   | 62         |

Imputing values is also another way of handling missing data. Imputation refers to the replacement of missing or erroneous values with representative values. The replacement values you choose depends on the feature and context. For example, *cash_type*, *money* and *date* are all missing some values. 

| sales_index | hour_of_day | cash_type | money | coffee_name         | Date       |
| ----------- | ----------- | --------- | ----- | ------------------- | ---------- |
| 1           | 10          | card      | 38.7  | Latte               | 2024-03-01 |
| 2           | 12          | card      | 38.7  | Hot Chocolate       | 2024-03-01 |
| 3           | 12          | card      | ?     | Hot Chocolate       | ?          |
| 4           | 13          | card      | 28.9  | Americano           | 2024-03-01 |
| 5           | 13          | ?         | 38.7  | Latte               | 2024-03-01 |
| 6           | 15          | card      | 33.8  | Americano with Milk | 2024-03-01 |
| ...         | ...         | ...       | ...   | ...                 | ...        |

A qualitative feature like *cash_type* can be replaced by the **mode** of the feature, while a quantitative feature like *money* can be replaced with the **mean/median** of the feature. We will talk about mean, median and mode some more in future discussions but for now these values are statistical measurements that summarize the feature in its entirety. Imputing missing values with these  will allow you to keep the row while providing a reasonable replacement for the missing values.

One thing to keep in mind with imputation, is that you are essentially estimating/making up replacement values. In some cases this will help you since you are able to keep as much as data as possible. The more information you can use, the better the insights are. But in other cases, imputed values can risk introducing bias in your insights. For example, if you impute the mode of a qualitative feature then you will end up overrepresenting the mode of said feature. If you impute the mean/median of a qualitative feature then you will end up changing the distribution of said feature.

In other cases you can impute missing values with the logical replacement. This specific imputation method can only work on some cases but it is the safest form of imputation. In the example dataset above, row 3 is missing the *Date* value. But if you know that the dataset is ordered according to transaction date, then you can safely assume that the actual date value for this row would be the same as the date values in the previous and succeeding rows. Therefore, you can safely replace the missing value with "2024-03-01".

When deciding between removal and imputation always consider the effect on your dataset. If you have a lot of good data and you know that you are not gonna risk underrepresenting any part of your dataset, then the best option might be to completely remove the offending rows or columns. If you don't have a lot of data to work with and you want to keep as much information as possible, then imputation might be the best option for you. If you're not sure, you can always do both approaches and compare which approach produces the most relevant insights for your problem.

### Redundant Data

If you have a good index for your dataset, then you can easily detect redundant rows. You can simply sort your dataset by index and check if any of the indices repeat. After finding these redundant rows, you can check if they are indeed redundant by comparing the values of each feature. If they are all the same then you can safely remove all the redundant rows, making sure to keep exactly one copy of the sample in your dataset. In the example below you can remove the redundant *Student_Number*=5.

| Student_Number | Hours_Studied | Attendance | Parental_Involvement | Access_to_Resources | Extracurricular_Activities |
| -------------- | ------------- | ---------- | -------------------- | ------------------- | -------------------------- |
| 1              | 23            | 84         | Low                  | High                | No                         |
| 2              | 19            | 64         | Low                  | Medium              | No                         |
| 3              | 24            | 98         | Medium               | Medium              | Yes                        |
| 4              | 29            | 89         | Low                  | Medium              | Yes                        |
| 5              | 19            | 92         | Medium               | Medium              | Yes                        |
| 5              | 19            | 92         | Medium               | Medium              | Yes                        |
| 6              | 19            | 88         | Medium               | Medium              | Yes                        |
| 7              | 29            | 84         | Medium               | Low                 | Yes                        |

If you do not have an index for your dataset, you need to be more discerning with what you delete. In the example below, you can check that the row 4 and 5 have the same values across all feature. You can suspect that this is duplicated data. You can verify this based on the *Date* and *Time* feature. It doesn't really make sense for two of the exact same sales transactions to happen at the exact same time down to the last second. Based on this you can decide to delete the redundant rows.

| coffee_name         | Time_of_Day | Weekday | Month_name | Weekdaysort | Monthsort | Date       | Time     |
| ------------------- | ----------- | ------- | ---------- | ----------- | --------- | ---------- | -------- |
| Latte               | Morning     | Fri     | Mar        | 5           | 3         | 2024-03-01 | 10:15:51 |
| Hot Chocolate       | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 12:19:23 |
| Hot Chocolate       | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 12:20:18 |
| Americano           | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 13:46:33 |
| Americano           | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 13:46:33 |
| Latte               | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 13:48:15 |
| Americano with Milk | Afternoon   | Fri     | Mar        | 5           | 3         | 2024-03-01 | 15:39:48 |

When your dataset doesn't have a lot of features while having a lot samples, it can easily have two of the exact same rows just by coincidence. You need to understand the context on how the data was collected to consider whether or not you are looking at duplicate samples.

### Inconsistent Data

Inconsistent data can be the most time consuming data quality issue to fix. This is because there might be no automatic ways to uniformly format the data. Here are some of the things you need to consider to keep your data consistent:

**All date values should be uniform formatting.** Within the same features it is important to use the same date format. And if you have multiple features that are date values, it is also good practice to have consistent formatting for them all. This will help you easily combine different date features together.

**All quantitative values must be in the same units.** For example if one value is using kg as the unit for weight, while another value is using lb as the unit, you need to set a consistent unit across all of them. When you have values related to money try to convert them all into a consistent currency. Once you set a consistent unit or currency, you can remove unit information in the values and transfer them to the column headers:

| hour_of_day | cash_type | money (in USD) | coffee_name         |
| ----------- | --------- | -------------- | ------------------- |
| 10          | card      | 38.7           | Latte               |
| 12          | card      | 38.7           | Hot Chocolate       |
| 12          | card      | 38.7           | Hot Chocolate       |
| 13          | card      | 28.9           | Americano           |
| 13          | card      | 38.7           | Latte               |
| 15          | card      | 33.8           | Americano with Milk |

**Use consistent qualitative values.** For example if you have an *Is Member* feature that denotes if the specific customer in the transaction is a member or not, only use two possible values for the feature.

| Is Member (inconsistent) | ---> | Is Member (consistent) |
| ------------------------ | :--: | ---------------------- |
| True                     |      | Yes                    |
| No                       |      | No                     |
| False                    |      | No                     |
| Yes                      |      | Yes                    |
| Yes                      |      | Yes                    |
| True                     |      | Yes                    |
| Yes                      |      | Yes                    |

### Too Granular Data

If you are trying to uncover insights on the daily sales of the Coffee Sales dataset then you need to find a way to summarize the all the transaction on a specific date. There are a lot of tools you can use for this. Most spreadsheet software has a pivot table transformation, some tools can perform groupby information.

| sales_index | hour_of_day | cash_type | money | coffee_name         | Date       |
| ----------- | ----------- | --------- | ----- | ------------------- | ---------- |
| 1           | 10          | card      | 38.7  | Latte               | 2024-03-01 |
| 2           | 12          | card      | 38.7  | Hot Chocolate       | 2024-03-01 |
| 3           | 12          | card      | 38.7  | Hot Chocolate       | 2024-03-01 |
| 4           | 13          | card      | 28.9  | Americano           | 2024-03-01 |
| 5           | 13          | card      | 38.7  | Latte               | 2024-03-01 |
| 6           | 15          | card      | 33.8  | Americano with Milk | 2024-03-01 |
| ...         | ...         | ...       | ...   | ...                 | ...        |

When summarizing data, you also need to choose the correct aggregation method. For quantitative features you can find the sum of all transactions. You can also use descriptive statistics like mean and median. Qualitative features are harder to summarize, you can either find the mode, or just select one value.

| Date       | SUM of money | number of transactions |
| ---------- | ------------ | ---------------------- |
| 2024-03-01 | 396.3        | 11                     |
| 2024-03-02 | 188.1        | 6                      |
| 2024-03-03 | 309.1        | 9                      |
| 2024-03-04 | 135.2        | 4                      |