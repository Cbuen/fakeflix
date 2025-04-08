document.addEventListener("DOMContentLoaded", function () {
  search_button = document.getElementById("search-button");
  search_input = document.getElementById("hidden-input");
  top_container = document.getElementById("top-container");

  search_button.addEventListener("mouseover", function () {
    search_input.classList.add("show");
    search_input.removeAttribute("disabled");
  });

  // user enters back main container
  top_container.addEventListener("mouseover", function () {
    search_input.classList.remove("show");
  });
});
