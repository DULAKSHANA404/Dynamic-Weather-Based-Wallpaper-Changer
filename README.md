# Dynamic Weather Based Wallpaper Changer

This Python application changes your desktop wallpaper based on real-time weather data. The wallpaper updates automatically based on the weather conditions in your specified location. 

### Features:
- Fetches real-time weather data via a weather API.
- Changes wallpaper based on the weather (sunny, rainy, cloudy, etc.).
- Customizable location by entering the country and postal code.
- Supports multiple weather conditions and wallpaper change logic.

### Requirements:
- Python 3.12.10
- Libraries:
  - `os`
  - `cv2`
  - `ctypes`
  - `screeninfo`
  - `requests`

### Installation

1. Clone this repository or download the files.

2. Install the necessary dependencies:

### Usage

1. Open a terminal/command prompt in the directory where `main.py` is located.
2. Run the script:
3. Enter your country code (e.g., `US`, `IN`, `LK`) and postal code when prompted.

4. The script will fetch the current weather and change the wallpaper accordingly. 

### Example:

```plaintext
Enter your Country code :- lk
Enter your postal code :- 12400
Horana DS Division.... is it right ? (Y/N)y
current weather is overcast clouds
