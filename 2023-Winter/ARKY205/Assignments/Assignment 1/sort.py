data = """
Harmand, Sonia, Jason E. Lewis, Craig S. Feibel, Christopher J. Lepre, Sandrine Prat, Arnaud Lenoble, Xavier Boës, Rhonda L. Quinn, Michel Brenet, Adrian Arroyo, Nicholas Taylor, Sophie Clément, Guillaume Daver, Jean-Philip Brugal, Louise Leakey, Richard A. Mortlock, James D. Wright, Sammy Lokorodi, Christopher Kirwa, Dennis V. Kent, and Hélène Roche
2015 3.3-million-year-old stone tools from Lomekwi 3, West Turkana, Kenya. Nature 521:310-315

Spagnolo, Vincenzo, Guilia Marciani, Daniele Aureli, Francesco Berna, Ginevra Toniello, Fernando Astudillo, Francesco Boschin, Paolo Boscato, and Annamaria Ronchitelli
2019 Neanderthal activity and resting areas from stratigraphic unit 13 at the Middle Palaeolithic site of Oscurusciuto (Ginosa - Taranto, Southern Italy). Quaternary Science Reviews 217:169-193

Hou, Y.M., L.X. Zhao
2010 An archeological view for the presence of early humans in China. Quaternary International 223:10-19

Arther Bettis III, E., Adrianne K. Milius, Scott J. Carpenter, Roy Larick, Yahdi Zaim, Yan Rizal, Russel L. Ciochon, Stephanie A. Tassier-Surine, Daniel Murral, Suminto, and Sutinko Bronto
2009 Way out of Africa: Early Pleistocene paleoenvironments inhabited by Homo erectus in Sangiran, Java. Journal of Human Evolution 56:11-24

Árnason, Úlfur, and Björn Hallström
2020 The reversal of human phylogeny: Homo left Africa as erectus, came back as sapiens sapiens. Hereditas  157:51-51

Bennett, Matthew R., David Bustos, Jeffrey S. Pigati, Kathleen B. Springer, Thomas M. Urban, Vance T. Holliday, Sally C. Reynolds, Marcin Budka, Jeffrey S. Honke, Adam M. Hudson, Brendan Fenerty, Clare Connelly, Patrick J. Martinez, Vincent L. Santucci, and Daniel Odess
2021 Evidence of humans in North America during the Last Glacial Maximum. Science (American Association for the Advancement of Science) 373:1528-1531

Hoffecker, John F., Scott A. Elias, Dennis H. O'Rourke, G. Richard Scott, and Nancy H. Bigelow
2016 Beringia and the global dispersal of modern humans. Evolutionary anthropology 25:64-78

Gauvrit Roux, Eugénie
2022 Socio-economic dynamics of Magdalenian hunter-gatherers: Functional perspective. PloS ONE 17: e0274819

Lane, Paul J.
2015 Archaeology in the age of the Anthropocene: A critical assessment of its scope and societal contributions. Journal of Field Archaeology 40:485-498

Ardelean, Ciprian F., Lorena Becerra-Valdivia, Mikkel Winther Pedersen, Jean-Luc Schwenninger, Charles G. Oviatt, Juan I. Macías-Quintero, Joaquin Arroyo-Cabrales, Martin Sikora, Yam Zul E. Ocampo-Díaz, Igor I. Rubio-Cisneros, Jennifer G. Watling, Vanda B. de Medeiros, Paulo E. De Oliveira, Luis Barba-Pingarón, Agustín Ortiz-Butrón, Jorge Blancas-Vázquez, Irán Rivera-González, Corina Solís-Rosales, María Rodríguez-Ceja, Devlin A. Gandy, Zamara Navarro-Gutierrez, Jesús J. De La Rosa-Díaz, Vladimir Huerta-Arellano, Marco B. Marroquín-Fernández, L. Martin Martínez-Riojas, Alejandro López-Jiménez, Thomas Higham, and Eske Willerslev
2020 Evidence of human occupation in Mexico around the Last Glacial Maximum. Nature (London) 584:87-92

Fuller, Dorian Q., George Willcox, and Robin G. Allaby
2011 Cultivation and domestication had multiple origins: arguments against the core area hypothesis for the origins of agriculture in the Near East. World Archaeology 43:628-652

Zeder, Melinda A
2011 The Origins of Agriculture in the Near East. Current Anthropology 52: S221-S235

Morales, Jacob, Guillem Pérez-Jordà, Leonor Peña-Chocarro, Lydia Zapata, Mónica Ruíz-Alonso, Jose Antonio López-Sáez, and Jörg Linstädter
2013 The origins of agriculture in North-West Africa: macro-botanical remains from Epipalaeolithic and Early Neolithic levels of Ifri Oudadane (Morocco). Journal of Archaeological Science 40:2659-2669

Hodder, Ian
2022 Staying Egalitarian and the Origins of Agriculture in the Middle East. Cambridge Archaeological Journal 32:619-642

Jones, Glynis, Thomas Kluyver, Catherine Preece, Jennifer Swarbrick, Emily Forster, Michael Wallace, Michael Charles, Mark Rees, and Colin P. Osborne
2021 The origins of agriculture: Intentions and consequences. Journal of Archaeological Science 125: 105290

Benati, Giacomo, and Carmine Guerriero
2022 The origins of the state: technology, cooperation and institutions. Journal of Institutional Economics 18:29-43

Daems, Dries
2020 On complex archaeologies: conceptualizing social complexity and its potential for archaeology. Adaptive Behavior 28:323-328

Furholt, Martin, Colin Grier, Matthew Spriggs, and Timothy Earle
2020 Political Economy in the Archaeology of Emergent Complexity: a Synthesis of Bottom-Up and Top-Down Approaches. Journal of Archaeological Method and Theory 27:157-191

Kenoyer, J. Mark, T. Douglas Price, and James H. Burton
2013 A new approach to tracking connections between the Indus Valley and Mesopotamia: initial results of strontium isotope analyses from Harappa and Ur. Journal of Archaeological Science 40:2286-2297

Liu, Li
2009 State Emergence in Early China. Annual Review of Anthropology 38:217-232

Pozorski, Thomas, and Shelia Pozorski
2018 Early Complex Society on the North and Central Peruvian Coast: New Archaeological Discoveries and New Insights. Journal of Archaeological Research 26:353-386
"""

class Entry:
    def __init__(self, authors, text):
        self.authors = authors
        self.year = text[0:4]
        self.text = text[5:]

    def print(self):
        print(self.authors)
        print(f"{self.year} {self.text}\n")

d = data.split('\n')
entries = []
author = ""
text = ""
for line in d:
    if line == "":
        continue
    elif line[0] == '2':
        text = line
        entries.append(Entry(author, text))
        author = ""
        text = ""
    else:
        author = line

entries.sort(key=lambda x: x.text)

for e in entries:
    e.print()
