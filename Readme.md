
# Simple Marketplace Contract

## Overview

This project implements a simple marketplace smart contract using Solidity. Users can add products and retrieve a list of available products. The contract is designed to run on the Ethereum blockchain and can be deployed using Remix IDE.

## Features

- Add products to the marketplace with a unique ID and name.
- Retrieve the list of products from the marketplace.
- Easy deployment using Remix IDE or via a local/test Ethereum network.

## Technologies Used

- Solidity: Programming language for writing smart contracts.
- Ethereum: Blockchain platform for deploying the smart contract.
- Remix IDE: An online IDE for developing, deploying, and managing smart contracts.

## Smart Contract Code

The contract code is as follows:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleMarketplace {
    struct Product {
        uint256 id;
        string name;
    }

    mapping(uint256 => Product) public products;
    uint256 public productCount;

    function addProduct(string memory _name) public {
        productCount++;
        products[productCount] = Product(productCount, _name);
    }

    function getProducts() public view returns (Product[] memory) {
        Product[] memory productList = new Product[](productCount);
        for (uint256 i = 1; i <= productCount; i++) {
            productList[i - 1] = products[i];
        }
        return productList;
    }
}
```

## Deployment Instructions

1. Open [Remix IDE](https://remix.ethereum.org/).
2. Create a new file named `SimpleMarketplace.sol` and paste the contract code into it.
3. Compile the contract by selecting the correct compiler version.
4. Navigate to the **Deploy & Run Transactions** tab.
5. Select **Injected Provider - MetaMask** to connect to a test network (e.g., Rinkeby, Sepolia).
6. Deploy the contract and confirm the transaction in MetaMask.
7. After deployment, you will receive a contract address to interact with your contract.

## Interacting with the Contract

You can interact with the deployed contract using the following functions:

- **addProduct**: Adds a new product to the marketplace.
  - Input: `_name` (string) - The name of the product.
  
- **getProducts**: Retrieves the list of products from the marketplace.
  - Output: An array of `Product` structs containing `id` and `name`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## Contact

For questions or inquiries, please contact:

- **Name**: Aniket
- **Email**: aniketpen8478@gmail.com (mailto: aniketpen8478@gmail.com)


### Instructions to Upload to GitHub
1. Create a new repository on GitHub.
2. Clone the repository to your local machine using `git clone <repository-url>`.
3. Navigate to the cloned repository folder.
4. Create a new file named `README.md` and paste the content above.
5. Add your smart contract file (e.g., `SimpleMarketplace.sol`) to the repository.
6. Commit your changes:
   ```bash
   git add README.md SimpleMarketplace.sol
   git commit -m "Add simple marketplace contract and README"
   ```
7. Push your changes to GitHub:
   ```bash
   git push origin main
   ```