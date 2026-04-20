extends SequenceEvent

func trigger():
	for index in range(5):
		use_highlight_tool(get_frac_shape_part(0, index), true)
		await delay(0.2)