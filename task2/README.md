# Task 2: Unauthorized Sales Detection

## Description
This task involves identifying unauthorized sales transactions given product listings and sales data. It requires comparing product listings with sales transactions to find unauthorized sales.

## Solution
The solution provides a Flask endpoint `/task` that accepts a POST request containing product listings and sales transactions. It then compares sales transactions against product listings to identify unauthorized sales and returns the results.

## How to Run

### Prerequisites
- Python installed on your system.
- Flask library installed (`pip install Flask`).

### Steps
1. **Clone the Repository**:
   - Clone or download the repository containing the Flask application code.

2. **Navigate to Task 2 Directory**:
   - Use the command line to navigate to the directory where your Task 2 files are located.

3. **Run the Flask Application**:
   - Run the following command to start the Flask application:
     ```
     python task2.py
     ```

4. **Access the Endpoint**:
   - Once the Flask application is running, you can access the `/task` endpoint.(`http://127.0.0.1:5000/task`)

### Example JSON for POST Method
Here's an example JSON object you can use for the POST method:
```json
{
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
