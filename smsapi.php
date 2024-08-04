<?php
// Get the parameters from the URL
$number = isset($_GET['number']) ? $_GET['number'] : '';
$message = isset($_GET['message']) ? $_GET['message'] : '';

// Validate the inputs
if (empty($number) || empty($message)) {
    echo "Error: Both 'number' and 'message' parameters are required.";
    exit;
}

// Here you can add logic to send SMS using an SMS gateway API
// For this example, we will just return the message

echo "Message to $number: $message";
?>
