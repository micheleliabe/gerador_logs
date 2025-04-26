import random
import time
import os
import json
import logging
from typing import List, Dict, Any
from datetime import datetime

# Environment variables with defaults
LOG_FORMAT_JSON = os.getenv('LOG_FORMAT_JSON', 'false').lower() in ('true', '1', 'yes')
CONFIG_FILE = os.getenv('CONFIG_FILE', 'logs_config.json')

# Debug environment variables
print(f"Environment variables:")
print(f"LOG_FORMAT_JSON: {LOG_FORMAT_JSON} (raw: {os.getenv('LOG_FORMAT_JSON')})")

# Map string log levels to logging constants
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Configure logging
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name
        }
        return json.dumps(log_data)

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set to DEBUG to allow all log levels

# Remove any existing handlers
logger.handlers = []

# Create console handler
console_handler = logging.StreamHandler()

# Set formatter based on LOG_FORMAT_JSON
if LOG_FORMAT_JSON:
    print("Using JSON formatter")
    console_handler.setFormatter(JsonFormatter())
else:
    print("Using text formatter")
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

logger.addHandler(console_handler)

def load_logs_config(file_path: str) -> List[Dict[str, Any]]:
    """Load logs configuration from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log configuration file not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            
        if not config.get('logs'):
            raise ValueError("Log configuration file must contain a 'logs' array")
            
        # Validate log entries
        for log in config['logs']:
            if 'message' not in log or 'level' not in log:
                raise ValueError("Each log entry must have 'message' and 'level' fields")
            if log['level'] not in LOG_LEVELS:
                raise ValueError(f"Invalid log level: {log['level']}. Must be one of: {list(LOG_LEVELS.keys())}")
        
        return config['logs'], config.get('interval', 1)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")

def generate_logs(config_file: str = CONFIG_FILE) -> None:
    """Generate random logs from the specified configuration file."""
    try:
        logs, interval = load_logs_config(config_file)
        logger.info("Log generator started successfully")
        logger.info(f"Configuration: format={'JSON' if LOG_FORMAT_JSON else 'TEXT'}, interval={interval}s")
        
        while True:
            log_entry = random.choice(logs)
            log_level = LOG_LEVELS[log_entry['level']]
            logger.log(log_level, log_entry['message'])
            time.sleep(interval)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        generate_logs()
    except KeyboardInterrupt:
        logger.info("Log generator stopped by user")
    except Exception as e:
        logger.error(f"Program terminated due to error: {str(e)}") 