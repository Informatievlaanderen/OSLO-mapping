const axios = require("axios");
const https = require("https");

const LDIO_PIPELINE_URL = process.env.LDIO_OVERSTORT_METING_CLEANSED_URL || "https://ldio-overstort.test.az.aquafin.be/overstort-meting-cleansed";

const httpsAgent = new https.Agent({ rejectUnauthorized: false });

module.exports = async function (context, eventHubMessages) {
    context.log(`Received ${eventHubMessages.length} messages from Event Hub.`);

    for (const message of eventHubMessages) {
        try {
            // Print the message content to the logs
            context.log(`Processing message: ${JSON.stringify(message)}`);

            const response = await axios.post(LDIO_PIPELINE_URL, message, {
                headers: { "Content-Type": "application/json" },
                httpsAgent
            });
            context.log(`Event sent successfully. Response status: ${response.status}`);
        } catch (error) {
            context.log.error(`Failed to send event. Error: ${error.message}`);
        }
    }
};
