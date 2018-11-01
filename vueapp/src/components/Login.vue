<template>
<div class="login">
    <form @submit.prevent="login">
       <h2>Login</h2>
       <input type="username" v-model="username" placeholder="Type your username">
       <input type="password" v-model="password" placeholder="Type your password">
       <button>Login</button>
     </form>
</div>
    
</template>

<script>
import {APIAuthenticateUser} from '@/api/APIAuthentification'

const Authenticate = new APIAuthenticateUser()


export default {

    methods: {
        login () {
            Authenticate.login(this.username, this.password)
        },
    }
}
</script>
