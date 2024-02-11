from tkinter import ttk
import cv2
from tkinter import *
import requests
#import handTracker as hT
#from pygrabber.dshow_graph import FilterGraph
import flet as ft
from API.Models.user import User
from API.Services.userService import UserService

def openCamera():
    if selected_camera_index is not None:
        print("Камера вмикається !")
        pass
    else:
        print("Камера не обрана!!!")
        return

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_SETTINGS, 1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    tracker = hT.handTracker()

    while True:
        success, image = cap.read()
        image = tracker.handsFinder(image)
        #lmList = tracker.positionFinder(image)
        #if len(lmList) != 0:
            #print(lmList[4])

        cv2.imshow("Video", image)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def get_connected_cameras():
    devices = FilterGraph().get_input_devices()

    available_cameras = {}

    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name

    return available_cameras

def on_combobox_change(event, combobox, label_result):
    global selected_camera_index
    selected_camera_index = combobox.get()[1]
    selected_value = combobox.get()
    label_result.config(text=f'Обрана камера: {selected_value}')

def createWindow():
    win = Tk()
    win.title("Аналізатор")
    win.geometry("400x300")
    win.resizable(width=False, height=False)

    button = Button(win, text="Ввімкнути камеру", font=40, command=openCamera)
    button.pack(side=BOTTOM, pady=40)

    label = Label(win, text="Виберіть камеру:")
    label.pack(pady=10)

    connected_cameras = get_connected_cameras()

    global  combobox
    combobox = ttk.Combobox(win, values=connected_cameras)
    combobox.pack(pady=10)
    if connected_cameras:
        combobox.set("Не обрана")
    else:
        combobox.set("Камери не виявлено")

    combobox.bind("<<ComboboxSelected>>", lambda event: on_combobox_change(event, combobox, label_result))

    # Создание метки для вывода выбранного значения
    label_result = Label(win, text="Обрана камера: ")
    label_result.pack(pady=10)

    return win

def registration(e):
    user = User()
    user.id = 0
    user.email = "em"
    user.login = "log"
    user.password = "pas"
    service = UserService()
    res = service.register(user)

user_email = ft.TextField(value="Введіть почту", width=200, height=40, text_align=ft.TextAlign.LEFT)
user_password = ft.TextField(value="Пароль", width=200, height=40, text_align=ft.TextAlign.LEFT, password=True)

def login(e):
    user = User()
    user.email = user_email.value
    user.password = user_password.value
    service = UserService()
    res, status = service.login(user)
    print("Result: " + res + ". Status: " +  str(status))


def main(page : ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.width = 400
    page.height = 400
    page.window_resizable = False
    page.add(
        ft.Row(
            [
                ft.Text('E-mail')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                user_email
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text('Пароль')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                user_password
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                
                ft.FilledButton(text="Авторизуватися", on_click=login, width=200, disabled=False)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.FilledButton(text="Зареєструватися", on_click=page.window_close)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)