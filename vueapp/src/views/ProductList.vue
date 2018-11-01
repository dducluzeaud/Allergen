<template>
    <div v-if="products">
        <div class="columns is-multiline">
            <div class="column is-one-quarter is-centered " v-for="product in products" :key='product.id'>
                    <div class='card-content is-flex is-horizontal-center'>
                    <img class="image is-128x128" :src="product.image_url">
                    </div>
                    <p>{{product.product_name}}</p>

            </div>
        </div>
    </div>
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

<style>
.is-horizontal-center {
  justify-content: center;
}
</style>
