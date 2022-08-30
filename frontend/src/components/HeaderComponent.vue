<template>
  <div class="header">
    <div class="header-select">
      <Multiselect
        v-model="value"
        :options="this.categories"
        placeholder="Select category"
        label="name"
        track-by="id"
        :searchable="false"
      ></Multiselect>
    </div>
    <div class="header-element-list">
      <button
        class="header-element header-button"
        @click="$emit('new-category')"
      >
        Add new Category
      </button>
      <button class="header-element header-button" @click="$emit('new-note')">
        Add new Note
      </button>
    </div>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";

export default {
  components: { Multiselect },
  props: {
    categories: [],
    removeSelectedCategory: Boolean,
  },
  data() {
    return {
      value: null,
    };
  },
  watch: {
    value(newValue) {
      this.$emit("category-selected", newValue);
    },
    removeSelectedCategory(newValue) {
      if (newValue === true) {
        this.value = null;
      }
    },
  },
};
</script>

<style scoped>
.header {
  background-color: rgb(52, 97, 235);
  vertical-align: middle;
  text-align: left;
  padding: 15px 10px;
  width: 100%;
  height: 50px;
}
.header-select {
  position: absolute;
  top: 20;
  margin-left: 20px;
  margin-top: 5px;
  width: 240px;
}
.header-element-list {
  margin-left: 270px;
}
.header-element {
  margin: 0 15px;
  display: inline-block;
}

@media only screen and (max-width: 912px) {
  .header {
    text-align: center;
    height: 100%;
  }
  .header-element {
    margin: 15px auto;
    display: block;
  }
  .header-element-list {
    margin: 0 auto;
    text-align: center;
  }
  .header-select {
    float: none;
    margin: 15px auto;
    position: relative;
    width: 250px;
  }

  .header-button {
    width: 250px !important;
  }
}

.header-element:hover {
  background-color: rgb(207, 202, 54);
  cursor: pointer;
  transform: scale(1.1);
}

.header-button {
  background-color: rgb(252, 247, 71);
  width: 200px;
  border: none;
  border-radius: 5px;
  color: rgb(52, 97, 235);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  transition: 0.3s;
}

.hide-it {
  display: none;
}
</style>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
.multiselect__placeholder {
  color: rgb(52, 97, 235);
  opacity: 0.5;
}
.multiselect__tags {
  color: rgb(52, 97, 235);
}
.multiselect__option {
  color: rgb(52, 97, 235);
}
.multiselect__option--highlight {
  background: rgb(252, 247, 71);
  color: rgb(52, 97, 235);
}
.multiselect__option--selected {
  background: rgb(200, 200, 200);
  color: rgb(52, 97, 235);
}
.multiselect__option--selected.multiselect__option--highlight {
  background: rgb(237, 103, 26);
  color: #fff;
}

.multiselect__option--highlight:after {
  content: attr(data-select);
  background: rgb(252, 247, 71);
  color: rgb(52, 97, 235);
}

.multiselect__option--selected.multiselect__option--highlight:after {
  background: rgb(237, 103, 26);
  color: #fff;
}

.multiselect__option--selected.multiselect__option:after {
  background: rgb(200, 200, 200);
  color: rgb(52, 97, 235);
}

.multiselect__option.multiselect__option--highlight.multiselect__option--selected:after {
  background: rgb(237, 103, 26);
  color: #fff;
}
</style>
