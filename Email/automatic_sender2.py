import PySimpleGUI as sg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

form_window = None


def send_mail(val):
    global form_window

    # Construct mail headers
    msg = MIMEMultipart()
    msg['From'] = ''
    msg['To'] = val['-receiver-']
    msg['Subject'] = val['-subject-']
    message = val['-message-']

    sender_email = ''
    receiver_email = ''

    # Check for mandatory fields
    if not val['-subject-']:
        sg.popup_ok(
            "Моля, попълнете полето 'Тема'!",
            title="Системно Съобщение")
        return
    elif not val['-receiver-']:
        sg.popup_ok(
            "Моля, попълнете полето 'Получател'!",
            title="Системно Съобщение")
        return
    elif not val['-message-']:
        sg.popup_ok(
            "Моля, попълнете полето 'Съобщение'!",
            title="Системно Съобщение")
        return

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Add attachment
    if val['-attach_file-']:

        attachment_file = val['-attach_file-']

        with open(attachment_file, 'rb') as file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename="{attachment_file}"')
            msg.attach(attachment)

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
        form_window["-msg-"].update("Писмото беше изпратено успешно!")
    except smtplib.SMTPException:
        form_window["-msg-"].update("Грешка при изпращане на писмо!")
        form_window["-msg-"].text_color = 'red'


def construct_window():
    global form_window

    # Set the window theme
    sg.theme('DarkBrown')

    # Cconstruct columns layout
    col_1 = [
        [sg.Text('Получател:')],
        [sg.Text('Тема:')],
        [sg.Text('Избор на файл:')],
        [sg.Text('Съобщение:', size=(0, 7))]
    ]

    col_2 = [
        [sg.InputText(key='-receiver-')],
        [sg.InputText(key='-subject-')],
        [sg.Input(), sg.FileBrowse("файл...", key="-attach_file-",
                                   initial_folder=str(Path.home() / "Downloads"),
                                   file_types=(("Excel Files", "*.xlsx"), ("Doc Files", "*.doc"),
                                               ("Doc Files 2010", "*.docx"),))],
        [sg.Multiline(key='-message-', autoscroll=True, size=(51, 7))]
    ]


    # Assemble layout
    layout = [[sg.Column(col_1), sg.Column(col_2)],
              [sg.OK('Изпрати'), sg.Cancel("Отказ"), sg.Text(""), sg.Text("", key="-msg-", text_color="green")]]

    form_window = sg.Window('Изпращане на мейл', layout, icon=f"files\\mail.ico", modal=True, finalize=True)

    while True:
        event, values = form_window.read()
        if event in (sg.WIN_CLOSED, 'Отказ'):
            break
        elif event == 'Изпрати':
            send_mail(values)
            pass

    form_window.close()


if __name__ == '__main__':
    # Open PySimpleGUI form
    construct_window()
