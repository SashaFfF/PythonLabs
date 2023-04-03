SEPARATORS = r'[.!\?]+'
NON_DECLARATIVE_SEPARATORS = r'[!\?]+'
WORD = r'\b[a-zA-Z\d]+\b'
NUMBER = r'\b\d+\b'
ABBREVIATION = ['mr.', 'mrs.', 'ms.', 'etc.', 'dr.', 'vs.', 'sr.', 'jr.', 'smth.', 'smb.', 'n.',
                'v.', 'adj.', 'adv.', 'prep.', 'p.', 'pp.', 'par.', 'ex.', 'pl.', 'sing.', 're.',
                'rf.', 'edu.', 'appx.', 'in.', 'sec.', 'gm.', 'cm.', 'qt.', 'ft.', 'oz.', 'pt.',
                'yr.', 'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.',
                'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu.', 'fri.', 'sat.', 'sun.', 'i.']
ABBREVIATION_TWO_WORDS = ['e.g.', 'i.e.', 'p.s.']