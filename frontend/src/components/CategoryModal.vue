<template>
  <div
    class="modal"
    :class="{ 'show-modal': openModal, 'hide-modal': !openModal }"
  >
    <!-- Modal content -->
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h3 v-if="existingCategory && this.category">
        Edit {{ this.existingCategory.name }}
      </h3>
      <h3 v-else>Add new Category</h3>
      <div class="editor-container">
        <label for="category-name"><b>Name</b></label>
        <input id="category-name" v-model="category.name" />
      </div>
      <div class="button-container">
        <button class="edit-button" @click="saveCategory">Save</button>
        <button class="delete-button" @click="closeModal">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    openModal: Boolean,
    existingCategory: null,
  },
  data() {
    return {
      category: {
        name: "",
      },
    };
  },
  methods: {
    saveCategory() {
      if (this.category.name) {
        this.$emit("save-category", this.category);
        this.category = { name: "" };
      }
    },
    closeModal() {
      this.category = { name: "" };
      this.$emit("close-modal");
    },
  },
  watch: {
    openModal() {
      if (this.existingCategory) {
        this.category = { id: this.existingCategory.id, name: this.existingCategory.name };
      }
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 1;
  left: 50%;
  top: 5%;
  transform: translate(-50%);
  width: 50%;
  height: 100%;
  overflow: auto;
}

@media only screen and (max-width: 1200px) {
  .modal {
    width: 90%;
  }
}

.show-modal {
  display: block;
}

.hide-modal {
  display: none;
}

.modal-content {
  background-color: #ffffff;
  color: rgb(52, 97, 235);
  margin: 15% auto;
  padding: 20px;
  border: 2px solid rgb(52, 97, 235);
  border-radius: 5px;
  width: 80%;
}

.close {
  color: rgb(52, 97, 235);
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: rgb(0, 46, 185);
  text-decoration: none;
  cursor: pointer;
}

h3 {
  font-size: 24px;
}

.button-container {
  margin-top: 20px;
  text-align: center;
}
</style>
