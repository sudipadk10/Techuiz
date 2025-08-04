document.addEventListener("DOMContentLoaded", function () {
    const profileBtn = document.getElementById("user-menu-button");
    const dropdown = document.getElementById("user-dropdown");
    const menuToggle = document.getElementById("menu-toggle");
    const mobileNav = document.getElementById("mobile-nav");

    if (profileBtn) {
      profileBtn.addEventListener("click", () => {
        dropdown.classList.toggle("hidden");
      });
    }

    if (menuToggle) {
      menuToggle.addEventListener("click", () => {
        mobileNav.classList.toggle("hidden");
      });
    }

    // Optional: Close dropdown if clicked outside
    document.addEventListener("click", function (e) {
      if (!profileBtn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.add("hidden");
      }
    });
  });
  