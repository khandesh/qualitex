const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("menu");

if (menuBtn && menu) {
  menuBtn.addEventListener("click", () => {
    menu.classList.toggle("open");
  });
}

// Navbar scroll effect
const navbar = document.querySelector(".navbar");
if (navbar) {
  window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 20);
  }, { passive: true });
}

// Slideshow logic
const slideshows = new Map();

function showSlide(id, nextIndex) {
  const slideshow = slideshows.get(id);
  if (!slideshow || slideshow.slides.length === 0) return;

  slideshow.index = (nextIndex + slideshow.slides.length) % slideshow.slides.length;
  slideshow.slides.forEach((slide, index) => {
    slide.classList.toggle("active", index === slideshow.index);
  });
}

function startSlideshow(id) {
  const slideshow = slideshows.get(id);
  if (!slideshow || slideshow.slides.length <= 1) return;

  window.clearInterval(slideshow.timer);
  slideshow.timer = window.setInterval(() => {
    showSlide(id, slideshow.index + 1);
  }, slideshow.delay);
}

function moveSlide(id, direction) {
  showSlide(id, (slideshows.get(id)?.index || 0) + direction);
  startSlideshow(id);
}

document.addEventListener("DOMContentLoaded", () => {
  const whatsappForm = document.getElementById("whatsappForm");

  if (whatsappForm) {
    whatsappForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const formData = new FormData(whatsappForm);
      const message = [
        "New testing enquiry from Qualitex website",
        "",
        `Name: ${formData.get("name") || ""}`,
        `Contact: ${formData.get("contact") || ""}`,
        `Email: ${formData.get("email") || ""}`,
        "",
        "Message:",
        formData.get("message") || "",
      ].join("\n");
      const whatsappNumber = whatsappForm.dataset.whatsappNumber || "918956699841";
      const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;

      window.open(whatsappUrl, "_blank", "noopener");
    });
  }

  document.querySelectorAll(".slideshow").forEach((container) => {
    const slides = Array.from(container.querySelectorAll(".slide"));
    const delay = Number(container.dataset.autoplay) || 4500;
    slideshows.set(container.id, { slides, index: 0, timer: null, delay });
    showSlide(container.id, 0);
    startSlideshow(container.id);
  });

  document.querySelectorAll("[data-slide-prev]").forEach((button) => {
    button.addEventListener("click", () => moveSlide(button.dataset.slidePrev, -1));
  });

  document.querySelectorAll("[data-slide-next]").forEach((button) => {
    button.addEventListener("click", () => moveSlide(button.dataset.slideNext, 1));
  });
});
