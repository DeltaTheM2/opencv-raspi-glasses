

# Smart Glasses Image Classification Project

## Project Overview
This project is part of a student's endeavor to explore image classification using OpenCV and Roboflow. The Python script integrates with a Roboflow-trained model to classify images captured by a camera, identifying objects and scenes based on pre-defined categories.

## Repository Contents
- Python scripts for real-time image classification.
- Configuration files for model integration.
- Documentation on setup and execution.

## Getting Started

### Prerequisites
- Python 3.x
- Git (for version control)
- Access to the internet for installing packages and accessing the Roboflow model.

### Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone [repository URL]
   cd [repository directory]
   ```

2. **Create and Activate a Virtual Environment**
   - On macOS and Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

3. **Install Required Packages**
   Use the following command to install the required packages:
   ```bash
   pip install roboflow opencv-python
   ```

4. **Setting Up OpenCV**
   Follow the instructions in [this video](https://www.youtube.com/watch?v=QzVYnG-WaM4&t=1s) for setting up OpenCV. Please refer to the video description for specific commands.

### Running the Script
Run the script directly from the terminal with:
```bash
python script_name.py
```
Replace `script_name.py` with the name of the script you wish to run.

### Roboflow Model Access
- The model used for classification can be accessed here: [Roboflow Model](https://app.roboflow.com/soroush-mirzaee-omf8x/smart-glasses-nv4nt/1)
- API endpoint: [Roboflow API](https://classify.roboflow.com/?model=smart-glasses-nv4nt&version=1&api_key=4V69D2ZdRCtg7FrxNNyh)
