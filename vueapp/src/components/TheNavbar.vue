<template>
    <div class="hero-head">
        <nav class="navbar has-shadow is-spaced">
            <div class="container">
                <div class="navbar-brand">
                    <router-link :to="{name: 'Home'}" class="navbar-item">
                        <img id="nav-logo" src="../assets/img/logo.png" height="80px">
                    </router-link>
                    <div id="navbarBurger" class="navbar-burger burger dropdown" v-on:click="showNav = !showNav"
                        v-bind:class="{ 'is-active' : showNav }" data-target="navbarMenu">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
                <div id="navbarMenu" class="navbar-menu" v-bind:class="{ 'is-active' : showNav }">
                    <div class="navbar-end">
                        <router-link :to="{name: 'Home'}" class="navbar-item">Home</router-link>
                        <router-link :to="{name: 'Additives'}" class="navbar-item">Additifs</router-link>
                        <router-link :to="{name: 'Product'}" class="navbar-item">Product</router-link>
                        <div class="navbar-item has-dropdown is-hoverable">
                            <div class="navbar-item has-dropdown"><a class="navbar-link">Nutriment</a>
                                <div class="navbar-dropdown is-boxed">
                                    <div v-for="nutriment in nutriments" :key='nutriment.id'>
                                        <router-link :to="{name: 'Nutriment', params: { pk: nutriment.id}}" class="navbar-item" replace>{{nutriment.nutriment_name | capitalize}}</router-link>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <router-link :to="{name: 'Home'}" class="navbar-item">FAQ</router-link>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import { APIServiceNutriment } from "../APIService";

const APINutriment = new APIServiceNutriment();

export default {
    name: "NavBar",
    data() {
        return {
            nutriments: [],
            showNav: false
        };
    },
    methods: {
        getNutriments() {
            APINutriment.getNutriments().then(data => {
                this.nutriments = data.results;
            });
        }
    },
    mounted() {
        this.getNutriments();
    }
};
</script>

<style>
#nav-logo {
    max-height: None;
    border: None;
    width: 80px;
    height: 80px;
}
</style>