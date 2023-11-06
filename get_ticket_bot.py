from pyautogui import mouseDown, mouseUp, locateOnScreen, locateCenterOnScreen, scroll
from time import sleep
img_folder = "image/"
def find_image_and_click(file_name, offset_x=0, offset_y=0):
    if not "/" in file_name:
        file_name = img_folder + file_name
    while True:
        try:
            location = locateOnScreen(file_name)

            if location is not None:
                x, y = locateCenterOnScreen(file_name)
                mouseDown(button='left', x=x+offset_x, y=y)
                mouseUp(button='left')
                break
            else:
                print("not")

        except Exception as e:
            print(f"error: {str(e)}")

if __name__ == "__main__":
    scroll(-1000000) # 往下滑
    find_image_and_click("next.png")
    while True:
        try:
            location = locateOnScreen("image/select.png")
            if location is not None:
                sleep(1)
                scroll(-1000000) # 往下滑
                break
            else:
                print("not select")
        except Exception as e:
            print(f"error: {str(e)}")
    find_image_and_click("2200.png", 230)
    find_image_and_click("agree.png")
    find_image_and_click("next2.png")
