<template>
  <div id="plants">
    <router-link :to="{ name: 'plants' }">
      <button id="name">Back To Plants</button>
    </router-link>
    <br />
    <br />
    <br />
    <br />
    <form v-on:submit.prevent="submitRequest">
      <label for="pname">Plant name:</label><br />
      <input id="pname" type="text" v-model="pname">
      <br/>
      <br />
      <br />
      <button id="name" :class="[pname ? activeClass : '']" type="submit">Request Plant</button>
    </form>
    <h4>{{ message }}</h4>
  </div>
</template>

<style>
#name {
  background-color: #99ccb3;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: bold;
  color: #2c3e50;
  padding: 14px 40px;
  border-style: none;
  height: 50px;
  width: 306px;
}

#name:hover {
  background-color: #aac5dd;
}
</style>

<script>
import { getAPI } from '../axios-api'

export default {
    name: 'Request',

    data() {
        return {
            pname : '',
            message : '',
            exists : [],
            requests : []
        }
    },
    methods:{
        submitRequest(){
            getAPI.get('/requests/', )
            .then(response => {
                console.log('Got requests')
                this.requests = response.data
                this.exists = this.requests.filter(x => x.plant_name == this.pname)
                
                if (this.exists.length == 0) {
                 getAPI.post('/requests/', {plant_name: this.pname})
                .then(response => {
                    console.log('Request posted to plants api')
                    this.getAPI = response.data
                    this.message = 'Plant has been requested'
                    this.pname = ''
                })
                .catch(err => {
                    console.log(err)
                })
                }
                else {
                    this.message = 'Plant has already been requested, check back soon.'
                }
            })
            .catch(err => {
                console.log(err)
            })
        }
    } 
}
</script>