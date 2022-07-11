# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium_youtube import Youtube
from selenium_firefox.firefox   import Firefox

def run(name):
    # Use a breakpoint in the code line below to debug your script.
    firefox = Firefox()
    youtube = Youtube(
        browser=firefox  # or firefox
    )
    #
    # upload_result = youtube.upload('path_to_video', 'title', 'description', ['tag1', 'tag2'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
