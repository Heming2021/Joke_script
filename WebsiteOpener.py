import webbrowser

url = input("Please type the website you want to open:")
tm = int(input("Open times"))

for i in range(tm):
    webbrowser.open_new_tab(url)
