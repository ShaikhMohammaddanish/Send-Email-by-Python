from cx_Freeze import setup, Executable

setup ( name = "Send Email",
        version = "1.0",
        author = "Danish Shaikh",
        description = "Simple programm to send email easly",
        executables = [ Executable ( r"send_email.py", shortcutName = "send mail by danish", shortcutDir = "DesktopFolder"  ) ] )