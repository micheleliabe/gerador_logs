# Log Generator Application

A Python application that generates random log messages with configurable formats and intervals. Perfect for testing log aggregation systems, monitoring tools, or development environments.

## Features

- 🎯 **Configurable Log Generation**
  - Random log messages from a predefined list
  - Customizable intervals between logs
  - Multiple log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)

- 📝 **Flexible Log Formats**
  - Text format (default)
  - JSON format (structured logging)
  - ISO 8601 timestamps

- 🐳 **Docker Support**
  - Easy deployment with Docker
  - Configurable via environment variables
  - Volume mounting for log configuration

- ☸️ **Kubernetes Support**
  - Ready-to-deploy Kubernetes manifests
  - ConfigMap for log configuration
  - Easy scaling and management

- ⚙️ **Configuration Options**
  - Environment variable based configuration
  - External JSON configuration file
  - Runtime customization

## Quick Start

### Using Docker Compose

```bash
# Start with default settings
docker-compose up

# Start with JSON format
docker-compose run -e LOG_FORMAT_JSON=true log-generator
```

### Using Docker Directly

```bash
# Build the image
docker build -t log-generator .

# Run with default settings
docker run -it log-generator

# Run with custom settings
docker run -it \
  -e LOG_FORMAT_JSON=true \
  log-generator
```

### Kubernetes Deployment

See the [Kubernetes Deployment Guide](k8s/README.md) for detailed instructions on deploying to a Kubernetes cluster.

```bash
# Deploy to Kubernetes
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml

# Monitor the deployment
kubectl logs -f deployment/log-generator
```

### Running Locally

```bash
# With default settings
python app.py

# With custom settings
LOG_FORMAT_JSON=true python app.py
```

## Configuration

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `LOG_FORMAT_JSON` | Use JSON format for logs | false | true |
| `CONFIG_FILE` | Path to log configuration file | logs_config.json | custom_config.json |

### Log Configuration File

The application uses a JSON configuration file (`logs_config.json` by default) to define the log messages, their levels, and the interval between logs:

```json
{
    "interval": 1,
    "logs": [
        {
            "message": "User authentication successful for user_id: 12345",
            "level": "INFO"
        },
        {
            "message": "Cache miss for key: user_profile_12345",
            "level": "WARNING"
        }
    ]
}
```

## Log Formats

### Text Format (default)
```
2024-03-14 10:30:45 - INFO - User authentication successful for user_id: 12345
2024-03-14 10:30:46 - WARNING - Cache miss for key: user_profile_12345
```

### JSON Format
```json
{
    "timestamp": "2024-03-14T10:30:45",
    "level": "INFO",
    "message": "User authentication successful for user_id: 12345",
    "logger": "__main__"
}
{
    "timestamp": "2024-03-14T10:30:46",
    "level": "WARNING",
    "message": "Cache miss for key: user_profile_12345",
    "logger": "__main__"
}
```

## Project Structure

```
gerador_logs_v2/
├── app.py              # Main application code
├── logs_config.json    # Log message configuration
├── Dockerfile          # Docker build instructions
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── k8s/               # Kubernetes deployment files
│   ├── deployment.yaml # Kubernetes deployment
│   ├── configmap.yaml  # Log configuration
│   └── README.md      # Kubernetes deployment guide
└── README.md          # This file
```

## Development

### Prerequisites

- Python 3.11 or higher
- Docker (optional)
- Docker Compose (optional)
- Kubernetes cluster (optional)

### Building and Running

1. Clone the repository
2. Install dependencies (if running locally)
3. Configure your log messages in `logs_config.json`
4. Run using Docker, Kubernetes, or Python directly

### Customizing Logs

To add or modify log messages:
1. Edit the `logs_config.json` file
2. Add new entries with `message` and `level` fields
3. Set the desired interval between logs
4. Restart the application

## Use Cases

- Testing log aggregation systems
- Development environment testing
- Monitoring system validation
- Log analysis tool testing
- System integration testing
- Kubernetes logging testing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 