# Exploratory Data Analysis

Exploratory data analysis (EDA) is the the phase of analytics that comes after Data Cleaning/Processing. Once data is cleaned and processed it is now ready for exploration. During this phase your objective as a data analyst it to explore some interesting descriptive insights. These would usually involve calculating descriptive statistics, visualization, and multivariate analysis.

# Descriptive statistics

One of the easiest descriptive insights to uncover from any data would be descriptive statistics. As the name suggests, descriptive statistics are statistical measurements that describe the data. As statistical measurements, they are used to summarize the dataset into a single measurement. They are especially useful for quantitative features.

## Measures of Central Tendency

Measures of central tendency are descriptive statistics that represent the "center" of a collection of quantitative values. A collection of many values is not easy to picture, therefore we use measures of central tendency to summarize all of these values into their center.

**Mean** - you can think of the mean as the arithmetic center of a collection of qualitative values. Given a collection of values you can calculate the mean of said collection as the sum of all values, divided by the number of values.

| Pre-test Scores |
| --------------- |
| 95              |
| 89              |
| 78              |
| 89              |
| 77              |
| 84              |
| 91              |

For example the mean of these 7 values can be calculated as $\frac{95+89+78+89+77+84+91}{7} = 86.14$. 

**Median** - the median is the middle of all the values when the values are sorted from smallest to largest. For example, to calculate the median of the pre-test scores above, you must first sort the values:

| position | Pre-test Scores |
| -------- | --------------- |
| 1        | 77              |
| 2        | 78              |
| 3        | 84              |
| 4        | 89              |
| 5        | 89              |
| 6        | 91              |
| 7        | 95              |

Since there are 7 values, the middle can be found in position 4 which is $89$ (The middle value can be found as $\frac{n+1}{2}$ where $n$ is the number of values). If there are an even number of values this means that there is no clear middle. You can find the median as the mean of the two middle values. For example if we add one more pre-test score so that there are 8 instead of 7 values:

| Position | Pre-test Scores |
| -------- | --------------- |
| 1        | 77              |
| 2        | 78              |
| 3        | 84              |
| 4        | 85 (new value)  |
| 5        | 89              |
| 6        | 89              |
| 7        | 91              |
| 8        | 95              |

The median in this case is the mean of the values in position 4 and 5, which is calculated as $\frac{85+89}{2} = 87$.

**Mode** - the mode of a collection of values is simply the most frequent value. In the pre-test scores, since there are two instances of $89$ and one instance for the rest, the mode is $89$.

| Pre-test Scores |
| --------------- |
| 95              |
| 89              |
| 78              |
| 89              |
| 77              |
| 84              |
| 91              |

| Pre-test scores | Frequency |
| --------------- | --------- |
| 77              | 1         |
| 78              | 1         |
| 85              | 1         |
| 89              | 2         |
| 91              | 1         |
| 95              | 1         |

### When to use mean, median, and mode

All three measures of central tendency are used to represent the data. As an analyst you will choose which measure of central tendency is the most appropriate representative for the collection. The mean is the easiest to calculate out of the three, so it is usually used as the representative (this is why the mean is also colloquially known as the average). The mean is useful for symmetrically distributed data with no strong outliers. Symmetrical in this context means that the values in the dataset that are greater than the mean or lesser than the mean have the same characteristics (more about symmetry in the visualization section). The mean is also a good representative when you are describing quantities that are usually added up. For example, a feature like sales or profit are usually added up together to describe sales or profit over a period of time. The mean is a good representative for this case.

While the mean is a good for general cases, this measurement is sensitive to strong outliers. Outliers refer to individual values that don't conform within the overall distribution. Since all values contribute to the mean, this means that the outliers can easily influence the overall mean, makin mean an inappropriate representative. For example, consider the dataset below:

| Person_id | Income |
| --------- | ------ |
| 1         | 25000  |
| 2         | 32500  |
| 3         | 26600  |
| 4         | 145900 |
| 5         | 25500  |
| 6         | 31000  |
| Mean      | 47750  |

Person 4 in this example has an income that is uncharacteristically high when compared to the rest of the dataset. We can classify person 4's income as an outlier value. Because of this outlier, the mean value is unusually high as well. Most of the values are within the 25000 - 33000 range but the mean is found outside of this range. Therefore, the mean is not a good representation for this feature.

In this context, instead of using the mean, the median is a better representation of the feature.

| Person_id | Income |
| --------- | ------ |
| 1         | 25000  |
| 5         | 25500  |
| 3         | 26600  |
| 6         | 31000  |
| 2         | 32500  |
| 4         | 145900 |
| Median    | 28800  |

The mode on the other hand is useful when describing qualitative features. Mean and median cannot be used on qualitative features since their calculations involve arithmetic or ordering. You can still use mode for quantitative features but it is not appropriate for quantitative features with diverse or continuous values. If you really want to use the mode on these quantitative feature, you can convert the values into qualitative values using bins.

## Measures of Dispersion

Measures of dispersion describe how spread out a collection of values is. Consider these two sets of ages below:

| Age A | Age B |
| ----- | ----- |
| 24    | 21    |
| 24    | 17    |
| 26    | 21    |
| 25    | 27    |
| 26    | 25    |
| 24    | 12    |
| 25    | 27    |
| 26    | 26    |
| 23    | 22    |

You can see the values in Age A are closer to each other while values in Age B are more spread out.  There are descriptive measurements that can describe this characteristic: variance and standard deviation. To calculate the **variance**, you first find the mean of the values. And then, for each value in the column you calculate said value's square-difference with respect to the mean. A square difference is calculated as $(x - \overline{x})^2$, where $x$ is one value from the column and $\overline{x}$ is the mean of the values. For Age A, the square differences are:

| Age A, ($\overline{x} = 24.77$) | Square Difference |
| ------------------------------- | ----------------- |
| 24                              | 0.6               |
| 24                              | 0.6               |
| 26                              | 1.49              |
| 25                              | 0.05              |
| 26                              | 1.49              |
| 24                              | 0.6               |
| 25                              | 0.05              |
| 26                              | 1.49              |
| 23                              | 3.16              |

The variance is then calculated as the total square difference divided by ($n-1$) where $n$ is the number of values.: $\text{Var} = \frac{9.55}{9-1}=1.19$. 

Age B on the other hand has the following variance: $\text{Var} = \frac{202}{9-1}=25.25$

| Age B, ($\overline{x} = 22$) | Square Difference |
| ---------------------------- | ----------------- |
| 21                           | 1                 |
| 17                           | 25                |
| 21                           | 1                 |
| 27                           | 25                |
| 25                           | 9                 |
| 12                           | 100               |
| 27                           | 25                |
| 26                           | 16                |
| 22                           | 0                 |

As seen in these examples, the higher the variance the more spread out the dataset is.

Another useful measure of dispersion is the **standard deviation**. The standard deviation (stdev) is simply the square root of the variance. For Age A, the stdev is: $\text{stdev} = \sqrt{1.19} = 1.09$, while for age B the stdev is: $\text{stdev} = \sqrt{25.25}={5.02}$. Variance is often useful when you are combining multiple features or when you are performing statistical inference. But for the sake of descriptive statistics, standard deviation is the more intuitive measurement. Unlike variance, stdev has the same units as the data that you have. For example, since our example data expresses age in years, you can also express the standard deviation values as years:

| Data group | Standard Deviation |
| ---------- | ------------------ |
| Age A      | 1.09 years         |
| Age B      | 5.02 years         |



> **On sample variance and sample stdev vs population variance and population stdev.** What we calculated above are specifically the sample variance and sample stdev of the the dataset. When calculating measures of dispersion you can use either sample statistics or population statistics. You use sample statistics if the dataset that you have is merely a subset of the entire population. Population statistics are exclusively used for datasets which contain the entire population. In most cases the dataset that you have is merely a sample since the entire population has to take into account every possible observation.



# Exploratory Data Analysis with Visualization

You can also use visualization to perform exploratory data analysis. Creating visualizations allow you view the characteristics of your data in an intuitive sense. You can create visualizations that show the distribution characteristics of a feature, compare values from qualitative variables, or explore the relationships between variables.

## Histogram Chart

A histogram chart is a bar chart that shows the distribution of a quantitative feature. Each bar in a histogram chart represents a bin defined by a specific range (recall bins from converting quantitative features to qualitative). The height of each bar corresponds to the frequency of values that belong on said bin. With a histogram chart you can see which values frequently occur for a specific feature. Taller bars represent higher frequencies while shorter vars represent lower frequencies.

![HoursStudiedFrequencies](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/HoursStudiedFrequencies.png)

> A histogram chart of the feature Hours_Studied from the StudentPerformanceFactors datastet. This histogram shows that the most students study between 20 to 22 hours.

![RentedBikeCountFrequency](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/RentedBikeCountFrequency.png)



> A histogram chart of the feature Rented Bike Count from the SeoulBikeSharing dataset. This histogram shows that the most frequent rented bike counts fall in the lower ranges.

#### Distribution Characteristics

You can describe a group off values based on the characteristics  of the distribution chart it creates. You can describe the **skewness** and **kurtosis** of a distribution:

Skewness describes how asymmetrical the distribution is. A distribution where larger values are more frequent than smaller values is called negatively skewed. On the other hand, a distribution where smaller values are more frequent than larger values is called positively skewed. 

![skew](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/skew.png)

> *Photo by Danielle J. Navarro, David R. Foxcroft, and Sebastian Jentschke retrieved from https://lsj.readthedocs.io/en/latest/Ch04/Ch04_Descriptives_3/*

Skewness can be calculated as a statistic. A positive skew value means that the distribution is positively skewed while a negative skew value means that the distribution is negatively skewed.

Kurtosis describes the "tailedness" of a distribution with respect to the normal distribution. A platykurtic distribution has thin tails, meaning the distribution is less concentrated on the mode. A platykurtic distribution also appears flatter than the normal distribution. A leptokurtic distribution has fat tails, which means that the distribution is more concentrated towards the mode. We call a distribution that is neither leptokurtic not platykurtic as mesokurtic.

![kurt](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/kurt.png)

> *Photo by Danielle J. Navarro, David R. Foxcroft, and Sebastian Jentschke retrieved from https://lsj.readthedocs.io/en/latest/Ch04/Ch04_Descriptives_3/*

Kurtosis can also be calculated as a statistic. A very large kurtosis value means that the distribution is leptokurtic, a kurtosis values that is around 3 means that the distribution is mesokurtic, while a very small kurtosis value means that the distribution is platykurtic.



## Box Plots

A box plot shows a visual representation of the descriptive statistics of a feature. It can plot the mean value, the median value, the interquartile range, the maximum value and the minimum value.

![box-whisker-plot](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/boxplot.jpg) 

> *Photo by [Dcbmariano](https://commons.wikimedia.org/wiki/User:Dcbmariano), retrieved from https://en.wikipedia.org/wiki/File:Box_plot_description.jpg*

#### Parts of the box plot:

- The **min** is the smallest in the group.
- The **max** is the largest value in the group.

- The **lower quartile (Q1)** is the value ranked at the lower 25% of all the values. In the same way that the median is the middle of all the values, the lower quartile is in the middle of all the values between the minimum and median. A quarter of all the values are ranked below the lower quartile
- The **upper quartile (Q3)** is the value ranked at the upper 25% of all the values. The upper quartile is in the middle of all the values between the median and the maximum. A quarter of all the values are ranked above the upper quartile.

- The **interquartile range (IQR)** shows the dispersion of the upper and lower quartiles of the feature. In the box plot, the IQR is represented by the actual box. The length (width for horizontal box plots, and height for vertical box plots) of the box shows how dispersed the dataset is. If the box represented by the IQR is longer, then it means that the values in the dataset are more dispersed. If the box is shorter, then the values are close together.
- Box plots can also show **outliers**, values that do not conform to the

![BoxplotRentedBikeCount](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/BoxplotRentedBikeCount.png)

> Box plot showing the feature Rented Bike Count from the SeoulBikeSharing dataset.

The box plot can summarize both measures of central tendency and dispersion in a visual way. You can even use box plots to visually compare related groups of data. Using a box plot like this provides insights on which group of data is generally higher or lower by comparing their medians. It can also provide insights on which group of data is more dispersed by comparing their IQR lengths.

![BoxPlotTempVsSeason](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/BoxPlotTempVsSeason.png)

> Box plots of the feature Temperature, grouped according to the qualitative feature Season from the SeoulBikeSharing dataset.

# Multivariate Exploratory Data Analysis

During EDA you can also explore insights that show the relationships between features. 

#### Bivariate Analysis Between Two Qualitative Features

To show the relationship between two qualitative variables, you can use a contingency table. A contingency table shows frequencies of samples for each combination of categories. 

![Screenshot 2025-10-26 234639](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/Screenshot 2025-10-26 234639.png)

> Contingency table comparing the features Peer_Influence and Motivation_Level from the StudentPerformanceFactors dataset. The category combination with the highest frequency is medium motivation level and neutral peer influence. While the category combination with the lowest frequency is high motivation level and negative peer influence. 

#### Bivariate Analysis Between Two Quantitative Features

To show the relationship between two quantitative features, you can plot them in a scatter plot. One of the features will be plotted in the x-axis and the other feature will be plotted in the y-axis. Each sample in your dataset will be plotted in the scatter plot as a point. The scatter plot will reveal if there is some sort of relationship between these two quantitative features

![HoursStudiedVsExamScore](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/HoursStudiedVsExamScore.png)

> Scatter plot of Exam_Score vs Hours_Studied from the StudentPerformanceFactors dataset. There is a relationship between number of hours studied and exam score. The more hours dedicated to studying the higher the student's exam score.

![PreviousScoresVsExamScore](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/PreviousScoresVsExamScore.png)

> Scatter plot of Previous_scores and Exam_Score from the StudentPerformanceFactors dataset. There is weak/no relationship between these features. 

#### Bivariate Analysis Between Qualitative and Quantitative Features

When analyzing the relationship between a qualitative feature and a quantitative feature, you can use a scatter plot or a box plot. Both of these plots can visually show if there is any meaningful difference between the distribution of a qualitative feature across different categories.

![ScatterPlotTempVsSeason](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/ScatterPlotTempVsSeason.png)

> Scatter plot of Temperature (quantitative) vs Seasons (qualitative). Samples labelled Winter tend to have lower temperatures.

![BoxPlotTempVsSeason](https://raw.githubusercontent.com/HowDoIGitHelp/COMPED20/refs/heads/master/assets/BoxPlotTempVsSeason.png)

>  Box plots of the feature Temperature, grouped according to the qualitative feature Season from the SeoulBikeSharing dataset. Winter tends to have a lower temperatures compared to other seasons.

#### 
