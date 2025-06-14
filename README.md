# nysc-checker

A Python script to automatically check the NYSC (National Youth Service Corps) registration portal and send alerts when registration opens.

## Features

- **Automated Checking:** Periodically checks the NYSC registration portal for open registration.
- **Email Notification:** Sends an email alert when registration is open.
- **WhatsApp Notification:** Sends a WhatsApp message using Twilio when registration is open.
- **Environment Variables:** Uses a `.env` file to securely store credentials.

## Requirements

- Python 3.x
- See `requirements.txt` for required Python packages.

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd nysc-checker
    ```
2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure environment variables:**
    - Create a `.env` file in the project root.
    - Add your NYSC portal credentials and notification settings:
      ```
      NYSC_PORTAL_EMAIL=your_email
      NYSC_PORTAL_PASSWORD=your_password
      TWILIO_PHONE_NUMBER=your_twilio_number
      RECEIVER_PHONE_NUMBER=receiver_number
      ```
4. **Run the script:**
    ```bash
    python nysc_checker.py
    ```

## How it Works

- The script fetches the NYSC registration portal page.
- It checks for the presence of the phrase "No Active Registration".
- If registration is open, it sends notifications via email and WhatsApp.

## Customization

- Change the recipient email in `send_email_alert()` if needed.
- Update WhatsApp numbers in the `.env` file.

## Disclaimer

This project is not affiliated with NYSC.  
Use responsibly and do not spam the portal.

## License

MIT License