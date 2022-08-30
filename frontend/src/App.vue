<template>
  <div id="app">
    <DeleteModal
      :openModal="this.openDeleteModal"
      :category="this.categoryToDelete"
      @close-modal="closeDeleteModalHandler"
      @delete-category="deleteCategoryHandler"
    />
    <CategoryModal
      :openModal="this.openCategoryModal"
      @close-modal="closeCategoryModalHandler"
      :existingCategory="this.editedCategory"
      @save-category="saveCategoryHandler"
    />
    <NoteModal
      :openModal="this.openNoteModal"
      @close-modal="closeNoteModalHandler"
    />
    <div :class="{ inactive: openCategoryModal || openNoteModal }">
      <HeaderComponent
        :categories="this.categories"
        @new-category="openCategoryModalHandler"
        @new-note="newNoteHandler"
        @category-selected="updateNotes"
        :remove-selected-category="this.removeSelectedCategory"
      />
      <ListComponent
        :notes="this.notes"
        :category="this.choosenCategory"
        @note-selected="fetchNote"
        @edit-category="openCategoryModalHandler"
        @delete-category="openDeleteModalCategory"
      />
      <DetailsComponent :note="this.choosenNote" />
    </div>
  </div>
</template>

<script>
import { graphql } from "./main";
import HeaderComponent from "./components/HeaderComponent.vue";
import ListComponent from "./components/ListComponent.vue";
import DetailsComponent from "./components/DetailsComponent.vue";
import CategoryModal from "./components/CategoryModal.vue";
import NoteModal from "./components/NoteModal.vue";
import DeleteModal from "./components/DeleteModal.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    ListComponent,
    DetailsComponent,
    CategoryModal,
    NoteModal,
    DeleteModal,
  },
  data() {
    return {
      openCategoryModal: false,
      openNoteModal: false,
      openDeleteModal: false,
      categories: [],
      notes: [],
      choosenCategory: null,
      choosenNote: null,
      editedCategory: null,
      categoryToDelete: null,
      removeSelectedCategory: false,
    };
  },
  methods: {
    openCategoryModalHandler(category) {
      if (category) {
        this.editedCategory = category;
      }
      this.openCategoryModal = true;
    },
    openDeleteModalCategory(category) {
      this.categoryToDelete = category;
      this.openDeleteModal = true;
    },
    newNoteHandler() {
      this.openNoteModal = true;
    },
    closeDeleteModalHandler() {
      this.openDeleteModal = false;
      this.categoryToDelete = null;
    },
    closeCategoryModalHandler() {
      this.openCategoryModal = false;
      this.editedCategory = null;
    },
    closeNoteModalHandler() {
      this.openNoteModal = false;
    },
    saveCategoryHandler(category) {
      this.openCategoryModal = false;
      this.editedCategory = null;
      if (category.id) {
        graphql(
          `mutation { updateCategory(id: "${category.id}", name: "${category.name}") { category { id, name } } }`
        ).then((data) => {
          let updatedCategory = data.data.updateCategory.category;
          let categoryToUpdate = this.categories.find(
            (cat) => cat.id === updatedCategory.id
          );
          categoryToUpdate.name = updatedCategory.name;
        });
      } else {
        graphql(
          `mutation { createCategory(name: "${category.name}") { category { id, name } } }`
        ).then((data) =>
          this.categories.push(data.data.createCategory.category)
        );
      }
    },
    deleteCategoryHandler(category) {
      this.openDeleteModal = false;
      this.categoryToDelete = null;
      this.choosenCategory = null;
      graphql(
        `mutation { deleteCategory(id: "${category.id}") { id, ok } }`
      ).then(() => {
        const categoryToDelete = this.categories.findIndex((cat) => {
          return cat.id === category.id;
        });
        this.categories.splice(categoryToDelete, 1);
        this.removeSelectedCategory = true;
      });
    },
    updateNotes(event) {
      if (event) {
        this.notes = event.notes;
        this.choosenCategory = event;
        this.removeSelectedCategory = false;
      } else {
        this.notes = [];
        this.choosenCategory = null;
        this.removeSelectedCategory = false;
      }
    },
    fetchNote(id) {
      graphql(`query {noteById (id:${id}) { id, title, text, status} }`).then(
        (data) => (this.choosenNote = data.data.noteById)
      );
    },
  },
  mounted() {
    graphql(`
    query { allCategories { id, name, notes {id, title} } }`).then(
      (data) => (this.categories = data.data.allCategories)
    );
  },
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  background-color: rgb(200, 200, 200);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.inactive {
  opacity: 0.5;
  pointer-events: none;
}

.button-container {
  text-align: left;
}

@media only screen and (max-width: 1360px) {
  .button-container {
    text-align: center;
  }
}

.edit-button {
  background-color: rgb(252, 247, 71);
  border: none;
  border-radius: 5px;
  color: rgb(52, 97, 235);
  padding: 15px 32px;
  margin: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition: 0.3s;
  width: 180px;
}

.edit-button:hover {
  background-color: rgb(207, 202, 54);
  cursor: pointer;
  transform: scale(1.1);
}

.delete-button {
  background-color: rgb(237, 103, 26);
  border: none;
  border-radius: 5px;
  color: #ffffff;
  padding: 15px 32px;
  margin: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition: 0.3s;
  width: 180px;
}

.delete-button:hover {
  background-color: rgb(191, 83, 21);
  cursor: pointer;
  transform: scale(1.1);
}

label {
  display: inline;
  margin-right: 20px;
  font-size: 20px;
}

.editor-container {
  text-align: center;
}

input {
  display: inline;
  font-size: 20px;
  width: 80%;
  padding: 5px 15px;
  border-radius: 5px;
  border: 2px solid rgb(52, 97, 235);
  color: rgb(52, 97, 235);
}

input.middle:focus {
  outline-width: 0;
}
</style>
