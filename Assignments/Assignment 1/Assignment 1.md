# Assignment 1

You are a Data Analyst working for a school. You are tasked in improving  the performance of students based on their scores on a Standardized  Assessment. You some data available for each students scores along with  some data related to their background. Each row in this tabular data  represents one student.



| **Column**                     | **Description**                                          |
| ------------------------------ | -------------------------------------------------------- |
| **Hours_Studied**              | Number of hours spent studying per week.                 |
| **Attendance**                 | Percentage of classes attended.                          |
| **Parental_Involvement**       | Level of parental involvement in the student's education |
| **Access_to_Resources**        | Availability of educational resources                    |
| **Extracurricular_Activities** | Participation in extracurricular activities              |
| **Sleep_Hours**                | Average number of hours of sleep per night.              |
| **Previous_Scores**            | Scores from previous exams.                              |
| **Motivation_Level**           | Student's level of motivation                            |
| **Internet_Access**            | Availability of internet access                          |
| **Tutoring_Sessions**          | Number of tutoring sessions attended per month.          |
| **Family_Income**              | Family income level                                      |
| **Teacher_Quality**            | Quality of the teachers                                  |
| **School_Type**                | Type of school attended                                  |
| **Peer_Influence**             | Influence of peers on academic performance               |
| **Physical_Activity**          | Average number of hours of physical activity per week.   |
| **Learning_Disabilities**      | Presence of learning disabilities                        |
| **Parental_Education_Level**   | Highest education level of parents                       |
| **Distance_from_Home**         | Distance from home to school                             |
| **Gender**                     | Gender of the student                                    |
| **Exam_Score**                 | Standardized Assessment Score.                           |



You did not collect this  dataset. So your first objective is to perform some preliminary  exploration. You want to figure out how many features are in the  dataset, how many samples are in the dataset, which features are  quantitative, which features are qualitative and to convert some  datasets fro qualitative to quantitative and some features from  quantitative to qualitative.



**Tasks**

1. Download the .csv file included. Import this dataset into a Google Sheet. Rename this Google Sheet into **StudentPerformanceFactorsDataset.**
2. Add a indexes to the dataset. This index should be under the column called **Student_Id** and said column must be the leftmost column in the dataset. The created index is valid as long each sample has a unique index.
3. Format the dataset into a Table. The table must be named **Dataset**.
4. Create a new sheet to store dataset information (don't create a separate  google sheet file for this new sheet). Name this new sheet **information.** 
5. Count the number of features and samples (refer to the Workshop video as a  guide). Add this information in the information sheet you just created.
6. Identify which features are qualitative. Add a list of all qualitative features  in the information sheet. Count the number of unique values for each  qualitative feature.
7. Identify which features are quantitative. Add a list of all quantitative  features in the information sheet. Find the minimum and maximum value  for each quantitative feature.
8. Convert the feature **Parental_Education_Level** from qualitative to quantitative. Use the following encoding: *High School*=1, *College*=2, *Postgraduate*=3. Do not delete/replace **Parental_Education_Level**, create a new feature instead. Use the name **Parental_Education_Level_Quant** for the new feature. Include this new feature in the list of quantitative  features. Find the min and max value for this new feature.
9. Convert the feature **Previous_Scores** from quantitative to qualitative. Use the following bin names (0 to 30)=*Very Poor*, (30 to 59)=*Poor*, (60 to 90)=*Moderate*, (90 above)=*Excellent.* Do not delete/replace **Previous_Scores**, create a new feature instead. Use the name **Previous_Scores_Qual** for the new feature. Include this new feature in the list of qualitative  features. Count the number of unique values for this new feature.
10. For each unique value of **Previous_Scores_Qual,** find the frequency/count (number of samples with said value) of each possible value of **Previous_Scores_Qual.**
11. Download the first sheet (the one containing the dataset) as a csv file. To do this go to File>Download>