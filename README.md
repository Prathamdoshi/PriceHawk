# PriceHawk

## Introduction

The Amazon Price Tracker is a Python script that monitors the price of a specific Amazon product and sends an email notification when the price falls within a user-defined budget. This README will explain the code structure and functionality of the script.

## Code Structure

The script consists of the following components:

1. **Libraries**: The script begins by importing the necessary Python libraries. These include `requests` for making HTTP requests, `BeautifulSoup` (with `lxml` parser) for web scraping, and `smtplib` for sending email notifications.

2. **Constants**: The script defines two constants:
   - `AMAZON_URL`: The URL of the Amazon product page you want to track.
   - `BUDGET`: The maximum price you are willing to pay for the product.

3. **Headers**: A dictionary named `header` is created with user-agent and accept-language headers. This header is used in the HTTP request to make it appear as if the request is coming from a web browser.

4. **HTTP Request**: The script sends an HTTP GET request to the Amazon product page specified by `AMAZON_URL` with the provided headers. The response text is stored in `product_response`.

5. **Soup Creation**: BeautifulSoup is used to parse the HTML content of the product page. A BeautifulSoup object `soup` is created using the `lxml` parser.

6. **Price Extraction**: The script finds all HTML elements with the class `"a-offscreen"`, which typically contain the product price. It then extracts the price as a string and converts it into a floating-point number.

7. **Price Comparison**: The extracted price is compared with the user-defined budget (`BUDGET`). If the price is lower than the budget, an email notification will be sent.

8. **Email Notification**: If the price is within the budget, the script prepares an email message with a subject and body. It then uses the SMTP library to establish a connection with a Gmail SMTP server. After a secure connection is established, it logs in with your Gmail credentials, sends the email to the specified recipient, and closes the connection.

## How to Use

To use the Amazon Price Tracker:

1. Set the `AMAZON_URL` to the Amazon product page URL you want to track.

2. Define your desired `BUDGET`.

3. Ensure you have a Gmail account and provide your email credentials (`my_email` and `my_password`) in the script. Note that it's a good practice to use environment variables or a configuration file to store sensitive information securely.

4. Run the script.

The script will check the product's price daily and send you an email notification if the price falls within your budget.

## Future Enhancements

Here are some potential improvements for the script:

- **Error Handling**: Implement robust error handling to handle network issues, HTML structure changes, and authentication errors gracefully.

- **Customizable Email Content**: Allow users to customize the email message and subject according to their preferences.

- **Logging**: Implement logging to keep track of price changes and script activities.

- **User Input Handling**: Enhance the script to accept user input for the Amazon URL and budget interactively.

- **Database Integration**: Store price history and user preferences in a database for more advanced tracking and analytics.

Feel free to expand and customize the script further based on your requirements and preferences.
