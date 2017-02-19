#!/usr/bin/env bash
# /etc/init.d/uv_runner

### BEGIN INIT INFO
# Provides:          uv_runner
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: uv_leds initscript
# Description:       This service is used to run uv_leds
### END INIT INFO


start_stop() {
	case "$1" in
		start)
			echo "Starting..."
			python /home/pi/Public/UV-Bicycle/src/pi/images_test/main.py&
			;;
		stop)
			echo "Stopping..."
			killall python
			;;
	esac
}

case "$1" in
    start|stop)
        start_stop "$1"
        ;;
    restart)
        start_stop "start"
        start_stop "stop"
        ;;
    *)
        echo "Usage: $0 start|restart|stop"
        exit 1
        ;;
esac

exit 0
