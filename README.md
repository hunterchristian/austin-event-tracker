# austin-event-tracker

## Getting started
1. Open up a new terminal window.
2. Run the following commands:

   1. `git clone git@github.com:hunterchristian/austin-event-tracker.git`

       _If you receive an error, i.e. cloning the repository via SSH failed, clone the repository using https_
      
       `git clone https://github.com/hunterchristian/austin-event-tracker.git`
   
   2. `cd sf-event-tracker`
3. Open `config.ini` and change the value of `ProjectPath` to the path of your project folder. If you need help finding this, navigate to the austin-event-tracker directory in your terminal and type `pwd`, then copy and path the output as the value of the `ProjectPath` field. If your curious as to why this is necessary, [view this question in Stack Overflow](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder). TL;DR; we use the project path to enable importing file from other folders without needing to specify a relative path.
4. [Install python 3.7.3](https://www.python.org/downloads/release/python-373/)
5. [Install virtualenv](https://realpython.com/python-virtual-environments-a-primer/)
6. From the root folder of the project (you should still be here if you haven't used `cd` or closed the terminal window), run the following commands:

   1. `virtualenv env`
   2. `source env/bin/activate`
   3. `pip3 install -r requirements.txt` 

7. From the root folder of the project, the following commands are now available to you:

   * To run the web scraper: `make scrape`
   * To run the server that serves the scraped data via a rest API: `make serve`
   * To upload to scraped data to the Google calendar: `make upload`

When you return to the project, be sure to activate the virtual environment before attempting to run any commands: `source env/bin/activate`
