<template>
  <div
    class="modal"
    :class="{ 'show-modal': openModal, 'hide-modal': !openModal }"
  >
    <!-- Modal content -->
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h3>
        Are you sure you want to delete
        {{
          category ? category.name : note ? note.name : " "
        }}?
      </h3>
      <div class="button-container">
        <button class="delete-button" @click="deleteCategory">Yes</button>
        <button class="edit-button" @click="closeModal">No</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    openModal: Boolean,
    category: null,
    note: null,
  },
  data() {
    return {};
  },
  methods: {
    deleteCategory() {
      if (this.category.name) {
        this.$emit("delete-category", this.category);
      }
    },
    deleteNote() {
	console.log()
      this.$emit("delete-note", this.note);
    },
    closeModal() {
      this.$emit("close-modal");
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
