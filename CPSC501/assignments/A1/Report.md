Github Repository: https://github.com/alexs2112/CPSC501-YTMP3

First commit made for this assignment: 
```
Sep 23, 2023: Add unit tests for metadata
6edefd8816490cf08f2bf5d50997b79238380211
```

### Refactoring 1
**Git Commit**: [35f76a55292a2fc039a5807ae23169e59e9bc7ec](https://github.com/alexs2112/CPSC501-YTMP3/commit/35f76a55292a2fc039a5807ae23169e59e9bc7ec)
**Improvement**: Large Class (Major)
 - Basically everything is being handled in `YTMP3.py`.  The main thing to be refactored is the actual download of music files that uses the `yt-dlp` library.
**Steps**:
 - Performed the `Extract Class` refactoring on every method that was strictly related to downloading files. Iteratively touched on methods using the `yt-dlp` library and then followed up on how these changes affected other methods. The class that was extracted is now under `downloader.py`
**Code Snippets**:
 - The main method that uses the `yt-dlp` library that prompted this change was the rather large `download` method in `YTMP3.py`.
```python
def download(self):
	data = self.song_input.get("1.0", tkinter.END).split('\n')
	songs = []
	for link in data:
		if "youtu.be" in link:
			songs.append(link)
		elif "playlist" in link:
			ids = self.get_playlist_songs(link)
			for id in ids:
				songs.append(f"https://youtu.be/{id}")
		elif "music.youtube" in link:
			songs.append(link)
		elif "www.youtube.com" in link:
			video_code = link.split("?v=")
			if len(video_code) == 2:
				code = video_code[1].split("&")[0]
				songs.append(f"https://youtu.be/{code}")
			else:
				self.error(f"Could not split {link} by '?v='")
		elif len(link.strip()) > 0:
			self.error(f"Could not read {link}, skipping.")

	if (len(songs) == 0):
		self.error("No songs to download")
		self.directory.config(state="normal")
		return

	audio = self.get_downloader(embed_metadata = self.metadata.get())
	failed = []
	for i in range(len(songs)):
		url = songs[i]
		try:
			data = audio.extract_info(url)
			try:
				filepath = data['requested_downloads'][0]['filepath']
				title = os.path.basename(filepath)
			except Exception as e:
				# The video title is not accurate to the filename, this may break
				# yt-dlp replaces certain punctuation marks to make them windows safe
				title = f"{data['title']}.mp3"  # data['ext'] returns m4a

			self.add_song(title)
		except Exception as e:
			print(e)
			failed.append(i)
			continue

	if len(failed) > 0:
		self.error(f"\n{str(len(failed))} Failures Detected")    
		for i in failed:
			self.print(songs[i])

	self.print(f"\nDownload Complete!\nFiles located at {self.directory.get()}\n")

	# Reallow users to edit the directory
	self.directory.config(state="normal")
```
 - This method essentially does 2 things:
	1. Parse the list of links input by the user captured by the `data` variable. This will return a list of links in a standardized format while also parsing playlists of multiple files to download in a single list.
	2. It then fetches the downloader object that uses `yt-dlp`, called here as `self.get_downloader`, which is then used to iterate over the standardized list of links and downloads them in order.
 - As this method is rather large, by moving it to the new `Downloader` class it is also broken down into two new methods. This is a `Large Method` and the `Extract Method` refactoring is used here as well.
```python
def parse_user_data(self, application, data):
	songs = []
	for link in data:
		...
		Same parsing code as in the previous code snippet
		...
	return songs

def download(self, application, data, directory, add_metadata):
	songs = self.parse_user_data(application, data)
	if (len(songs) == 0):
		application.error("No songs to download")
		return

	...
	Same download and error handling code as in the previous code snippet
	...

	application.print(f"\nDownload Complete!\nFiles located at {directory}\n")
```
**Testing**:
 - This change was tested manually, by considering a variety of download links and potential errors while making sure that everything downloaded correctly and messages were displayed as expected. The executable was then built through the `build.bat` script, and the tests were manually performed again.
 - Unit testing will need to be implemented after further refactoring is done. Currently the download process requires the entire application to be running to handle logging messages. See below.
**What Comes Next**:
 - The code is better structured as this refactoring was able to remove over 100 lines of code from the large `Application` class. This makes it more succinct and ensures that download related code is handled within a download class, instead of all in the main class. This will allow further bug fixes and changes regarding downloads to be created easier.
 - As mentioned above, unit tests are currently out of scope for this change as the entire `Application` process gets passed between various download related functions to handle logging. A new class to specifically handle logging messages that can be stored in `Application` and passed to `Downloader` would be a much better solution and implemented next.

### Refactoring 2
**Git Commit**: [500fc2c02dfe3187293d7ba966511b3615aa6f67](https://github.com/alexs2112/CPSC501-YTMP3/commit/500fc2c02dfe3187293d7ba966511b3615aa6f67)
**Improvement**: Inappropriate Intimacy (sort of)
 - While this is not strictly correct, as python doesn't really have private variables, it is bad practice for the new `Downloader` class to be taking the `Application` class as a parameter just to access various logging methods. These logging methods should otherwise be kept private.
**Steps**:
 - Performed `Extract Class` on the logging methods to create a new `Logger` class. This takes the window console as a constructor parameter so must be initialized in `Application` after the GUI is set up.
 - Change each method in `Application` to use the new `Logger` object rather than itself when printing messages to the console.
 - Pass the new `Logger` object into the `Downloader` as a constructor parameter. Change each method in `Downloader` to use this `Logger` object rather than passing `Application` into each method.
 - The `Download` method in `Downloader` still uses `Application` to add songs to the list of completed songs upon successful download. This is changed to instead pass the `Application.add_song` method into `Download` as a parameter. This is not the best solution, however due to the downloads running in a separate thread it is the best one to not interrupt workflow.
	 - An alternative solution would be to return the list of successful songs at the end of `Download` and add them all to the list in `Application`, however this means that the list will *not* update itself while downloads are still running.
**Code Snippets**:
 - New `Logger` class extracted from `Application`
```python
class Logger:
    def __init__(self, console):
        self.console = console
        self.last_log = None

    def print(self, msg):
        if self.last_log != None:
            msg = "\n" + msg
        self.console.insert(END, msg)
        self.console.see(END)
        self.last_log = msg

    def debug(self, msg):
        msg.strip()
        if "[download]" in msg and "[download]" in self.last_log and "Destination" not in self.last_log:
            last = self.console.index("end-1c linestart")
            self.console.delete(last, END)
        self.print(msg if "[" in msg else f"[debug]: {msg}")

    def warning(self, msg):
        self.print(f"[warning]: {msg}")

    def error(self, msg):
        self.print(f"[error]: {msg}")
```
 - This can then be created in `Application` and passed into `Downloader` so they can both use these logging functions without treading on each others toes.
```python
class Application:
	def __init__(self):
		...
		self.logger = Logger(self.console)
		self.downloader = Downloader(self.logger)
		...
```
 - Either class can now log messages to the same console by calling
```python
self.logger.print("Message")
self.logger.debug("Message")
self.logger.warning("Message")
self.logger.error("Message")
```
**Testing**:
 - Testing the new logging messages through the same manual tests as in *Refactoring 1*
 - Now that this `Logger` object is created, unit tests for downloads can be created. Example:
```python
def test_download(self):
	data = ["https://music.youtube.com/watch?v=MG4vQOtVRMI&si=4vseqt5-SgG4tPbN"]
	self.downloader.download(data, self.directory, False, self.add_song)
	path = os.path.join(self.directory, "Lofi Chill Beats To Study To.webm")
	assert os.path.exists(path)
```
 - These new unit tests take a little while due to the nature of the downloads, however it is the most important functionality of the application.
 - All unit tests are rerun to ensure no critical functionality has been broken.

**What Comes Next**:
 - A logging object was desperately needed after the previous refactoring. Passing the entire `Application` object into `Downloader` to access the console log was extremely bad practice.
 - This refactoring on its own does not lead to any others and the program should have had a logging object from the beginning.

### Refactoring 3
**Git Commit**:
**Improvement**:
 - 
**Steps**:
 - 
**Code Snippets**:
 - 
**Testing**:
 - 
**What Comes Next**:
 - 

### Refactoring 4
**Git Commit**:
**Improvement**:
 - 
**Steps**:
 - 
**Code Snippets**:
 - 
**Testing**:
 - 
**What Comes Next**:
 - 

### Refactoring 5
**Git Commit**:
**Improvement**:
 - 
**Steps**:
 - 
**Code Snippets**:
 - 
**Testing**:
 - 
**What Comes Next**:
 - 

# Ideas
 - Clean up code for setting up application window (Major, Data Clumps -> Extract Method)
 - `Downloader.download`, clean up parameter list (Long Parameter List, -> Introduce Parameter Object)
 - Blow up the repo, count the second part of Refactoring 1 as (Long Method -> Extract Method)
	 - Manually copy the last 3 commits to their own folder (`git checkout [hash]`)
	 - Delete the last 3 commits (`git rebase -i [hash]`)
	 - Then redo each commit by copying the files into main folder, commit and push