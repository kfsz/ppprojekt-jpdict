# adds to django database objects from xml
#set DJANGO_SETTINGS_MODULE=khaoohprojekt.settings
#python -m idlelib <script_to_edit> 
#doesn't parse <misc> like <misc>&arch;</misc>  - coming in 1.01

#wordentry = Word(word = "朝", reading = "あさ")
#tlentry = WordTL(word = wordentry, translation = "morning", word_type = "noun")

import xml.etree.ElementTree as ET
import django

django.setup()

from dict.models import Word, WordTL

tree = ET.parse('JMdict_e.xml')
#test xml

root = tree.getroot()

for entry in root:
    #print(entry)
    
    #what if word is null?
    #no link in that case - let's fix!
    
    common = False #check if common word (for main)
    dbword = ''
    dbalterword = ''
    dbreading = ''
    dbalterreading = ''
    
    #main word
    word = entry.find('k_ele')
    if word is not None:
        for w in word.findall('keb'):
            dbword = w.text
        if word.findall('ke_pri'):
            common = True
        #print("main word - " + dbword) #test
    
    for word in entry.findall('k_ele')[1:]:
        for w in word.findall('keb'):
            dbalterword = dbalterword + w.text + ', '
            
    if len(dbalterword) > 2:
        dbalterword = dbalterword[:-2]
        
    #print("words - " + dbalterword) #test

    #main reading
    reading = entry.find('r_ele')
    if reading is not None:
        for r in reading.findall('reb'):
            dbreading = r.text
        #print("main reading - " + dbreading) #test
        
    if dbword == '':
        dbword = dbreading
    
    for reading in entry.findall('r_ele')[1:]:
        for r in reading.findall('reb'):
            dbalterreading = dbalterreading + r.text + ', '
            
    if len(dbalterreading) > 2:
        dbalterreading = dbalterreading[:-2]
        
    #print("readings - " + dbalterreading) #test

    wordentry = Word(word = dbword, reading = dbreading, alterword = dbalterword, alterreading = dbalterreading, common=common)
    wordentry.save()
    dbid=wordentry.id

#now for translations (separate model, and entry)
    for sense in entry.findall('sense'):
        dbgloss = ''
        dbtype = ''
        
        for pos in sense.findall('pos'):
            dbtype = dbtype + pos.text + ', '
            
        if len(dbtype) > 2:
            dbtype = dbtype[:-2]
           
        for gloss in sense.findall('gloss'):
            dbgloss = dbgloss + gloss.text + ', '
            
        if len(dbgloss) > 2:
            dbgloss = dbgloss[:-2]

       #print("wtype - " + dbtype) #test    
        #print("glosses - " + dbgloss) #test
        
        key = Word.objects.get(id=dbid)
        tlentry = WordTL(word = key, translation = dbgloss, word_type = dbtype)
        tlentry.save()
        
    print(dbword)    #test
    print('\n')

print('done!')            
#finished

    
