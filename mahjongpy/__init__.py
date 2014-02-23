import tiles

# String to array of tiles
def str2tile(srcStr):
	import re
	sStr = re.sub('\\s', '', srcStr, 0) # Ignore whitespace characters
	if re.match('^([1-9]+[mps]|[ESWNPFC])*$', sStr):
		tilelist = []
		tile_tmp = []
		for chr in sStr:
			if chr >= '1' and chr <= '9':
				tile_tmp += [int(chr)]
			elif (chr == 'm' or chr == 'p' or chr == 's') and tile_tmp:
				for tilenum in tile_tmp:
					tilelist += [(tiles.characters if chr == 'm' else (tiles.bamboos if chr == 's' else tiles.circles))[tilenum - 1]]
				tile_tmp = []
			elif chr == 'E' and not tile_tmp: tilelist += [tiles.east]
			elif chr == 'S' and not tile_tmp: tilelist += [tiles.south]
			elif chr == 'W' and not tile_tmp: tilelist += [tiles.west]
			elif chr == 'N' and not tile_tmp: tilelist += [tiles.north]
			elif chr == 'P' and not tile_tmp: tilelist += [tiles.white]
			elif chr == 'F' and not tile_tmp: tilelist += [tiles.green]
			elif chr == 'C' and not tile_tmp: tilelist += [tiles.red]
			else:
				raise ValueError("illegal character '"+chr+"' detected in argument \""+str+"\"")
		if tile_tmp:
			raise ValueError("suit character required after numerals; in argument \""+str+"\"")
		return tilelist
	else:
		raise ValueError("cannot understand argument \""+str+"\"")

# Count tiles by kind
def counttiles(tileList):
	result = {}
	for tile in (tiles.characters + tiles.bamboos + tiles.circles + tiles.honors + (tiles.flower,)):
		result[tile] = 0
	for tile in tileList:
		if tile in tiles.flowers:
			result[tiles.flower] += 1
		elif tile in result and tile != tiles.flower:
			result[tile] += 1
		else:
			raise ValueError("invalid item found: "+repr(tile))
	return result

