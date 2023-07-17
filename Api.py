from flask import Flask
from flask import Flask, jsonify
import requests
import asyncio
from prisma import Prisma

app = Flask(__name__)

async def get_users_from_db():
    db = Prisma()
    await db.connect()
    users = await db.user.find_many() # Removed the 'where' clause
    await db.disconnect() # Disconnect from the database when done
    return users

@app.route("/getproducts", methods=["GET"])
def get_products():
    users = asyncio.run(get_users_from_db())
    return {'users': [user.__dict__ for user in users]} # Assuming the Prisma models can be converted to dict using __dict__

async def get_singleproduct():
    db = Prisma()
    await db.connect()
    product = await db.user.find_first(
        where={
            'id': 1,
        }
    )
    await db.disconnect() # Disconnect from the database when done
    return product

@app.route("/getproduct", methods=["GET"])
def get_product():
    product = asyncio.run(get_singleproduct())
    if product:
        product_dict = product.__dict__
        return jsonify(product_dict)
    else:
        return jsonify({"error": "Product not found"})  # Return an error response if product is not found


if __name__ == "__main__":
    app.run(debug=True)