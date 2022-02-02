<template>
  <div>
    <!-- Table is: 
            striped, 
            has mouse over hover, 
            items are binded to "items" in the js script
            fields are binded to "fields" in the js script   
    -->
    <b-table striped hover :items="items" :fields="fields"></b-table>
  </div>
</template>

<script>
// Vue exports a object, by default the object is called "default"
  export default {
    // data is a predefined function that returns a object for the templat to use
    data() {
        // Vue 
      return {
        // Note 'isActive' is left out and will not appear in the rendered table
        fields: [
          {
            key: 'last_name',
            sortable: true
          },
          {
            key: 'first_name',
            sortable: false
          },
          {
            key: 'age',
            label: 'Person age',
            sortable: true,
            // Variant applies to the whole column, including the header and footer
            variant: 'danger'
          }
        ],
        items: [
          { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
      }
    }
  }
</script>

<style lang="scss" scoped>
  div.solid {border-style: solid;}
</style>>

