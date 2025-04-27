document.addEventListener('DOMContentLoaded', function() {
    const textContent = document.getElementById('textContent');
    const increaseBtn = document.getElementById('increaseBtn');
    const decreaseBtn = document.getElementById('decreaseBtn');
    const currentSizeDisplay = document.getElementById('currentSize');
    
    let currentSize = 16;
    const minSize = 12;
    const maxSize = 24;
    const step = 2;
    
function updateTextSize() {
        textContent.style.fontSize = currentSize + 'px';
        currentSizeDisplay.textContent = currentSize;
        
        increaseBtn.disabled = currentSize >= maxSize;
        decreaseBtn.disabled = currentSize <= minSize;
        
        if (increaseBtn.disabled) {
            increaseBtn.style.opacity = '0.6';
            increaseBtn.style.cursor = 'not-allowed';
        } else {
            increaseBtn.style.opacity = '1';
            increaseBtn.style.cursor = 'pointer';
        }
        
        if (decreaseBtn.disabled) {
            decreaseBtn.style.opacity = '0.6';
            decreaseBtn.style.cursor = 'not-allowed';
        } else {
            decreaseBtn.style.opacity = '1';
            decreaseBtn.style.cursor = 'pointer';
        }
    }
    
    increaseBtn.addEventListener('click', function() {
        if (currentSize < maxSize) {
            currentSize = Math.min(currentSize + step, maxSize);
            updateTextSize();
        }
    });
    
    decreaseBtn.addEventListener('click', function() {
        if (currentSize > minSize) {
            currentSize = Math.max(currentSize - step, minSize);
            updateTextSize();
        }
    });
    
    document.addEventListener('keydown', function(e) {
        if (e.key === '+' || e.key === '=') {
            if (currentSize < maxSize) {
                currentSize = Math.min(currentSize + step, maxSize);
                updateTextSize();
            }
            e.preventDefault();
        } else if (e.key === '-' || e.key === '_') {
            if (currentSize > minSize) {
                currentSize = Math.max(currentSize - step, minSize);
                updateTextSize();
            }
            e.preventDefault();
        }
    });
    
    updateTextSize();
});
