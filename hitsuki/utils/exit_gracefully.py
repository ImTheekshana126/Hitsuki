# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
#
# This file is part of Hitsuki (Telegram Bot)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import signal

from hitsuki.services.redis import redis
from hitsuki.utils.logger import log


def exit_gracefully(signum, frame):
    log.warning("Bye!")

    try:
        redis.save()
    except Exception:
        log.error("Exiting immediately!")
    os.kill(os.getpid(), signal.SIGUSR1)


# Signal exit
log.info("Setting exit_gracefully task...")
signal.signal(signal.SIGINT, exit_gracefully)
