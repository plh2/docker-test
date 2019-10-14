<template lang="pug">
  .container 
    .row.left left {{message}}
      el-button click me
    .row.middle middle
    .row.right 
      .person(:key="item.id" v-for="item in onlineList") {{item.name}}

</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

@Component({})
export default class MyComponent extends Vue {
  message: string = "Hello!";
  public onlineList: object[] = [
    { name: "peng", id: "1" },
    { name: "heng", id: "2" },
    { name: "ling", id: "3" },
    { name: "bing", id: "4" }
  ];

  mounted() {
    io = window.io;
    var socket = io.connect("http://" + document.domain + ":" + 5000);
    socket.on("connect", (data) => {
      socket.emit('join', {data: 'I\'m connected!'});
    });
    socket.on("my response", msg => {
      if (msg.data) {
        this.$message({
          type: "success",
          showClose: true,
          message: msg.data
        });
      }
      if (typeof msg.user_name !== "undefined") {
        debugger;
      }
    });
  }
}
</script>

<style lang="scss" scoped>
.container {
  color: red;
  display: flex;
  flex-direction: row;
  height: 100%;
  .row {
    flex: 1;
  }
}
</style>