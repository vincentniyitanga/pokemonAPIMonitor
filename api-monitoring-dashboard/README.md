# API Monitoring Dashboard with Automated Issue Tracking

## Project Overview
This project is designed to monitor the health of a public API, visualize the data, and automatically create tickets for issues. It includes scripts for monitoring API responses, parsing logs, and integrating with automation tools to streamline issue tracking.

## Features
- Periodic monitoring of a chosen public API.
- Logging of response times and status codes.
- Visualization of API metrics using Datadog and Kibana.
- Automated ticket creation in Jira for detected API failures.

## Project Structure
```
api-monitoring-dashboard
├── src
│   ├── scripts
│   │   ├── monitor_api.py        # Script to monitor API health
│   │   └── log_parser.py         # Script to parse API logs
│   ├── workflows
│   │   └── automation_workflow.zapier  # Automation workflow for Zapier
│   └── dashboard
│       └── dashboard_config.json  # Configuration for the dashboard
├── config
│   ├── datadog_config.yaml        # Datadog configuration
│   ├── kibana_config.json         # Kibana configuration
│   └── jira_config.json           # Jira configuration
├── logs
│   └── api_logs.txt               # Log file for API monitoring
├── package.json                   # npm configuration file
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd api-monitoring-dashboard
   ```

2. **Install Python dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure API Monitoring:**
   - Update the `config/jira_config.json`, `config/datadog_config.yaml`, and `config/kibana_config.json` files with your API keys and project details.

4. **Run the API Monitoring Script:**
   ```
   python src/scripts/monitor_api.py
   ```

5. **Set Up Automation Workflows:**
   - Use the `src/workflows/automation_workflow.zapier` file to configure your Zapier account for automated ticket creation.

6. **Visualize Data:**
   - Use Datadog and Kibana to visualize the API metrics as per the configurations in `src/dashboard/dashboard_config.json`.

## Usage Guidelines
- Ensure that the public API you are monitoring is accessible and stable.
- Regularly check the logs in `logs/api_logs.txt` for any anomalies.
- Monitor the dashboard for real-time insights into API performance.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.