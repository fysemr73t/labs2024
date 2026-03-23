function makeContentFallAndFade() {
  console.log("Starting text fall and image fade...");

  // Recursive function to walk the DOM and process text nodes
  function walkDOM(node) {
    // If it's a text node and contains non-whitespace content
    if (node.nodeType === Node.TEXT_NODE && node.nodeValue.trim()) {
      // Wrap the text in a span for animation
      const span = document.createElement("span");
      span.textContent = node.nodeValue.trim();
      span.style.position = "absolute";
      span.style.transition = "transform 2s linear";
      span.style.transform = "translateY(0px)"; // Initial position

      // Replace the text node with the span
      const parent = node.parentNode;
      parent.replaceChild(span, node);

      // Start the falling animation
      setTimeout(() => {
        span.style.transform = `translateY(${window.innerHeight}px)`; // Move off the screen
      }, Math.random() * 500); // Small random delay for variety

      return; // Stop further recursion for this node
    }

    // If it's an element node, recursively process its children
    if (node.nodeType === Node.ELEMENT_NODE) {
      Array.from(node.childNodes).forEach(walkDOM);
    }
  }

  // Process all <img> tags for fade-to-black effect
  function fadeImages() {
    document.querySelectorAll("img").forEach((img) => {
      img.style.transition = "filter 2s linear"; // Smooth fade effect
      img.style.filter = "brightness(0)"; // Fade to black
    });
  }

  // Start walking the DOM from the <body> element
  walkDOM(document.body);

  // Start fading images
  fadeImages();

  console.log("Text fall and image fade animation applied.");
}

// Trigger the effect
makeContentFallAndFade();
