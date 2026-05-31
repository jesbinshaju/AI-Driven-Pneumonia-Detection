async function predict() {
    let file = document.getElementById('fileInput').files[0];
    let formData = new FormData();
    formData.append('file', file);

    let res = await fetch('/predict', { method: 'POST', body: formData });
    let data = await res.json();
    document.getElementById('output').innerText = `Diagnosis: ${data.result} (Confidence: ${data.confidence})`;
}