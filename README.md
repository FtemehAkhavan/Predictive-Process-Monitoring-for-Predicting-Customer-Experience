# Predictive-Process-Monitoring-for-Predicting-Customer-Experience

## Abstract
It is essential to innovate and improve service levels by predicting possible process outcomes due to the growth of online service providers. This study estimates the customer satisfaction level based on customer experience analysis. In doing so, we answer recent calls for research about a more thorough exploration of customer behavior using predictive process monitoring  techniques. In particular, a hybrid framework of supervised/unsupervised machine learning methods is proposed to predict the outcomes of customers’ experiences while dealing with the problem of high intra-class variance. This problem occurs due to the large dispersion of traces identified in the customer journeys . In this regard, customer journeys  are first matched with the event log format aiming to implement a Density-Based Spatial Clustering of Applications with Noise (DBSCAN) clustering technique based on the similarity between the customer journeys. After summarizing the journeys by removing low-value activities, the multi-class decision tree classification method is applied, and the level of customer satisfaction is predicted. Due to the imbalanced nature of the data, the oversampling for imbalanced classification is applied to achieve good results in accuracy indicators such as recall, precision, and F1-score . Finally, the proposed approach has been evaluated on a real-life event log, BPI Challenge 2016, to investigate unsatisfied customers. The results of the machine learning models on the test data show a high degree of accuracy in predicting customer dissatisfaction.

## Usage
We provide the necessary code to use the algorithm with the event logs of your choice. We illustrate the examples using the BPI Challenge 2016 dataset.

For the data preprocessing (encoding), run: Frequency based encoding.py

To train and evaluate the model, run:
1. DBSCAN implemintation.py
2. removing columns with high covariance.py
3. removing columns withlow variance.py
4. classification-decision tree.py

## Data
The events log for the predictive busienss process monitoring can be found at 4TU Research Data

