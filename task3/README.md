# Task 3: Maximum Number of Interviews

## Description
The task is to determine the maximum number of interviews that can be scheduled without any overlap. Given start and end times of interviews, the goal is to maximize the number of interviews conducted.

## Solution
The solution provides a Flask endpoint `/task` that accepts a POST request containing arrays of start times and end times for interviews. It then calculates the maximum number of interviews that can be conducted without overlap and returns the result.

## How to Run

### Prerequisites
- Python installed on your system.
- Flask library installed (`pip install Flask`).

### Steps
1. **Clone the Repository**:
   - Clone or download the repository containing the Flask application code.

2. **Navigate to Task 3 Directory**:
   - Use the command line to navigate to the directory where your Task 3 files are located.

3. **Run the Flask Application**:
   - Run the following command to start the Flask application:
     ```
     python task3.py
     ```

4. **Access the Endpoint**:
   - Once the Flask application is running, you can access the `/task` endpoint.(`http://127.0.0.1:5000/task`)

### Example JSON for POST Method
Here's an example JSON object you can use for the POST method:
```json
{
  "start_times": [1, 2, 3, 4, 5, 6, 9, 12],
  "end_times": [5, 9, 7, 12, 6, 8, 10, 13]
}
