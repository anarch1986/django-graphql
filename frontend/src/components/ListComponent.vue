<template>
  <div class="data-list">
    <h3 v-if="category">List of Notes for {{ category.name }}</h3>
    <h3 v-else>Select a Category</h3>
    <div class="data-list-outer">
      <div class="data-list-inner">
        <ul>
          <li
            v-for="note in notes"
            :key="note.id"
            @click="$emit('note-selected', note.id)"
          >
            {{ note.title }}
          </li>
        </ul>
      </div>
      <div v-if="category" class="button-container">
        <button class="edit-button" @click="$emit('edit-category', category)">Edit Category</button>
        <button class="delete-button" @click="$emit('delete-category', category)">Delete Category</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    notes: [],
    category: { },
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.data-list {
  float: left;
  width: 50%;
  color: rgb(52, 97, 235);
}

.data-list-outer {
  margin: 0 auto;
  padding: 10px 20px;
  border: 2px solid rgb(52, 97, 235);
  border-radius: 5px;
  width: 50%;
  min-height: 50vh;
}

.data-list-inner {
  min-height: 40vh;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  border: none;
  border-radius: 5px;
  background-color: #ffffff;
  margin: 10px;
  padding: 10px;
  transition: 0.3s;
  font-size: 20px;
  cursor: pointer;
}

li:hover {
  transform: scale(1.075);
}

@media only screen and (max-width: 860px) {
  .data-list {
    width: 100%;
    float: none;
  }

  .data-list-outer {
    min-width: 75%;
    min-height: auto;
  }
}

.button-container {
  text-align: center;
  margin-top: 20px;
}
</style>
