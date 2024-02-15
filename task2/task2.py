from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello SKAI Labs!"

#function that returns all the unauthorised sales
def checkSales(product_listings, sales_transactions):
    unauthorized_sales = []

    for sale in sales_transactions:
        #creating test_sale for easier use of 'not ... in..' with product_listing
        test_sale = {"productID": sale["productID"], "authorizedSellerID": sale["sellerID"]}

        if not sale in product_listings:
            #if we can't find an instance where seller is authorised to sell product, then add it to unauthorised list
            unauthorized_sales.append({"productID": sale["productID"], "unauthorizedSellerID": sale["sellerID"]})
            break

    return unauthorized_sales

########TASK ENDPOINT#######
@app.route("/task", methods=["POST"])
def task():
    #checks if request body has all the elements needed to proceed
    if not request.json or "productListings" not in request.json or "salesTransactions" not in request.json:
        return jsonify({"error": "Bad Request"}), 400
    
    product_listings = request.json["productListings"]
    sales_transactions = request.json["salesTransactions"]

    unauthorized_sales = checkSales(product_listings, sales_transactions)

    response = {"unauthorizedSales": unauthorized_sales}
    return jsonify(response), 200

if __name__ == "__main__":  
   app.run()