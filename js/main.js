const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("menu");

if (menuBtn && menu) {
  menuBtn.addEventListener("click", () => {
    menu.classList.toggle("open");
  });
}

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
