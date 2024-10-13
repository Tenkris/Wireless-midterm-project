# viaBike

หลังจากลง OS ให้ Raspberry Pi เรียบร้อย ให้ลง library ดังนี้

```bash
sudo apt install ffmpeg
```

```bash
sudo apt install python3
```

```bash
sudo apt install python3-pip 
```

```bash
sudo apt install python3-pika
```

## จาก กล้องโทรศัพท์ มาที่ Raspberry Pi

- **ให้ทำตาม**: https://mycourseville-default.s3.ap-southeast-1.amazonaws.com/useruploaded_course_files/2024_1/58418/materials/Phone_to_RTSP-1040937-17253429920654.pdf
- ทำจนถึง step 4 จะได้ RTSP URL มา

- จากนั้น สร้าง folder มาที่ path `/home/viabike/5secImage` (แต่จริงๆจะไม่ต้องก็ได้แต่ต้องไปเปลี่ยน path ใน capture_image.sh กับ rabbit.py ด้วย)
- นำ file capture_image.sh มาไว้ใน folder
- แก้ RTSP URL ให้เป็นของตัวเอง
- double click แล้วเลือก Execute in terminal

## จาก Raspberry Pi มาที่ คอม

### ใน Raspberry Pi
- นำ file rabbit.py และ send_image.sh มาไว้ใน folder
- แก้ไข rabbitmq_host ใน file rabbit.py ให้เป็น **ip address** ของ **คอม** ที่จะรับรูปภาพ
- double click send_image.sh แล้วเลือก Execute in terminal

### ในคอม
- start container rabbitmq
- สร้าง folder output
- กด run file rabbit_server.py