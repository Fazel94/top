# -*- coding: utf-8 -*-

import os
from os.path import dirname, join as pjoin

# Settings
DEBUG = True


# Files and locations
_CUR_PATH = dirname(os.path.abspath(__file__))
BASE_PATH = pjoin(_CUR_PATH, os.pardir, 'static', '')
TEMPLATE_PATH = pjoin(_CUR_PATH, 'templates')
DATA_FILE_TMPL = '{lang}/{project}/{year}/{month}/{day}.json'
DATA_PATH_TMPL = pjoin(BASE_PATH, DATA_FILE_TMPL)
LANG_PROJ_LINK_TMPL = u'http://top.hatnote.com/{lang}/{project}/'
DATE_PERMALINK_TMPL = (u'http://top.hatnote.com/{lang}/{project}/'
                       '{year}/{month}/{day}.html')
PERMALINK_TMPL = (u'http://top.hatnote.com/{lang}/{project}/{year}/{month}/'
                  '{day}.html#title-{title}')
FEED_FILE_TMPL = 'feeds/{lang}{project}.rss'
FEED_PATH_TMPL = pjoin(BASE_PATH, FEED_FILE_TMPL)
STRINGS_PATH_TMPL = pjoin(TEMPLATE_PATH, 'strings', '{lang}_strings.yaml')

# Valuable and important URLs
TOP_API_URL = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/'\
              'top/{lang}.{project}/all-access/{year}/{month}/{day}'
MW_API_URL = 'https://{lang}.{project}.org/w/api.php?'
TOTAL_TRAFFIC_URL = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/aggregate/{lang}.{project}.org/all-access/all-agents/daily/{datestr}00/{datestr}00'


# Other variables
LOCAL_LANG_MAP = {'en': u'English',
                  'de': u'Deutsch',
                  'fr': u'Français',
                  'ko': u'한국어',
                  'et': u'Eesti',
                  'sv': u'Svenska',
                  'hu': u'Magyar',
                  'da': u'Dansk',
                  'it': u'Italiano',
                  'pa': u'ਪੰਜਾਬੀ',
                  'ca': u'Català',
                  'es': u'Español',
                  'fa': u'فارسی',
                  'ur': u'اردو',
                  'zh': u'中文',
                  'kn': u'ಕನ್ನಡ',
                  'no': u'bokmål',
                  'bn': u'বাংলা',
                  'id': u'Bahasa Indonesia',
                  'ta': u'தமிழ்',
                  'lv': u'latviešu valoda',
                  'el': u'ελληνικά',
                  'fi': u'Suomenkielinen',
                  'ar': u'العربية',
                  'fa': u'فارسی',
                  'cs': u'Česká',
                  'or': u'ଓଡ଼ିଆ',
                  'te': u'తెలుగు',
                  'gl': u'Galega'
}
DEFAULT_LANG = 'en'
DEFAULT_PROJECT = 'wikipedia'


# These prefixes are not for articles
PREFIXES = ['Special', 'Template', 'Sp?cial', 'Project']
