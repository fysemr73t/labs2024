const canvas = document.getElementById("spinCanvas");
const context = canvas.getContext("2d");

const squareSize = 50;
let angle = 0;

// Rotate 1 RPM (360 degrees per minute)
const rotationSpeed = (2 * Math.PI) / 10; // radians per second

function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Save context state
    context.save();

    // Move the origin to the center of the canvas
    context.translate(canvas.width / 2, canvas.height / 2);

    // Rotate the square
    context.rotate(angle);

    // Draw the square centered at the origin
    context.fillStyle = "blue";
    context.fillRect(-squareSize / 2, -squareSize / 2, squareSize, squareSize);

    // Restore the context state
    context.restore();

    // Update the angle
    angle += rotationSpeed / 60;

    // Request next frame
    requestAnimationFrame(draw);
}

// Start animation
draw();
