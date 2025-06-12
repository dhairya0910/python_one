📹 YouTube Video Manager (Console App)
This is a simple Python-based console application that helps you manage a list of YouTube videos locally using JSON for data persistence. The app allows you to:

✅ Add new videos with name and duration

📝 Update existing videos by selecting their index

❌ Delete unwanted videos

📃 List all saved videos in a formatted output

💾 Save and load all data from a file (youtube.txt) using the json module

🔧 Tech Stack
Language: Python 3

Data Storage: JSON File (youtube.txt)

📁 File Structure
youtube.txt: Stores your video list data in JSON format.

Main Script: Contains all functionality including:

data_saver() – Saves videos to file

load_data() – Loads existing data

add_video() – Adds a new video

update_video() – Updates a selected video

delete_video() – Deletes a selected video

list_all_videos() – Displays all saved videos in a formatted way

💡 Notes
The app uses enumerate() to provide a clean numbered list of videos.

It handles missing file scenarios with a try-except block.

Modular structure makes it easy to extend (e.g., add search, sort, or export features).