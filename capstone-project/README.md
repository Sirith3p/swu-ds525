# Capstone Project

สำหรับ capstone project นี้เป็นส่วนหนึ่งของรายวิชา DS525 Data Engineer

โดย Dataset ที่นำมาใช้เป็นชุดข้อมูลจาก Kaggle
[Coffee shop sample data](https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113)

## สมมติปัญหา
ทางบริษัทร้านกาแฟประสบปัญหากับการจำหน่ายสินค้าและบริการ โดยเฉพาะสินค้าประเภทเบเกอรี่ (pastry) ทางผู้บริหารอยากทราบว่า
- การขายสินค้าประเภทดังกล่าวในแต่ละสาขาเป็นอย่างไร
- การทิ้งสินค้าที่ขายไม่ออกเป็นอย่างไร
- ยอดการขายของสินค้าแต่ละชนิดเป็นอย่างไร
<br> ทั้งนี้เพื่อนำมาวางแผนและปรับกลยุทธ์ในการขายและการให้บริการต่อไป

## Data Model

## Data pipeline and related technologies

### 1.&2. Loading data into data lake and Cleansing and Transforming data
Source code: [01 and 02 create data lake](https://github.com/Sirith3p/swu-ds525/blob/67b6f0de77ab3f863043f2f1ee5a04425e643a8e/capstone-project/dags/01_etl_s3.ipynb)

### 3.&4. Creating table in data warehouse and Inserting data from lake into warehouse
Source code: [03 and 04 create tables in data warehouse and insert data into tables](https://github.com/Sirith3p/swu-ds525/blob/67b6f0de77ab3f863043f2f1ee5a04425e643a8e/capstone-project/dags/02_dwh.py)

### 5. Analysis and Visualization

เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้

sudo chmod 777 .
แล้วค่อยรัน

docker-compose up

1. Ctrl+C ก่อน
2. docker-compose down
3. sudo rm -rf logs plugins
4. mkdir -p ./dags ./logs ./plugins
5. echo -e "AIRFLOW_UID=$(id -u)" > .env
6. docker-compose up