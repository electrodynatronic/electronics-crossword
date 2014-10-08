#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, re, time, string
from copy import copy as duplicate
#http://bryanhelmig.com/python-crossword-puzzle-generator/

# optional, speeds up by a factor of 4
#import psyco
#psyco.full()
 
class Crossword(object):
    def __init__(self, cols, rows, empty = '-', maxloops = 2000, available_words=[]):
        self.cols = cols
        self.rows = rows
        self.empty = empty
        self.maxloops = maxloops
        self.available_words = available_words
        self.randomize_word_list()
        self.current_word_list = []
        self.debug = 0
        self.clear_grid()
 
    def clear_grid(self): # initialize grid and fill with empty character
        self.grid = []
        for i in range(self.rows):
            ea_row = []
            for j in range(self.cols):
                ea_row.append(self.empty)
            self.grid.append(ea_row)
 
    def randomize_word_list(self): # also resets words and sorts by length
        temp_list = []
        for word in self.available_words:
            if isinstance(word, Word):
                temp_list.append(Word(word.word, word.clue))
            else:
                temp_list.append(Word(word[0], word[1]))
        random.shuffle(temp_list) # randomize word list
        temp_list.sort(key=lambda i: len(i.word), reverse=True) # sort by length
        self.available_words = temp_list
 
    def compute_crossword(self, time_permitted = 1.00, spins=2):
        time_permitted = float(time_permitted)
 
        count = 0
        copy = Crossword(self.cols, self.rows, self.empty, self.maxloops, self.available_words)
 
        start_full = float(time.time())
        while (float(time.time()) - start_full) < time_permitted or count == 0: # only run for x seconds
            self.debug += 1
            copy.current_word_list = []
            copy.clear_grid()
            copy.randomize_word_list()
            x = 0
            while x < spins: # spins; 2 seems to be plenty
                for word in copy.available_words:
                    if word not in copy.current_word_list:
                        copy.fit_and_add(word)
                x += 1
            #print copy.solution()
            #print len(copy.current_word_list), len(self.current_word_list), self.debug
            # buffer the best crossword by comparing placed words
            if len(copy.current_word_list) > len(self.current_word_list):
                self.current_word_list = copy.current_word_list
                self.grid = copy.grid
            count += 1
        return
 
    def suggest_coord(self, word):
        count = 0
        coordlist = []
        glc = -1
        for given_letter in word.word: # cycle through letters in word
            glc += 1
            rowc = 0
            for row in self.grid: # cycle through rows
                rowc += 1
                colc = 0
                for cell in row: # cycle through  letters in rows
                    colc += 1
                    if given_letter == cell: # check match letter in word to letters in row
                        try: # suggest vertical placement
                            if rowc - glc > 0: # make sure we're not suggesting a starting point off the grid
                                if ((rowc - glc) + word.length) <= self.rows: # make sure word doesn't go off of grid
                                    coordlist.append([colc, rowc - glc, 1, colc + (rowc - glc), 0])
                        except: pass
                        try: # suggest horizontal placement
                            if colc - glc > 0: # make sure we're not suggesting a starting point off the grid
                                if ((colc - glc) + word.length) <= self.cols: # make sure word doesn't go off of grid
                                    coordlist.append([colc - glc, rowc, 0, rowc + (colc - glc), 0])
                        except: pass
        # example: coordlist[0] = [col, row, vertical, col + row, score]
        #print word.word
        #print coordlist
        new_coordlist = self.sort_coordlist(coordlist, word)
        #print new_coordlist
        return new_coordlist
 
    def sort_coordlist(self, coordlist, word): # give each coordinate a score, then sort
        new_coordlist = []
        for coord in coordlist:
            col, row, vertical = coord[0], coord[1], coord[2]
            coord[4] = self.check_fit_score(col, row, vertical, word) # checking scores
            if coord[4]: # 0 scores are filtered
                new_coordlist.append(coord)
        random.shuffle(new_coordlist) # randomize coord list; why not?
        new_coordlist.sort(key=lambda i: i[4], reverse=True) # put the best scores first
        return new_coordlist
 
    def fit_and_add(self, word): # doesn't really check fit except for the first word; otherwise just adds if score is good
        fit = False
        count = 0
        coordlist = self.suggest_coord(word)
 
        while not fit and count < self.maxloops:
 
            if len(self.current_word_list) == 0: # this is the first word: the seed
                # top left seed of longest word yields best results (maybe override)
                vertical, col, row = random.randrange(0, 2), 1, 1
                '''
                # optional center seed method, slower and less keyword placement
                if vertical:
                    col = int(round((self.cols + 1)/2, 0))
                    row = int(round((self.rows + 1)/2, 0)) - int(round((word.length + 1)/2, 0))
                else:
                    col = int(round((self.cols + 1)/2, 0)) - int(round((word.length + 1)/2, 0))
                    row = int(round((self.rows + 1)/2, 0))
                # completely random seed method
                col = random.randrange(1, self.cols + 1)
                row = random.randrange(1, self.rows + 1)
                '''
 
                if self.check_fit_score(col, row, vertical, word):
                    fit = True
                    self.set_word(col, row, vertical, word, force=True)
            else: # a subsquent words have scores calculated
                try:
                    col, row, vertical = coordlist[count][0], coordlist[count][1], coordlist[count][2]
                except IndexError: return # no more cordinates, stop trying to fit
 
                if coordlist[count][4]: # already filtered these out, but double check
                    fit = True
                    self.set_word(col, row, vertical, word, force=True)
 
            count += 1
        return
 
    def check_fit_score(self, col, row, vertical, word):
        '''
        And return score (0 signifies no fit). 1 means a fit, 2+ means a cross.
 
        The more crosses the better.
        '''
        if col < 1 or row < 1:
            return 0
 
        count, score = 1, 1 # give score a standard value of 1, will override with 0 if collisions detected
        for letter in word.word:           
            try:
                active_cell = self.get_cell(col, row)
            except IndexError:
                return 0
 
            if active_cell == self.empty or active_cell == letter:
                pass
            else:
                return 0
 
            if active_cell == letter:
                score += 1
 
            if vertical:
                # check surroundings
                if active_cell != letter: # don't check surroundings if cross point
                    if not self.check_if_cell_clear(col+1, row): # check right cell
                        return 0
 
                    if not self.check_if_cell_clear(col-1, row): # check left cell
                        return 0
 
                if count == 1: # check top cell only on first letter
                    if not self.check_if_cell_clear(col, row-1):
                        return 0
 
                if count == len(word.word): # check bottom cell only on last letter
                    if not self.check_if_cell_clear(col, row+1):
                        return 0
            else: # else horizontal
                # check surroundings
                if active_cell != letter: # don't check surroundings if cross point
                    if not self.check_if_cell_clear(col, row-1): # check top cell
                        return 0
 
                    if not self.check_if_cell_clear(col, row+1): # check bottom cell
                        return 0
 
                if count == 1: # check left cell only on first letter
                    if not self.check_if_cell_clear(col-1, row):
                        return 0
 
                if count == len(word.word): # check right cell only on last letter
                    if not self.check_if_cell_clear(col+1, row):
                        return 0
 
 
            if vertical: # progress to next letter and position
                row += 1
            else: # else horizontal
                col += 1
 
            count += 1
 
        return score
 
    def set_word(self, col, row, vertical, word, force=False): # also adds word to word list
        if force:
            word.col = col
            word.row = row
            word.vertical = vertical
            self.current_word_list.append(word)
 
            for letter in word.word:
                self.set_cell(col, row, letter)
                if vertical:
                    row += 1
                else:
                    col += 1
        return
 
    def set_cell(self, col, row, value):
        self.grid[row-1][col-1] = value
 
    def get_cell(self, col, row):
        return self.grid[row-1][col-1]
 
    def check_if_cell_clear(self, col, row):
        try:
            cell = self.get_cell(col, row)
            if cell == self.empty:
                return True
        except IndexError:
            pass
        return False
 
    def solution(self): # return solution grid
        outStr = ""
        for r in range(self.rows):
            for c in self.grid[r]:
                outStr += '%s ' % c
            outStr += '\n'
        return outStr
 
    def word_find(self): # return solution grid
        outStr = ""
        for r in range(self.rows):
            for c in self.grid[r]:
                if c == self.empty:
                    outStr += '%s ' % string.lowercase[random.randint(0,len(string.lowercase)-1)]
                else:
                    outStr += '%s ' % c
            outStr += '\n'
        return outStr
 
    def order_number_words(self): # orders words and applies numbering system to them
        self.current_word_list.sort(key=lambda i: (i.col + i.row))
        count, icount = 1, 1
        for word in self.current_word_list:
            word.number = count
            if icount < len(self.current_word_list):
                if word.col == self.current_word_list[icount].col and word.row == self.current_word_list[icount].row:
                    pass
                else:
                    count += 1
            icount += 1
 
    def display(self, order=True): # return (and order/number wordlist) the grid minus the words adding the numbers
        outStr = ""
        if order:
            self.order_number_words()
 
        copy = self
 
        for word in self.current_word_list:
            copy.set_cell(word.col, word.row, word.number)
 
        for r in range(copy.rows):
            for c in copy.grid[r]:
                outStr += '%s ' % c
            outStr += '\n'
 
        outStr = re.sub(r'[a-z]', u'⫍', outStr)
        return outStr
 
    def word_bank(self):
        outStr = ''
        temp_list = duplicate(self.current_word_list)
        random.shuffle(temp_list) # randomize word list
        for word in temp_list:
            outStr += '%s\n' % word.word
        return outStr
 
    def legend(self): # must order first
        outStr = ''
        for word in self.current_word_list:
            outStr += '%d. (%d,%d) %s: %s\n' % (word.number, word.col, word.row, word.down_across(), word.clue )
        return outStr
 
class Word(object):
    def __init__(self, word=None, clue=None):
        self.word = re.sub(r'\s', '', word.lower())
        self.clue = clue
        self.length = len(self.word)
        # the below are set when placed on board
        self.row = None
        self.col = None
        self.vertical = None
        self.number = None
 
    def down_across(self): # return down or across
        if self.vertical:
            return 'down'
        else:
            return 'across'
 
    def __repr__(self):
        return self.word
 
### end class, start execution
#start_full = float(time.time())
 
word_list = ['electron', 'define electron'], \
    ['coulomb', 'A fundamental unit of electrical charge, and is also the SI derived unit of electric charge (symbol: Q or q). It is equal to the charge of approximately 6.241×1018 electrons.'], \
    ['Ampere', 'A measure of the amount of electric charge passing a point in an electric circuit per unit time. 1 coulomb per second.'], \
    ['Watt', 'A joule per second.'], \
    ['milli', 'A prefix in the metric system denoting a factor of one thousandth (10-3).'], \
    ['micro', 'A prefix in the metric system denoting a factor of one millionth (10-6).'], \
    ['nano', 'A prefix in the metric system denoting a factor of one billionth (10-9).'], \
    ['pico', 'A prefix in the metric system denoting a factor of one trillionth (10-12).'], \
    ['femto', 'A prefix in the metric system denoting a factor of one quadrillionth (10-15).'], \
    ['atto', 'A prefix in the metric system denoting a factor of one quintillionth (10-18).'], \
    ['zepto', 'A prefix in the metric system denoting a factor of one sextillionth (10-21).'], \
    ['yocto', 'A prefix in the metric system denoting a factor of one septillionth (10-24).'], \
    ['binary', 'two states'], \
    ['transistor', 'A semiconductor device used to amplify and switch electronic signals and electrical power.'], \
    ['amplifier', 'An electronic device that increase the power of a signal.'], \
    ['inductance', 'he property of a conductor by which a change in current flowing through it "induces" (creates) a voltage (electromotive force) in both the conductor itself and in any nearby conductors.'], \
    ['capacitance', 'define capacitance'], \
    ['impedance', 'define impedance'], \
    ['resistance', 'define resistance'], \
    ['resistor', 'define resistor'], \
    ['capacitor', 'define capacitor'], \
    ['inductor', 'define inductor'], \
    ['kilo', 'define kilo'], \
    ['Mega', 'define Mega'], \
    ['Giga', 'define Giga'], \
    ['Tera', 'define Tera'], \
    ['Peta', 'define Peta'], \
    ['bit', 'define bit'], \
    ['byte', 'define byte'], \
    ['diode', 'define diode'], \
    ['LED', 'define LED'], \
    ['triac', 'define triac'], \
    ['FET', 'define FET'], \
    ['MOSFET', 'define MOSFET'], \
    ['NPN', 'define NPN'], \
    ['PNP', 'define PNP'], \
    ['spectrum', 'define spectrum'], \
    ['spectra', 'define spectra'], \
    ['Fourier', 'define Fourier'], \
    ['FFT', 'define FFT'], \
    ['potentiometer', 'define potentiometer'], \
    ['digital', 'define digital'], \
    ['analog', 'define analog'], \
    ['gain','define gain'], \
    ['bridge','define bridge'], \
    ['rectifier','define rectifier'], \
    ['filter','define filter'], \
    ['sawtooth','define sawtooth'], \
    ['sine','define sine'], \
    ['waveform','define waveform'], \
    ['current','define current'], \
    ['Kirchhoff','define Kirchhoff'], \
    ['Faraday','define Faraday'], \
    ['farad','define farad'], \
    ['Norton','define Norton'], \
    ['Thevenin','define Thevenin'], \
    ['cable','define cable'], \
    ['coaxial','define coaxial'], \
    ['Ohm','define Ohm'], \
    ['DMM','define DMM'], \
    ['silicon','define silicon'], \
    ['dopant','define dopant'], \
    ['orbital','define orbital'], \
    ['Centigrus','A real unit for measuring temperature. Invented at WCJC by Blake Folmar.'], \
    ['arduino','define arduino'], \
    ['Atmel','define Atmel'], \
    ['AVR','define AVR'], \
    ['PIC','define PIC'], \
    ['picaxe','define picaxe'], \
    ['ARM','define ARM'], \
    ['RISC','define RISC'], \
    ['MIPS','define MIPS'], \
    ['x86','define x86'], \
    ['Intel','define Intel'], \
    ['Fairchild','define Fairchild'], \
    ['TI','define TI'], \
    ['National','define National Semiconductor'], \
    ['semiconductor','define semiconductor'], \
    ['germanium','define germanium'], \
    ['Linux','define Linux'], \
    ['Microsoft','define Microsoft'], \
    ['Windows','define Windows'], \
    ['Macintosh','define Macintosh'], \
    ['Apple','define Apple'], \
    ['BSD','define BSD'], \
    ['Unix','define Unix'], \
    ['Posix','define Posix'], \
    ['oscillator','define oscillator'], \
    ['triangle','define triangle'], \
    ['square','define square'], \
    ['breakdown','define breakdown'], \
    ['Tesla','define Tesla'], \
    ['Gauss','define Gauss'], \
    ['plot','define plot'], \
    ['data','define data'], \
    ['network','define network'], \
    ['Maxwell','define Maxwell'], \
    ['feedback','define feedback'], \
    ['feedforward','define feedforward'], \
    ['PID','define PID'], \
    ['Lucent','define Lucent'], \
    ['BellLabs','define BellLabs'], \
    ['Alcatel','define Alcatel'], \
    ['HP','define HP'], \
    ['HewlettPackard','define HewlettPackard'], \
    ['Agilent','define Agilent'], \
    ['oscilloscope','define oscilloscope'], \
    ['snubber','define snubber'], \
    ['RAM','define RAM'], \
    ['ROM','define ROM'], \
    ['Flash','define Flash'], \
    ['serial','define serial'], \
    ['USB','define USB'], \
    ['IEEE','define IEEE'], \
    ['Firewire','define Firewire'], \
    ['parallel','define parallel'], \
    ['Chua','define Chua'], \
    ['PROM','define PROM'], \
    ['EPROM','define EPROM'], \
    ['EEPROM','define EEPROM'], \
    ['FPGA','define FPGA'], \
    ['VHDL','define VHDL'], \
    ['Verilog','define Verilog'], \
    ['PLD','define PLD'], \
    ['CPLD','define CPLD'], \
    ['linear','define linear'], \
    ['logarithmic','define logarithmic'], \
    ['exponential','define exponential'], \
    ['polynomial','define polynomial'], \
    ['RMS','define RMS'], \
    ['Power','define Power'], \
    ['invert','define invert'], \
    ['phase','define phase'], \
    ['agc','define agc'], \
    ['control','define control'], \
    ['logic','define logic'], \
    ['microprocessor','define microprocessor'], \
    ['microcontroller','define microcontroller'], \
    ['architecture','define architecture'], \
    ['alu','define alu'], \
    ['register','define register'], \
    ['word','define word'], \
    ['bitmask','define bitmask'], \
    ['variable','define variable'], \
    ['static','define static'], \
    ['dynamic','define dynamic'], \
    ['polar','define polar'], \
    ['data','define data'], \
    ['type','define type'], \
    ['compiler','define compiler'], \
    ['assembler','define assembler'], \
    ['opcode','define opcode'], \
    ['memory','define memory'], \
    ['PLC','define PLC'], \
    ['relay','define relay'], \
    ['SSR','define SSR'], \
    ['diac','define diac'], \
    ['IGBT','define IGBT'], \
    ['macro','define macro'], \
    ['ASCII','define ASCII'], \
    ['unicode','define unicode'], \
    ['encode','define encode'], \
    ['protocol','define protocol'], \
    ['circuit','define circuit'], \
    ['PCB','define PCB'], \
    ['transformer','define transformer'], \
    ['flux','define flux'], \
    ['lumen','define lumen'], \
    ['proportional','define proportional'], \
    ['Hitachi','define Hitachi'], \
    ['decibel','define decibel'], \
    ['bel','define bel'], \
    ['encrypt','The process of encoding messages or information in such a way that only authorized parties can read it.'], \
    ['ethernet','IEEE 802.3, RJ-45, Gigabit, etc.'], \
    ['antenna','A transducer for sending or receiving waves.'], \
    ['transducer','A device that converts a signal in one form of energy to another form of energy.'], \
    ['login','signon'], \
    ['password','Authentication token.'], \
    ['URL','TLA for web address. See RFC 3986'], \
    ['internet','Not a truck. A series of tubes.'], \
    ['DARPA','Military agency responsible for cat videos.'], \
    ['satellite','A thing that kind of hangs around. There are a bunch of them overhead.'], \
    ['apogee','The big Apsis. Not perihelion, the other one.'], \
    ['perigee','The little Apsis. Not aphelion, the other one.'], \
    ['GPS','Satnav'], \
    ['latency','A measure of the time delay experienced by a system.'], \
    ['timeout','A delay.'], \
    ['band','A small section of the radio spectrum.'], \
    ['bandwidth','A measure of the width of a range of frequencies, measured in hertz.'], \
    ['axial','Two leads, one on each end, pointing in opposite directions.'], \
    ['radial','Two leads, both on the same end.'], \
    ['sink','A heat ___.'], \
    ['NO','"Make" contacts. Form A contacts.'], \
    ['NC','"Break" contacts. Form B contacts.'], \
    ['JFET','Electric charge flows through a semiconducting channel between source and drain terminals.'], \
    ['Ground','The reference point in an electrical circuit from which voltages are measured, a common return path for electric current, or a direct physical connection to the Earth.'], \
    ['Vcc','Collector supply line voltage in a common NPN circuit.'], \
    ['TTL','A mechanism that limits the lifespan of data in a computer or network. A popular family of integrated-circuit digital logic.'], \
    ['SCPI','A standard for syntax and commands to use in controlling programmable test and measurement devices. Think *IDN?'], \
    ['Volt','The derived unit for electric potential'], \
    ['Voltage','The electric potential difference between two points.'], \
    ['loop','A hardware or software method which feeds a received signal or data back to the sender. A pseudo-device that makes a file accessible as a block device.'], \
    ['sensor','A device that detects events or changes in quantities and provides a corresponding output, generally as an electrical or optical signal.'], \
    ['thermistor','A temperature-dependent resistor.'], \
    ['photocell','A kind of light-dependent resistor.'], \
    ['phototransistor','A light-sensitive transistor.'], \
    ['optocoupler','A component that transfers electrical signals between two isolated circuits by using light.'], \
    ['optoisolator','A component that transfers electrical signals between two isolated circuits by using light.'], \
    ['software','Instructions that direct a computer processor to perform specific operations.'], \
    ['firmware','Embedded systems have this. Embedded engieers write it. It usually is not installable by the end user.'], \
    ['automation','Robotic labor'], \
    ['DCS','A very broad term used to monitor and control distributed equipment in process plants and industrial processes.'], \
    ['LCD','TN, IPS, S-IPS, AFFS, etc. Uses polarized light. '], \
    ['OLED', 'Totally natural emissive electroluminescent.'], \
    ['VFD','AC motor power supply.'], \
    ['transmitter','Makes waves, best paired with an antenna'], \
    ['receiver','Converts the information carried by radio waves to a usable form.'], \
    ['duplex','Two-way'], \
    ['ECC','Successor to Hamming code, self fixing.'], \
    ['SRAM','A type of semiconductor memory that uses bistable latching circuitry to store each bit. '], \
    ['SDRAM','Synchronous, and dynamic.'], \
    ['DRAM','A type of memory that stores each bit of data in a separate capacitor. '], \
    ['DDR','Twice as fast.'], \
    ['NVRAM','random-access memory that retains its information when power is turned off '], \
    ['RTC','A computer clock (most often in the form of an integrated circuit) that keeps track of the current time, usually contains a long-life battery.'], \
    ['SPICE','An open source analog electronic circuit simulator'], \
    ['SPI','SCLK, MISO, MOSI, SS.'], \
    ['Actel','FPGA Manufacturer.'], \
    ['Altera','FPGA Manufacturer.'], \
    ['Xilinx','FPGA Manufacturer.'], \
    ['RaspberryPi','Small $35.00 computer.'], \
    ['Android','Paranoid _______'], \
    ['Fahrenheit','A temperature scale based on one proposed in 1724 by the German physicist, after whom the scale is named.'], \
    ['Celcius','A scale and unit of measurement for temperature with 0 degrees as the freezing point of water.'], \
    ['Centigrade','A scale and unit of measurement for temperature with 0 degrees as the freezing point of water.'], \
    ['Kelvin','An absolute, thermodynamic temperature scale using as its null point absolute zero.'], \
    ['Oersted','Danish physicist who discovered that a steady electric current creates a magnetic field around it.'], \
    ['FCC','Spectrum regulator.']

#    ['source','define source'], \
#    ['','define '], \
#    ['','define '], \
#    ['Samsung','define Samsung'], \
#    ['RCA','define RCA'], \


word_list_original = ['saffron', 'The dried, orange yellow plant used to as dye and as a cooking spice.'], \
    ['pumpernickel', 'Dark, sour bread made from coarse ground rye.'], \
    ['leaven', 'An agent, such as yeast, that cause batter or dough to rise..'], \
    ['coda', 'Musical conclusion of a movement or composition.'], \
    ['paladin', 'A heroic champion or paragon of chivalry.'], \
    ['syncopation', 'Shifting the emphasis of a beat to the normally weak beat.'], \
    ['albatross', 'A large bird of the ocean having a hooked beek and long, narrow wings.'], \
    ['harp', 'Musical instrument with 46 or more open strings played by plucking.'], \
    ['piston', 'A solid cylinder or disk that fits snugly in a larger cylinder and moves under pressure as in an engine.'], \
    ['caramel', 'A smooth chery candy made from suger, butter, cream or milk with flavoring.'], \
    ['coral', 'A rock-like deposit of organism skeletons that make up reefs.'], \
    ['dawn', 'The time of each morning at which daylight begins.'], \
    ['pitch', 'A resin derived from the sap of various pine trees.'], \
    ['fjord', 'A long, narrow, deep inlet of the sea between steep slopes.'], \
    ['lip', 'Either of two fleshy folds surrounding the mouth.'], \
    ['lime', 'The egg-shaped citrus fruit having a green coloring and acidic juice.'], \
    ['mist', 'A mass of fine water droplets in the air near or in contact with the ground.'], \
    ['plague', 'A widespread affliction or calamity.'], \
    ['yarn', 'A strand of twisted threads or a long elaborate narrative.'], \
    ['snicker', 'A snide, slightly stifled laugh.']
 
a = Crossword(30, 30, u'█', 5000, word_list)
a.compute_crossword(2)
print a.word_bank()
print a.solution()
print a.word_find()
print a.display()
print a.legend()
print len(a.current_word_list), 'out of', len(word_list)
print a.debug
#end_full = float(time.time())
#print end_full - start_full
