#MenuTitle: Match Brace Layers of Composite Glyphs to original Components 
# -*- coding: utf-8 -*-

__doc__="""
Matches the setup of brace layers for all glyphs with components whose root glyph has brace layers
"""

import GlyphsApp


# list of glyphs with added braces
new_glyphs_w_braces_ls = []

def check_if_brace_layer(source, target):
	for originalLayer in source.layers:
		if originalLayer.isSpecialLayer and "{" in originalLayer.name and "}" in originalLayer.name:
			layerAlreadyExists = False
			for thisGlyphLayer in target.layers:
				nameIsTheSame = originalLayer.name == thisGlyphLayer.name
				masterIsTheSame = originalLayer.associatedMasterId == thisGlyphLayer.associatedMasterId
				if nameIsTheSame and masterIsTheSame:
					layerAlreadyExists = True
			if layerAlreadyExists:
				print("%s, layer '%s' already exists. Skipping." % (target.name, originalLayer.name))
			else:
				newLayer = GSLayer()
				newLayer.name = originalLayer.name
				newLayer.setAssociatedMasterId_(originalLayer.associatedMasterId)
				print "Added %s in %s" % (newLayer.name, target)
				newLayer.width = originalLayer.width
				target.layers.append(newLayer)
				newLayer.reinterpolate()
				newLayer.reinterpolateMetrics()
				newLayer.syncMetrics()
				new_glyphs_w_braces_ls.append(target.name)


# Main
def main():
	# clear macro window log:
	Glyphs.clearLog()
	
	# Set the glyphs file
	font = Glyphs.font
	
	# Check each Glyph (G1) in the list of transformed components (currently it goes down up to 7 levels of nesting
	for thisGlyph in font.glyphs: 
		
		# for each component of the first layer of G1 get the glyph (G2) of the component and check if G2 has brace layer and copy it
		for thisComponent in thisGlyph.layers[0].components:
			thisGlyph2 = font.glyphs[thisComponent.name]
			print "Nesting (depth=0) inside %s is %s" % (thisGlyph.name, thisGlyph2.name)
			check_if_brace_layer( thisGlyph2 , thisGlyph)
			
			#check if the G2 glyph has components
			hasComponents = thisGlyph2.layers[0].components
			if hasComponents:
				
				#if G2 has components ifor each component of the first layer of G2 get the glyph (G3) of the component and check if G3 has brace layer and copy it to G1
				for thisComponent2 in thisGlyph2.layers[0].components:
					thisGlyph3 = font.glyphs[thisComponent2.name]
        			print "-Nesting (depth=1) inside %s is %s" % (thisGlyph2.name, thisGlyph3.name)
        			check_if_brace_layer( thisGlyph3 , thisGlyph)

					#check if the G3 glyph has components	
        			hasComponents2 = thisGlyph3.layers[0].components
        			if hasComponents2:
						
						#if G3 has components for each component of the first layer of G3 get the glyph (G4) of the component and check if G4 has brace layer and copy it to G1
						for thisComponent3 in thisGlyph3.layers[0].components:
							thisGlyph4 = font.glyphs[thisComponent3.name]
							print "--Nesting (depth=2) inside %s is %s" % (thisGlyph3.name, thisGlyph4.name)
							check_if_brace_layer( thisGlyph4 , thisGlyph)
	
							#check if the G4 glyph has components	
							hasComponents3 = thisGlyph4.layers[0].components
							if hasComponents3:
						
								#if G4 has components for each component of the first layer of G4 get the glyph (G5) of the component and check if G5 has brace layer and copy it to G1
								for thisComponent4 in thisGlyph4.layers[0].components:
									thisGlyph5 = font.glyphs[thisComponent4.name]
									print "---Nesting (depth=3) inside %s is %s" % (thisGlyph4.name, thisGlyph5.name)
									check_if_brace_layer( thisGlyph5 , thisGlyph)
			
									#check if the G5 glyph has components	
									hasComponents4 = thisGlyph5.layers[0].components
									if hasComponents4:
						
									#if G5 has components for each component of the first layer of G5 get the glyph (G6) of the component and check if G6 has brace layer and copy it to G1
										for thisComponent5 in thisGlyph5.layers[0].components:
											thisGlyph6 = font.glyphs[thisComponent5.name]
											print "----Nesting (depth=4) inside %s is %s" % (thisGlyph5.name, thisGlyph6.name)
											check_if_brace_layer( thisGlyph6 , thisGlyph)
											
											#check if the G6 glyph has components	
											hasComponents5 = thisGlyph6.layers[0].components
											if hasComponents5:
						
												#if G6 has components for each component of the first layer of G6 get the glyph (G7) of the component and check if G7 has brace layer and copy it to G1
												for thisComponent6 in thisGlyph6.layers[0].components:
													thisGlyph7 = font.glyphs[thisComponent6.name]
													print "-----Nesting (depth=5) inside %s is %s" % (thisGlyph6.name, thisGlyph7.name)
													check_if_brace_layer( thisGlyph7 , thisGlyph)
											else:
												check_if_brace_layer( thisGlyph6 , thisGlyph)
									else:
										check_if_brace_layer( thisGlyph5 , thisGlyph)
							else:
								check_if_brace_layer( thisGlyph4 , thisGlyph)
        			else:
						check_if_brace_layer( thisGlyph3 , thisGlyph)	
			else:
				check_if_brace_layer( thisGlyph2 , thisGlyph)				
    
    
   	#opens a new tab with all glyphs with new brace layers
	tabStringBraces = "added brace layers: "+"/"+"/".join(new_glyphs_w_braces_ls)
	font.newTab(tabStringBraces)

				
# Runs main		
if __name__ == "__main__":
	main()
			








