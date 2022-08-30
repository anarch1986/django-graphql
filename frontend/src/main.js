import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;

export const eventBus = new Vue();

export async function graphql(data) {
  try {
    let response = await fetch("http://localhost:8000/graphql", {
      method: "POST",
      headers: { "Content-Type": "application/json", accesstoken: "testtoken" },
      body: JSON.stringify({
        query: data,
      }),
    });
    if (response.status >= 400 && response.status < 600) {
      alert(
        "Bad response from server: " +
          response.status +
          " " +
          response.statusText
      );
    }
    response = await response.json();
    if ("errors" in response) {
      let errorMessages = "";
      for (const error of response.errors) {
        errorMessages += error.message + "; ";
      }
      alert(errorMessages);
    } else {
      return response;
    }
  } catch (error) {
    alert(error);
  }
}

new Vue({
  render: (h) => h(App),
}).$mount("#app");
