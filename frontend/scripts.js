const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const analyzeBtn = document.getElementById('analyzeBtn');
const result = document.getElementById('result');
const captionEl = document.getElementById('caption');
const summaryEl = document.getElementById('summary');

imageInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = 'block';
    }
});

analyzeBtn.addEventListener('click', async function() {
    const file = imageInput.files[0];
    if (!file) {
        alert('Please select an image first!');
        return;
    }

    analyzeBtn.textContent = 'Analyzing...';

    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();

    captionEl.textContent = data.caption;
    summaryEl.textContent = data.summary;
    result.style.display = 'block';
    analyzeBtn.textContent = 'Analyze Image';
});