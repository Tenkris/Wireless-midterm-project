#!/bin/bash

RTSP_URL="rtsp://admin:admin@192.168.1.100:8554/live"

ffmpeg -i $RTSP_URL -vf "fps=1/5" /home/pi/Desktop/Viabike/5secImage/output_%03d.jpg