<template>
    <div class="hero-body">
        <div class="container has-text-centered">
            <div class="columns is-vcentered">
                <div class="column is-5">
                    <figure class="image is-4by3">
                        <img :src=nutriment.image alt="Description">
                    </figure>
                </div>
                <div class="column is-6 is-offset-1">
                    <h1 class="title is-2">
                        {{nutriment.nutriment_name | capitalize}}<br>
                    </h1>
                    <h3 class="is-4 has-text-justified">
                        {{nutriment.description}}
                    </h3>
                    <br>
                    <div v-if="nutriment.daily_quantity_m != nutriment.daily_quantity_f">
                        <p>Apport journalier homme: {{nutriment.daily_quantity_m}}</p>
                        <p>Apport journalier femme: {{nutriment.daily_quantity_f}}</p>
                    </div>
                    <div v-else>
                        <p>Apport journalier: {{nutriment.daily_quantity_f}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {
        APIServiceNutriment
    } from '@/api/APIService';

    const APINutriment = new APIServiceNutriment();

    export default {
        data() {
            return {
                nutriment: [],
            };
        },
        created () {
            // Fethc the data the view is created
            // and the data is already being observed
            this.getNutriment()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'getNutriment'
        },
        methods: {
            getNutriment() {
                APINutriment.getNutriment(this.$route.params.pk).then(data => {
                    this.nutriment = data
                });
            },
        },
    }
</script>
