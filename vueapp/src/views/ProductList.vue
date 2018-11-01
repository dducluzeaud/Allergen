<template>
    <ul v-if="products">
        <p>{{numberOfProducts}}</p>
        <li v-for="product in products" :key='product.id'>
            <p><strong>{{product.product_name}}</strong></p>
            <p>{{nextPage}}</p>
        </li>
    </ul>
    <div v-else>
        <p>No data</p>
    </div>
</template>

<script>
    import {
        APIServiceProduct
    } from '@/api/APIService';
    
    const APIProduct = new APIServiceProduct();

    export default {
        data() {
            return {
                products: [],
                numberOfProducts: 0,
                nextPage: '',
                previousPage: '',
                errors: []
            };
        },
        created () {
            this.getProducts()
        },
        watch: {
            '$route': 'getProducts'
        },
        methods: {
            getProducts(){
                APIProduct.getProducts().then((data) => {
                    this.products = data.results
                    this.numberOfProducts = data.count
                    this.nextPage = data.next
                    this.previousPage = data.previous
                });
            },
        },
    }
</script>