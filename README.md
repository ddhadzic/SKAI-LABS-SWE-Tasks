# SKAI LABS SWE Tasks

## Task 1: Map Polygon Visualization

### Description
The task involves visualizing a polygon on a map. The polygon data is retrieved from a JSON file or an API, and the map is displayed with OpenLayers library.

### Solution
The solution includes two main functions:
1. `readJSON(json_URL)`: Fetches polygon data from a JSON file or API specified by `json_URL`.
2. `calculateZoomAndCenter(poly)`: Calculates the zoom level and center point based on the polygon's bounding box.

The solution utilizes OpenLayers for map visualization. It fetches the polygon data, calculates zoom and center points, then displays the map with the polygon overlay.

## Task 2: Unauthorized Sales Detection

### Description
This task involves identifying unauthorized sales transactions given product listings and sales data. It requires comparing product listings with sales transactions to find unauthorized sales.

### Solution
The solution provides a Flask endpoint `/task` that accepts a POST request containing product listings and sales transactions. It then compares sales transactions against product listings to identify unauthorized sales and returns the results.

## Task 3: Maximum Number of Interviews

### Description
The task is to determine the maximum number of interviews that can be scheduled without any overlap. Given start and end times of interviews, the goal is to maximize the number of interviews conducted.

### Solution
The solution implements an algorithm that sorts interviews based on their starting times and calculates how many interviews will be excluded after each interview starts. It then iterates through the exclusions to find the maximum number of interviews that can be conducted without overlap.

## How to Run
To run each task solution, follow the instructions provided in their respective README files. Ensure you have the necessary dependencies installed and run the Flask applications as directed.

For any questions or issues, please contact me.
