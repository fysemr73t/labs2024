const canvas = document.getElementById("spinCanvas");
const context = canvas.getContext("2d");

const squareSize = 50;
let angle = 0;
const rotationSpeed = (2 * Math.PI) / 3; // 1 RPM in radians per second

// Variables to calculate refresh rate
let frames = 0;
let startTime = performance.now();
let refreshRate = 0;

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

    // Update the angle for rotation
    angle += rotationSpeed / 60;

    // Calculate frames per second (refresh rate)
    frames++;
    const currentTime = performance.now();
    const elapsed = currentTime - startTime;

    if (elapsed >= 1000) { // One second has passed
        refreshRate = Math.round(frames / (elapsed / 1000)); // Calculate refresh rate in Hz
        frames = 0;
        startTime = currentTime;
    }

    // Display refresh rate on the canvas
    context.font = "16px Arial";
    context.fillStyle = "black";
    context.fillText(`Refresh Rate: ${refreshRate} Hz`, 10, 20);

    // Request the next frame
    requestAnimationFrame(draw);
}

// Start animation
draw();
