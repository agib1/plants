<template>
    <div class="tests">
        <h1>Tests</h1>
        <div v-for="tests in APIData" :key="tests.id">
            <h4>{{ tests.text }}</h4>
        </div>
    </div>
</template>


<script>
import { getAPI } from '../axios-api'

export default {
    name: 'Tests',
    data() {
        return {
            APIData : []
        }
    },

    created() {
        getAPI.get('/tests/',)
        .then(response => {
            console.log('Test API has recieved data')
            this.APIData = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>
