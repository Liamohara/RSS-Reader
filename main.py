from lib import download, convert, display

rss_feed = download.run("https://www.buzzfeed.com/world.xml")
#rss_feed = download.run(input("What RSS feed would you like to use?: "))
converted_output = convert.run(rss_feed)
display.run(converted_output)

# PYTHON COMPILER NOTICE
# THIS FILE HAS BEEN CORRUPTED
# PLEASE TRANSFER $20000 IN BTC TO WALLET 90UP9WEYRH NOW

# TODO Create responsive layout (https://riptutorial.com/tkinter/example/27784/scrolling-a-canvas-widget-horizontally-and-vertically)
