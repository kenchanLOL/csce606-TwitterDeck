# csce606-TwitterDeck
A Twitter Deck clone for digital humanitarian purpose 

## Installation
1. conda create -y -n crisisdeck python-3.8
2. conda activate crisisdeck
3. pip install -r requirements.txt
4. python main.py

### Reminder of PyQt
After building new UI by running 
```
pyside6-uic .\main.ui -o .\modules\ui_main.py
```
modify these two import statements
```
# from twitter_deck import TwitterDeck
# import resources_rc
```
into the following two
```
from widgets import TwitterDeck
from . resources_rc import *
```

