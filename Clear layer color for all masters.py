#MenuTitle: Clear Layer Color for all Masters in Font selection
# -*- coding: utf-8 -*-
# by Kostas Bartsokas
from __future__ import division, print_function, unicode_literals
__doc__="""
Clears the layer color in all masters for selected glyphs.
"""

Glyphs.clearLog()

thisFont = Glyphs.font # frontmost font
selectedGlyphs = thisFont.selection # user selection

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

# iterate through selection:
for thisGlyph in selectedGlyphs:
	for layer in thisGlyph.layers:
		layer.color = 9223372036854775807
			
Font.enableUpdateInterface()

print("All layers color set to empty.")


