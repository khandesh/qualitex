const ejs = require('ejs');
const fs = require('fs');
const path = require('path');

const viewsDir = path.join(__dirname, 'views');
const outDir = path.join(__dirname, 'public');

// Data (copied from server.js)
const featuredServices = [
  "Pile & Foundation Testing",
  "Advanced NDT Testing",
  "Concrete Mix Design",
  "Concrete Durability",
  "Equipment Calibration",
  "Soil & Geotechnical Testing",
  "Mechanical & Steel Testing",
  "Building Material Testing"
];

const serviceCategories = [
  {
    title: "Pile & Foundation Testing",
    summary: "Comprehensive assessment of deep foundations using advanced techniques like Pile Integrity, Dynamic Load, and Cyclic testing.",
    tests: ["Pile Integrity Test", "Pile Dynamic Test", "Pile Lateral Load Test", "Pile Pull Out Test"]
  },
  {
    title: "Advanced Non-Destructive Testing",
    summary: "Structure-friendly checks for assessing in-situ concrete and reinforcement condition with high precision.",
    tests: ["Ultrasonic pulse velocity testing", "Rebound hammer testing", "Half-cell potential assessment", "Carbonation depth test"]
  },
  {
    title: "Concrete Mix Design",
    summary: "Specialized mix designs for strength, durability, and special applications like Self-Compacting Concrete.",
    tests: ["Normal Concrete Mix Design", "High Performance Concrete Mix", "Self-Compacting Concrete Mix", "PQC Mix"]
  },
  {
    title: "Equipment Calibration",
    summary: "Accurate, well-calibrated equipment is crucial for reliable and precise measurements. We provide full calibration services.",
    tests: ["Force Calibration", "Weighing Balance", "Basic Dimension", "Pressure Calibration"]
  },
  {
    title: "Mechanical & Steel Testing",
    summary: "Physical and chemical testing for steel, structural steel, couplers, coatings, and reinforcement materials.",
    tests: ["Steel physical testing", "Structural steel testing", "Coupler bar / splice bar testing", "Zinc coating and grade confirmation"]
  },
  {
    title: "Soil & Geotechnical Testing",
    summary: "Soil, murum, rock, and foundation-support testing for site investigation and earthwork control.",
    tests: ["Soil and murum physical testing", "Soil chemical testing", "On-site soil testing", "Bearing capacity, compaction, permeability support"]
  },
  {
    title: "Aggregate Testing",
    summary: "Fine and coarse aggregate checks for concrete, roadwork, and infrastructure applications.",
    tests: ["Fine aggregate physical testing", "Coarse aggregate physical testing", "Coarse and fine aggregate chemical testing"]
  },
  {
    title: "Building Material & Chemical Testing",
    summary: "Construction material testing for cement, fly ash, admixture, water, GGBS, silica fume, mortar, gypsum, and POP.",
    tests: ["Hydraulic cement physical and chemical testing", "Fly ash, GGBS and micro silica testing", "Construction and drinking water testing", "Mortar, gypsum, POP and admixture testing"]
  }
];

const accreditedParameters = [
  { category: "Bitumen", tests: "Fire Point, Flash Point, Specific Gravity, Penetration, Softening Point", standard: "IS 1202, IS 1203, IS 1205, IS 1209" },
  { category: "Bituminous Mix", tests: "Binder Content, Marshall Stability", standard: "ASTM D2172, ASTM D6927" },
  { category: "Aggregates", tests: "Sieve Analysis, Impact Value, Crushing Value, Water Absorption", standard: "IS 2386 (Part 1, 3, 4)" },
  { category: "Concrete", tests: "Fresh Slump, Density, Cube/Core Compressive Strength", standard: "IS 1199, IS 516" },
  { category: "Cement", tests: "Fineness, Setting Time, Soundness, Strength, Consistency", standard: "IS 4031" },
  { category: "Soil & Rock", tests: "CBR, Atterberg Limits, Compaction, UCS, Porosity", standard: "IS 2720, IS 9143, IS 13030" },
];

const capabilityHighlights = [
  { label: "NABL Accredited", value: "ISO/IEC 17025:2017" },
  { label: "Certificate", value: "TC-16872" },
  { label: "Scope", value: "Civil engineering materials" },
  { label: "Support", value: "Lab + on-site collection" }
];

const certificateExtracts = [
  { label: "Accreditation standard", value: "ISO/IEC 17025:2017" },
  { label: "Certificate number", value: "TC-16872" },
  { label: "Issued on", value: "03/10/2025" },
  { label: "Valid until", value: "02/10/2029" },
  { label: "Laboratory", value: "Qualitex Test House Chhatrapati Sambhajinagar Pvt. Ltd." },
  { label: "Location", value: "Gut No. 162, Plot No. N-9, Chikalthana, Chhatrapati Sambhajinagar, Maharashtra" }
];

const certificateScopeExtracts = [
  "Pile, Foundation and NDT testing",
  "Bitumen and bituminous mix testing",
  "Concrete, cement, and aggregate testing",
  "Soil, rock, and geotechnical investigation",
  "Building material, chemical, and water testing",
  "On-site sampling and field testing support"
];

// Dynamically load images
const imagesDir = path.join(__dirname, "public", "images");
let imageFiles = [];
try {
  imageFiles = fs.readdirSync(imagesDir).filter(f => f.match(/\.(webp|jpg|jpeg|png)$/i));
} catch (error) {
  console.error("Error reading images directory:", error);
}

const naturalSort = (a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" });
const getImagePrefix = (fileName) => {
  const match = fileName.match(/^([a-zA-Z]+)(?=\d)/);
  if (!match) return "gallery";
  return match[1].replace(/s$/, "").toLowerCase();
};

const imageCategories = imageFiles.reduce((groups, file) => {
  const prefix = getImagePrefix(file);
  groups[prefix] = groups[prefix] || [];
  groups[prefix].push(file);
  return groups;
}, {});

Object.keys(imageCategories).forEach((key) => {
  imageCategories[key].sort(naturalSort);
});

const equipmentImages = imageCategories.equipment || [];
const inlabImages = imageCategories.inlab || [];
const onsiteImages = imageCategories.onsite || [];

const getRandomImages = (arr, num) => {
  const shuffled = [...arr].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, num);
};

const getCategorySlideCount = (images) => {
  if (images.length <= 2) return images.length;
  return 2 + Math.floor(Math.random() * 2);
};

const getMixedSlideshowImages = () => Object.values(imageCategories)
  .flatMap((images) => getRandomImages(images, getCategorySlideCount(images)))
  .sort(() => 0.5 - Math.random());

const baseData = {
  labName: "Qualitex Test House Chhatrapati Sambhajinagar Pvt. Ltd.",
  certificateNumber: "TC-16872",
  issueDate: "03/10/2025",
  validUntil: "02/10/2029",
  location: "Gut No. 162, Plot No. N-9, Chikalthana, Chhatrapati Sambhajinagar, Maharashtra",
  whatsappNumber: "+91 9657126633"
};

// Pages to render
const pages = [
  {
    template: 'home.ejs',
    output: 'index.html',
    data: { 
      pageTitle: "Home", 
      featuredServices, 
      serviceCategories,
      capabilityHighlights,
      certificateExtracts,
      certificateScopeExtracts,
      mixedSlideshowImages: getMixedSlideshowImages(),
      equipmentImages,
      inlabImages,
      onsiteImages 
    }
  },
  {
    template: 'about.ejs',
    output: 'about.html',
    data: { pageTitle: "About" }
  },
  {
    template: 'services.ejs',
    output: 'services.html',
    data: { pageTitle: "Services", accreditedParameters, featuredServices, serviceCategories }
  },
  {
    template: 'accreditation.ejs',
    output: 'accreditation.html',
    data: { pageTitle: "Accreditation", accreditedParameters, galleryImages: equipmentImages.slice(0, 8), capabilityHighlights, certificateExtracts, certificateScopeExtracts }
  },
  {
    template: 'contact.ejs',
    output: 'contact.html',
    data: { pageTitle: "Contact", sent: false }
  }
];

if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

pages.forEach(page => {
  const templatePath = path.join(viewsDir, page.template);
  const outputPath = path.join(outDir, page.output);
  
  const mergedData = { ...baseData, ...page.data };
  
  ejs.renderFile(templatePath, mergedData, (err, str) => {
    if (err) {
      console.error(`Error rendering ${page.template}:`, err);
    } else {
      fs.writeFileSync(outputPath, str);
      console.log(`Generated ${page.output}`);
    }
  });
});
