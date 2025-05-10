import requests
import time
from datetime import datetime

# List of API endpoints to monitor
API_URLS = [
    "https://pokeapi.co/api/v2/move/pound",
    "https://pokeapi.co/api/v2/language/6",
    "https://pokeapi.co/api/v2/ability/1",
    "https://pokeapi.co/api/v2/berry/1"
]

def monitor_api():
    while True:
        for api_url in API_URLS:
            try:
                # Record the start time
                start_time = time.time()
                
                # Make the API Request
                response = requests.get(api_url)
                
                # Calculate the response time
                response_time = time.time() - start_time
                
                # Log the results
                log_message = f"{datetime.now()} | URL: {api_url} | Status: {response.status_code} | Response Time: {response_time:.4f} seconds"
                print(log_message)
                
                # Save to a log file
                with open("v:\\Podium-Prep\\pokemonAPIMonitor\\api-monitoring-dashboard\\logs\\api_logs.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
                    
            except Exception as e:
                # Log any errors
                error_message = f"{datetime.now()} | URL: {api_url} | Error: {str(e)}"
                print(error_message)
                with open("v:\\Podium-Prep\\pokemonAPIMonitor\\api-monitoring-dashboard\\logs\\api_logs.txt", "a") as log_file:
                    log_file.write(error_message + "\n")
        
        # Wait for 10 seconds before the next round of requests
        time.sleep(10)

if __name__ == "__main__":
    monitor_api()
