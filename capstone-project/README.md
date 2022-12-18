# Capstone Project

สำหรับ capstone project นี้เป็นส่วนหนึ่งของรายวิชา DS525 Data Engineer

โดย Dataset ที่นำมาใช้เป็นชุดข้อมูลจาก Kaggle
[Coffee shop sample data](https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113)

## สมมติปัญหา
ทางบริษัทร้านกาแฟประสบปัญหากับการจำหน่ายสินค้าและบริการ โดยเฉพาะสินค้าประเภทเบเกอรี่ (pastry) ทางผู้บริหารอยากทราบว่า
- การขายสินค้าประเภทดังกล่าวในแต่ละสาขาเป็นอย่างไร
- การทิ้งสินค้าที่ขายไม่ออกเป็นอย่างไร
- ยอดการขายของสินค้าแต่ละชนิดเป็นอย่างไร
ทั้งนี้เพื่อนำมาวางแผนและปรับกลยุทธ์ในการขายและการให้บริการต่อไป

## Data Model

## Data pipeline and related technologies

### 1. Loading data into data lake
### 2. Cleansing and Transforming data
### 3.&4. Creating table in data warehouse and Inserting data from lake into warehouse
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