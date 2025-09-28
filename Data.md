# What is data

At its simplest form data is collection of facts. Almost anything can be data. This is why when we realized the power of analytics, we started to collect data from almost anything. Data can describe some value, some fact, some statistic, or it can even be any representation that can be interpreted in a meaningful way.

#### Some examples of data

##### Facts 

- A person's gender
- A person's name
- Whether or not a house is yellow

##### Measurements

- The land area of a city
- The width of a flower petal
- The energy usage of a refrigerator
- The budget of a flood control value

##### Unstructured representations

- Text from a book
- A photo of a mango fruit
- Documents from legal discovery
- Audio recordings of whale noise

##### Statistics

- Average life expectancy in a country
- An athletes Player Impact Estimate
- The median household income of a city

# Dataset

The dataset refers to a collection of data. Datasets can be structured in a specific. For example, tabular data is structured into a table. Relational data is structured into a relational database (a collection of interconnected tables), JSON data which is based on the JavaScript Object Notation, and many more. For this course we will usually structure datasets into tabular data. Below is an example of a dataset of store transactions structured into tabular data

| Sample Number | Age Bracket | Customer Type | Final Bill (in Pesos) | Number of Items | Is a store member? |
| ------------- | ----------- | ------------- | --------------------- | --------------- | ------------------ |
| 1             | Old         | 1             | 2399                  | 1               | Yes                |
| 2             | Young Adult | 1             | 4000                  | 1               | Yes                |
| 3             | Old         | 3             | 7999                  | 3               | Yes                |
| 4             | Teen        | 1             | 2399                  | 2               | No                 |
| 5             | Young Adult | 2             | 2200                  | 1               | No                 |
| 6             | Teen        | 2             | 500                   | 1               | No                 |

#### Parts of Tabular Data

- **Variables/Features/Columns** - Variables refer to the columns in tabular data. These are also know as features. The dataset above has 5 variables: `Age Bracket`, `Customer Type`, `Final Bill`, `Number of Items`, and `Is a store member`
- **Samples/Observations/Rows** - Samples refer to the rows in tabular data. Each row in tabular data represents one observation. From the example above one observation/sample represents one customer transaction. There are 6 samples in the dataset above
- **Values** - Values refer to the specific value of a specific sample and variable. For example, *2399* is the value of sample number 1's `Final Bill`, *Teen* is the value of sample number 4's Age Bracket
- **Index** -  Index is the special column that represents a unique identifier for observations. Each observation will have a unique index value. In the example above, `Sample Number` is the column that serves as the index. 

# Types of Data

#### Quantitative data

Quantitative data is also known as numerical data. This type of data represents some quantity or numerical value. It would make sense for you to perform arithmetic operations on this data, like adding, multiplying or finding averages. Examples of quantitative data would be age, income, measurements like length, duration and etc. Quantitative data can be either discrete or continuous

- **Discrete data** - Discrete data can only be specific countable values. For example, "number of children" can only have the values 0,1,2,3 ... etc. It is not possible (or it doesn't make sense) to have 0.53 as your number of children. This type of called discrete
- **Continuous data** - This is the opposite of discrete, continuous values can be any value from a range. For example, height can be any value from 0 to infinity. It can have values such as 145.3 cm, 23.5103 cm, 400 cm etc.

#### Qualitative data

Qualitative data or also known as categorical data, represents some form of quality or category. If your data is not meant to be performed arithmetic on then it is qualitative data. Examples of these are gender, color, and city. Qualitative data can also be either ordinal or nominal:

- **Ordinal data** - is qualitative data that can be arranged in some natural[^1] order. For example, consider an opinion that can have the following possible values: *Strongly Disagree, Disagree, Neutral, Agree, Disagree*. While it wouldn't make sense to add these values, it would make sense to order them according to level of agreement. Therefore opinion data like this Ordinal.
- **Nominal data** - nominal data on the other hand does not have any inherent order. For example, book titles, city names, gender are nominal data.

[^1]: You can almost find a way to order something. For example any text can be ordered alphabetically. While this is some kind of ordering, this usually not considered natural ordering. It just how you would arrange text in a dictionary.

#### Converting Qualitative Data to Quantitative Data

In some cases you find yourself finding a way to convert qualitative data into quantitative data. As discussed earlier qualitative doesn't convey some type of measurement or value. You also cannot perform arithmetic with these values. For cases like these you will need to find a way to convert qualitative data to quantitative data.

Lets look at an example:

| Row  | Opinion        |
| ---- | -------------- |
| 1    | Agree          |
| 2    | Strongly Agree |
| 3    | Agree          |
| 4    | Neutral        |
| 5    | Strongly Agree |

The table above shows respondent data. Specifically the responses on a particular `Opinion`. One of the things we can do to obtain some insight like this to reveal the overall opinion of the respondents. It would be of interest to us to see if the overall sentiment is towards agreement or disagreement. One thing we can do is to count how many respondents answered *Strongly Agree*, how many respondents respondents answered *Agree*, and so on. This will give a us a an overall picture of the all of the respondents opinion.

| Opinion           | Number of responses |
| ----------------- | ------------------- |
| Strongly Agree    | 2                   |
| Agree             | 2                   |
| Neutral           | 1                   |
| Disagree          | 0                   |
| Strongly Disagree | 0                   |

A simple count like the one above provides us with measurements and values. This convert the data into quantitative data. It also gives us insight on what the overall opinion is.

While this converts our opinion data into quantitative data, we do lose details. This conversion summarizes the data into an overall picture that represents the group, without accounting for individual responses. 

##### Encoding Ordinal Data

To preserve the details of the `Opinion` data, we can instead take advantage of the ordinal nature of `Opinion` and replace each response with a corresponding numerical value. Based on the order of how much a respondent agrees upon the opinion, you can convert *Strongly Agree* to 5, *Agree* to 4, *Neutral* to 3, *Disagree* to 2, *Strongly Disagree* to 1. We call this process **encoding**. With the encoding of `Opinion`  we convert the question "What is the response?"  into "How much do you agree with the opinion?". The encoding of `Opinion` will convert the data into a quantitative measurement. This measurement will also remain intuitive i.e. the higher the value, the more the respondent agrees with the opinion.

| Row  | Opinion (Quantitative) |
| ---- | ---------------------- |
| 1    | 4                      |
| 2    | 5                      |
| 3    | 4                      |
| 4    | 3                      |
| 5    | 5                      |

Now that we have these quantities we can use numerical operations. For example, we can calculate the overall opinion by finding the average (mean) of all of the `Opinion` values.

| Column                 | Average |
| ---------------------- | ------- |
| Opinion (Quantitative) | 4.2     |

The average value also remains meaningful. With an average `Opinion` of 4.2, a value close to 4, we gain the insight that the overall opinion is somewhere near *Agree*.

> Take note that the conversion of values from ordinal to quantitative is up to you. It will also be valid to encode `Opinion` into "How much do you disagree with the opinion?" With this you convert 
>
> - *Strongly Agree* to 1, 
> - *Agree* to 2, 
> - *Neutral* to 3, 
> - *Disagree* to 4, 
> - *Strongly Disagree* to 5. 
>
> You can even choose negative numbers for your encoding. For example you can convert 
>
> - *Strongly Agree* to 2, 
> - *Agree* to 1, 
> - *Neutral* to 0, 
> - *Disagree* to -1, 
> - *Strongly Disagree* to -2
>
> This gives you an intuitive encoding where the positive values convey agreement and negative values convey disagreement. Whatever encoding you choose, you just need to make sure that you communicate the exact conversion you used. This ensures you do not lose the original meaning of the data. 

##### Encoding Nominal Data (Dummy values)

This particular way of encoding is only possible for ordinal data. If you try this for data that doesn't have any inherent ordering, the resulting encoded data will lose their inherent meaning. For example if we have a qualitative value that describe movie genres, the possible values would be *Horror*, *Comedy*, *Action*, *Thriller*, *Drama*. You can encode these values as 1,2,3,4,5 respectively. But since genre doesn't have a natural ordering, the conversion is meaningless. 

Unlike `Opinion` from the example above, where the number 5 and 4 being close values to each other mean that *Strongly Agree* and *Agree* are similar opinions. On the other hand, 5 and 1 are values that are far from each other also mean that *Strongly Agree* and *Strongly Disagree* are very different opinions as well.

Despite this, there is a way to encode nominal data. We can encode nominal data through the use of dummy variables. Using the movie genre example:

| Movie Number | Genre  |
| ------------ | ------ |
| 1            | Horror |
| 2            | Comedy |
| 3            | Comedy |
| 4            | Action |
| 5            | Action |

For every possible value genre could have (let's say we only have 5 genres), we create a new column. You would name these columns based on the genre types. For this example we create 5 new columns called `Horror Genre`, `Comedy Genre`, `Action Genre`, `Thriller Genre`, and `Drama Genre`.

If the the genre of a movie is *Horror*, we write 0 for all other columns except for `Horror Genre`, we write 1 in the `Horror Genre` column instead. If the genre of a movie is *Comedy* then we write 0 for all columns other than `Comedy Genre` and so on.

| Movie Number | Genre  | Horror Genre | Comedy Genre | Action Genre | Thriller Genre | Drama Genre |
| ------------ | ------ | ------------ | ------------ | ------------ | -------------- | ----------- |
| 1            | Horror | 1            | 0            | 0            | 0              | 0           |
| 2            | Comedy | 0            | 1            | 0            | 0              | 0           |
| 3            | Comedy | 0            | 1            | 0            | 0              | 0           |
| 4            | Action | 0            | 0            | 1            | 0              | 0           |
| 5            | Action | 0            | 0            | 1            | 0              | 0           |

We call these new columns **dummy columns**/**dummy variables**. We also call the encoded values as **dummy values**. 

If you have nominal data that only has two possible values, you can omit one of the dummy columns. For example if you have a Customer type variable that can only be *Member* and *Non-member*, then you can have one dummy column

| Customer | Membership (1 = Member, 0 = Non-member) |
| -------- | --------------------------------------- |
| 1        | 1                                       |
| 2        | 0                                       |
| 3        | 0                                       |
| 4        | 1                                       |

While dummy columns are not as meaningful as encoded ordinal values, the conversion from qualitative to quantitative will help during the modeling phase of analytics.

> In some cases you might encounter qualitative data that appears to be quantitative. For example, if you look at the customer transactions dataset, `Customer Type` appears to be quantitative since the values are numeric. But it could also be improperly encoded nominal data. It always depends on context. 

##### Special ways of converting qualitative to quantitative

In special cases you can convert qualitative data to quantitative data by extracting some underlying measure from the variable. This can only work in specific cases where qualitative values have a direct quantitative conversion. 

Here are some examples:

- **Date** can converted into quantitative data by separating it into `Month`, `Date` and `Year`. Date can also be converted to `Days From`. Where you replace the date with the number of days from a specific date (see also Unix Time). With this, date values that are close to each other will have similar date 
- **Location** can be converted to `longitude` and `latitude`. With these, locations that are close to each will have similar `longitude` and `latitude` values. This conversion even allows you to easily calculate distances between two location values
- **Color** can be converted to RGB channel values. This way similar colors will have similar Red, Blue, Green values

#### Converting Quantitative Data to Qualitative Data

There are also circumstances where you might need to convert quantitative data to qualitative data. You might be interested in counting how many samples are there that have a high value for a specific feature. Simply counting frequencies for every value might not always lead to helpful insights. There might be too many possible values that you just end up with low frequencies for each possible value.

| House Number | House Area in sq. m |
| ------------ | ------------------- |
| 1            | 423.5               |
| 2            | 1900.31             |
| 3            | 230.2               |
| 4            | 400                 |
| 5            | 312.5               |
| 6            | 354.0               |
| 7            | 512                 |

To reduce the number of possible values you can instead create **bins**. A bin is a range your values can fall in. For example you can create 3 bins `from 0 to 399.99`, `from 400.00  to 799.99` and `from 800 to infinity`. You can assign descriptive names to each of the bins if possible:

- `from 0 to 399.99` as *Small*
-  `from 400.00 to 799.99` as *Medium*, 
-  `from 800 to infinity` as *Large*.

With these bins, if a value falls inside these ranges, instead of using the exact value, you replace the value with the bin name. For example:

| House Number | House Area |
| ------------ | ---------- |
| 1            | Medium     |
| 2            | Large      |
| 3            | Small      |
| 4            | Medium     |
| 5            | Small      |
| 6            | Small      |
| 7            | Medium     |

Using these bins you can now reveal counts in a meaningful way:

| House Area | Count |
| ---------- | ----- |
| Small      | 3     |
| Medium     | 3     |
| Large      | 1     |

> When deciding the appropriate ranges for your bins you need to make sure that all possible values are accounted for. This means that here must be an existing bin for every possible value your data could have. You also need to choose the appropriate range sizes. If you increase the number of bins, then your ranges can end up becoming too narrow. If you have too few bins then your ranges can end up too wide. It all depends on the context.