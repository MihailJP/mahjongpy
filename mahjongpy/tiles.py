# -*- coding: utf-8 -*-

# Superclass for Mahjong tiles
class Tile:
	# Singleton
	_instance = None
	def __new__(cl, *argc, **argv):
		if cl._instance == None:
			cl._instance = object.new(cl)
		return cl._instance

	def __str__(self): return '🀫'
	def __int__(self): return None
	def isSuited(self): return False
	def isCharacter(self): return False
	def isBamboo(self): return False
	def isCircle(self): return False
	def isHonor(self): return False
	def isWind(self): return False
	def isDragon(self): return False
	def isFlower(self): return False
	def sortkey(self): return 99
	def __cmp__(self, other): return self.sortkey() - other.sortkey()
	def __nonzero__(self): return self.__str__() != '🀫'
	def __repr__(self):
		if self.__nonzero__():
			return self.__str__()
		else:
			return "<Unknown Mahjong tile>"

# Superclass for suited tiles
class SuitedTile(Tile):
	def isSuited(self): return True

# Superclass for character suit (Wanzi, Wanzu)
class CharacterTile(SuitedTile):
	def isCharacter(self): return True

# Superclass for bamboo suit (Suozi, Sohzu)
class BambooTile(SuitedTile):
	def isBamboo(self): return True

# Superclass for ciecle suit (Tongzi, Pinzu)
class CircleTile(SuitedTile):
	def isCircle(self): return True

# Superclass for honor tiles
class HonorTile(Tile):
	def isHonor(self): return True

# Superclass for wind tiles (Fengpai, Kazehai)
class WindTile(HonorTile):
	def isWind(self): return True

# Superclass for dragon tiles (Sanyuanpai, Sangenpai)
class DragonTile(HonorTile):
	def isDragon(self): return True

# Superclass for flower tiles
class FlowerTile(Tile):
	def isFlower(self): return True

# Wind tiles
class EastWindTileClass(WindTile):
	def __str__(self): return '🀀'
	def sortkey(self): return 31
class SouthWindTileClass(WindTile):
	def __str__(self): return '🀁'
	def sortkey(self): return 32
class WestWindTileClass(WindTile):
	def __str__(self): return '🀂'
	def sortkey(self): return 33
class NorthWindTileClass(WindTile):
	def __str__(self): return '🀃'
	def sortkey(self): return 34

# Dragon tiles
class RedDragonTileClass(DragonTile):
	def __str__(self): return '🀄'
	def sortkey(self): return 37
class GreenDragonTileClass(DragonTile):
	def __str__(self): return '🀅'
	def sortkey(self): return 36
class WhiteDragonTileClass(DragonTile):
	def __str__(self): return '🀆'
	def sortkey(self): return 35

# Character suit tiles
class Character1Class(CharacterTile):
	def __str__(self): return '🀇'
	def __int__(self): return 1
	def sortkey(self): return 1
class Character2Class(CharacterTile):
	def __str__(self): return '🀈'
	def __int__(self): return 2
	def sortkey(self): return 2
class Character3Class(CharacterTile):
	def __str__(self): return '🀉'
	def __int__(self): return 3
	def sortkey(self): return 3
class Character4Class(CharacterTile):
	def __str__(self): return '🀊'
	def __int__(self): return 4
	def sortkey(self): return 4
class Character5Class(CharacterTile):
	def __str__(self): return '🀋'
	def __int__(self): return 5
	def sortkey(self): return 5
class Character6Class(CharacterTile):
	def __str__(self): return '🀌'
	def __int__(self): return 6
	def sortkey(self): return 6
class Character7Class(CharacterTile):
	def __str__(self): return '🀍'
	def __int__(self): return 7
	def sortkey(self): return 7
class Character8Class(CharacterTile):
	def __str__(self): return '🀎'
	def __int__(self): return 8
	def sortkey(self): return 8
class Character9Class(CharacterTile):
	def __str__(self): return '🀏'
	def __int__(self): return 9
	def sortkey(self): return 9

# Bamboo suit tiles
class Bamboo1Class(BambooTile):
	def __str__(self): return '🀐'
	def __int__(self): return 1
	def sortkey(self): return 11
class Bamboo2Class(BambooTile):
	def __str__(self): return '🀑'
	def __int__(self): return 2
	def sortkey(self): return 12
class Bamboo3Class(BambooTile):
	def __str__(self): return '🀒'
	def __int__(self): return 3
	def sortkey(self): return 13
class Bamboo4Class(BambooTile):
	def __str__(self): return '🀓'
	def __int__(self): return 4
	def sortkey(self): return 14
class Bamboo5Class(BambooTile):
	def __str__(self): return '🀔'
	def __int__(self): return 5
	def sortkey(self): return 15
class Bamboo6Class(BambooTile):
	def __str__(self): return '🀕'
	def __int__(self): return 6
	def sortkey(self): return 16
class Bamboo7Class(BambooTile):
	def __str__(self): return '🀖'
	def __int__(self): return 7
	def sortkey(self): return 17
class Bamboo8Class(BambooTile):
	def __str__(self): return '🀗'
	def __int__(self): return 8
	def sortkey(self): return 18
class Bamboo9Class(BambooTile):
	def __str__(self): return '🀘'
	def __int__(self): return 9
	def sortkey(self): return 19

# Circle suit tiles
class Circle1Class(CircleTile):
	def __str__(self): return '🀙'
	def __int__(self): return 1
	def sortkey(self): return 21
class Circle2Class(CircleTile):
	def __str__(self): return '🀚'
	def __int__(self): return 2
	def sortkey(self): return 22
class Circle3Class(CircleTile):
	def __str__(self): return '🀛'
	def __int__(self): return 3
	def sortkey(self): return 23
class Circle4Class(CircleTile):
	def __str__(self): return '🀜'
	def __int__(self): return 4
	def sortkey(self): return 24
class Circle5Class(CircleTile):
	def __str__(self): return '🀝'
	def __int__(self): return 5
	def sortkey(self): return 25
class Circle6Class(CircleTile):
	def __str__(self): return '🀞'
	def __int__(self): return 6
	def sortkey(self): return 26
class Circle7Class(CircleTile):
	def __str__(self): return '🀟'
	def __int__(self): return 7
	def sortkey(self): return 27
class Circle8Class(CircleTile):
	def __str__(self): return '🀠'
	def __int__(self): return 8
	def sortkey(self): return 28
class Circle9Class(CircleTile):
	def __str__(self): return '🀡'
	def __int__(self): return 9
	def sortkey(self): return 29

# Circle suit tiles
class PlumFlowerClass(FlowerTile):
	def __str__(self): return '🀢'
	def sortkey(self): return 45
class OrchidFlowerClass(FlowerTile):
	def __str__(self): return '🀣'
	def sortkey(self): return 46
class ChrysanthemumFlowerClass(FlowerTile):
	def __str__(self): return '🀤'
	def sortkey(self): return 48
class BambooFlowerClass(FlowerTile):
	def __str__(self): return '🀥'
	def sortkey(self): return 47
class SpringSeasonClass(FlowerTile):
	def __str__(self): return '🀦'
	def sortkey(self): return 41
class SummerSeasonClass(FlowerTile):
	def __str__(self): return '🀧'
	def sortkey(self): return 42
class AutumnSeasonClass(FlowerTile):
	def __str__(self): return '🀨'
	def sortkey(self): return 43
class WinterSeasonClass(FlowerTile):
	def __str__(self): return '🀩'
	def sortkey(self): return 44

east = EastWindTileClass()
south = SouthWindTileClass()
west = WestWindTileClass()
north = NorthWindTileClass()
red = RedDragonTileClass()
green = GreenDragonTileClass()
white = WhiteDragonTileClass()

char1 = Character1Class()
char2 = Character2Class()
char3 = Character3Class()
char4 = Character4Class()
char5 = Character5Class()
char6 = Character6Class()
char7 = Character7Class()
char8 = Character8Class()
char9 = Character9Class()

bamb1 = Bamboo1Class()
bamb2 = Bamboo2Class()
bamb3 = Bamboo3Class()
bamb4 = Bamboo4Class()
bamb5 = Bamboo5Class()
bamb6 = Bamboo6Class()
bamb7 = Bamboo7Class()
bamb8 = Bamboo8Class()
bamb9 = Bamboo9Class()

circ1 = Circle1Class()
circ2 = Circle2Class()
circ3 = Circle3Class()
circ4 = Circle4Class()
circ5 = Circle5Class()
circ6 = Circle6Class()
circ7 = Circle7Class()
circ8 = Circle8Class()
circ9 = Circle9Class()

plum = PlumFlowerClass()
orchid = OrchidFlowerClass()
chrys = ChrysanthemumFlowerClass()
bamboo = BambooFlowerClass()
spring = SpringSeasonClass()
summer = SummerSeasonClass()
autumn = AutumnSeasonClass()
winter = WinterSeasonClass()
