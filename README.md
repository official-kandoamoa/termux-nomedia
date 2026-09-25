**AI development disclosure:** This project was developed with assistance from the free versions of ChatGPT, Grok, and Claude (LLMs), with the user providing ideas and testing while the AIs and user collaboratively suggested, generated, reviewed, and refined code and solutions.

# `.nomedia` File Creator for Android (Termux)

This Python script recursively creates empty `.nomedia` files in directories under a selected path.

Android media apps generally ignore media files inside directories containing a `.nomedia` file. This can be useful for preventing images, videos, audio files, or other media from appearing in gallery and media-player apps.

## Features

- Creates a `.nomedia` file in the target directory and its subdirectories
- Skips hidden directories whose names begin with `.`
- Preserves existing `.nomedia` files
- Reports created files, skipped files, and errors
- Uses the current working directory by default

## Requirements

- Android device
- [Termux](https://termux.dev/)
- Python installed in Termux

Install Python with:

```bash
pkg update
pkg install python
```

To allow Termux to access shared Android storage, run:

```bash
termux-setup-storage
```

Grant the requested storage permission when prompted.

## Installation

Save the script as `nomedia.py`.

For example:

```bash
mkdir -p ~/scripts
cd ~/scripts
nano nomedia.py
```

Paste the script into the file, then save it.

You can also make it executable:

```bash
chmod +x nomedia.py
```

## Usage

Navigate to the directory where you want to create `.nomedia` files and run the script:

```bash
cd ~/storage/shared/YourFolder
python nomedia.py
```

Or, if the script is executable:

```bash
./nomedia.py
```

The script uses the current working directory as its target.

### Example: Hide a Download Folder

```bash
cd ~/storage/shared/Download
python ~/scripts/nomedia.py
```

### Example: Hide a Pictures Subdirectory

```bash
cd ~/storage/shared/Pictures/Private
python ~/scripts/nomedia.py
```

## Example Output

```text
📁 Target: /data/data/com.termux/files/home/storage/shared/Pictures/Private

✅ Created  : 3
⏭️  Skipped  : 1 (already exist)
❌ Errors   : 0

--- Created ---
  /data/data/com.termux/files/home/storage/shared/Pictures/Private/.nomedia
  /data/data/com.termux/files/home/storage/shared/Pictures/Private/Videos/.nomedia
  /data/data/com.termux/files/home/storage/shared/Pictures/Private/Images/.nomedia
```

## Important Notes

- A `.nomedia` file affects media scanning for the directory where it exists and its subdirectories.
- Some media apps may need to be restarted before the change becomes visible.
- Android media databases may retain previously indexed files for some time.
- Creating `.nomedia` files does not encrypt or protect your files.
- File-manager apps may still display files located inside `.nomedia` directories.
- The script skips directories beginning with `.`, such as `.thumbnails` and `.cache`.
- Run the script carefully. Running it from a high-level directory may create many `.nomedia` files.

## Removing `.nomedia` Files

To remove the `.nomedia` files created under a directory, use the following command carefully:

```bash
find ~/storage/shared/YourFolder -type f -name ".nomedia" -delete
```

Replace `YourFolder` with the directory you want to process.

> Be careful when using `find` and `-delete`. Verify the target path before running the command.

## Customizing the Target Directory

The script currently uses the directory from which it is executed:

```python
target = os.getcwd()
```

You can replace it with a fixed path:

```python
target = "/data/data/com.termux/files/home/storage/shared/YourFolder"
```

Alternatively, change the script to accept a path from the command line.

## License

You may use, modify, and distribute this script freely.
