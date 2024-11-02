from time import sleep
import alive_progress as ap
import banners
import os
import menu

os.system("cls")

LoadingLines = [("smooth", 1732, 1.3), ("brackets", 476, 0.9), ("filling", 291, 0.3)]


def LoadingTool1(LoadingLine, longitude, timeLoading):
    delay = timeLoading / longitude
    with ap.alive_bar(longitude, bar=LoadingLine) as bar:
        for _ in range(longitude):
            sleep(delay)
            bar()


print(banners.BANNER_1)


for LoadingLine, longitude, timeLoading in LoadingLines:
    LoadingTool1(LoadingLine, longitude, timeLoading)

os.system("cls")
menu.mainMenu()