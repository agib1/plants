<template>
    <div id="plants">
        <router-link :to="{ name: 'plant', params: { slug: PlantsAPIData[Math.floor(Math.random()*PlantsAPIData.length)].slug}}">
        <button id="name">Random Plant</button>
        </router-link>
        <div id="top"></div>
        <router-link :to="{ name: 'request'}">
        <button id="name">Request Plant</button>
        </router-link>
        <div id="grid">
        <div id="entries" v-for="plants in PlantsAPIData" :key="plants.id">
            <div id="entry">
                <img id="entryimg" :src="baseUrl + plants.image"/>
                <br/>
                <router-link :to="{ name: 'plant', params: { slug: plants.slug}}">
                <button id="name">{{ plants.name }}</button>
                </router-link>
            </div>
        </div>
        </div>
    </div>
</template>

<style>

#top {
    padding: 30px;
    display: inline-block;
}

#grid {
    float:left;
    padding-left: 110px;
}
#entries {
    max-width: 300px;
    display: inline-block;
    padding: 30px;
}

#entry {
    background-color: white;
    max-width: 300px;
    padding: 30px;
}

#name {
    background-color: #99ccb3;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    color: #2c3e50;
    padding: 14px 40px;
    border-style: none;
    height:50px;
    width:306px;
}

#name:hover {
    background-color: #aac5dd;
}

#entryimg {
    border-style: solid;
    border-color: #2c3e50;
    max-width: 300px;
    height: auto;
}

</style>

<script>
import { getAPI } from '../axios-api'

export default {
    name: 'Plants',

    data() {
        return {
            PlantsAPIData : [],
            baseUrl : "http://0.0.0.0:8000",
        }
    },

    created() {
        getAPI.get('/plants/',)
        .then(response => {
            console.log('Plants API has recieved data')
            this.PlantsAPIData = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>
