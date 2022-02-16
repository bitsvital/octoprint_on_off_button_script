#! /bin/sh

# Provides:          pi_pwr_button_on_off.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

case "$1" in
  start)
    echo "Starting Pi Power Button On Off Script"
    /usr/local/bin/pi_pwr_button_on_off.py &
    ;;
  stop)
    echo "Stopping Pi Power Button On Off Script"
    pkill -f /usr/local/bin/lpi_pwr_button_on_off.py
    ;;
  *)
    echo "Usage: /etc/init.d/pi_pwr_button_on_off.sh {start|stop}"
    exit 1
    ;;
esac

exit 0