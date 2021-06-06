# API Access Log Anomaly Detection

This repository contains the final submission for **VMWare Campus Ambassador Hackathon**. We have used unsupervised Machine Learning algorithms to detect anomalies in web server access logs. 

## Dataset
A [publicly available](https://github.com/linuxacademy/content-elastic-log-samples/blob/master/access.log) access log from a web server was used. After parsing the log file, features such as mean number of requests per day, mean time between successive requests, etc were extract for each IP address. The final dataset is present in `finaldata.csv`. The code used for data processing can be found in `data_preparation.ipynb`

## Approach 
More information and proper discussion on our approach as well as the proposed improvements can be found in `Prototype_Submission.pdf`
The following unsupervised learning algorithms were used to detect anomalous requests present in the dataset:
1. K Means Clustering
2. Isolation Forest
3. One Class SVM 

Code, data visualisation and anomaly detection results can be found in `Unsupervised Learning.ipynb`

## Video Demonstration of Code
[Click Here](https://drive.google.com/file/d/16Lp6IfvONdPzKp3VMGpGr268eF8tot2_/view) or the link can be found in `video.md`


## Contributors 
- [Aishani Mitra](https://github.com/Aishani2001) <br>
- [Shreya Singh](https://github.com/ss0313) <br>
- [Vignesh Ravichandra Rao](https://github.com/vrrao01) <br>
- [Dibya Darshney](https://github.com/ddarshney)

