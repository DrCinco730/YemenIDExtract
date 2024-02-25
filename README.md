### Extended Setup Instructions

### Installing
A step-by-step series of examples that tell you how to get a development environment running.

#### Clone the repository

```bash
git clone https://github.com/DrCinco730/YemenIDExtract.git
cd YemenIDExtract
```

#### Set up a virtual environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### Install the dependencies

```bash
pip install -r requirements.txt
```

### Tesseract-OCR Installation

Tesseract-OCR is a crucial dependency for this project. Follow the instructions below to install Tesseract on your system and configure it for Arabic language support.

#### For Linux (Ubuntu/Debian)

1. **Install Tesseract-OCR**:

```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

2. **Install Arabic Language Support**:

```bash
sudo apt-get install tesseract-ocr-ara
```

#### For Windows

1. **Download the Installer**: Go to the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) repository and download the latest installer for Windows.

2. **Run the Installer**: Execute the downloaded installer. During the installation, make sure to note the installation path of Tesseract, as you will need it to configure your project.

3. **Add Tesseract to System PATH**:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Navigate to 'Advanced system settings' and click on 'Environment Variables'.
   - Find the 'Path' variable in 'System variables', select it, and click 'Edit'.
   - Click 'New' and add the path where Tesseract is installed (e.g., `C:\Program Files\Tesseract-OCR`).
   - Click 'OK' to close all dialog boxes.

4. **Install Arabic Language Support**: The installer should give you the option to download and install language packs. Make sure to select Arabic (ara) during the installation. If you need to add Arabic support later, you can download the appropriate `.traineddata` file from the [tessdata repository](https://github.com/tesseract-ocr/tessdata) and place it in the `tessdata` directory of your Tesseract installation.

### Configuring the Project

Edit the `config.py` file in your project to set the correct path to the Tesseract executable on your machine. This step is particularly important for Windows users.

For Linux users, if Tesseract is in your PATH, you might not need to change anything.

```python
# Example configuration for Windows
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Example configuration for Linux (default might just work)
TESSERACT_CMD = '/usr/bin/tesseract'
```

### Usage

To start the application, run:

```bash
python app.py
```

The API endpoints `/api/card_front` and `/api/card_back` can then be accessed to submit images of Yemeni ID cards for processing.
