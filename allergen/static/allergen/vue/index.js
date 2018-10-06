import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

Vue.config.delitmiters = ["[[", "]]"]


const store = new Vuex.Store({
    state: {
        jwt: localStorage.getItem('t'),
        endpoints: {
            obtainJWT: 'http://0.0.0.0:10000/auth/obtain_token',
            refreshJWT: 'http://0.0.0.0:10000/auth/refresh_token'
        }
    },
    mutations: {
        updateToken(state, newToken) {
            localStorage.setItem('t', newToken);
            state.jwt = newToken;
        },
        removeToken(state) {
            localStorage.removeItem('t');
            state.jwt = null;
        }
    },
    actions: {
        // WE WILL ADD THIS LATER
    }
})


var demo = new Vue({
    el: '#app',
    data: {
        'productName': 'Django Vue.JS Job Board',
        'product': []
    },
    methods: {
        addProduct: function () {
            var newProduct = {
                productName: this.productName.trim(),
                productdescription: this.productdescription.trim()
            };

            this.$http.post('http://0.0.0.1:8000/api/products/', newproduct);
        },
        removeJob: function (index) {
            this.$http.delete('http://0.0.0.0:8000/api/products/'.concat(this.products[index].id));
            this.jobs.splice(index, 1);
        }
    },
    ready: function () {
        this.$http.get('http://0.0.0.0:8000/api/products/').then(function (response) {
                this.jobs = response.data;
            },
            function (response) {
                console.log(response);
            });
    }
});