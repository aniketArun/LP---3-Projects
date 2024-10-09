
let web3;
let contract;
let contractAddress = ' you contract address here'; // Replace with your deployed contract address
let abi = [ 'enter ur abi here'];  // Replace with your contract ABI (copy from Remix after deploying)

window.onload = async () => {
    if (typeof window.ethereum !== 'undefined') {
        // Request account access
        await window.ethereum.enable();
        web3 = new Web3(window.ethereum);
        contract = new web3.eth.Contract(abi, contractAddress);
    } else {
        alert('Please install MetaMask or another Ethereum wallet.');
    }
};

// List a new product
document.getElementById('listProductBtn').addEventListener('click', async () => {
    const productName = document.getElementById('productName').value;
    const productPrice = document.getElementById('productPrice').value;
    const accounts = await web3.eth.getAccounts();

    if (productName && productPrice) {
        try {
            await contract.methods.listProduct(productName, web3.utils.toWei(productPrice, 'ether')).send({ from: accounts[0] });
            document.getElementById('message').innerHTML = '<div class="alert alert-success">Product listed successfully!</div>';
        } catch (error) {
            document.getElementById('message').innerHTML = '<div class="alert alert-danger">Error listing product.</div>';
        }
    } else {
        document.getElementById('message').innerHTML = '<div class="alert alert-warning">Please enter product name and price.</div>';
    }
});

// Purchase a product
document.getElementById('purchaseProductBtn').addEventListener('click', async () => {
    const productId = document.getElementById('productId').value;
    const accounts = await web3.eth.getAccounts();
    const product = await contract.methods.products(productId).call();

    if (product && !product.purchased) {
        try {
            await contract.methods.purchaseProduct(productId).send({ from: accounts[0], value: product.price });
            document.getElementById('message').innerHTML = '<div class="alert alert-success">Product purchased successfully!</div>';
        } catch (error) {
            document.getElementById('message').innerHTML = '<div class="alert alert-danger">Error purchasing product.</div>';
        }
    } else {
        document.getElementById('message').innerHTML = '<div class="alert alert-warning">Product not available or already purchased.</div>';
    }
});

