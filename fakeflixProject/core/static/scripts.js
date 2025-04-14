document.addEventListener("DOMContentLoaded", function () {
  search_button = document.getElementById("search-button");
  search_input = document.getElementById("hidden-input");
  top_container = document.getElementById("top-container");

  // Function to handle screen size changes
  function handleScreenSize() {
    if (window.matchMedia("(max-width: 500px)").matches) {
      // Mobile behavior - always show
      search_input.classList.add("show");
      search_input.removeAttribute("disabled");
    } else {
      // Desktop behavior - hide by default (hover will show)
      search_input.classList.remove("show");
    }
  }

  // Initial check
  handleScreenSize();

  // Add resize listener to update dynamically
  window.addEventListener("resize", handleScreenSize);

  // Hover behaviors (only relevant for desktop)
  if (!window.matchMedia("(max-width: 500px)").matches) {
    search_button.addEventListener("mouseover", function () {
      search_input.classList.add("show");
      search_input.removeAttribute("disabled");
    });

    search_button.addEventListener("mouseleave", function () {
      search_input.classList.remove("show");
    });

    search_input.addEventListener("mouseover", function () {
      search_input.classList.add("show");
      search_input.removeAttribute("disabled");
    });

    search_input.addEventListener("mouseleave", function () {
      search_input.classList.remove("show");
    });
  }
});
