# reader

## Set up local server

**You'll need a OpenAI Account. Create one if you haven't already**

```bash
./venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Don't forget to update the newly created `.env` file with your OpenAI Api Key


### Running local Server:

``` bash
flask run
```

## Installing Chrome extension

Go to [chrome://extensions/](chrome://extensions/)

Load unpacked, navigate to `/PATH/TO/REPOSITORY/extensions/chrome` and hit 'select'. The extension should be loaded and will direct tts requests to the server (ensure it is running!).

Right now, it just saves the output to a file in the local repository directory.

Been meaning to get playback working but I haven't gotten around to it.

## Usage

If everything is working, highlight some text in your chrome browser and you'll see a 'Synthesize' button. Click it, and wait a bit. Eventually, a file will be written to this repo's local dir.
