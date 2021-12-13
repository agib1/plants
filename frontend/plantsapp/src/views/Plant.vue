<template>
    <div id="plant">
        <h2 id="p_name">{{ plant.name }}</h2>
        <br/>
        <img id="p_img" :src="baseUrl + plant.image"/>
        <div id="text">
        <h3>{{ plant.description }}</h3>
        <br/>
        <h3>{{ plant.instructions }}</h3>
        <br/>
        </div>
    </div>
</template>

<style>

#plant {
    padding: 20px;
}

#space {
    padding: 30px;
    display: inline-block;
}

#p_img {
    float: left;
    max-width: 300px;
    height: auto;
    border-style: solid;
    border-color: #2c3e50;
}

#save {
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

#save:hover {
    background-color: #aac5dd;
}

#text {
    text-align: left;
    padding: 30px;
    font-size: 12px;
    float: right;
}

</style>

<script>
import { getAPI } from '../axios-api'

export default {
    name: 'Plant',
    data() {
        return {
            plant : [],
            baseUrl : "http://0.0.0.0:8000"
        }
    },

    created() {
        var slug = this.$route.params.slug
        getAPI.get('/plants/' + slug,)
        .then(response => {
            console.log('Plants API has recieved data')
            this.plant = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>
