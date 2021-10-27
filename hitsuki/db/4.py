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

from hitsuki.services.mongo import mongodb
from hitsuki.utils.logger import log

log.info('Hitsuki Database v4')
log.info("Filters: move 'note' to 'note_name'")
log.info('Starting updating all filters...')

all_filters = mongodb.filters.find({})
all_filters_count = all_filters.count()
counter = 0
changed_filters = 0
for item in all_filters:
    counter += 1
    log.info(f'Updating {counter} of {all_filters_count}...')

    if 'note' in item:
        changed_filters += 1
        item['note_name'] = item['note']
        del item['note']
        mongodb.notes_v2.replace_one({'_id': item['_id']}, item)

log.info('Update done!')
log.info('Modified filters - ' + str(changed_filters))
log.info('Unchanged filters - ' + str(all_filters_count - changed_filters))
