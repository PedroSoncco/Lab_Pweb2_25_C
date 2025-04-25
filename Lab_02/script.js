document.addEventListener('DOMContentLoaded', function() {
    const textContent = document.getElementById('textContent');
    const increaseBtn = document.getElementById('increaseBtn');
    const decreaseBtn = document.getElementById('decreaseBtn');
    const currentSizeDisplay = document.getElementById('currentSize');
    
    let currentSize = 16;
    const minSize = 12;
    const maxSize = 24;
    const step = 2;
    
