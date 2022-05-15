<template>
    <div>
        <b-card :title="title">
            <slot></slot>
        </b-card>
    </div>
</template>

<script>

export default {
    props: ['title'],
    data: function() {
        return {
        }
    }

}

</script>

<style scoped>
    .card {
        height: 400px;
        margin-bottom: 20px;
    }
</style>