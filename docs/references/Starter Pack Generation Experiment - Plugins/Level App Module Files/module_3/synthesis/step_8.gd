extends SequenceEvent

func trigger():
	reset_shaded(get_frac_bar())
	await delay(0.5)
	for index in range(6):
		use_paint_tool(get_frac_shape_part(0, index))
		await delay(0.5)