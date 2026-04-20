extends SequenceEvent

func trigger():
	for index in range(5):
		use_paint_tool(get_frac_shape_part(0, index))
		await delay(0.2)