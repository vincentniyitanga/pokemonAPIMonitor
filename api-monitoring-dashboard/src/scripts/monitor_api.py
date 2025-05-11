import requests
import time
from datetime import datetime
from datadog import statsd

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
                start_time = time.time()
                response = requests.get(api_url)
                response_time = time.time() - start_time

                log_message = f"{datetime.now()} | URL: {api_url} | Status: {response.status_code} | Response Time: {response_time:.4f} seconds"
                print(log_message)
                with open("v:\\Podium-Prep\\pokemonAPIMonitor\\api-monitoring-dashboard\\logs\\api_logs.txt", "a") as log_file:
                    log_file.write(log_message + "\n")

                # Send metrics to Datadog Agent via DogStatsD
                statsd.gauge('pokemonapi.response_time', response_time, tags=[f"url:{api_url}", f"status:{response.status_code}"])

            except Exception as e:
                error_message = f"{datetime.now()} | URL: {api_url} | Error: {str(e)}"
                print(error_message)
                with open("v:\\Podium-Prep\\pokemonAPIMonitor\\api-monitoring-dashboard\\logs\\api_logs.txt", "a") as log_file:
                    log_file.write(error_message + "\n")
                # Send error metric to Datadog Agent
                statsd.increment('pokemonapi.errors', tags=[f"url:{api_url}"])
        time.sleep(60)

if __name__ == "__main__":
    monitor_api()
