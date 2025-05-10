import re

def parse_logs(log_file):
    response_times = []
    error_rates = {}
    
    with open(log_file, 'r') as file:
        for line in file:
            # Assuming log format: "timestamp - status_code - response_time"
            match = re.match(r'(\S+) - (\d{3}) - (\d+)', line)
            if match:
                timestamp, status_code, response_time = match.groups()
                response_times.append(int(response_time))
                
                if status_code not in error_rates:
                    error_rates[status_code] = 0
                error_rates[status_code] += 1

    return response_times, error_rates

def main():
    log_file = '../logs/api_logs.txt'
    response_times, error_rates = parse_logs(log_file)
    
    print(f'Response Times: {response_times}')
    print(f'Error Rates: {error_rates}')

if __name__ == "__main__":
    main()