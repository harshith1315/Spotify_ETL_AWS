# Spotify_ETL_AWS
### Architecture
![image](https://github.com/harshith1315/Spotify_ETL_AWS/assets/111886682/8b12b22b-2614-4b2d-b438-60dfeb8c9ec2)
## ETL
ETL refers to Extract, Transform, Load, which is a common data processing technique used in data warehousing. In this context, it refers to the process of extracting data from various sources (Spotify, Python, Microsoft SQL), transforming it into a format suitable for the data warehouse (AWS RDS), and loading it into the data warehouse.

### AWS  
AWS refers to Amazon Web Services, a comprehensive, on-demand cloud computing platform that provides compute power, database storage, content delivery and other functionality to help businesses scale and grow their applications.

### Scheduled
Scheduled refers to a scheduling tool that is used to automate the ETL process. This ensures that data is extracted, transformed, and loaded into the data warehouse on a regular basis.

### Data Migration 
Data Migration refers to a software application that is used to migrate data between different sources and targets. In this context, it refers to the tool that is used to extract data from the source systems (Spotify, Python, Microsoft SQL) and stage it in the AWS S3 bucket.

### Amazon S3  
Amazon Simple Storage Service, which is an object storage service that offers industry-leading scalability, data availability, security, and performance. In this context, the data extracted from the source systems is likely to be stored in the S3 bucket before being loaded into the data warehouse.

### Amazon RDS 
Amazon RDS refers to Amazon Relational Database Service, a managed relational database service that simplifies setting up, operating, and scaling databases in the cloud. In this context, the Amazon RDS appears to be the data warehouse that stores the transformed data.

### Power BI 
Power BI refers to Business Intelligence, which is a broad category of applications and technologies for gathering, storing, analyzing, and interpreting data. In this context, the BI tool is likely to be used to query and analyze the data in the data warehouse.

Overall, the data warehouse architecture depicted in the image seems to be a typical example of a cloud-based data warehouse that leverages AWS services to extract, transform, load, and store data for business intelligence purposes.


