<template>
    <div>
        <h3>My Profile</h3>
        <h4>{{$route.params.id}}</h4>
        <router-link :to="{name: 'Profile', params: {id: 456}}">Another route</router-link>
    </div>
</template>

<script>
export default 
{
    mounted(){
        console.log(this.$route.params.id); // Prints out parameters in the console
    },
    watch: {
        $route(to, from){
            console.log("to", to);
            console.log("from", from);
        }
    }
}
</script>

<style scoped>

</style>