	                                                    
def fadein(clip, duration):
	"""
	Makes the clip fade to black progressively, over ``duration`` seconds.
	For more advanced fading, see ``composition.crossfade``
	"""
    
	return clip.fl(lambda gf, t: min(1.0 * t / duration, 1) * gf(t))
