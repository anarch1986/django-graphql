<template>
  <div class="details">
    <h3 v-if="note">{{ note.title }}</h3>
    <h3 v-else>Select a Note</h3>
    <div class="details-outer">
      <div class="details-inner">
        <div v-for="(value, key) in note" :key="key" class="detail-line">
          <b>{{ key.toUpperCase() }}: </b>{{ value }}
        </div>
      </div>
      <div class="button-container" v-if="note">
        <button class="edit-button">Edit Note</button>
        <button class="delete-button">Delete Note</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    note: null,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.details {
  float: right;
  width: 50%;
  color: rgb(52, 97, 235);
}

.details-outer {
  margin: 0 auto;
  padding: 10px 20px;
  border: 2px solid rgb(52, 97, 235);
  border-radius: 5px;
  width: 50%;
  min-height: 50vh;
}

@media only screen and (max-width: 860px) {
  .details {
    width: 100%;
    min-height: auto;
    float: none;
  }

  .details-outer {
    width: 75%;
  }
}
.details-inner {
  border: none;
  border-radius: 5px;
  background-color: #ffffff;
  margin: 10px 0;
  padding: 10px 20px;
  transition: 0.3s;
  font-size: 20px;
  text-align: left;
  min-height: 40vh;
}

.detail-line {
  padding: 3px 0;
}
</style>
