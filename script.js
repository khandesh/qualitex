const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");
const enquiryForm = document.getElementById("enquiryForm");
const formNote = document.getElementById("formNote");

if (menuToggle && navLinks) {
  menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("open");
  });
}

if (enquiryForm && formNote) {
  enquiryForm.addEventListener("submit", (event) => {
    event.preventDefault();
    formNote.textContent =
      "Thank you. Your enquiry is captured. We will contact you shortly.";
    enquiryForm.reset();
  });
}
