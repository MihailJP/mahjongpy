MahjongPY
=========

Python library to do with Mahjong tiles

## Usage

```python
import mahjongpy
```

### Tiles

Tiles as objects are in `mahjongpy.tiles`.

|Objects                               |Description                            |
|--------------------------------------|---------------------------------------|
|`east`, `south`, `west`, `north`      |Wind tiles _(Fengpai, Kazehai)_        |
|`red`, `green`, `white`               |Dragon tiles _(Sanyuanpai, Sangenpai)_ |
|`char1` to `char9`                    |Character suit _(Wanzi, Wanzu)_        |
|`bamb1` to `bamb9`                    |Bamboo suit _(Suozi, Sohzu)_           |
|`circ1` to `circ9`                    |Circle suit _(Tongzi, Pinzu)_          |
|`plum`, `orchid`, `chrys`, `bamboo`   |Flower tiles _(Huapai, Hanapai)_       |
|`spring`, `summer`, `autumn`, `winter`|Flower tiles _(Huapai, Hanapai)_       |
|`flower`                              |Abstract flower tile (for special use) |

#### Sequence of suited tiles

These methods return a tuple consisting of nine uniformly suited tile objects in ascending order.

|Method      |Returns a tuple of...           |
|------------|--------------------------------|
|`characters`|Character suit _(Wanzi, Wanzu)_ |
|`bamboos`   |Bamboo suit _(Suozi, Sohzu)_    |
|`circles`   |Circle suit _(Tongzi, Pinzu)_   |

... and also available:

|Method      |Returns a tuple of...                  |
|------------|---------------------------------------|
|`winds`     |Wind tiles _(Fengpai, Kazehai)_        |
|`dragons`   |Dragon tiles _(Sanyuanpai, Sangenpai)_ |
|`honors`    |Honor tiles _(Zipai, Jihai)_           |
|`flowers`   |Flower tiles _(Huapai, Hanapai)_       |

#### Sorting

Since `Tile` class includes `__cmp__` method, a list of tile objects can be sorted by the following order.

1. Characters, ascending order
2. Bamboos, ascending order
3. Circles, ascending order
4. East, south, west, north
5. **White, green, red** dragons (in Japanese order)
6. Spring, summer, autumn, winter
7. Plum, orchid, chrysanthemum, bamboo (in Taiwanese order)
8. Invalid tile

### Tile object class hierarchy

* Tile
    * SuitedTile
        * CharacterTile
            * Character1Class
            * Character2Class
            * Character3Class
            * Character4Class
            * Character5Class
            * Character6Class
            * Character7Class
            * Character8Class
            * Character9Class
        * BambooTile
            * Bamboo1Class
            * Bamboo2Class
            * Bamboo3Class
            * Bamboo4Class
            * Bamboo5Class
            * Bamboo6Class
            * Bamboo7Class
            * Bamboo8Class
            * Bamboo9Class
        * CircleTile
            * Circle1Class
            * Circle2Class
            * Circle3Class
            * Circle4Class
            * Circle5Class
            * Circle6Class
            * Circle7Class
            * Circle8Class
            * Circle9Class
    * HonorTile
        * WindTile
            * EastWindTileClass
            * SouthWindTileClass
            * WestWindTileClass
            * NorthWindTileClass
        * DragonTile
            * RedDragonTileClass
            * GreenDragonTileClass
            * WhiteDragonTileClass
    * FlowerTile
        * PlumFlowerClass
        * OrchidFlowerClass
        * ChrysanthemumFlowerClass
        * BambooFlowerClass
        * SpringSeasonClass
        * SummerSeasonClass
        * AutumnSeasonClass
        * WinterSeasonClass

#### Methods implemented in tile object class

|Methods                     |Description                                                  |
|----------------------------|-------------------------------------------------------------|
|`__new__(cl, *argc, **argv)`|_overridden for singleton pattern_                           |
|`__str__(self)`             |shows with Unicode Mahjong tile character                    |
|`__int__(self)`             |an integer value if `self` is a suited tile, `None` otherwise|
|`isSuited(self)`            |`True` if `self` is a suited tile                            |
|`isCharacter(self)`         |`True` if `self` is a tile of character suit                 |
|`isBamboo(self)`            |`True` if `self` is a tile of bamboo suit                    |
|`isCircle(self)`            |`True` if `self` is a tile of circle suit                    |
|`isHonor(self)`             |`True` if `self` is a honor tile, i.e. wind or dragon tile   |
|`isWind(self)`              |`True` if `self` is a wind tile                              |
|`isDragon(self)`            |`True` if `self` is a dragon tile                            |
|`isFlower(self)`            |`True` if `self` is a flower tile                            |
|`__cmp__(self, other)`      |compares sort keys of two tiles                              |
|`__nonzero__(self)`         |returns `True` if `self` is a valid tile                     |
|`__repr__(self)`            |returns string like `<Mahjong tile, 1 of bamboos>`           |
|`__hash__(self)`            |returns hash value of `self`                                 |
|`isTerminal(self)`          |`True` if `self` is a terminal tile, i.e. one or nine        |
|`isTermHonor(self)`         |returns `self.isTerminal() or self.isHonor()`                |

### Make an array of tile objects from a string

```python
mahjongpy.str2tile("19m19s19pESWNPFC")
```

#### Alphabetic notation

This notation is widely used by Japanese (especially online) Mahjong players.

|Regexp   |Description   |
|---------|--------------|
|`[1-9]+m`|Character suit|
|`[1-9]+s`|Bamboo suit   |
|`[1-9]+p`|Circle suit   |
|`[ESWN]` |Wind tiles    |
|`P`      |White dragon  |
|`F`      |Green dragon  |
|`C`      |Red dragon    |
|`\s`     |ignored       |

#### Unicode notation

Not implemented at this moment.

#### Exception

This method raises `ValueError` if the argument is invalid.

### Count tiles in a sequence by kind

```python
mahjongpy.counttiles(mahjongpy.str2tile("1112345678999m"))
```

This method returns a dict with tile objects as keys.
All flower tiles are put in `mahjongpy.tiles.flower` key together.

#### Exception

This method raises `ValueError` if the sequence includes an invalid tile object.

