import os , sys
from dulwich.repo import Repo

clone = ' git clone http://github.com/NeverSinkDev/NeverSink-Filter.git .'

user_folder = os.environ['USERPROFILE']
filter_route = user_folder +'\\Documents\\My Games\\Path of Exile'

print "Downloading Neversink's Item Filter."
os.chdir(filter_route) # Specifying the path where the cloned project has to be copied
os.system(clone) # Cloning
os.system('git pull')

print "Filter Downloaded and moved to your Path of Exile filter folder. Enjoy and thanks Neversink with a beer."