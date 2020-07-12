# This is a program in which you enter a year to find out which emperor was ruling the Roman Empire that year #

# To make sure that the code returns to its start after every entry,
# I chose to use "while True" in this version.
# But in upcoming versions I envision to replace this cumbersome structure
# with a def enteryear() function.

# First we print the notice to its users #
print("""Dear Mr/Ms, this is a program in which you enter a year
    to find out which Roman emperor was in place at the time.""")
print("""Enter a Common Era (C.E. or A.D.) year as a positive number.
    And enter a Before Common Era (B.C.E.) year as one negative.""")
print("""Do note, however, that the Empire was founded by Augustus in 27 BC,
    and had its Western half destroyed by the Germanic invaders in 476 AD.""")

# Then we ask for the year they are interested in #
while True:
    print("""\n
    Now choose the year you are interested in, such as \"-15\" or \"309\".""")
    year = int(input("Enter the year:"))

# And now we discard the incorrect years #
    if year < -27:
        print("It was the Roman Republic then. The Empire was created in 27 B.C.E.")
    elif year > 476:
        print("The Western Empire fell in 476 A.D., but the Eastern half endured until 1453.")

# And produce the name of the Emperor(s) concerned #
    elif year >= -27 and year < 14:
        print("Caesar Augustus was in place. He ruled from 27 BC to 14 AD.")
    elif year == 14:
        print("""Caesar Augustus was in place until August,
        then he was succeeded by Tiberius.
        The former ruled from 27 BC to 14 AD.""")
    elif year > 14 and year < 37:
        print("Tiberius was in place. He ruled from 14 to 37 AD.")
    elif year == 37:
        print("""Tiberius was in place until March,
        then he was succeeded by Caligula.
        The former ruled from 14 to 37 AD.""")
    elif year > 37 and year < 41:
        print("Caligula was in place. He ruled from 37 to 41 AD.")
    elif year == 41:
        print("""Caligula was in place until January,
        then he was succeeded by Claudius.
        The former ruled from 37 to 41 AD.""")
    elif year > 41 and year < 54:
        print("Claudius was in place. He ruled from 41 to 54 AD.")
    elif year == 54:
        print("""Claudius was in place until October,
        then he was succeeded by Nero.
        The former ruled from 41 to 54 AD.""")
    elif year > 54 and year < 68:
        print("Nero was in place. He ruled from 54 to 68 AD.")
    elif year == 68:
        print("""Nero was in place until June,
        then he was succeeded by Galba.
        The former ruled from 54 to 68 AD.""")
    elif year == 69:
        print("""Galba was in place until January,
        then he was succeeded by Otho.
        \n
        Otho ruled until April,
        then he was succeeded Vitellius.
        \n
        Vitellius ruled until December,
        then he was succeeded by Vespasian.""")
    elif year > 69 and year < 79:
        print("Vespasian was in place. He ruled from 69 to 79 AD.")
    elif year == 79:
        print("""Vespasian was in place until June,
        then he was succeeded by Titus.
        The former ruled from 69 to 79 AD.""")
    elif year > 79 and year < 81:
        print("Titus was in place. He ruled from 79 to 81 AD.")
    elif year == 81:
        print("""Titus was in place until September,
        then he was succeeded by Domitian.
        The former ruled from 79 to 81 AD.""")
    elif year > 81 and year < 96:
        print("Domitian was in place. He ruled from 81 to 96 AD.")
    elif year == 96:
        print("""Domitian ruled until September,
        then he was succeeded by Nerva.
        The former ruled from 81 to 96 AD.""")
    elif year > 96 and year < 98:
        print("Nerva was in place. He ruled from 96 to 98 AD.")
    elif year == 98:
        print("""Nerva was in place until January,
        then he was succeeded by Trajan.
        The former ruled from 96 to 98 AD.""")
    elif year > 98 and year < 117:
        print("Trajan was in place. He ruled from 98 to 117 AD.")
    elif year == 117:
        print("""Trajan was in place until August,
        then he was succeeded by Hadrian.
        The former ruled from 98 to 117 AD.""")
    elif year > 117 and year < 138:
        print("Hadrian was in place. He ruled from 117 to 138 AD.")
    elif year == 138:
        print("""Hadrian was in place until July,
        then he was succeeded by Antonius Pius.
        The former ruled from 117 to 138 AD.""")
    elif year > 138 and year < 161:
        print("Antonius Pius was in place. He ruled from 138 to 161 AD.")
    elif year == 161:
        print("""Antonius Pius ruled until March,
        then he was co-succeeded by Marcus Aurelius and Lucius Verus.
        Pius ruled from 138 to 161 AD.""")
    elif year > 161 and year < 169:
        print("""Marcus Aurelius and Lucius Verus were in place as co-emperors.
        The former ruled from 161 to 180 AD.
        The latter ruled from 161 to 169 AD.""")
    elif year == 169:
        print("""Co-emperor Lucius Verus was in place until January,
        afterwards Marcus Aurelius ruled solely.
        The former ruled from 161 to 169 AD.
        The latter ruled from 161 to 180 AD.""")
    elif year > 169 and year < 177:
        print("Marcus Aurelius was in place. He ruled from 161 to 180 AD.")
    elif year == 177:
        print("""Marcus Aurelius was in place.
        Commodus began his rule as co-emperor.
        The former ruled from 161 to 180 AD.""")
    elif year > 177 and year < 180:
        print("""Marcus Aurelius and Commodus were in place as co-emperors.
        The former ruled from 161 to 180 AD.
        The latter ruled from 177 to 192 AD.""")
    elif year == 180:
        print("""Marcus Aurelius was in place until March,
        then co-emperor Commodus ruled solely.
        The former ruled from 161 to 180 AD.
        The latter ruled from 177 to 192 AD.""")
    elif year > 180 and year < 192:
        print("Commodus was in place. He ruled from 177 to 192 AD.")
    elif year == 192:
        print("""Commodus was in place until December,
        then he was succeeded by Pertinax.
        The former ruled from 177 to 192 AD.""")
    elif year == 193:
        print("""Pertinax was in place until March,
        then he was succeeded by Didius Julianus.
        The former ruled from December 192 to March 193.
        \n
        Julianus was in place until June,
        then he was succeeded by Septimius Severus.""")
    elif year > 193 and year < 211:
        print("Septimius Severus was in place. He ruled from 193 to 211 AD.")
    elif year == 211:
        print("""Septimius Severus was in place until February,
        then he was co-succeeded by Caracalla and Geta.
        Severus ruled from 193 to 211 AD.
        \n
        Geta was in place until December,
        then Caracalla ruled solely.""")
    elif year > 211 and year < 217:
        print("Caracalla was in place. He ruled from 211 to 217 AD.")
    elif year == 217:
        print("""Caracalla was in place until April,
        then he was succeeded by Macrinus.
        The former ruled from 211 to 217 AD.""")
    elif year == 218:
        print("""Macrinus was in place until June,
        then he was succeeded by Elagabalus.
        The former ruled from April 217 to June 218.""")
    elif year > 218 and year < 222:
        print("Elagabalus was in place. He ruled from 218 to 222 AD.")
    elif year == 222:
        print("""Elagabalus was in place until March,
        then he was succeeded by Severus Alexander.
        The former ruled from 218 to 222 AD.""")
    elif year > 222 and year < 235:
        print("Severus Alexander was in place. He ruled from 222 to 235 AD.")
    elif year == 235:
        print("""Severus Alexander was in place until March,
        then he was succeeded by Maximinus Thrax.
        The former ruled from 222 to 235 AD.""")
    elif year > 235 and year < 238:
        print("Maximinus Thrax was in place. He ruled from 235 to 238 AD.")
    elif year == 238:
        print("""Maximinus Thrax was in place until May.
        He ruled from 235 to 238 AD.
        \n
        Gordian I and Gordiann II declared themselves co-emperors in March.
        They were in place until April.
        \n
        Pupienus and Balbinus declared themselves co-emperors in April.
        They were in place until July.
        \n
        Gordian III succeeded them in July.""")
    elif year > 238 and year < 244:
        print("Gordian III was in place. He ruled from 238 to 244 AD.")
    elif year == 244:
        print("""Gordian III was in place until February,
        then he was succeeded by Philip the Arab.
        The former ruled from 238 to 244 AD.""")
    elif year > 244 and year < 249:
        print("Philip the Arab was in place. He ruled from 244 to 249 AD.")
    elif year == 249:
        print("""Philip the Arab was in place until September,
        then he was succeeded by Decius.
        The former ruled from 244 to 249 AD.""")
    elif year == 250:
        print("Decius was in place. He ruled from 249 to 251.")
    elif year == 251:
        print("""Decius and Herennius Etruscus were in place as co-emperors until June.
        The former ruled from 249 to 251 AD.
        The latter ruled from May to June 251.
        \n
        Trebonianus Gallus and Hostilian co-succeeded them.
        Hostilian was in place until November,
        and then he was succeeded by co-emperor Volusianus.""")
    elif year > 251 and year < 253:
        print("""Trebonianus Gallus and Volusianus were in place as co-emperors.
        The former ruled from 251 to 253 AD.
        The latter ruled from 251 to 253 AD.""")
    elif year == 253:
        print("""Trebonianus Gallus and Volusianus were in place until August,
        then they were succeeded by Aemilianus.
        Gallus and Volusianus co-ruled from 251 to 253 AD.
        \n
        Aemilianus was in place until September,
        then he was co-succeeded by Valerian and Gallienus.""")
    elif year > 253 and year < 260:
        print("""Valerian annd Gallienus were in place as co-emperors.
        The former ruled from 253 to 260 AD.
        The latter ruled from 253 to 268 AD.""")
    elif year == 260:
        print("""Co-emperor Valerian was in place until spring,
        then Gallienus ruled solely.
        The former ruled from 253 to 260 AD.""")
    elif year > 260 and year < 268:
        print("Gallienus was in place. He ruled from 253 to 268 AD.")
    elif year == 268:
        print("""Gallienus was in place until September,
        then he was succeeded by Claudius Gothicus.
        The former ruled from 253 to 268 AD.""")
    elif year > 268 and year < 270:
        print("Claudius Gothicus was in place. He ruled from 268 to 270 AD.")
    elif year == 270:
        print("""Claudius Gothicus was in place until January,
        then he was succeeded by Quintillus.
        The former ruled from 268 to 270 AD.
        \n
        Quintillus was in place until April,
        then he was succeeded by Aurelian.""")
    elif year > 270 and year < 275:
        print("Aurelian was in place. He ruled from 270 to 275 AD.")
    elif year == 275:
        print("""Aurelian was in place until fall,
        then he was succeeded by Tacitus.
        The former ruled from 270 to 275 AD.""")
    elif year == 276:
        print("""Tacitus was in place until June,
        then he was succeeded by Florianus.
        The former ruled from 275 to 276 AD.
        \n
        Florianus was in place until September,
        then he was succeeded by Probus.""")
    elif year > 276 and year < 282:
        print("Probus was in place. He ruled from 276 to 282 AD.")
    elif year == 282:
        print("""Probus was in place until September,
        then he was succeeded by Carus.
        The former ruled from 276 to 282 AD.""")
    elif year == 283:
        print("""Carus was in place until mid-year,
        then he was co-succeeded by Carinus and Numerian.
        Carus ruled from 282 to 283 AD.""")
    elif year == 284:
        print("""Co-emperor Numerian was in place until November,
        then Carinus ruled solely.
        The former ruled from 283 to 284 AD.
        \n
        In November, Diocletian declared himself emperor.""")
    elif year == 285:
        print("""Carinus was in place until July,
        then he was succeeded by Diocletian.
        The former ruled from 283 to 285 AD.""")
    elif year > 285 and year < 476:
        print("""Diocletian declared in 286 the 'tetrarchy',
        which created two senior emperors and two junior ones.
        Under this system there was one Augustus in the West,
        and a parallel one in the East.
        \n
        Therefore, please enter which half you are interested in.""")
        section = input("\"East\" or \"West\"? Enter here:")
        if section == "East":
            if year > 285 and year < 305:
                print("Diocletian was in place. He ruled from 284 to 305 AD.")
            elif year == 305:
                print("""Diocletian was in place until May,
                then he was succeeded by Galerius.
                The former ruled from 284 to 305 AD.""")
            elif year > 305 and year < 311:
                print("Galerius was in place. He ruled from 305 to 311 AD.")
            elif year == 311:
                print("""Galerius was in place until May,
                then he was succeeded by competing Maximinus Daia and Licinius.
                Galerius ruled from 305 to 311 AD.""")
            elif year > 311 and year < 313:
                print("Maximinus Daia was competing with Licinius.")
            elif year == 313:
                print("""Maximinus Daia was in place until May,
                then he was defeated by Licinius.
                The former ruled from 311 to 313 AD.""")
            elif year > 313 and year < 324:
                print("Licinius was in place. He ruled from 311 to 324 AD.")
            elif year == 324:
                print("""Licinius was in place until September,
                then he was succeeded by Constantine I.
                The former ruled from 311 to 324 AD.""")
            elif year > 324 and year < 337:
                print("Constantine I was in place. He ruled solely from 324 to 337 AD.")
            elif year == 337:
                print("""Constantine I was in place until September,
                then he was succeeded by Constantius II.
                The former ruled from 324 to 337 AD.""")
            elif year > 337 and year < 361:
                print("Constantius II was in place. He ruled from 337 to 361 AD.")
            elif year == 361:
                print("""Constantius II was in place until November,
                then he was succeeded by Julian.
                The former ruled from 337 to 361 AD.""")
            elif year > 361 and year < 363:
                print("Julian was in place. He ruled from 361 to 363 AD.")
            elif year == 363:
                print("""Julian was in place until June,
                then he was succeeded by Jovian.
                The former ruled from 361 to 363 AD.""")
            elif year == 364:
                print("""Jovian was in place until February,
                then he was succeeded by Valentinian I.
                The former ruled from 363 to 364 AD.
                \n
                Valentinian I relinquished the Eastern half in March,
                and chose Valens as his co-emperor.""")
            elif year > 364 and year < 378:
                print("Valens was in place. He ruled from 364 to 378 AD.")
            elif year == 378:
                print("""Valens was in place until August,
                then he was succeeded by Theodosius I.
                The former ruled from 364 to 378 AD.""")
            elif year > 378 and year < 395:
                print("Theodosius I was in place. He ruled from 378 to 395 AD.")
            elif year == 395:
                print("""Theodosius I was in place until January,
                then he was succeeded by Arcadius.
                The former ruled from 378 to 395 AD.""")
            elif year > 395 and year < 408:
                print("Arcadius was in place. He ruled from 395 to 408 AD.")
            elif year == 408:
                print("""Arcadius was in place until May,
                then he was succeeded by Theodosius II.
                The former ruled from 395 to 408 AD.""")
            elif year > 408 and year < 450:
                print("Theodosius II was in place. He ruled from 408 to 450 AD.")
            elif year == 450:
                print("""Theodosius II was in place until July,
                then he was succeeded by Marcian.
                The former ruled from 408 to 450 AD.""")
            elif year > 450 and year < 457:
                print("Marcian was in place. He ruled from 450 to 457 AD.")
            elif year == 457:
                print("""Marcian was in place until January,
                then he was succeeded by Leo I.
                The former ruled from 450 to 457 AD.""")
            elif year > 457 and year < 474:
                print("Leo I was in place. He ruled from 457 to 474 AD.")
            elif year == 474:
                print("""Leo I was in place until January,
                then he was succeeded by Leo II.
                The former ruled from 457 to 474 AD.
                \n
                Leo II was in place until November,
                then he was succeeded by Zeno.""")
            elif year > 474 and year <= 476:
                print("""Zeno was in place in the East.
                He ruled from 474 to 491 AD.
                \n
                However, during his reign in 476 AD,
                the Western Empire fell under Romulus Augustus.""")
        elif section == "West":
            print("This part is still under construction. Sorry.")

# Ask if the user would like to enter another year (Ignore for now) #
def useagain():
    while True:
        print("\n"
        "If you want to enter another year, enter \"Yes\"; if not, enter \"No\".")
        again = input("Another year? Enter:")
        if again == "No":
            print("So be it.")
        elif again == "Yes":
            return enteryear()

