import axios from 'axios';

export async function getServerSideProp() {
    try {
        const response = await axios.get('http://localhost:8000/api/products/');
        const products = response.data;
        return {
            props: { products }
        };

    } catch (error) {
        console.error('Error fetching products: ', error);
        return {
            props: {products: [] },
        };
    }
}

const HomePage = ({ products }) =>{

    return (
        <div>
            <h1>Product List</h1>
            { products && products.length > 0 ? (
            <ul>
                {products.map((products) => (
                    <li key={products.id}>
                        <h3>{products.name}</h3>
                        <p>{product.description}</p>
                        <p>Price: {product.price}</p>
                    </li>
                ))}
            </ul>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default HomePage;