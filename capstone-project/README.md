
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