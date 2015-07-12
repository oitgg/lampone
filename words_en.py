DEFAULT_BANWORDS = ['A', 'ABILITY', 'ABLE', 'ABOUT', 'ABSOLUTE', 'ABSOLUTELY', 'ACROSS', 'ACTUAL', 'ACTUALLY', 'AFTER',
                    'AGAIN', 'AGAINST', 'AGO', 'AGREE', 'ALL', 'ALMOST', 'ALONG', 'ALREADY', 'ALTHOUGH', 'ALWAYS',
                    'AN', 'AND', 'ANOTHER', 'ANY', 'ANYHOW', 'ANYTHING', 'ANYWAY', 'ARE', "AREN'T", 'AROUND', 'AS',
                    'AWAY', 'BACK', 'BAD', 'BE', 'BEEN', 'BEFORE', 'BEHIND', 'BEING', 'BELIEVE', 'BELONG', 'BEST',
                    'BETWEEN', 'BIG', 'BIGGER', 'BIGGEST', 'BIT', 'BOTH', 'BUDDY', 'BUT', 'BY', 'CALL', 'CALLED',
                    'CAME', 'CAN', "CAN'T", 'CANNOT', 'CARE', 'CARING', 'CASE', 'CATCH', 'CAUGHT', 'CERTAIN',
                    'CHANGE', 'CLOSE', 'CLOSER', 'COME', 'COMING', 'COMMON', 'CONSTANT', 'CONSTANTLY', 'COULD',
                    'DAY', 'DAYS', 'DERIVED', 'DESCRIBE', 'DESCRIBES', 'DETERMINE', 'DETERMINES', 'DID', "DIDN'T",
                    'DOES', "DOESN'T", 'DOING', "DON'T", 'DONE', 'DOUBT', 'DOWN', 'EACH', 'EARLIER', 'EARLY', 'ELSE',
                    'ESPECIALLY', 'EVEN', 'EVER', 'EVERY', 'EVERYBODY', 'EVERYONE', 'EVERYTHING', 'FACT', 'FAIR',
                    'FAR', 'FELLOW', 'FEW', 'FIND', 'FINE', 'FOR', 'FORM', 'FOUND', 'FROM', 'FULL', 'FURTHER', 'GAVE',
                    'GETTING', 'GIVE', 'GIVEN', 'GIVING', 'GO', 'GOING', 'GONE', 'GOOD', 'GOT', 'GOTTEN', 'GREAT',
                    'HAS', "HASN'T", 'HAVE', "HAVEN'T", 'HAVING', 'HELD', 'HERE', 'HIGH', 'HOLD', 'HOLDING', 'HOW',
                    'IN', 'INDEED', 'INSIDE', 'INSTEAD', 'INTO', 'IS', "ISN'T", 'IT', "IT'S", 'ITS', 'JUST', 'KEEP',
                    'KNEW', 'KNOW', 'KNOWN', 'LARGE', 'LARGER', 'LARGETS', 'LAST', 'LATE', 'LATER', 'LEAST', 'LESS',
                    "LET'S", 'LEVEL', 'LIKES', 'LITTLE', 'LONG', 'LONGER', 'LOOK', 'LOOKED', 'LOOKING', 'LOOKS', 'LOW',
                    'MAKE', 'MAKING', 'MANY', 'MATE', 'MAY', 'MAYBE', 'MEAN', 'MEET', 'MENTION', 'MERE', 'MIGHT',
                    'MORE', 'MORNING', 'MOST', 'MOVE', 'MUCH', 'MUST', 'NEAR', 'NEARER', 'NEVER', 'NEXT', 'NICE',
                    'NONE', 'NOON', 'NOONE', 'NOT', 'NOTE', 'NOTHING', 'NOW', 'OBVIOUS', 'OF', 'OFF', 'ON', 'ONCE',
                    'ONTO', 'OPINION', 'OR', 'OTHER', 'OUR', 'OUT', 'OVER', 'OWN', 'PART', 'PARTICULAR',
                    'PERHAPS', 'PERSON', 'PIECE', 'PLACE', 'PLEASANT', 'PLEASE', 'POPULAR', 'PREFER', 'PRETTY', 'PUT',
                    'REAL', 'REALLY', 'RECEIVE', 'RECEIVED', 'RECENT', 'RECENTLY', 'RELATED', 'RESULT', 'RESULTING',
                    'SAID', 'SAME', 'SAW', 'SAY', 'SAYING', 'SEE', 'SEEM', 'SEEMED', 'SEEMS', 'SEEN', 'SELDOM',
                    'SET', 'SEVERAL', 'SHALL', 'SHORT', 'SHORTER', 'SHOULD', 'SHOW', 'SHOWS', 'SIMPLE', 'SIMPLY',
                    'SO', 'SOME', 'SOMEONE', 'SOMETHING', 'SOMETIME', 'SOMETIMES', 'SOMEWHERE', 'SORT', 'SORTS',
                    'SPENT', 'STILL', 'STUFF', 'SUCH', 'SUGGEST', 'SUGGESTION', 'SUPPOSE', 'SURE', 'SURELY',
                    'SURROUNDS', 'TAKE', 'TAKEN', 'TAKING', 'TELL', 'THAN', 'THANK', 'THANKS', 'THAT', "THAT'S",
                    'THE', 'THEIR', 'THEM', 'THEN', 'THERE', 'THEREFORE', 'THESE', 'THEY', 'THING', 'THINGS', 'THIS',
                    'THOUGH', 'THOUGHTS', 'THOUROUGHLY', 'THROUGH', 'TINY', 'TO', 'TODAY', 'TOGETHER', 'TOLD',
                    'TOO', 'TOTAL', 'TOTALLY', 'TOUCH', 'TRY', 'TWICE', 'UNDER', 'UNDERSTAND', 'UNDERSTOOD', 'UNTIL',
                    'US', 'USED', 'USING', 'USUALLY', 'VARIOUS', 'VERY', 'WANT', 'WANTED', 'WANTS', 'WAS', 'WATCH',
                    'WAYS', 'WE', "WE'RE", 'WELL', 'WENT', 'WERE', 'WHAT', "WHAT'S", 'WHATEVER', 'WHATS', 'WHEN',
                    "WHERE'S", 'WHICH', 'WHILE', 'WHILST', 'WHO', "WHO'S", 'WHOM', 'WILL', 'WISH', 'WITH', 'WITHIN',
                    'WONDERFUL', 'WORSE', 'WORST', 'WOULD', 'WRONG', 'YESTERDAY', 'YET']

DEFAULT_AUXWORDS = ['DISLIKE', 'HE', 'HER', 'HERS', 'HIM', 'HIS', 'I', "I'D", "I'LL", "I'M", "I'VE", 'LIKE', 'ME',
                    'MY', 'MYSELF', 'ONE', 'SHE', 'THREE', 'TWO', 'YOU', "YOU'D", "YOU'LL", "YOU'RE", "YOU'VE", 'YOUR',
                    'YOURSELF']

DEFAULT_SWAPWORDS = {"YOU'RE": "I'M", "YOU'D": "I'D", 'HATE': 'LOVE', 'YOUR': 'MY', "I'LL": "YOU'LL", 'NO': 'YES',
                     'WHY': 'BECAUSE', 'YOU': 'ME', 'LOVE': 'HATE', 'I': 'YOU', 'MINE': 'YOURS', 'YOURSELF': 'MYSELF',
                     'DISLIKE': 'LIKE', "I'M": "YOU'RE", 'ME': 'YOU', 'MYSELF': 'YOURSELF', 'LIKE': 'DISLIKE',
                     "I'D": "YOU'D", "YOU'VE": "I'VE", 'YES': 'NO', 'MY': 'YOUR'}
