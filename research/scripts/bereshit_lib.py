"""Bereshit's lib: the shared helpers (nechama_lib.py) pointed at Bereshit, plus its folio panels."""
from nechama_lib import *  # noqa: F401,F403
from nechama_lib import use, verse_range, words

use('bereshit')

LENINGRAD_CREDIT = {
    'en': 'Leningrad Codex (1008 CE). Bruce Zuckerman, West Semitic Research, in collaboration '
          'with the Ancient Biblical Manuscript Center; courtesy Russian National Library, Saltykov-Schedrin',
    'url': 'https://dornsife.usc.edu/wsrp/biblical-manuscripts'}

# Regions: measured on the full-resolution JPEGs; derivation in bereshit.md §5b.
FOLIO_1V = {
    'ref': 'Leningrad Codex, folio 1v', 'mode': 'image',
    'src': 'https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F001B.jpg',
    'link': 'https://www.sefaria.org/Genesis.1.1?with=Manuscripts',
    'width': 3683, 'height': 4224,
    'alt': 'Folio 1v of the Leningrad Codex: Genesis 1:1–26 in three columns of Hebrew script, with Masoretic notes in the margins.',
    'caption': {'en': 'Genesis 1:1–26. Columns read right to left.'},
    'credit': LENINGRAD_CREDIT,
    'regions': {
        'day-1': {'x': 0.61, 'y': 0.452, 'w': 0.2, 'h': 0.026},
        'day-2': {'x': 0.61, 'y': 0.672, 'w': 0.2, 'h': 0.026},
        'day-3': {'x': 0.34, 'y': 0.426, 'w': 0.21, 'h': 0.05},
        'day-4': {'x': 0.08, 'y': 0.252, 'w': 0.2, 'h': 0.048},
        'day-5': {'x': 0.08, 'y': 0.56, 'w': 0.2, 'h': 0.028},
    },
}
FOLIO_2R = {
    'ref': 'Leningrad Codex, folio 2r', 'mode': 'image',
    'src': 'https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F002A.jpg',
    'link': 'https://www.sefaria.org/Genesis.2.1?with=Manuscripts',
    'width': 3958, 'height': 4248,
    'alt': 'Folio 2r of the Leningrad Codex: Genesis 1:26–2:19 in three columns of Hebrew script, with Masoretic notes in the margins.',
    'caption': {'en': 'Genesis 1:26–2:19. Columns read right to left.'},
    'credit': LENINGRAD_CREDIT,
    'regions': {
        'day-6': {'x': 0.625, 'y': 0.664, 'w': 0.195, 'h': 0.026},
        'vayechulu-a': {'x': 0.625, 'y': 0.688, 'w': 0.195, 'h': 0.07},
        'vayechulu-b': {'x': 0.37, 'y': 0.158, 'w': 0.2, 'h': 0.142},
    },
}



def gen_1_31_2_3():
    he, en = verse_range('1:31', '2:3')
    return {'ref': 'Genesis 1:31-2:3', 'he': he, 'en': en, 'words': words(he, en, {
        'tov-meod': ('והנה טוב מאד', 'found it very good'),
        'yom-hashishi': ('יום הששי', 'the sixth day'),
        'vayechulu': ('ויכלו השמים והארץ וכל צבאם', 'The heaven and the earth were finished, and all their array'),
        'vaychal': ('ויכל אלהים ביום השביעי מלאכתו', 'On the seventh day God finished the work'),
        'vayishbot': ('וישבת ביום השביעי', 'ceasing on the seventh day'),
    })}
