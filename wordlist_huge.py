#!/usr/bin/python
# -*- coding: UTF-8 -*-
word_list = ['coulomb', 'A fundamental unit of electrical charge, and is also the SI derived unit of electric charge (symbol: Q or q). It is equal to the charge of approximately 6.241×1018 electrons.'], \
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
    ['electron', 'define electron'], \
    ['binary', 'two states'], \
    ['transistor', 'A semiconductor device used to amplify and switch electronic signals and electrical power.'], \
    ['amplifier', 'An electronic device that increase the power of a signal.'], \
    ['inductance', 'he property of a conductor by which a change in current flowing through it "induces" (creates) a voltage (electromotive force) in both the conductor itself and in any nearby conductors.'], \
    ['Centigrus','A real unit for measuring temperature. Invented at WCJC by Blake Folmar.'], \
    ['logic','define logic'], \
    ['microprocessor','define microprocessor'], \
    ['microcontroller','define microcontroller'], \
    ['architecture','define architecture'], \
    ['register','define register'], \
    ['word','define word'], \
    ['bitmask','define bitmask'], \
    ['variable','Programmers store things in these.'], \
    ['static','define static'], \
    ['dynamic','define dynamic'], \
    ['polar','define polar'], \
    ['data','define data'], \
    ['type','define type'], \
    ['compiler','define compiler'], \
    ['assembler','define assembler'], \
    ['opcode',' the portion of a machine language instruction that specifies the operation to be performed'], \
    ['memory','refers to the physical devices used to store programs or data on a temporary or permanent basis for use in a computer or other digital electronic device'], \
    ['PLC','a digital computer used for automation of typically industrial electromechanical processes'], \
    ['relay','an electrical device that is activated by a current or signal in one circuit to open or close another circuit'], \
    ['SSR','an electronic switching device that switches conduction states when a small external voltage is applied along its n-type and p-type junctions'], \
    ['diac','a diode that conducts current only after its breakover voltage has been reached momentarily'], \
    ['IGBT','a three-terminal power semiconductor device primarily used as an electronic switch'], \
    ['macro','a set of instructions that is represented in an abbreviated format'], \
    ['ASCII','a character-encoding scheme originally based on the English alphabet that encodes 128 specified characters'], \
    ['unicode','an international encoding standard for use with different languages and scripts, by which each letter, digit, or symbol is assigned a unique numeric value that applies across different platforms and programs'], \
    ['encode','to convert information or an instruction into a particular form'], \
    ['protocol','a system of digital rules for data exchange within or between computers'], \
    ['PCB','mechanically supports and electrically connects electronic components using conductive tracks, pads and other features etched from copper sheets laminated onto a non-conductive substrate'], \
    ['transformer','an electrical device that transfers energy between two or more circuits through electromagnetic induction'], \
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
    ['RaspberryPi','Small $35.00 computer. For hobbyists and education.'], \
    ['Android','Paranoid _______. (Radiohead)'], \
    ['Fahrenheit','A temperature scale based on one proposed in 1724 by the German physicist, after whom the scale is named.'], \
    ['Celcius','A scale and unit of measurement for temperature with 0 degrees as the freezing point of water.'], \
    ['Centigrade','A scale and unit of measurement for temperature with 0 degrees as the freezing point of water.'], \
    ['Kelvin','An absolute, thermodynamic temperature scale using as its null point absolute zero.'], \
    ['Oersted','Danish physicist who discovered that a steady electric current creates a magnetic field around it.'], \
    ['FCC','Spectrum regulator.'], \
    ['National', 'American semiconductor manufacturer which specialized in analog devices and subsystems. Employer of Bob Pease.'], \
    ['semiconductor', 'A substance that has conductivity between an insulator and most metals'], \
    ['germanium', 'Atomic number 32'], \
    ['Linux', 'A Unix-like and mostly POSIX-compliant computer operating system'], \
    ['Microsoft', 'A multinational corporation that develops, manufactures, licenses, and sells computer software'], \
    ['Windows', 'is a series of graphical interface operating systems developed, marketed, and sold by Microsoft'], \
    ['Macintosh', 'A series of personal computers (PCs) designed, developed, and marketed by Apple Inc'], \
    ['Apple', 'American multinational corporation that designs develops and sells consumer electronics'], \
    ['BSD', 'A Unix operating system derivative developed and distributed by the CSRG.'], \
    ['Unix', 'A multitasking, multiuser computer operating system that exists in many variants. Invented at AT&T'], \
    ['Posix', 'Standards specified by the IEEE for maintaining compatibility between operating systems.'], \
    ['Oscillator', 'A electronic circuit that produces a periodic, repeating electronic signal.'], \
    ['triangle', 'A polygon with three edges and three vertices. Also a name for a waveform.'], \
    ['square', 'A rectangular quadrilateral'], \
    ['breakdown', 'The abrupt failure of an insulator or insulating medium to restrict the flow of current.'], \
    ['filter', 'Blocks out any unwanted frequency in a circuit'], \
    ['sawtooth', 'a non sine wave that resembles the teeth of a saw'], \
    ['sine', 'A waveform that is curvy'], \
    ['waveform', 'T representation of a signal as a plot of amplitude versus time'], \
    ['current', 'The flow of electric charge'], \
    ['Kirchhoff', 'Inventor of current and voltage law'], \
    ['Faraday', 'The si unit of capacitance is named after him'], \
    ['farad', 'si unit of capacitance'], \
    ['Norton', 'developed nortons theorem'], \
    ['Thevenin', 'developed Thevenins theorem'], \
    ['cable', 'Two or more wires side by side'], \
    ['coaxial', 'A cable with a center conductor, insulation, wire braid around that, and more insulation'], \
    ['Ohm', 'Unit of resistance.'], \
    ['DMM', 'A typically handheld electronic measurement device.'], \
    ['silicon', 'The basis for most semiconductors.'], \
    ['Tesla', 'The wickedest electrical genius ever.'], \
    ['Gauss', 'is the cgs unit of measurement of a magnetic field'], \
    ['Plot', 'is a graph of the transfer function of a linear, time-invariant system versus frequency'], \
    ['Data', 'the quantities, characters, or symbols on which operations are performed by a computer, being stored and transmitted in the form of electrical signals and recorded on magnetic, optical, or mechanical recording media'], \
    ['Network', 'a group or system of interconnected people or things'], \
    ['Maxwell', 'a unit of magnetic flux in the centimeter-gram-second system, equal to that induced through one square centimeter by a perpendicular magnetic field of one gauss'], \
    ['Feedback', 'the return to the input of a part of the output of a machine, system, or process'], \
    ['Feedforward' , 'an element or pathway within a control system which passes a controlling signal from a source in its external environment, often a command signal from an external operator, to a load elsewhere in its external environment'], \
    ['PID', 'A popular control algorithm.'], \
    ['Lucent', 'Another name for Bell Labs.'], \
    ['BellLabs', 'Defunct research and development subsidiary of AT&T.'], \
    ['Alcatel', 'A french global telecommunications equipment company. Purchaser of Bell Labs.'], \
    ['HP', 'Agilent predecessor. Company started in a garage.'], \
    ['HewlettPackard', 'Agilent predecessor. Company started in a garage.'], \
    ['Agilent', 'Successor to HP.'], \
    ['triac', 'An electronic component that can conduct current in either direction when it is triggered '], \
    ['FET', 'A type of transistor.'],\
    ['MOSFET', 'A type of transistor.'], \
    ['NPN', 'One type of BJT.'],\
    ['PNP', 'One type of BJT.'],\
    ['spectrum', 'A condition that is not limited to a specific set of values but can vary infinitely within a continuum. '],\
    ['spectra', 'conditions or values that vary over a continuum.'], \
    ['Fourier', 'French mathematician and physicist interested in heat transfer and vibrations.'],\
    ['potentiometer', 'A three-terminal adjustable resistor.'],\
    ['digital', 'signals by discrete bands of analog levels, rather than by a continuous range.'], \
    ['analog', 'electronic systems with a continuously variable signal, in contrast to digital electronics where signals usually take only two different levels.'],\
    ['gain', 'a measure of the ability of a circuit to increase the power or amplitude of a signal from the input to the output by adding energy converted from some power supply to the signal.'],\
    ['bridge', 'a type of electrical circuit in which two circuit branches are "bridged" by a third branch connected between the first two branches at some intermediate point along them. '],\
    ['rectifier', 'AC -> DC.'],\
    ['microprocessor', 'Incorporates the functions of a computer central processing unit (CPU) on a single integrated circuit (IC).'], \
    ['microcontroller', ' is a small computer on a single integrated circuit containing a processor core, memory, and programmable input/output peripherals.'], \
    ['architecture', 'refers to the identification of a systems physical components and their interrelationships'], \
    ['ALU', 'Is a digital circuit that performs integer arithmetic and logical operations.'], \
    ['Register', 'Are data storage devices that are more sophisticated than latches. Is a group of binary cells suitable for holding binary information.'], \
    ['Word', 'Is basically a fixed-sized group of digits (binary or decimal) that are handled as a unit by the instruction set or the hardware of the processor.'], \
    ['Bitmask', 'Makes use of the fact that binary numbers are made up of 1s and 0s, each digit in a binary number being equivalent to one bit'], \
    ['Variable', 's a storage location and an associated symbolic name (an identifier) which contains some known or unknown quantity or information'], \
    ['Static', 'displayed when no transmission signal is obtained by the antenna receiver of television sets and other display devices.'], \
    ['Dynamic', ' Of data storage, processing, or programming affected by the passage of time or the presence or absence of power'], \
    ['Data', 'Information'], \
    ['Type', 'is a classification identifying one of various of data, such as real, integer or Boolean'], \
    ['Compiler', 'Source code written in a programming language (the source language) into another computer language (the target language, often having a binary form known as object code)'], \
    ['Assembler', 'is a program which creates object code by translating combinations of mnemonics and syntax for operations and addressing modes into their numerical equivalents.'], \
    ['VHDL',' Hardware description language used in electronic design automation and general purpose parallel programming language.'], \
    ['Verilog',' Hardware description language.'], \
    ['PLD','Build re-configurable digital circuits with it.'], \
    ['CPLD','Build re-configurable digital circuits with it.'], \
    ['linear','Able to be represented by a straight line on a graph'], \
    ['logarithmic','Constructed so that successive points along an axis, or graduations that are an equal distance apart, represent values that are in an equal ratio'], \
    ['exponential',' Becoming more and more rapid'], \
    ['polynomial','An expression of more than two algebraic terms'], \
    ['RMS','Multiplying a sine wave times 0.707 will get you the ___ Voltage.'], \
    ['Power','Energy that is produced by electrical means and used to operate a device'], \
    ['invert','To put in opposite arrangement'], \
    ['phase','The relationship in time between successive states or cycles'], \
    ['agc','The average or peak output signal level is used to adjust the signal output to a suitable level'], \
    ['control','A means of limiting or regulating something'], \
    ['logic','A system or set of principles underlying the arrangements of elements in a computer or device so as to perform a specified task'], \
    ['oscilloscope', 'a type of electronic test equipment that allows observation of constantly varying signal voltages, usually as a two-dimensional plot of one or more signals as a function of time'], \
    ['snubber', 'a device to suppress voltage transients in electrical systems'], \
    ['RAM', 'Daft Punk named an album after this kind of memory.'], \
    ['ROM', 'Memory that cannot form new memories.'], \
    ['Flash', 'an electronic non-volatile computer storage medium that can be electrically erased and reprogrammed'], \
    ['serial', 'any medium issued in successive parts bearing numerical or chronological designation and intended to be continued indefinitely'], \
    ['USB', 'an industry standard that defines the cables, connectors and communication protocols used in a bus for connection, communication, and power supply between computers and electronic devices'], \
    ['IEEE', ' a professional association formed in 1963 from the amalgamation of the American Institute of Electrical Engineers and the Institute of Radio Engineers'], \
    ['Firewire', 'an interface standard for a serial bus for high-speed communications and isochronous real-time data transfer, a.k.a IEEE 1394'], \
    ['parallel', 'Side by side'], \
    ['Chua', 'Memristor predictor.'], \
    ['PROM', 'a form of digital memory where the setting of each bit is locked by a fuse or antifuse'], \
    ['EPROM', 'a type of memory chip that retains its data when its power supply is switched off'], \
    ['EEPROM', 'a type of non-volatile memory used in computers and other electronic devices to store small amounts of data that must be saved when power is removed'], \
    ['FPGA', 'an integrated circuit designed to be configured by a customer or a designer after manufacturing, field-programmable'], \
    ['capacitance', 'The ability of a body to store an electrical charge'], \
    ['impedance', 'The measure of the opposition that a circuit presents to a current when a voltage is applied'], \
    ['resistance', 'A measure of the degree to which conductor opposes an electric current through that conductor'], \
    ['resistor', 'A passive two-terminal electrical component that implements electrical resistance as a circuit element'], \
    ['capacitor', 'A passive two-terminal electrical component used to store energy electrostatically in an electric field'], \
    ['inductor', 'Also called a coil or reactor, is a passive two-terminal electrical component which resists changes in electric current passing through it'], \
    ['kilo', 'Denoting multiplication by one thousand'], \
    ['Mega', 'A factor of one million'], \
    ['Giga', 'A factor of a billion'], \
    ['Tera', 'Multiplication of a power of twelve'], \
    ['Peta', 'Multiplication of a power of fifteen'], \
    ['bit', 'The basic unit of information in computing and digital communications'], \
    ['byte', 'A unit of digital information in computing and telecommunications that most commonly consists of eight bits'], \
    ['diode', 'A two-terminal electronic component with asymmetric conductance; it has low (ideally zero) resistance to current in one direction, and high (ideally infinite) resistance in the other'], \
    ['LED', 'A two-lead semiconductor light source'], \
    ['dopant',' a trace impurity element that alters electrical/optical properties'], \
    ['orbital','actual\potential patterns of electron density represented as a wave function '], \
    ['Centigrus',' A real unit of measure for temperature. Inventor: Blake Folmar.'], \
    ['arduino',' Microcontroller developer kit named after a pub in Italy.'], \
    ['Atmel',' Corporation was founded in 1984 by George Perlegos'], \
    ['AVR',' modified Harvard architecture 8-bit RISC single chip micro controller. Arduino CPU.'], \
    ['PIC', 'micro controller built to be used with General Instruments new CP1600 16-bit CPU. Microchip makes them.'], \
    ['picaxe',' a UK-sourced micro controller system with chips made by Revolution Education. Popular with hobbyists. '], \
    ['ARM',' a family of instruction set architectures for computer processors based on RISC developed by British company in 1985. Processors from 8bits to 64bits.'], \
    ['RISC',' microprocessor with a CPU design strategy based on the insight that simplified instruction set'], \
    ['MIPS',' microprocessor based on RISC, introduced in 1981'], \
    ['x86',' a family of backward compatible instruction set architectures based on the Intel 8086 CPU.'], \
    ['Intel','Semiconductor manufacturer. Robert Noyce, Gordon Moore, etc.'], \
    ['Fairchild','Semiconductor company established by the traitorous eight, according to William Shockley'], \
    ['TI',' company that designs and makes semiconductors, which it sells to electronics designers and manufacturers globally. Headquartered at Dallas, Texas, United States '], \
    ['protocol','a set of rules governing the exchange or transmission of data between devices.'], \
    ['cicuit',' a complete and closed path around which a circulating electric current can flow.'], \
    ['PCB','mechanically supports and electrically connects electrical components using conductive tracks, pads and other features etched from copper sheets'], \
    ['decibel',' A logarithmic unit used to express the ratio between power or intensity values'], \
    ['transformer','Optimus Prime; or an electrical component that reduces or increases voltage of AC.'], \
    ['bel','10 db.'],

if(__name__=="__main__"):
    for line in word_list:
        print line

