const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');

const app = express();
const PORT = 5000;

app.use(bodyParser.text());

app.post('/webhook', async (req, res) => {
    const data = req.body;
    if (data) {
        if (data.includes('SubscribeURL')) {
            const subscribeUrl = data.split('"SubscribeURL": "')[1].split('"')[0];
            try {
                const response = await fetch(subscribeUrl);
                if (response.ok) {
                    res.status(200).send('Subscription activated successfully');
                } else {
                    res.status(400).send('Failed to activate subscription');
                }
            } catch (error) {
                console.error('Error occurred:', error);
                res.status(500).send('Internal server error');
            }
        } else {
            console.log(data);
            res.status(200).send('Request received successfully');
        }
    } else {
        res.status(400).send('Empty request');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
