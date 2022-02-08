<template>
    <div class="Example">
        <h2>Component mounted successfully!</h2>
    </div>
</template>



<script>
// import statements go here
export default {
    name: "", // name of component for use in vue devtools
    components: {
        // register any vue or javascript object here
    },
    props: {
        // define objects passed from the parent component
    },
    data: function() {
    return {
        // define objects for use in this component
    }
    },
    mounted() {
    // trigger functions or logic to be executed when the component is mounted for the user to see
    },
    methods: {
    // define methods to be used in this component
    },
    watch: {
    // define logic to be triggered when a variable or object changes
    }
}