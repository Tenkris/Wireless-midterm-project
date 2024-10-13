# RabbitMQ Bicycle Counter with InfluxDB and Streamlit

This project implements a real-time bicycle counting system using computer vision, message queuing, time-series database, and a web-based dashboard. It processes images from a RabbitMQ queue, detects bicycles using YOLOv5, stores count data in InfluxDB, and visualizes statistics through a Streamlit dashboard.

## Features

- Image consumption from RabbitMQ queue
- Bicycle detection using YOLOv5
- Real-time data storage in InfluxDB
- Live statistics visualization with Streamlit
- Dockerized setup for easy deployment

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- CUDA-capable GPU (recommended for faster inference)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/rabbitmq-bicycle-counter.git
   cd rabbitmq-bicycle-counter
   ```

2. Set up and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Start RabbitMQ and InfluxDB services:

   ```
   docker-compose up -d
   ```

2. Update configuration in `bicycle_counter.py` and `streamlit_app.py` if necessary.

## Usage

1. Run the bicycle counter:

   ```
   python rabbit_server.py
   ```

2. Launch the Streamlit dashboard:

   ```
   streamlit run streamlit-main.py
   ```

3. Access the dashboard at `http://localhost:8501`.

## Project Structure

- `bicycle_counter.py`: Main script for image processing and data storage
- `streamlit_app.py`: Streamlit dashboard for data visualization
- `docker-compose.yml`: Docker services configuration
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Troubleshooting

- Verify Docker and Docker Compose installation
- Check RabbitMQ and InfluxDB service accessibility
- Ensure RabbitMQ queue exists and receives messages
- Run scripts within the activated virtual environment

## Contributing

Contributions are welcome! Please submit Pull Requests for any improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
