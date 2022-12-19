# Capstone Project

สำหรับ capstone project นี้เป็นส่วนหนึ่งของรายวิชา DS525 Data Engineer
<br>

โดย Dataset ที่นำมาใช้เป็นชุดข้อมูลจาก Kaggle
[Coffee shop sample data](https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113)
<br>

ํYoutube clip [Link Youtube](https://youtu.be/E557vRDh_y4)
<br>

## สมมติปัญหา
ทางบริษัทร้านกาแฟประสบปัญหากับการจำหน่ายสินค้าและบริการ โดยเฉพาะสินค้าประเภทเบเกอรี่ (pastry) ทางผู้บริหารอยากทราบว่า
- การขายสินค้าประเภทดังกล่าวในแต่ละสาขาเป็นอย่างไร
- การทิ้งสินค้าที่ขายไม่ออกเป็นอย่างไร
- ยอดการขายของสินค้าแต่ละชนิดเป็นอย่างไร
<br> 

ทั้งนี้เพื่อนำมาวางแผนและปรับกลยุทธ์ในการขายและการให้บริการต่อไป
<br>

## Data Model
![alt text](https://github.com/Sirith3p/swu-ds525/blob/9ed8ae8e73ed7bd1557eca255c8933d853ca38c6/capstone-project/images/datamodel.png)
<br>

## Data pipeline and related technologies
![alt text](https://github.com/Sirith3p/swu-ds525/blob/9ed8ae8e73ed7bd1557eca255c8933d853ca38c6/capstone-project/images/datapipeline.png)
<br>

## Instruction
### 1.&2. Loading data into data lake and Cleansing and Transforming data
- Create S3 bucket for building datalake
- Import data and cleasing data as the below code
- Source code: [01 and 02 create data lake](https://github.com/Sirith3p/swu-ds525/blob/67b6f0de77ab3f863043f2f1ee5a04425e643a8e/capstone-project/dags/01_etl_s3.ipynb)
<br>

### 3.&4. Creating table in data warehouse and Inserting data from lake into warehouse
- Create Amazon Redshift for building datawarehouse
- Run the below code for automated creating and inserting tables processs
- Source code: [03 and 04 create tables in data warehouse and insert data into tables](https://github.com/Sirith3p/swu-ds525/blob/67b6f0de77ab3f863043f2f1ee5a04425e643a8e/capstone-project/dags/02_dwh.py)
<br>

### 5. Analysis and Visualization
- Link redshift to the Tableau workbook and create the data dashboard
![alt text](https://github.com/Sirith3p/swu-ds525/blob/9ed8ae8e73ed7bd1557eca255c8933d853ca38c6/capstone-project/images/dataviz.png)
