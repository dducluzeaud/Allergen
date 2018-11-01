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
                        <!-- <div v-if='authUser'>
                            <router-link :to="{name: 'Profile'}" class="navbar-item">Profile</router-link>
                        </div> -->
                        <div>
                            <router-link :to="{name: 'Login'}" class="navbar-item">Connexion</router-link>
                        </div>
                        <router-link :to="{name: 'Additives'}" class="navbar-item">Additifs</router-link>
                        <router-link :to="{name: 'ProductList'}" class="navbar-item">Product</router-link>
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
import { APIServiceNutriment } from "@/api/APIService";
import {mapGetters} from 'vuex'

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
    },
    computed: {
        ...mapGetters({
            'user': 'authUser'
        })
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