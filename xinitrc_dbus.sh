#!/bin/sh
# Скрит для проверки наличия строки в .xinitrc запуска DBUS для PCManFM 0.9.7
# Автор - Александр Казанцев <kazancas@mandriva.ru>
# Скрипт распространяется по лицензии GPL v.3

# Проверяем наличие файла у текущего пользователя

if [ -f ~/.xinitrc ]; then
 
 if cat ~/.xinitrc | grep -o 'dbus-launch'
    then
 
	echo "ничего править не надо!"
	else
	echo "## test for an existing bus daemon, just to be safe" >> ~/.xinitrc
	echo "if which dbus-launch >/dev/null && test -z \"\$DBUS_SESSION_BUS_ADDRESS\"; then" >> ~/.xinitrc
	echo "eval \"\$(dbus-launch --sh-syntax --exit-with-session)\"" >> ~/.xinitrc
	echo "fi" >> ~/.xinitrc

	fi
 
else
 echo "## test for an existing bus daemon, just to be safe" >> ~/.xinitrc
 echo "if which dbus-launch >/dev/null && test -z \"\$DBUS_SESSION_BUS_ADDRESS\"; then" >> ~/.xinitrc
 echo "eval \"\$(dbus-launch --sh-syntax --exit-with-session)\"" >> ~/.xinitrc
 echo "fi" >> ~/.xinitrc

fi
