# Task 1: Map Polygon Visualization

## Description
This task involves visualizing a polygon on a map. The polygon data is retrieved from a JSON file or an API, and the map is displayed with the OpenLayers library.

## Solution
The solution includes two main parts:
1. **JavaScript Functions**: These functions are responsible for fetching the polygon data, calculating zoom level and center point based on the polygon's bounding box, and displaying the map with the polygon overlay using OpenLayers.

2. **HTTP Server Setup**: To visualize the map and polygon locally, we need to set up an HTTP server to serve the HTML, JavaScript, and CSS files. We'll use `http-server`, a simple, zero-configuration command-line HTTP server.

## How to Run

1. **Install Node.js (if not already installed)**:
   - Download and install Node.js from the [official website](https://nodejs.org/).
   - Follow the installation instructions provided for your operating system.

2. **Install http-server Globally**:
   - Open Command Prompt as an administrator.
   - Run the following command to install `http-server` globally:
     ```
     npm install -g http-server
     ```

3. **Navigate to Task 1 Directory**:
   - Use the `cd` command to navigate to the directory where your Task 1 files are located.

4. **Run http-server**:
   - Once inside the Task 1 directory, run the following command to start the HTTP server:
     ```
     http-server
     ```

5. **Access the Map in Browser**:
   - Open a web browser (e.g., Google Chrome, Mozilla Firefox).
   - Enter the following URL in the address bar:
     ```
     http://localhost:8080
     ```
   - You should now see the map with the polygon overlay rendered in the browser window.
