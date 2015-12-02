import matplotlib as plot

def convertFR(frames, fr=2000):
	"""
	Function that will convert the frame rate of a given file to a smaller one.
	"""
	total_frames = len(frames)
	ratio = total_frames % fr
	new_frames = []
	count = 0
	for i in frames[::ratio]:
		# we'll select the maximum value for the ratio interval
		new_frames.append(max(frames[count*ratio:count*ratio+ratio]))
		# we'll also need to register the frame that was select
	return new_frames