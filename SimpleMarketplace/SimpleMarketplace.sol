// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleMarketplace {

    // Struct to represent a product
    struct Product {
        uint id;
        string name;
        uint price;
        address payable seller;
        bool purchased;
    }

    // State variables
    uint public productCount = 0; // Number of products in the marketplace
    mapping(uint => Product) public products; // Mapping of product IDs to products

    // Event to emit when a new product is listed
    event ProductListed(uint id, string name, uint price, address seller);

    // Event to emit when a product is purchased
    event ProductPurchased(uint id, string name, uint price, address buyer);

    // Modifier to check that the price is greater than 0
    modifier isValidPrice(uint _price) {
        require(_price > 0, "Price must be greater than 0.");
        _;
    }

    // Function to list a new product
    function listProduct(string memory _name, uint _price) public isValidPrice(_price) {
        productCount++; // Increment product count
        products[productCount] = Product(productCount, _name, _price, payable(msg.sender), false); // Add product to the mapping
        emit ProductListed(productCount, _name, _price, msg.sender); // Emit event
    }

    // Function to purchase a product
    function purchaseProduct(uint _id) public payable {
        Product memory product = products[_id]; // Get the product from the mapping
        require(product.id > 0 && product.id <= productCount, "Product does not exist."); // Check if the product exists
        require(msg.value == product.price, "Please send the exact price."); // Check if the buyer sent the correct amount
        require(!product.purchased, "Product has already been purchased."); // Check if the product is already purchased
        require(product.seller != msg.sender, "Seller cannot buy their own product."); // Prevent seller from buying their own product

        product.seller.transfer(msg.value); // Transfer funds to the seller
        product.purchased = true; // Mark the product as purchased
        products[_id] = product; // Update the product in the mapping

        emit ProductPurchased(product.id, product.name, product.price, msg.sender); // Emit event
    }
}
