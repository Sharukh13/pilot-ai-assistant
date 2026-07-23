import os
from winotify import Notification, audio


def Alert(text):
    # Current project folder
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Optional Pilot AI logo
    icon_path = os.path.join(project_dir, "logo.png")

    toast = Notification(
        app_id="Pilot AI",
        title=text,
        duration="long",
        icon=icon_path if os.path.exists(icon_path) else ""
    )

    toast.set_audio(
        audio.Default,
        loop=False
    )

    toast.add_actions(
        label="Dismiss",
        launch=""
    )

    toast.show()