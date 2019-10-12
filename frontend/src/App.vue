<template lang="pug">
  .container 
    .left left {{message}}
      button(@click="greet") {click me}
    .middle middle
    .right right

</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component({})
export default class MyComponent extends Vue {
  message: string = "Hello!";

  // method
  greet() {
    alert("greeting: " + this.message);
  }
}
</script>

<style lang="scss" scoped>
.container {
  color: red;
}
</style>