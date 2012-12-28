#!/bin/bash
CURRENT_DESKTOP="$(gsettings get org.gnome.desktop.session session-name)"
if [ "$CURRENT_DESKTOP" == "'gnome'" ]
then
	gsettings set org.gnome.desktop.session session-name gnome-fallback
else
	gsettings set org.gnome.desktop.session session-name gnome
fi
CURRENT_DESKTOP="$(gsettings get org.gnome.desktop.session session-name)"
zenity --info --text "The desktop has been switched to $CURRENT_DESKTOP.\n\nPlease log out and back in."
