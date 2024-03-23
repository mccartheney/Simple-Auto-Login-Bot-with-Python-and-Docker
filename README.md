# Simple Auto Login Bot with Python and Docker

This project is a simple automated login bot implemented in Python using the Selenium library. It automates the process of logging into a website by providing a username and password. The bot is containerized using Docker for easy deployment and portability.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Prerequisites

Before running the bot, ensure you have the following installed:

- Docker
- Chrome WebDriver (for Selenium)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/Simple-Auto-Login-Bot-with-Python-and-Docker.git
   ```

2. Navigate to the project directory:

    ```bash
    cd Simple-Auto-Login-Bot-with-Python-and-Docker
    ```

## Usage

### Using Docker

To build and run the bot using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   make build
   ```

2. Run the Docker container:

    ```bash
    make run
    ```

3. Alternatively, you can use the following command to build and run the bot in one step:

    ```bash
    make build-run
    ```

## Configuration

Before running the bot, ensure you have set up the required environment variables. Create a `.env` file in the project directory and define the following variables:

- `USERNAME`: Your username for logging in.
- `PASSWORD`: Your password for logging in.
- `URL`: The URL of the login page.
- `USERNAME_INPUT`: The ID of the username input field.
- `PASS_INPUT`: The ID of the password input field.
- `SUBMIT_INPUT`: The ID of the submit button.

Example `.env` file:

    USERNAME=username_value
    PASSWORD=password_value
    URL=url_value
    USERNAME_INPUT=username_id
    PASS_INPUT=pass_id
    SUBMIT_INPUT=submit_id

## Contributing

Contributions are welcome! If you have any ideas, enhancements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE)

## Author

[Mccartheney Mendes](https://www.linkedin.com/in/mccartheney-mendes-892709292/) - [GitHub](https://github.com/mccartheney)

