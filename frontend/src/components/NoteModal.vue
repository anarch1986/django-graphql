<template>
  <div class="modal" :class="{ 'show-modal': openModal, 'hide-modal': !openModal }">
    <!-- Modal content -->
    <div class="modal-content">
      <span class="close" @click="$emit('close-modal')">&times;</span>
      <h3>Note Modal</h3>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    openModal: Boolean,
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 1;
  left: 50%;
  top: 25%;
  transform: translate(-50%);
  width: 70%;
  height: 100%;
  overflow: auto;
}

@media only screen and (max-width: 1200px) {
  .modal {
    width: 90%;
  }
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

.show-modal {
  display: block;
}

.hide-modal {
  display: none;
}

.close {
  color: rgb(52, 97, 235);
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: rgb(0, 46, 185);;
  text-decoration: none;
  cursor: pointer;
}
</style>
