const express = require('express');
const bodyParser = require('body-parser');
const joblib = require('joblib');
const { DataFrame } = require('pandas-js');

const app = express();
app.use(bodyParser.json());

// Load the model - Assuming the model_FPS_test.pkl is in the same directory
const loadedModelFPS = joblib.load('model_FPS_test.pkl');

// Define request body model
class PredictionRequest {
    constructor(data) {
        // Implement your validation logic here if needed
        Object.assign(this, data);
    }
}

// Endpoint for predictions
app.post('/predict', (req, res) => {
    const data = req.body;
    const predictionData = new PredictionRequest(data);
    const newData = new DataFrame([predictionData]);

    // Make predictions using the loaded model
    const predictions = loadedModelFPS.predict(newData);

    res.json({ predictions: predictions.tolist() });
});

// Endpoint for handling root request
app.post('/', (req, res) => {
    const data = req.body;
    const predictionData = new PredictionRequest(data);

    res.json(predictionData);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
