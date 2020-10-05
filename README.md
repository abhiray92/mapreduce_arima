# mapreduce_arima
This code forecasts a timeseries data using ARIMA by leveraging Map Reduce coding paradigm



############################### Performing Time Series Analysis on Hadoop ###################################

1. The .txt file is the original data which needs to be pre-processed in python with the .IPYNB file given.
2. The .IPYNB file will generate a CSV file named household_powerconsumption.csv, which has to be ingested into the Linux Server.
3. The file needs to be split using the 'split' command on the Linux server.
4. The file generated by the 'split' command need to be run on the Imputer.py file to clean the missing values using KNN Imputer.
5. The files generated have to be put on a Hadoop parition on HDFS.
6. The arima*.py files need to be run with the with the mapred streaming $HADOOP_HOME/bin/*.jar file to produce the output.
